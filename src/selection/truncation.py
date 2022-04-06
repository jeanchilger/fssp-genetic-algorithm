from typing import List
from .. import Chromosome

def truncation(
        parents: List[Chromosome], offspring: List[Chromosome], 
        max_population_size: int) -> List[Chromosome]:
    """
    Produces a new population based on parents and offspring,
    using the "Truncation selection" strategy.
    
    This strategy will keep only the best fitting individuals
    from both parents and offspring.

    Args:
        parents (List[Chromosome]): Parents from the population.
        offspring (List[Chromosome]): Offspring from the population.
        max_population_size (int): Max size of the population.

    Returns:
        List[Chromosome]: The new population.
    """
    
    return sorted(parents + offspring, key=lambda x: x.score)[:max_population_size]