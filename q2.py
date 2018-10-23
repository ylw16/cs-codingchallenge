import numpy as np
import more_itertools

def question02(cashFlowIn, cashFlowOut):
    
    in_sumsets = sum_subsets(list(more_itertools.powerset(cashFlowIn)),0)
    out_sumsets = sum_subsets(list(more_itertools.powerset(cashFlowOut)),1)
    
    mixed_sumsets = np.array(sorted(in_sumsets+out_sumsets))
    diff = np.diff(mixed_sumsets,axis=0)
    diff[0,0] = 100
    for n in range(2,len(diff)):
        if diff[n,1] == 0:
            diff[n,0] = 100
    answer = int(min(diff[:,0]))
    return answer

def sum_subsets(subsets,type):
    sumsets = []
    for r in range(len(subsets)):
        sumsets.append([sum(subsets[r]),type])
    return sumsets