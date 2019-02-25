from utilities.fileOperations import FileManipulation
from default.tokenData import TokenData
from default.tokenData import RangeData

import numpy


class converterBox:

    # Converter for RG65 dataset -  converts score to cosine sim range
    def convert_RG65(self, input_file, output_file, delimiter=';'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[2].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['rg65']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for MEN3K dataset -  converts score to cosine sim range
    def convert_MEN(self, input_file, output_file, delimiter=' '):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[2].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['men']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for SimLEx999 dataset -  converts score to cosine sim range
    def convert_SIMLEX(self, input_file, output_file, delimiter='\t'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[3].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['simlex']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for WordSimilarity353 dataset -  converts score to cosine sim range
    def convert_WSIM(self, input_file, output_file, delimiter='\t'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[2].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['wsim']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for MC28 dataset -  converts score to cosine sim range
    def convert_MC28(self, input_file, output_file, delimiter=';'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[2].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['mc28']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for YP130 dataset -  converts score to cosine sim range
    def convert_YP130(self, input_file, output_file, delimiter=' '):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[2].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['yp130']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for SimVerb3500 dataset -  converts score to cosine sim range
    def convert_SIMVERB(self, input_file, output_file, delimiter='\t'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[0]
                token.word2 = block[1]
                token.simvalue = float(block[3].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['simverb']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityWord(output_file, tokens)

    # Converter for SCWS dataset -  converts score to cosine sim range
    def convert_SCWS(self, input_file, output_file, delimiter='\t'):
        fio = FileManipulation()
        ranges = RangeData()
        tokens = []

        with open(input_file, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                block = line.split(delimiter)
                token.word1 = block[1]
                token.word2 = block[3]
                token.sent1 = block[5]  # target word1  between <b> </b>
                token.sent2 = block[6]  # target word2  between <b> </b>
                token.simvalue = float(block[7].strip('\n'))
                new_range = ranges.range_category['cos']
                old_range = ranges.range_category['scws']
                token.simvalue = numpy.interp(token.simvalue, old_range, new_range)
                tokens.append(token)
        fio.writeSimilarityContext(output_file, tokens)  # specific writer for SCWS
