import numpy as np
from typing import List
from .. import Chromosome


def parent_elitism(
        parents: List[Chromosome], offspring: List[Chromosome],
        max_population_size: int, elitism_rate: float=0.01) -> List[Chromosome]:
    """
    Produces a new population based on parents and offspring,
    using the "parent elitism" strategy.
    
    This strategy will select a best fitting percentage
    (set by `elitism_rate`) from the parents and combine them
    with the best fitting children.

    Args:
        parents (List[Chromosome]): Parents from the population.
        offspring (List[Chromosome]): Offspring from the population.
        max_population_size (int): Max size of the population.
        elitism_rate (float, optional): Percentage from the parents
            to keep. Defaults to 0.01.

    Returns:
        List[Chromosome]: The new population.
    """

    n_elites = int(elitism_rate * len(parents))
    n_offspring = max_population_size - n_elites

    best_parents = sorted(parents, key=lambda x: x.score)[:n_elites]
    best_offspring = sorted(offspring, key=lambda x: x.score)[:n_offspring]
    
    return sorted(best_parents + best_offspring, key=lambda x: x.score)
    
    
    
    