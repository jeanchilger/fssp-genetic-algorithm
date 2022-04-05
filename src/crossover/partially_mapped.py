import numpy as np
from copy import deepcopy
from pprint import pprint


def partially_mapped(p1, p2):
    cross_point_a = int(0.2 * len(p1))
    cross_point_b = int(0.8 * len(p1))
    
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
    
    # print()
    # print(p1)
    # print(p2)
    # print(offspring1)
    # print(offspring2)
    # print('-' * 30)
    # print(p1[cross_point_a:cross_point_b])
    # print(p2[cross_point_a:cross_point_b])
    # print('-' * 30)
    # pprint(cross_point_a)
    # pprint(cross_point_b)
    # pprint(fix_map1)
    # pprint(fix_map2)
    # print("REPEATED?: ", not len(offspring1) == len(set(offspring1)))
    # print()
    # input()
    
    return offspring1, offspring2


def _get_maps(substr1, substr2):
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
    