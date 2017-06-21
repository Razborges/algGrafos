# coding: utf-8

import sys
from Grafo import Grafo

def um(grafo):
    arquivo_saida = _arquivo_saida()
    grafo.escrever_arquivo(arquivo_saida)
    _fechando_arquivo_saida(arquivo_saida)
    escolha_de_caso(grafo)

def dois(grafo):
    tipo = input('Deseja imprimir em arquivo?S/N ')
    if tipo.upper() == 'S':
        arquivo_saida = _arquivo_saida()
        grafo.matriz(arquivo_saida)
        _fechando_arquivo_saida(arquivo_saida)
    else:
        grafo.matriz()
    escolha_de_caso(grafo)

def tres(grafo):
    tipo = input('Deseja imprimir em arquivo?S/N ')
    if tipo.upper() == 'S':
        arquivo_saida = _arquivo_saida()
        grafo.lista(arquivo_saida)
        _fechando_arquivo_saida(arquivo_saida)
    else:
        grafo.lista()
    escolha_de_caso(grafo)

def quatro(grafo):
    arquivo_saida = _arquivo_saida()
    inicio = input('Digite o vértice por onde deverá iniciar a busca: ')
    grafo.bfs_arquivo(arquivo_saida, inicio)
    _fechando_arquivo_saida(arquivo_saida)
    escolha_de_caso(grafo)

def cinco(grafo):
    arquivo_saida = _arquivo_saida()
    inicio = input('Digite o vértice por onde deverá iniciar a busca: ')
    grafo.dfs_arquivo(arquivo_saida, inicio)
    _fechando_arquivo_saida(arquivo_saida)
    escolha_de_caso(grafo)

def seis(grafo):
    inicio = input('Digite o vértice por onde deverá iniciar a busca de componentes conexos: ')
    print('\n')
    grafo.conexo(inicio)
    print('\n')
    escolha_de_caso(grafo)

def sete(grafo):
    inicio = input('Digite o vértice por onde deverá iniciar o caminho: ')
    fim = input('Digite o vértice onde deve terminar o caminho ou tecle ENTER para deixar em branco: ')
    if fim:
        print('\n')
        grafo.menor_caminho(inicio, fim)
        print('\n')
    else:
        print('\n')
        grafo.menor_caminho(inicio)
        print('\n')
    escolha_de_caso(grafo)

def escolha_de_caso(grafo):
    print('Escolha uma das opções abaixo:')
    print('1 - Imprimir em arquivo as informações detalhadas deste grafo.')
    print('2 - Representar o grafo como uma matriz de adjacência.')
    print('3 - Representar o grafo como uma lista de adjacência.')
    print('4 - Busca em Largura (BFS).')
    print('5 - Busca em Profundidade (DFS).')
    print('6 - Descobrir componentes conexos.')
    print('7 - Distância e Caminho Mínimo.')
    print('0 - Sair.')

    num = int(input('Digite uma das opções numéricas: '))

    if num == 1: um(grafo)
    elif num == 2: dois(grafo)
    elif num == 3: tres(grafo)
    elif num == 4: quatro(grafo)
    elif num == 5: cinco(grafo)
    elif num == 6: seis(grafo)
    elif num == 7: sete(grafo)
    elif num == 0:
        sys.exit()
    else:
        print('Você não digitou nenhum valor válido.')
        escolha_de_caso(grafo)

def _arquivo_saida():
    saida = input('Escreva o nome do arquivo de saída: ')
    try:
        arquivo_saida = open(saida, 'w')
    except IOError:
        sys.stderr.write('Não foi possível criar o arquivo.\n')
        sys.exit()
    return arquivo_saida

def _fechando_arquivo_saida(saida):
    try:
        saida.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('Arquivo criado com sucesso.\n')


if __name__ == '__main__':

    print('\n***Siga as orientações abaixo para excutar o processamento desejado***\n')
    arquivoGrafo = input('Digite o endereço do arquivo que possui o grafo: ')

    try:
        arquivo = open(arquivoGrafo, 'r')
    except IOError:
        sys.stderr.write('Não foi encontrado nenhum arquivo válido.\n')
        sys.exit()

    grafo = Grafo()
    grafo.ler_arquivo(arquivo)

    try:
        arquivo.close()
    except IOError:
        sys.stderr.write('Erro ao tentar fechar o arquivo.\n')
        sys.exit()

    print('O grafo foi gerado corretamente.\n')

    escolha_de_caso(grafo)