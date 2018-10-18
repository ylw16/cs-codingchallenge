import numpy as np
import itertools

def question01(portfolios):
    """computes the maximum evaluated value of a combined portfolio"""
    bin_ports = binary_portfolios(portfolios)
    two_binports = list(itertools.combinations(bin_ports, 2))
    comb_port = 0
    best_comb = 0
    for r in range(len(two_binports)):
        comb_port = combined_portfolio(two_binports[r][0],two_binports[r][1])
        if comb_port > best_comb:
            best_comb = comb_port
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
            