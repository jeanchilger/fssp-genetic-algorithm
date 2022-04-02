import numpy as np
from dataclasses import dataclass
from typing import Union
from .initialization import INITIALIZATION_FN_MAP


# Data class to represent a solution (chromosome)
@dataclass
class Chromosome:
    data: Union[list, np.ndarray]


# - 1. Initialization
# - 2. Fitness
# - 3. Selection
# - 4. Crossover
# - 5. Mutation
class GeneticAlgorithm:
    
    def __init__(
            self, n_tasks, population_size, init_type='random', fitness_type=None, selection_type=None,
            crossover_type=None, mutation_type=None):
        self._init_function = INITIALIZATION_FN_MAP[init_type]
        
        self.population = self._init_function(n_tasks, population_size)
    
    def step(self):
        pass
