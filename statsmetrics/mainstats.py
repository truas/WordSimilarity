import os
import sys

# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLineStats
from utilities.fileOperations import FileManipulation
from vecmanip.vectorOperations import VectorManipulation

if __name__ == '__main__':
    params = CommandLineStats()  # command line parameter validation
    fio = FileManipulation()
    stats_metrics = VectorManipulation()

    gold_path = os.path.join(ppydir_name, params.gold_input)
    ruby_path = os.path.join(ppydir_name, params.ruby_input)
    ou_loc = os.path.join(ppydir_name, params.output_folder)

    gold = fio.readFileLine(gold_path)
    docs = fio.doclist_multifolder(ruby_path)
    result = "Metric\tSpearman\tS-Rho\n"

    for doc in docs:
        ruby = fio.readFileLine(doc)
        fname = doc.split(os.sep)
        fname = fname[-1]
        tmp_sp, tmp_rho = stats_metrics.spearmanCorrelation(gold, ruby)
        result += fname[:-3]+'\t'+str(tmp_sp)+'\t'+str(tmp_rho)+'\n'

    fio.writeFileGeneric(ou_loc, result)





