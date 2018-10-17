import numpy as np
import itertools
from scipy.special import comb

def question01(portfolios):
    """computes the maximum evaluated value of a combined portfolio"""
    binports = binary_portfolios(portfolios)
    two_binports = list(itertools.combinations(binports, 2))
    combport = 0
    best_comb = 0
    for n in range(int(comb(len(portfolios),2))):
        combport = combined_portfolio(two_binports[n][0],two_binports[n][1])
        if combport > best_comb:
            best_comb = combport
    return best_comb
    
def binary_portfolios(ports):
    """portfolios' binary evaluation value"""
    binports = []
    for dec_portfolio in ports:
        bin_portfolio = np.binary_repr(dec_portfolio, width = 16)
        binports.append(bin_portfolio)
    return binports
        
def combined_portfolio(port1,port2):
    """computes the combined portfolio's decimal evaluation value"""
    combport = []
    for n in range(len(port1)):    
        if port1[n] == port2[n]:
            combport.append(0)
        else:
            combport.append(1)
    combport = ''.join(map(str, combport))
    combport = int(combport,2)
    return combport
            