import numpy as np
import itertools

def question01(portfolios):
    """computes the maximum evaluated value of a combined portfolio"""
    two_ports = list(itertools.combinations(portfolios, 2))
    comb_port = []
    result = 0
    for r in range(len(two_ports)):
        comb_port = int(two_ports[r][0]) ^ int(two_ports[r][1])
        if comb_port > result:
            result = comb_port
    return result
