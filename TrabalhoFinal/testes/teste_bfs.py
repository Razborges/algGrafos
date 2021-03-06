# coding: utf-8

import sys
from Grafo import Grafo

if __name__ == '__main__':

    try:
        arquivo = open('grafo_teste_bfs.txt', 'r')
        arquivo_saida = open('teste_bfs.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.bfs_arquivo(arquivo_saida, '1')

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE BFS FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_1.txt', 'r')
        arquivo_saida = open('teste_bfs_grafo1.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.bfs_arquivo(arquivo_saida, '22')

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE BFS GRAFO 1 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_2.txt', 'r')
        arquivo_saida = open('teste_bfs_grafo2.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.bfs_arquivo(arquivo_saida, '338')

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE BFS GRAFO 2 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_3.txt', 'r')
        arquivo_saida = open('teste_bfs_grafo3.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.bfs_arquivo(arquivo_saida, '2417')

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE BFS GRAFO 3 FINALIZADO ***')

    try:
        arquivo = open('./../grafos-de-entrada/grafo_4.txt', 'r')
        arquivo_saida = open('teste_bfs_grafo4.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.bfs_arquivo(arquivo_saida, '24498')

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('*** TESTE BFS GRAFO 4 FINALIZADO ***')
