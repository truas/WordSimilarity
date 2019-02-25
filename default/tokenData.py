# TokenData - Word and Sentence (when used)
class TokenData:

    def __init__(self):
        self.file_name = None
        self.word1 = None
        self.pos1 = None
        self.word2 = None
        self.pos2 = None
        self.sent1 = None  # only used for SCWS
        self.sent2 = None  # only used for SCWS
        self.simvalue = None
        self.sim = SimData()


# Similarity Metrics data - values
class SimData:
    def __init__(self):
        self.simvalue = None
        self.avg = None
        self.avgC = None
        self.max = None
        self.maxC = None
        self.glob = None
        self.globC = None


# Ranges of benchmarks
class RangeData:
    def __init__(self):
        self.range_category = {'cos': [-1, 1], 'rg65': [0, 4], 'simlex': [0, 10], 'simverb': [0, 10],
                               'scws': [0, 10], 'mc28': [0, 4], 'men': [0, 50], 'wsim': [0, 10], 'yp130': [0, 4]}
        self.range = {0: [0, 1], 1: [0, 10], 2: [0, 4], 3: [0, 50]}

# Name of metrics
class MetricsData:
    def __init__(self):
        self.avg = 'avgsim'
        self.avgC = 'avgsimc'
        self.max = 'maxsim'
        self.maxC = 'maxsimc'
        self.glob = 'globsim'
        self.globC = 'globsimc'