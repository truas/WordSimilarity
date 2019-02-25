import argparse
import distutils.util as util

# Command Line for default/source.py
class CommandLineDefault:
    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.model_folder = args.mod_f
        self.context = args.cont

    # parameter list for command line - mainconverter.py and source.py
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="Validate Similarity")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=True,
                            help='output folder to write document(s)')
        parser.add_argument('--model', type=str, action='store', dest='mod_f', metavar='<parameter>',
                            required=False, help='trained word embeddings model - using MSSA or Words')
        parser.add_argument('--cont', type=util.strtobool, action='store', dest='cont', metavar='<variable>',
                            required=False, help='Word similarity metrics selection. [True] context available; '
                                                 '[False] no context available', choices=[True, False])
        return parser


# Command line for converter/mainconverter.py
class CommandLineConverter:
    # constructor for parameters
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.converter = args.conv

    # parameter list for command line - mainconverter.py and source.py
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="Validate Similarity")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True,
                            help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=True,
                            help='output folder to write document(s)')
        parser.add_argument('--conv', type=str, action='store', dest='conv', metavar='<variable>',
                            required=False, help='Delimiter used by the file', choices=['rg65', 'simlex',
                            'simverb', 'scws', 'mc28', 'men', 'wsim', 'yp130'])
        return parser


# Command line for default/mainstats.py
class CommandLineStats:
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.gold_input = args.gd
        self.ruby_input = args.ry
        self.output_folder = args.on_f

    # parameter list for command line - mainconverter.py and source.py
    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="Statistical Analysis")
        parser.add_argument('--gold', type=str, action='store', dest='gd', metavar='<file>', required=True,
                            help='Gold standard file: w1 w2 similarity_score')
        parser.add_argument('--ruby', type=str, action='store', dest='ry', metavar='<file>', required=True,
                            help='Ruby compared file: w1 w2 similarity_score')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=False,
                            help='output folder to write document(s)')
        return parser