import numpy as np
from .initialization import INITIALIZATION_FN_MAP
from .fitness import FITNESS_FN_MAP
from .selection import SELECTION_FN_MAP
from .crossover import CROSSOVOER_FN_MAP
from . import Chromosome


# - 1. Initialization
# - 2. Fitness
# - 3. Selection
# - 4. Crossover
# - 5. Mutation
class GeneticAlgorithm:
    def __init__(
            self, n_tasks, population_size, init_type='random',
            fitness_type='makespan', selection_type='parent_elitism',
            crossover_type='partially_mapped', mutation_type=None):
        self._population_size = population_size
        
        self._init_function = INITIALIZATION_FN_MAP[init_type]
        self._fitness_function = FITNESS_FN_MAP[fitness_type]
        self._selection_function = SELECTION_FN_MAP[selection_type]
        self._crossover_function = CROSSOVOER_FN_MAP[crossover_type]

        self.population = self._init_function(n_tasks, population_size)
    
    def run(self, instance, max_generations=100) -> Chromosome:
        """
        Executes the algorithm for at least max_generations.

        Args:
            instance (_type_): Problem instance for which the
                solution is desired.
            max_generations (int, optional): The max number of
                generations (loops). Defaults to 100.

        Returns:
            Chromosome: A Chromosome object, representing the
                best solution found.
        """

        stop = False
        offspring = []

        while not stop:
            stop = max_generations <= 0
            max_generations -= 1
            
            # Fitness step
            for p in self.population:
                p.score = self._fitness_function(instance, p)

            # Selection step
            parents = self.population.copy()
            if len(offspring) > 0:
                self.population = self._selection_function(
                        parents, offspring, self._population_size)
            
            # Crossover step
            offspring = None
            p1 = [1, 2, 3, 4, 5, 6, 7]
            p2 = [5, 4, 6, 7, 2, 1, 3]
            of1, of2 = self._crossover_function(p1, p2)
            print(of1)
            print(of2)
            print("========")
            stop = True
            
            # Mutation step
            
            
            
            
            
            
            