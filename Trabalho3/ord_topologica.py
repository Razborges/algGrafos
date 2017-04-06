# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de implementação do algoritmo DFS com ordenação topológica para uso em grafo dirigido
'''

import sys, os

def dfs_recursivo(grafo, visitado, ordem):
    for vertice in grafo:
        if vertice not in visitado:
            dfs_recursivo_visita(grafo, vertice, visitado, ordem)

def dfs_recursivo_visita(grafo, vertice, visitado, ordem):
    visitado.append(vertice)
    if(vertice in grafo):
        for vertice_aux in grafo[vertice]:
            if vertice_aux not in visitado:
                dfs_recursivo_visita(grafo, vertice_aux, visitado, ordem)
        ordem.insert(0, vertice)
    else:
        ordem.append(vertice)

def dfs_recursao(grafo):
    visitado = []
    ordem = []
    dfs_recursivo(grafo, visitado, ordem)
    print(ordem)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.stderr.write('Erro na chamada do comando.\n')
        sys.stderr.write('Para executar digite: \'python ord_topologica.py NOME_ARQUIVO.TXT >>> onde NOME_ARQUIVO.TXT é o nome do arquivo que contém o grafo.\n')
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

    print('*** Ordenação Topológica do Grafo ***')
    dfs_recursao(grafo)