from .partially_mapped import partially_mapped

CROSSOVOER_FN_MAP = {
    'single_point': None,
    'two_point_point': None,
    'uniform': None,
    # use this instead single point and two point?
    'partially_mapped': partially_mapped, # https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8
    'cycle': None, # from https://codereview.stackexchange.com/questions/226179/easiest-way-to-implement-cycle-crossover
}