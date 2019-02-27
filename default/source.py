import os
import sys
import gensim


# python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

# python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

# local-imports
from utilities.commandLine import CommandLineDefault
from utilities.fileOperations import FileManipulation
from default.tokenData import MetricsData
from vecmanip.similarityCalc import ContextSimilarity
from vecmanip.similarityCalc import NoContextSimilarity

if __name__ == '__main__':
    params = CommandLineDefault()  # command line parameter validation
    fio = FileManipulation()
    context_sim = ContextSimilarity()
    nocontext_sim = NoContextSimilarity()
    metric_type = MetricsData()
    last_position = -1

    # Adjusting paths/parameters
    in_loc = os.path.join(ppydir_name, params.input_folder)
    ou_loc = os.path.join(ppydir_name, params.output_folder)
    mo_loc = os.path.join(ppydir_name, params.model_folder)
    context_flag = params.context

    # Load model and folders
    trained_model = gensim.models.KeyedVectors.load(mo_loc)
    docs = fio.doclist_multifolder(in_loc)

    for doc in docs:
        doc_name = doc.split(os.sep)
        doc_name = doc_name[-1]
        print('Calculating WordSim: %s' % doc_name)
        gold_tokens = fio.readFileLine(doc)
        output_name = doc.split(os.sep)
        output_name = output_name[last_position]
        output_abs = os.path.join(ou_loc, output_name)

        if context_flag:
            ruby_tokens = context_sim.yesContextSim(gold_tokens, trained_model)
            fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.globC)
            fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.maxC)
            fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.avgC)
        else:
            ruby_tokens = nocontext_sim.noContextSim(gold_tokens, trained_model)

        # Calculated with or without context
        fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.glob)
        fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.max)
        fio.writeSimMetrics(output_abs, ruby_tokens, metric_type.avg)
    print('Finished...')