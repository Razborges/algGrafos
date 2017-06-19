# coding: utf-8

import sys
from Grafo import Grafo

if __name__ == '__main__':

    sys.setrecursionlimit(60000)

    try:
        arquivo = open('grafo_teste_dfs_conexo.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.conexo('1')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE DFS CONEXO FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_1.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.conexo('22')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE DFS GRAFO 1 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_2.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.conexo('338')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE DFS GRAFO 2 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_3.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.conexo('2417')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE DFS GRAFO 3 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_4.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.conexo('24498')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE DFS GRAFO 4 FINALIZADO ***')
