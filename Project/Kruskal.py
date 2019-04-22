from itertools import count
import networkx as nx
from networkx.utils import UnionFind
import time
import Graph

def minimum_spanning_edges(G, weight='weight', data=True):
    subtrees = [i for i in range(5001)]
    edges = sorted(G.edges(data=True),
                   key=lambda t: t[2].get(weight, 1), reverse=True)
    res = []
    for u, v, d in edges:
        if not connected(subtrees, u, v):
            if data:
                res.append((u,v,d))
                # yield (u, v, d)
            else:
                res.append((u,v))
                # yield (u, v)
            union(subtrees,u, v)

def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]


def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


def connected(data, i, j):
    return find(data, i) == find(data, j)

if __name__ == "__main__":
    # G = nx.Graph()
    # G.add_edge(0, 1, weight=4)
    # G.add_edge(1, 2, weight=4)
    # G.add_edge(1, 3, weight=2)
    # G.add_edge(3, 2, weight=3)
    # G.add_edge(2, 4, weight=4)
    # G.add_edge(4, 5, weight=10)
    # mst = minimum_spanning_edges(G)
    # edgelist = list(mst)
    # print(edgelist)
    G = Graph.build_G1()
    start = time.clock()
    minimum_spanning_edges(G)
    print(time.clock()-start)
