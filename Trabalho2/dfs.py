# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de implementação do algoritmo DFS (Busca em profundidade em Grafo) imprimindo todos os vértices do grafo
'''
import sys, os


def dfs_recursivo(grafo, visitado):
    for vertice in grafo:
        if vertice not in visitado:
            print(vertice, end='\t')
            dfs_recursivo_visita(grafo, vertice, visitado)
    print('\n')

def dfs_recursivo_visita(grafo, vertice, visitado):
    visitado.append(vertice)
    for vertice_aux in grafo[vertice]:
        if vertice_aux not in visitado:
            print(vertice_aux, end='\t')
            dfs_recursivo_visita(grafo, vertice_aux, visitado)

def dfs_iterativo(grafo, visitado, pilha):
    for vertice in grafo:
        if vertice not in visitado:
            dfs_iterativo_visita(grafo, vertice, visitado, pilha)
    print('\n')

def dfs_iterativo_visita(grafo, vertice, visitado, pilha):
    pilha.append(vertice)
    while len(pilha) != 0:
        vertice = pilha.pop(0)
        if vertice not in visitado:
            visitado.append(vertice)
            print(vertice, end='\t')
            for vertice_aux in grafo[vertice]:
                pilha.append(vertice_aux)

def dfs_recursao(grafo):
    visitado = []
    dfs_recursivo(grafo, visitado)

def dfs(grafo):
    visitado = []
    pilha = []
    dfs_iterativo(grafo, visitado, pilha)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.stderr.write('Erro na chamada do comando.\n')
        sys.stderr.write('Para executar digite: \'python dfs.py NOME_ARQUIVO.TXT >>> onde NOME_ARQUIVO.TXT é o nome do arquivo que contém o grafo.\n')
        sys.exit()

    nome_arquivo = sys.argv[1]

    try:
        arquivo = open(nome_arquivo, 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler o arquivo, verifique se está válido.')
        sys.exit()

    grafo = {}

    for line in arquivo:
        u, v = map(str, line.split())
        if u not in grafo:
            grafo[u] = [v]
        else:
            grafo[u].append(v)

    print('*** Vertices usando DFS Recursivo ***')
    dfs_recursao(grafo)
    print('*** Vertices usando DFS Iterativo ***')
    dfs(grafo)