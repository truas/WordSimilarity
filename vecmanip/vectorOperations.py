import numpy

from scipy import spatial
from scipy.stats import pearsonr
from scipy.stats import spearmanr

#  Definitions
PRECISION = 7


class VectorManipulation:

    # calculates the cosine similarity between 2 vectors
    def cosine_similarity(self, v1, v2):
        if not numpy.any(v1) or not numpy.any(v2): return 0.0  # in case there is an empty vector we return 0.0
        cos_sim = 1.0 - round(spatial.distance.cosine(v1, v2), PRECISION)
        # some word vectors might be 0.0 for all dimensions
        return cos_sim

    # calculates the spearman and pearson correlation values
    def spearmanCorrelation(self, tokens_a, tokens_b):
        values_1 = [i.simvalue for i in tokens_a]
        values_2 = [i.simvalue for i in tokens_b]

        # pearson_value, p_rho = pearsonr(values_1, values_2) # not used for now
        spearman_value, s_rho = spearmanr(values_1, values_2)
        return spearman_value, s_rho

    # Retrieves the average of a vector, if it is empty, return an empty vector
    def checkVectorC(self, given_vector):
        altered_vector = numpy.array(given_vector)
        if altered_vector.size == 0:
            return [0.0]
        else:
            return numpy.average(given_vector, axis=0)