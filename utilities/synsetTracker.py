import numpy

class SynsetParserVector:

    # creates a list of synsetkeys that exist in the trained model
    def validate_synsets_model(self, word, synsets, trained_model):
        valid_synsets = []
        for synset in synsets:
            key = self.keyParser(word, synset)
            try:
                vec = trained_model.word_vec(key)
                valid_synsets.append(vec)  # put all vector words in the sentence together and average
            except KeyError:
                pass  # key not in the model
        return valid_synsets  # if the key is not on the model, it will return an empty list of valid synets

    # returns the dimension/values of a key in a word-embedding model
    def retrieve_synsetvec(self, key, model):
        key_vec = []
        try:
            key_vec = model.word_vec(key)
        except KeyError:
            #pass
            key_vec = []  # key not in the model we set as [0.0]
        return key_vec

    # parse word/synsets into key format for MSSA model
    def keyParser(self, word, synset):
        key = word.lower() + '#' + str(synset.offset()) + '#' + synset.pos()
        return key


