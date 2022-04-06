import numpy as np
from typing import List
from .. import Chromosome

def elitism_with_distance(
        parents: List[Chromosome], offspring: List[Chromosome], 
        max_population_size: int) -> List[Chromosome]:
    """
    Produces a new population based on parents and offspring,
    using the "Elitism with Distance" selection strategy.
    https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8426051
    
    This strategy will select an individual based on fitting, and them
    will select another individual that has the largest euclidean distance
    to it.

    Args:
        parents (List[Chromosome]): Parents from the population.
        offspring (List[Chromosome]): Offspring from the population.
        max_population_size (int): Max size of the population.

    Returns:
        List[Chromosome]: The new population.
    """
    
    full_population = sorted(parents + offspring, key=lambda x: x.score)
    population = []
    
    while len(population) < max_population_size:
        p1 = full_population.pop(0)
        population.append(p1)
        
        p2 = max(full_population, key=lambda x: np.linalg.norm(p1.data - x.data))
        population.append(p2)

    return population
