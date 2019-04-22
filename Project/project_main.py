import Graph
import Dijkstra_heap
import Dijkstra_ori
import Kruskal
import random
import time

for i in range(5):
    G1 = Graph.build_G1()
    G2 = Graph.build_G2()
    for j in range(5):
        print("%d time try" %(i+1))
        s = random.randint(1,5000)
        t = random.randint(1,5000)

        start = time.clock()
        Dijkstra_heap.dijkstraWithHeap(G1,s,t)
        t_Dheap_G1 = time.clock()
        print("Dijkstra with Heap running time: %f" %(t_Dheap_G1-start))
        Dijkstra_ori.dijkstra(G1,s,t)
        t_Do_G1 = time.clock()
        print("Dijkstra without Heap running time: %f" % (t_Do_G1-t_Dheap_G1))
        Kruskal.minimum_spanning_edges(G1)
        t_Kru_G1 = time.clock()
        print("Kruskal running time: %f" %(t_Kru_G1-t_Do_G1))
        Dijkstra_heap.dijkstraWithHeap(G2, s, t)
        t_Dheap_G2 = time.clock()
        print("Dijkstra with Heap running time: %f" % (t_Dheap_G2-t_Kru_G1))
        Dijkstra_ori.dijkstra(G2, s, t)
        t_Do_G2 = time.clock()
        print("Dijkstra without Heap running time: %f" % (t_Do_G2-t_Dheap_G2))
        Kruskal.minimum_spanning_edges(G2)
        t_Kru_G2 = time.clock()
        print("Kruskal running time: %f" % (t_Kru_G2-t_Do_G2))
