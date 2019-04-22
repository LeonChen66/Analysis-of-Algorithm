import networkx as nx
from MaxHeap import MaxHeap
import matplotlib.pyplot as plt
import Graph
import time

def maxfringe(bw, status, V):
    tempBW = 0
    TempStatus = 0
    for i in range(V):
        if status[i] == 1 and tempBW < bw[i]:
            tempBW = bw[i]
            TempStatus = i
    return TempStatus

def dijkstraWithHeap(G, s, t):
    V = len(G.nodes)
    bw = [0]*V
    parent = [-1]*V
    status = [2]*V
    heap = MaxHeap()

    status[s] = 0
    bw[s] = float('inf')

    for v in G[s]:
        bw[v] = G[s][v]['weight']
        parent[v] = s
        status[v] = 1
        heap.push((bw[v],v))

    while status[t] != 0:
        d,v = heap.pop()
        # print(v,end=" ")
        status[v] = 0
        for w in G[v]:
            if status[w] == 2:
                bw[w] = min(bw[v], G[v][w]['weight'])
                parent[w] = v
                status[w] = 1
                heap.push((bw[w],w))
            elif status[w] == 1 and bw[w] < min(bw[v], G[v][w]['weight']):
                #heap.delete(w)
                bw[w] = min(bw[v], G[v][w]['weight'])
                parent[w] = v
                heap.push((bw[w], w))
    return bw, parent


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge(0, 1, weight=4)
    G.add_edge(1, 2, weight=4)
    # G.add_edge(1, 3, weight=2)
    G.add_edge(3, 2, weight=3)
    G.add_edge(2, 4, weight=4)
    G.add_edge(4, 5, weight=10)
    print(dijkstraWithHeap(G, 0, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    # G = Graph.build_G1()
    # start = time.clock()
    # dijkstraWithHeap(G,1,100)
    # print(time.clock()-start)
