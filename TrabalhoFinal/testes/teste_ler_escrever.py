import sys, os
from Grafo import Grafo

if __name__ == '__main__':

    try:
        arquivo = open('grafo_teste_ler_escrever.txt', 'r')
        arquivo_saida = open('teste_ler_escrever.txt', 'w')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)
    grafo.escrever_arquivo(arquivo_saida)

    try:
        arquivo.close()
        arquivo_saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar os arquivos.\n')
        sys.exit()