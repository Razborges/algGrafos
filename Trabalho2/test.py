import graph

fin = open('../grafos-de-entrada/grafo_1.txt', 'r')
fout = open('out.txt', 'w')

graph.bfs(fin, fout, 26)
