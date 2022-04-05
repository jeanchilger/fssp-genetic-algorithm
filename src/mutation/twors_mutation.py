import numpy as np

def twors_mutation(offspring: np.ndarray, mutation_proba: float=0.5) -> np.ndarray:
    """
    Applies the Twors mutation to a given offspring.

    Args:
        offspring (np.ndarray): Offspring to be mutated.

    Returns:
        np.ndarray: Result of the mutation.
    """
    
    if np.random.rand(1) >= mutation_proba:
        return offspring
    
    pos1, pos2 = np.random.randint(0, len(offspring), 2)
    
    temp = offspring[pos2]
    offspring[pos2] = offspring[pos1]
    offspring[pos1] = temp
    
    return offspring