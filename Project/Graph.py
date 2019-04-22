import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
def build_G1(n=5000):
    G = nx.Graph()
    arr = np.arange(n-1)
    G.add_nodes_from(arr)
    mu, sigma = 100, 20  # mean and standard deviation
    e = np.random.normal(mu, sigma, 3*n)
    for i in range(3*n):
        x = random.randint(0,n)
        y = random.randint(0, n)
        while x==y:
            y = random.randint(0, n)
        G.add_edge(x,y,weight=e[i])
    return G

def build_G2(n=5000):
    G = nx.Graph()
    arr = np.arange(n-1)
    G.add_nodes_from(arr)
    mu, sigma = 100, 20
    e = np.random.normal(mu, sigma,6000*1000)
    
    for i in range(5000):
        for j in range(550):
            y=int(random.random()*5000)
            G.add_edge(i, y, weight=e[i*1000+j])
    
    return G


def main():
    random.seed(1)
    G = build_G1()
    #build_G2()
    print(G.nodes)

if __name__ == "__main__":
    main()
