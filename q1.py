import itertools

def question01(portfolios):
    """computes the maximum evaluated value of a combined portfolio"""
    two_ports = list(itertools.combinations(portfolios, 2))
    comb_port = []
    result = 0
    for port1, port2 in two_ports:
        comb_port = port1 ^ port2
        if comb_port > result:
            result = comb_port
            
    # max(port1 ^ port2 for port1, port2 in two_ports, key=lambda x: bin(x).count('1'))
    return result
