import networkx as nx

def maxfringe(bw, status, V):
	tempBW = 0
	TempStatus = 0
	for i in range(V):
		if status[i] == 1 and tempBW < bw[i]:
			tempBW = bw[i]
			TempStatus = i
	return TempStatus


def dijkstra(G, s, t):
	V = len(G.nodes)
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V
	status[s] = 0
	bw[s] = float('inf')

	for v in G[s]:
		bw[v] = G[s][v]['weight']
		parent[v] = s
		status[v] = 1

	while 1 in status:
		v = maxfringe(bw, status, V)
		status[v] = 0
		# print(v,len(neighbors))
		for w in G[v]:
			if status[w] == 2:
				bw[w] = min(bw[v], G[v][w]['weight'])
				parent[w] = v
				status[w] = 1
			elif status[w] == 1 and bw[w] < min(bw[v], G[v][w]['weight']):
				bw[w] = min(bw[v], G[v][w]['weight'])
				parent[w] = v
	return bw, parent


if __name__ == "__main__":
	G = nx.Graph()
	G.add_edge(0, 1, weight=4)
	G.add_edge(1, 2, weight=4)
	G.add_edge(1, 3, weight=2)
	G.add_edge(3, 2, weight=3)
	G.add_edge(2, 4, weight=4)
	G.add_edge(4, 5, weight=10)
	print(dijkstra(G, 0, 4))
