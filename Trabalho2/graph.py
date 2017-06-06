import sys, os


def out(fin, fout):

    grafo = {}
    m = 0

    for line in fin:
        if ' ' in line:
            u, v, p = map(str, line.split())
            if u not in grafo:
                grafo[u] = [v]
            else:
                grafo[u].append(v)

    for vertice in grafo.keys():
        for aresta in grafo.get(vertice):
            m += 1


    n = len(grafo)

    output = '# n = ' + str(n) + '\n'
    output += '# m = ' + str(m) + '\n'
    output += '# d_medio = ' + str(2*m/n) + '\n'
    fout.write(output)
