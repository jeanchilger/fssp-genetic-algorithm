import numpy as np

def random(n_tasks: int, population_size: int) -> np.ndarray:
    """
    Returns the initial population for the genetic algorithm.

    Args:
        n_tasks (int): Number of tasks from the task.
        population_size (int): Size of the population.

    Returns:
        np.ndarray: A matrix, where each row represents a 
        individual (chromosome) from the population
    """
    
    return np.array([
            np.random.choice(np.arange(1, n_tasks + 1), replace=False, size=n_tasks)
            for a in range(population_size)])