import numpy

from nltk.corpus import wordnet as wn
from vecmanip.vectorOperations import VectorManipulation
from nltk.corpus import wordnet
from utilities.textOperations import TextParser
from utilities.synsetTracker import SynsetParserVector
from default.tokenData import TokenData


class NoContextSimilarity:

    # calculates de similarity of two words - does not consider context
    def noContextSim(self, tokens, trained_model):
        print('Running: Word Similarity - Context False')
        synset_op = SynsetParserVector()
        new_tokens = []

        for token in tokens:
            new_token = TokenData()

            synsets_a = wordnet.synsets(token.word1)
            synsets_b = wordnet.synsets(token.word2)

            # clean synsets that only exist in the model
            vec_syna = synset_op.validate_synsets_model(token.word1, synsets_a, trained_model)
            vec_synb = synset_op.validate_synsets_model(token.word2, synsets_b, trained_model)

            # perform all metrics Word Similarity
            new_token.sim.max = self.maxSim(vec_syna, vec_synb)
            new_token.sim.avg = self.avgSim(vec_syna, vec_synb)
            new_token.sim.glob = self.globalSim(vec_syna, vec_synb)

            new_token.word1 = token.word1
            new_token.word2 = token.word2
            new_tokens.append(new_token)

        return new_tokens

    # calculates the highest similarity between two word-synsets-vectors - LocalSim
    def maxSim(self, vecs_a, vecs_b):
        vecmanip = VectorManipulation()
        highest = -1.0

        for vec_a in vecs_a:
            for vec_b in vecs_b:
                tmp_high = vecmanip.cosine_similarity(vec_a, vec_b)
                if tmp_high > highest:
                    highest = tmp_high
        return highest

    # calculates the average similarity between two word-synsets and their vectors
    def avgSim(self, vecs_a, vecs_b):
        vecmanip = VectorManipulation()
        partial_sim = 0.0

        for vec_a in vecs_a:
            for vec_b in vecs_b:
                tmp_ab = vecmanip.cosine_similarity(vec_a, vec_b)
                partial_sim += tmp_ab

        if not vecs_a or not vecs_b:
            final_sim = 0.0
        else:
            final_sim = (partial_sim / (len(vecs_a) * len(vecs_b)))

        return final_sim

    # global word vector - avg all vectors in the model and perform their similarity
    def globalSim(self, vecs_a, vecs_b):
        vecmanip = VectorManipulation()
        if not vecs_a or not vecs_b:
            global_sim = 0.0
        else:
            global_a = numpy.average(vecs_a, axis=0)
            global_b = numpy.average(vecs_b, axis=0)
            global_sim = vecmanip.cosine_similarity(global_a, global_b)

        return global_sim


class ContextSimilarity:

    # calculates the similarity of two words given a context
    def yesContextSim(self, tokens, trained_model):
        print('Running: Word Similarity - Context True')
        sim_nocontext = NoContextSimilarity()
        synset_op = SynsetParserVector()
        text_parser = TextParser()
        new_tokens = []

        for token in tokens:
            new_token = TokenData()
            synsets_a = wordnet.synsets(token.word1)
            synsets_b = wordnet.synsets(token.word2)
            # clean and tokenizer context
            context_a = text_parser.cleanText(token.sent1)
            context_b = text_parser.cleanText(token.sent2)
            # average vector for the context for each word
            clean_context_a = self.__contextParser(context_a, trained_model)
            clean_context_b = self.__contextParser(context_b, trained_model)
            # clean synsets that only exist in the model
            vec_syna = synset_op.validate_synsets_model(token.word1, synsets_a, trained_model)
            vec_synb = synset_op.validate_synsets_model(token.word2, synsets_b, trained_model)

            # perform all metrics Word Similarity
            # Context
            new_token.sim.maxC = self.__maxSimC(vec_syna, clean_context_a, vec_synb, clean_context_b)
            new_token.sim.avgC = self.__avgSimC(vec_syna, clean_context_a, vec_synb, clean_context_b)
            new_token.sim.globC = self.__globalSimC(clean_context_a, clean_context_b)
            # No Context
            new_token.sim.max = sim_nocontext.maxSim(vec_syna, vec_synb)
            new_token.sim.avg = sim_nocontext.avgSim(vec_syna, vec_synb)
            new_token.sim.glob = sim_nocontext.globalSim(vec_syna, vec_synb)

            new_token.word1 = token.word1
            new_token.word2 = token.word2
            new_tokens.append(new_token)

        return new_tokens

    # maximum similarity between v1 and v2 - takes context into account LocalSimC
    def __maxSimC(self, vecs_a, context_a, vecs_b, context_b):
        vecmanip = VectorManipulation()
        closest_a = self.__closestSenseContext(vecs_a, context_a)
        closest_b = self.__closestSenseContext(vecs_b, context_b)

        result = vecmanip.cosine_similarity(closest_a, closest_b)

        return result

    # calculates the average similarity between two word-synsets considering context
    def __avgSimC(self, vecs_a, context_a, vecs_b, context_b):
        vecmanip = VectorManipulation()
        partial_sim = 0.0

        for vec_a in vecs_a:
            pcwa = vecmanip.cosine_similarity(vec_a, context_a)
            for vec_b in vecs_b:
                pcwb = vecmanip.cosine_similarity(vec_b, context_b)
                dwab = vecmanip.cosine_similarity(vec_a, vec_b)
                partial_sim += pcwa * pcwb * dwab

        if not vecs_a or not vecs_b:
            final_sim = 0.0
        else:
            final_sim = (partial_sim / (len(vecs_a) * len(vecs_b)))

        return final_sim

    # global similarity considering the vector contexts of words
    def __globalSimC(self, context_a, context_b):
        vecmanip = VectorManipulation()
        global_simc = vecmanip.cosine_similarity(context_a, context_b)

        return global_simc

    # give the average vector from all words in the context
    def __contextParser(self, text_items, trained_model):
        track_synset = SynsetParserVector()
        vector_manip = VectorManipulation()
        context_vector = []

        for text_item in text_items:
            synsets = wn.synsets(text_item)
            for synset in synsets:
                key = track_synset.keyParser(text_item, synset)
                try:
                    key_vector = trained_model.word_vec(key)
                    context_vector.append(key_vector)  # put all vector words in the sentence together
                except KeyError:
                    pass

        return  numpy.average(context_vector, axis=0)

    # gives the closest sense to the context attached to it
    def __closestSenseContext(self, synset_vecs, contextvec):
        vecmanip = VectorManipulation()
        high_so_far = -1.0
        nearest = []

        for synset_vec in synset_vecs:  # closest sense (synset_vec) of 'word-A' to its context
            context_sim = vecmanip.cosine_similarity(synset_vec, contextvec)
            if context_sim > high_so_far:
                high_so_far = context_sim
                nearest = synset_vec

        return nearest
