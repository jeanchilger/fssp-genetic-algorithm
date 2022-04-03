from .parent_elitism import parent_elitism

SELECTION_FN_MAP = {
    'parent_elitism': parent_elitism,
    'only_offspring': None,
    'only_elites': None,
    'elitism_with_distance': None, # method from https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8426051
    'fitness_proportionate': None, # from https://en.wikipedia.org/wiki/Fitness_proportionate_selection
}