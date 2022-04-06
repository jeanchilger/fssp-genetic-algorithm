from typing import List
from .. import Chromosome

def keep_offspring(
        parents: List[Chromosome], offspring: List[Chromosome], 
        max_population_size: int) -> List[Chromosome]:
    """
    Produces a new population based on parents and offspring,
    using the "Keep Offspring" selection strategy.
    
    This strategy will keep the offspring, truncating if
    the total number of individuals is larger than max_population_size.

    Args:
        parents (List[Chromosome]): Parents from the population.
        offspring (List[Chromosome]): Offspring from the population.
        max_population_size (int): Max size of the population.

    Returns:
        List[Chromosome]: The new population.
    """
    
    
    return sorted(offspring, key=lambda x: x.score)[:max_population_size]
    