import sys, os
from Grafo import Grafo

if __name__ == '__main__':

    try:
        arquivo1 = open('grafo_teste_caminho_bfs.txt', 'r')
        arquivo2 = open('grafo_teste_caminho_dji.txt', 'r')
    except IOError:
        sys.stderr.write('Erro ao tentar ler ou criar o arquivo, verifique se estão válidos.\n')
        sys.exit()

    grafo1 = Grafo()
    grafo1.ler_arquivo(arquivo1)
    print('***MENOR CAMINHO GRAFO SEM PESO***')
    print('- Com início e sem fim')
    grafo1.menor_caminho('2')
    print('- Com início e com fim')
    grafo1.menor_caminho('2', '4')

    grafo2 = Grafo()
    grafo2.ler_arquivo(arquivo2)
    print('***MENOR CAMINHO GRAFO COM PESO***')
    print('- Com início e sem fim')
    grafo2.menor_caminho('3')
    print('- Com início e com fim')
    grafo2.menor_caminho('3', '4')

    try:
        arquivo1.close()
        arquivo2.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar os arquivos.\n')
        sys.exit()
