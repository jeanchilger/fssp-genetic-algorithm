from .partially_mapped import partially_mapped

CROSSOVOER_FN_MAP = {
    'partially_mapped': partially_mapped, # https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8
    'cycle': None, # from https://codereview.stackexchange.com/questions/226179/easiest-way-to-implement-cycle-crossover
    'ordered_crossover': None, # https://mat.uab.cat/~alseda/MasterOpt/GeneticOperations.pdf
}