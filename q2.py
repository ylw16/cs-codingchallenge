import numpy as np
import itertools

def question02(cashFlowIn, cashFlowOut):
    in_sumsets = sum_subsets(powerset(cashFlowIn),0)
    out_sumsets = sum_subsets(powerset(cashFlowOut),1)
    
    mixed_sumsets = np.array(sorted(in_sumsets+out_sumsets))
    num_sumsets = [num_sumsets for [num_sumsets] in mixed_sumsets[:,[0]]]
    type_sumsets = [type_sumsets for [type_sumsets] in mixed_sumsets[:,[1]]]
    
    diff_num = np.diff(num_sumsets) 
    diff_type = np.diff(type_sumsets)
    diff_num[0] = max(diff_num)
    for n in range(len(diff_type)):
        if diff_type[n] == 0:
            diff_num[n] = max(diff_num)
    answer = min(diff_num)
    return answer


def powerset(iterable):
    """computes all subsets of iterable"""
    subsets = []
    for r in range(len(iterable)+1):
        subsets = subsets + list(itertools.combinations(iterable, r))
    return subsets

def sum_subsets(subsets,type):
    sumsets = []
    for r in range(len(subsets)):
        sumsets.append([sum(subsets[r]),type])
    return sumsets



