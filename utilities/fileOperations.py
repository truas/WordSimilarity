import os

from default.tokenData import TokenData
from default.tokenData import MetricsData


class FileManipulation:
    #  handles file manipulation

    # creates list of documents in many folders
    def doclist_multifolder(self, folder_name):
        input_file_list = []
        for roots, dir, files in os.walk(folder_name):
            for file in files:
                file_uri = os.path.join(roots, file)
                if file_uri.endswith('txt'): input_file_list.append(file_uri)
        return input_file_list

    # reads file and creates list of Token Objects
    def readFileLine(self, fname, delimiter='\t'):
        tokens =[]
        record_items = 3
        with open(fname, 'r', encoding='utf-8') as fin:
            for line in fin:
                token = TokenData()
                record = line.split(delimiter)
                token.word1 = record[0]
                token.word2 = record[1]

                if len(record) == record_items:  # w1 w2 sim (3)
                    token.simvalue = float(record[2].strip('\n'))
                else:  # w1 w2 s1 s2 sim (5)
                    token.sent1 = record[2]
                    token.sent2 = record[3]
                    token.simvalue = float(record[4].strip('\n'))

                tokens.append(token)
        return tokens

    # writes output file with word1 word2 sim_value
    def writeSimilarityWord(self, fname, tokens):
        doc = open(fname, 'w+')
        for token in tokens:
            doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.simvalue) + '\n')
        doc.close()

    # writes output file with word1 word2 sentence1 sentence2 sim_value
    def writeSimilarityContext(self, fname, tokens):
        doc = open(fname, 'w+')
        for token in tokens:
            doc.write(token.word1 + '\t' + token.word2 + '\t' + token.sent1 + '\t' + token.sent2 + '\t' +
                      str(token.simvalue) + '\n')
        doc.close()

    # writes word similarity score for word pairs
    def writeSimMetrics(self, fname, tokens, metric_type):
        metrics = MetricsData()
        doc = open(fname[:-4] + '_' + metric_type+".txt", 'w+')
        for token in tokens:
            if metric_type == metrics.max: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.max) + '\n')
            elif metric_type == metrics.maxC: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.maxC) + '\n')
            elif metric_type == metrics.avg: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.avg) + '\n')
            elif metric_type == metrics.avgC: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.avgC) + '\n')
            elif metric_type == metrics.glob: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.glob) + '\n')
            elif metric_type == metrics.globC: doc.write(token.word1 + '\t' + token.word2 + '\t' + str(token.sim.globC) + '\n')
        doc.close()

    # writes entire string in one file
    def writeFileGeneric(self, output_file, text):
        doc = open(output_file, 'w+')
        doc.write(text)
        doc.close()

    # reads an entire file and returns its text
    def readFile(self, file_name):
        text = ""
        try:
            f = open(file_name, errors="ignore")
            text = f.read()
            f.close()
        except IOError as exc:
            raise ("FAILED: Problem reading file: " + file_name)
        return text