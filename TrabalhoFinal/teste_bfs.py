# coding: utf-8

import sys
from Grafo import Grafo

if __name__ == '__main__':

    try:
        arquivo = open('grafo_teste_bfs.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)

    print('*** TESTE BFS ***')
    grafo.bfs('1')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()
