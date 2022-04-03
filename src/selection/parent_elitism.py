import numpy as np


def parent_elitism(
        parents: np.ndarray, offspring: np.ndarray,
        max_population_size: int, elitism_rate: float=0.01) -> np.ndarray:
    """
    Produces a new population based on parents and offspring,
    using the "parent elitism" strategy.
    
    This strategy will select a best fitting percentage
    (set by `elitism_rate`) from the parents and combine them
    with the best fitting children.

    Args:
        parents (np.ndarray): Parents from the population.
        offspring (np.ndarray): Offspring from the population.
        max_population_size (int): Max size of the population
        elitism_rate (float, optional): Percentage from the parents
            to keep. Defaults to 0.01.

    Returns:
        np.ndarray: The new population.
    """

    n_elites = int(elitism_rate * len(parents))
    n_offspring = max_population_size - n_elites

    best_parents = sorted(parents, key=lambda x: x.score)[:n_elites]
    best_offspring = sorted(offspring, key=lambda x: x.score)[:n_offspring]
    
    return np.hstack([best_parents, best_offspring])
    
    
    
    