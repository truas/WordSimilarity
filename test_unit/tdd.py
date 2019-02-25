import unittest
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