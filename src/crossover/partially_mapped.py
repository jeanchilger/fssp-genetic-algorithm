import numpy as np
from typing import Sequence, Union
from .. import Chromosome


def partially_mapped(p1: Chromosome, p2: Chromosome) -> Sequence[Chromosome]:
    """
    Combines the provided chromosomes using the "Partially Mapped"
    crossover strattegy (https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8).
    
    This strategy is similar to the two-point crossover. The difference
    relies on the creation of a map relation between the
    transfered parts from the offsprings, which is used to fix
    repeated values.

    Args:
        p1 (Chromosome): A individual selected to mating.
        p2 (Chromosome): A individual selected to mating

    Returns:
        Sequence[Chromosome]: The resulting offsprings.
    """
    
    cross_point_a = int(np.random.uniform(0, 0.3) * len(p1))
    cross_point_b = int(np.random.uniform(0.5, 1) * len(p1))
    
    offspring1 = p1.copy()
    offspring2 = p2.copy()
    
    offspring1[cross_point_a:cross_point_b] = p2[cross_point_a:cross_point_b]
    offspring2[cross_point_a:cross_point_b] = p1[cross_point_a:cross_point_b]
    
    fix_map1, fix_map2 = _get_maps(
            offspring1[cross_point_a:cross_point_b],
            offspring2[cross_point_a:cross_point_b])
    
    offspring1[:cross_point_a] = np.array(list(map(
            lambda x: fix_map1.get(x, x), offspring1[:cross_point_a])))
    offspring1[cross_point_b:] = np.array(list(map(
            lambda x: fix_map1.get(x, x), offspring1[cross_point_b:])))
    
    offspring2[:cross_point_a] = np.array(list(map(
            lambda x: fix_map2.get(x, x), offspring2[:cross_point_a])))
    offspring2[cross_point_b:] = np.array(list(map(
            lambda x: fix_map2.get(x, x), offspring2[cross_point_b:])))
    
    return offspring1, offspring2


def _get_maps(
        substr1: Union[list, np.ndarray],
        substr2: Union[list, np.ndarray]) -> Sequence[dict]:
    """
    Return two mapping relationships between substr1 to substr2
    and the reverse of that.

    Args:
        substr1 (Union[list, np.ndarray]): First substring.
        substr2 (Union[list, np.ndarray]): Second substring.

    Returns:
        Sequence[dict]: Dicts, describing a map between both substrings.
    """

    subs_map1 = {}
    subs_map2 = {}
    
    for i in range(len(substr1)):
        subs_map1[substr1[i]] = substr2[i]
        
    normalized = False
    while not normalized:
        normalized = True
        for k, v in list(subs_map1.items()):
            if v in subs_map1:
                subs_map1[k] = subs_map1[v]
                subs_map1.pop(v)
                normalized = False
                break
        
    for k, v in list(subs_map1.items()):
        subs_map2[v] = k
    
    return subs_map1, subs_map2
    