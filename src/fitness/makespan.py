from .. import Chromosome

# TODO: Refactor Code
def makespan(instance, solution: Chromosome) -> int:
    """_summary_

    Args:
        instance (_type_): _description_
        solution (Chromosome): _description_

    Returns:
        int: _description_
    """
    
    nM = len(instance)
    tempo = [0] * nM
    tarefa = [0] * len(solution)
    for t in solution.data:
        # print(f"ITERATING VALUE >>> {t} <<<")
        if tarefa[t-1] == 1:
            return "SOLUÇÃO INVÁLIDA: tarefa repetida!"
        else:
            tarefa[t-1] = 1

        for m in range (nM):
            if tempo[m] < tempo[m-1] and m!=0:
                tempo[m] = tempo[m-1] 
            tempo[m] += instance[m][t-1] 
    return tempo[nM-1]
    