

# def readFileLine(fname):
#     with open(fname, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             yield line
#
#
# inp = 'C:\\Users\\terry\\Documents\\Programming\\PyCharmProjects\\WordSimilarity\\files_converter\\output\\mc28.txt'
#
# t = readFileLine(inp)
#
# print(next(t))

from nltk.corpus import wordnet

syns = wordnet.synsets("java")
for syn in syns:
    print(syn)