from .parent_elitism import parent_elitism
from .truncation import truncation
from .keep_offspring import keep_offspring
from .elitism_with_distance import elitism_with_distance

SELECTION_FN_MAP = {
    'parent_elitism': parent_elitism,
    'truncation': truncation,
    'keep_offspring': keep_offspring,
    'elitism_with_distance': elitism_with_distance,
}