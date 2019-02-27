import unittest
import numpy
import os

from vecmanip.vectorOperations import VectorManipulation
from utilities.fileOperations import FileManipulation


class TestSimilarity(unittest.TestCase):

    # cosine similarity
    def test_cosine_similarity(self):
        vec_manip = VectorManipulation()
        a = [1, 0]
        b = [-1, 0]
        self.assertEqual(-1, vec_manip.cosine_similarity(a, b))

    # test word1 word2 similarity
    def test_readLine3Columns(self):
        fio = FileManipulation()
        inp = 'mc28.txt'
        tokens = fio.readFileLine(inp)
        obj = tokens[1]
        output = obj.word1 + '\t' + obj.word2 + '\t' + str(obj.simvalue)
        self.assertEqual('gem\tjewel\t0.96', output)

    # test word1 word2 sent1 sent2 similarity
    def test_readLine5Columns(self):
        fio = FileManipulation()
        inp = 'scws.txt'
        tokens = fio.readFileLine(inp)
        obj = tokens[1]
        output1 = obj.word1 + '\t' + obj.word2 + '\t' + str(obj.simvalue)
        output2 = obj.sent1 + '\t' + obj.sent2
        self.assertEqual('Brazil\ttriple\t0.06', output1)
        self.assertEqual('i like potato\ti cat', output2)

    # test to obtain fname from absolute path
    def test_SplitFileName(self):
        pydir_name = os.path.dirname(os.path.abspath(__file__))
        file_location = os.path.join(pydir_name, 'scws.txt')
        file_location_test = file_location.split(os.sep)
        file_name = file_location_test[-1]
        self.assertEqual('scws.txt', file_name)

    # test the spearman correlation values for AvgSim in SCWS results
    def test_SpearmanAvg(self):
        fio = FileManipulation()
        vec_manip = VectorManipulation()
        gold_tokens = fio.readFileLine('scws.txt')
        ruby_avg = fio.readFileLine('scws_avgsim.txt')
        ruby_avgc = fio.readFileLine('scws_avgsimc.txt')
        t11,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_avg)  # not using rho
        t21,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_avgc)  # not using rho
        self.assertEqual('0.6672948584312471', str(t11))
        self.assertEqual(numpy.float64('0.5809138966365319'), t21)

    # test the spearman correlation values for MaxSim in SCWS results
    def test_SpearmanMax(self):
        fio = FileManipulation()
        vec_manip = VectorManipulation()
        gold_tokens = fio.readFileLine('scws.txt')
        ruby_max = fio.readFileLine('scws_maxsim.txt')
        ruby_maxc = fio.readFileLine('scws_maxsimc.txt')
        t11,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_max)  # not using rho
        t21,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_maxc)  # not using rho
        self.assertEqual('0.6127420529962664', str(t11))
        self.assertEqual(numpy.float64('0.6367583108796157'), t21)

    # test the spearman correlation values for GlobalSim in SCWS results
    def test_SpearmanGlobal(self):
        fio = FileManipulation()
        vec_manip = VectorManipulation()
        gold_tokens = fio.readFileLine('scws.txt')
        ruby_global = fio.readFileLine('scws_globsim.txt')
        ruby_globalc = fio.readFileLine('scws_globsimc.txt')
        t11,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_global)  # not using rho
        t21,__ = vec_manip.spearmanCorrelation(gold_tokens, ruby_globalc)  # not using rho
        self.assertEqual('0.6670118503142607', str(t11))
        self.assertEqual(numpy.float64('0.2969117412433547'), t21)