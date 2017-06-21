import sys, os
from Grafo import Grafo

if __name__ == '__main__':

    try:
        arquivo = open('grafo_teste_listar.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.dijkstra('3', '4')

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar os arquivos.\n')
        sys.exit()
