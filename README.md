# WordSimilarity
Program to calculate Word Similarity for different benchmarks.

It includes a  `converter` package to convert your data into a proper format used by th main program (`default`).

##### Requirements:
* `files` folder should be at the same level as packages `converter` and `default`
* Python +3.5
* NLTK/Wordnet
* Gensim +3.4.0

## Word Similarity
#### `default/source.py` Command Line Execution 

    # python3 mainconverter.py --input <location> --output <loaction> --cont <benchmark-delimiter>
    
`--input:` - Input folder-file (e.g. `converter` - output)
 
`--output` - Output folder for the converted files - This will produce the following metrics [avgSim, avgSimC, maxSim, maxSimC, globalSim, and globalSimC ]

`--model` - Synset Embeddings model to be used for representing the words (Format `word#offset#POS` - based on WordNet)

`--cont` - [True] - All metrics are produced - Context sentence has to be present
           [False] - No-Context metrics will be produced.`



## Statistical Metrics
#### `statsmetrics/mainstats.py` Command Line Execution 
     
     # python3 mainconverter.py --gold <location> --ruby <loacation> --output <location>
    
   `--gold:` - Input gold standard file (e.g. `converter` - output for each dataset)
   
   `--ruby:` - Input ruby compared file(s). Each file is compared with `--gold` - Folder with Different metrics calculated (e.g. `default` - output)
   
   `--output` - Output file_location where results will be saved

## Converter

#### `converter/mainconverter.py` Command Line Execution 

    # python3 mainconverter.py --input <location> --output <loaction> --conv <benchmark-delimiter>
    
`--input:` - Input folder-file
 
`--output` - Output for the converted file

`--conv` - choices of benchmark to convert - `choices=['rg65', 'simlex','simverb', 'scws', 'mc28', 'men', 'wsim', 'yp130']`

*Important:* delimiters used for each dataset (using original) reader are hardcoded under `convertBox.py` (`delimiter=*`)