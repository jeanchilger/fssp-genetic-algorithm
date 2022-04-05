def partially_mapped(p1, p2):
    cross_point_a = int(0.2 * len(p1))
    cross_point_b = int(0.8 * len(p1))
    
    offspring1 = p1.copy()
    offspring2 = p2.copy()
    
    offspring1[cross_point_a:cross_point_b] = p2[cross_point_a:cross_point_b]
    offspring2[cross_point_a:cross_point_b] = p1[cross_point_a:cross_point_b]
    
    fix_map = _get_map(
            offspring1[cross_point_a:cross_point_b],
            offspring2[cross_point_a:cross_point_b])
    
    offspring1[:cross_point_a] = map(
            lambda x: fix_map.get(x, x), offspring1[:cross_point_a])
    offspring1[cross_point_b:] = map(
            lambda x: fix_map.get(x, x), offspring1[cross_point_b:])
    
    offspring2[:cross_point_a] = map(
            lambda x: fix_map.get(x, x), offspring2[:cross_point_a])
    offspring2[cross_point_b:] = map(
            lambda x: fix_map.get(x, x), offspring2[cross_point_b:])
    
    return offspring1, offspring2


def _get_map(substr1, substr2):
    subs_map = {}
    
    for i in range(len(substr1)):
        subs_map[substr1[i]] = substr2[i]
        
    normalized = False
    while not normalized:
        normalized = True
        for k, v in list(subs_map.items()):
            if v in subs_map:
                subs_map[k] = subs_map[v]
                subs_map.pop(v)
                normalized = False
                
    for k, v in list(subs_map.items()):
        subs_map[v] = k
    
    return subs_map
    