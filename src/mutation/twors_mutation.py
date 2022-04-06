from .. import Chromosome
import numpy as np

def twors_mutation(offspring: Chromosome, mutation_proba: float=0.5, n_swaps: int=3) -> Chromosome:
    """
    Applies the Twors mutation to a given offspring.

    Args:
        offspring (np.ndarray): Offspring to be mutated.

    Returns:
        np.ndarray: Result of the mutation.
    """
    
    if np.random.rand(1) >= mutation_proba:
        return offspring
    
    pos = np.random.choice(
            np.arange(len(offspring)),
            replace=False, size=n_swaps * 2)
    
    for i in range(0, n_swaps * 2, 2):
        pos1, pos2 = pos[i:i + 2]
        
        temp = offspring[pos2]
        offspring[pos2] = offspring[pos1]
        offspring[pos1] = temp
    
    return offspring