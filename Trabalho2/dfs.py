# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de implementação do algoritmo DFS (Busca em profundidade em Grafo) imprimindo todos os vértices do grafo
'''

def imprimindo_vertices_dfs_recursivo(grafo, visitado):
    for vertice in grafo:
        if vertice not in visitado:
            print(vertice, end='\t')
            visita_dfs(grafo, vertice, visitado)
    print('')

def visita_dfs(grafo, vertice, visitado):
    visitado.append(vertice)
    for vertice_aux in grafo[vertice]:
        if vertice_aux not in visitado:
            print(vertice_aux, end='\t')
            visita_dfs(grafo, vertice_aux, visitado)

def imprimindo_vertices_dfs_iterativo(grafo, visitado, pilha):
    for vertice in grafo:
        if vertice not in visitado:
            iterativo_dfs(grafo, vertice, visitado, pilha)
    print('')

def iterativo_dfs(grafo, vertice, visitado, pilha):
    pilha.append(vertice)
    while len(pilha) != 0:
        vertice = pilha.pop(0)
        if vertice not in visitado:
            visitado.append(vertice)
            print(vertice, end='\t')
            for vertice_aux in grafo[vertice]:
                pilha.append(vertice_aux)

if __name__ == '__main__':
    grafo = {
        '1': ['2', '4', '5'],
        '2': ['1', '4', '6'],
        '3': ['7'],
        '4': ['1', '2', '5'],
        '5': ['1', '4'],
        '6': ['2'],
        '7': ['3']
    }

    visitado = []
    visitado2 = []
    pilha = []

    print('Vertices usando DFS Recursivo:')
    imprimindo_vertices_dfs_recursivo(grafo, visitado)
    print('Vertices usando DFS Iterativo:')
    imprimindo_vertices_dfs_iterativo(grafo, visitado2, pilha)