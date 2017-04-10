# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de implementação do algoritmo BFS (Busca em largura em Grafo) imprimindo todos os vértices do grafo
'''

import sys, os

def bfs(grafo, inicio):
    q = []
    visitado = []
    pais = {}
    q.append(inicio)
    visitado.append(inicio)
    print(inicio, end='\t')
    while len(q) != 0:
        u = q.pop(0)
        for vertice in grafo[u]:
            if vertice not in visitado:
                pais.update({vertice: u})
                visitado.append(vertice)
                q.append(vertice)
                print(vertice, end='\t')
    print('\n')

if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write('Erro na chamada do comando.\n')
        sys.stderr.write('Para executar digite: \'python bfs.py NOME_ARQUIVO.TXT VETOR_INICIO >>> onde NOME_ARQUIVO.TXT é o nome do arquivo que contém o grafo, e, VETOR_INICIO é o valor do vetor por onde deverá começar a ser feita a leitura.\n')
        sys.exit()

    nome_arquivo = sys.argv[1]
    vetor_inicio = sys.argv[2]

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

    print('*** Vertices usando BFS ***')
    bfs(grafo, vetor_inicio)