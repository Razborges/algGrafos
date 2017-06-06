# coding: utf-8

import sys, os
from Grafo import Grafo

if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.stderr.write('Erro na chamada do comando.\n')
        sys.stderr.write('Para executar digite: \'python teste.py NOME_ARQUIVO_ENTRADA.TXT NOME_ARQUIVO_SAIDA.TXT\n')
        sys.exit()

    nome_arquivo_entrada = sys.argv[1]
    nome_arquivo_saida = sys.argv[2]

    try:
        arquivo = open(nome_arquivo_entrada, 'r')
        arquivo_saida = open(nome_arquivo_saida, 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.escrever_arquivo(arquivo_saida)
    grafo.imprimir_grafo()

    print('*** TESTE BFS ***')
    grafo.bfs('1')
    print('*** TESTE DFS ***')
    grafo.dfs()
    print('*** TESTE ORDENAÇÃO TOPOLÓGICA ***')
    grafo.ordenacao_topologica()

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar os arquivos.\n')
        sys.exit()
        sys.exit()
