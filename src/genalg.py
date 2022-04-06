import numpy as np
import time
from .initialization import INITIALIZATION_FN_MAP
from .fitness import FITNESS_FN_MAP
from .selection import SELECTION_FN_MAP
from .crossover import CROSSOVOER_FN_MAP
from .mutation import MUTATION_FN_MAP
from . import Chromosome

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
        self.execution_time = None
        self.history = None
    
    def run(
            self, instance, max_generations: int=300,
            max_time: int=330) -> Chromosome:
        """
        Executes the algorithm for at least max_generations.

        Args:
            instance (_type_): Problem instance for which the
                solution is desired.
            max_generations (int, optional): The max number of
                generations (loops). Defaults to 300.
            max_time (int, optional): The maximum amount of seconds
                the loop should execute. Defaults to 330.

        Returns:
            Chromosome: A Chromosome object, representing the
                best solution found.
        """

        offspring = []
        initial_time = time.time()
        self.history = []

        while True:
            if time.time() - initial_time > max_time:
                print('Stopping due to timeout...')
                break
            
            if max_generations <= 0:
                break
            
            max_generations -= 1
            
            # 1. Fitness step
            for p in self.population:
                p.score = self._fitness_function(instance, p)

            # 2. Selection step
            parents = self.population[:]
            if len(offspring) > 0:
                self.population = self._selection_function(
                        parents, offspring, self._population_size)
            
            self.history.append(self.get_best_result().score)
            
            offspring = []
            
            # 3. Crossover step
            for i in range(0, len(self.population), 2):
                offspring.extend(self._crossover_function(
                        self.population[i], self.population[i + 1]))

            # 4. Mutation step
            offspring = list(map(self._mutation_function, offspring))
        
        self.execution_time = time.time() - initial_time
        
    def get_best_result(self) -> Chromosome:
        return sorted(self.population, key=lambda x: x.score)[0]
    
    def get_worst_result(self) -> Chromosome:
        return sorted(self.population, key=lambda x: x.score)[-1]
