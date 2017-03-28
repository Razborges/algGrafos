# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de implementação do algoritmo BFS (Busca em largura em Grafo) imprimindo todos os vértices do grafo
'''

def imprime_vertices_bfs(grafo, inicio):
    q = []
    visitado = []
    pais = {}
    q.append(inicio)
    visitado.append(inicio)
    print(inicio)
    while len(q) != 0:
        u = q.pop(0)
        for vertice in grafo[u]:
            if vertice not in visitado:
                pais.update({vertice: u})
                visitado.append(vertice)
                q.append(vertice)
                print(vertice)

if __name__ == '__main__':
    grafo = {
        '1': ['2', '3', '4'],
        '2': ['1', '3', '4'],
        '3': ['1', '2'],
        '4': ['2', '5'],
        '5': ['4']
    }

    imprime_vertices_bfs(grafo, '1')