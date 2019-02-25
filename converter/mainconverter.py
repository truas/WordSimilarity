import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLineConverter
from converter.converterBox import converterBox

if __name__ == '__main__':
    params = CommandLineConverter()  # command line parameter validation
    cb = converterBox()  # handles which converter runs

    in_fname = os.path.join(ppydir_name, params.input_folder)
    ou_fname = os.path.join(ppydir_name, params.output_folder)
    converter = params.converter

    # Converter selection by benchmark - delimiter had default value
    if converter == "rg65":
        cb.convert_RG65(in_fname, ou_fname)
    elif converter == "men":
        cb.convert_MEN(in_fname, ou_fname)
    elif converter == "simlex":
        cb.convert_SIMLEX(in_fname, ou_fname)
    elif converter == "wsim":
        cb.convert_WSIM(in_fname, ou_fname)
    elif converter == "mc28":
        cb.convert_MC28(in_fname, ou_fname)
    elif converter == "yp130":
        cb.convert_YP130(in_fname, ou_fname)
    elif converter == "simverb":
        cb.convert_SIMVERB(in_fname, ou_fname)
    elif converter == "scws":
        cb.convert_SCWS(in_fname, ou_fname)
    else:
        print('No benchmark selected')
        exit()
