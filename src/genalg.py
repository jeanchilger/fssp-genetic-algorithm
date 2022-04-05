import numpy as np
from .initialization import INITIALIZATION_FN_MAP
from .fitness import FITNESS_FN_MAP
from .selection import SELECTION_FN_MAP
from .crossover import CROSSOVOER_FN_MAP
from .mutation import MUTATION_FN_MAP
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
            crossover_type='partially_mapped', mutation_type='twors_mutation'):
        self._population_size = population_size
        
        self._init_function = INITIALIZATION_FN_MAP[init_type]
        self._fitness_function = FITNESS_FN_MAP[fitness_type]
        self._selection_function = SELECTION_FN_MAP[selection_type]
        self._crossover_function = CROSSOVOER_FN_MAP[crossover_type]
        self._mutation_function = MUTATION_FN_MAP[mutation_type]

        self.population = self._init_function(n_tasks, population_size)
    
    def run(self, instance, max_generations=300) -> Chromosome:
        """
        Executes the algorithm for at least max_generations.

        Args:
            instance (_type_): Problem instance for which the
                solution is desired.
            max_generations (int, optional): The max number of
                generations (loops). Defaults to 300.

        Returns:
            Chromosome: A Chromosome object, representing the
                best solution found.
        """

        stop = False
        offspring = []

        while not stop:
            stop = max_generations <= 0
            max_generations -= 1
            
            # 1. Fitness step
            for p in self.population:
                p.score = self._fitness_function(instance, p)

            # 2. Selection step
            parents = self.population[:]
            if len(offspring) > 0:
                self.population = self._selection_function(
                        parents, offspring, self._population_size)
            
            offspring = []
            
            ## Order population by fitness, to make pairs
            self.population = sorted(self.population, key=lambda x: x.score)
            
            # 3. Crossover step
            for i in range(0, len(self.population), 2):
                offspring.extend(self._crossover_function(
                        self.population[i], self.population[i + 1]))

            # 4. Mutation step
            offspring = list(map(self._mutation_function, offspring))
            # print('\nMUTATION -> offspring:')
            # print(type(offspring))
            # print(type(offspring[0]))
            
            
            
            
            