# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de Algoritmo em Grafos aplicado pelo Prof. Glauco Amorim para medição do tempo da criação de uma
matriz 10 x 10, outra de 100 x 100 e outra 1000 x 1000.
Medição também do tempo de uma multiplicação entre matrizes.
'''

import sys, os
from random import randint
import timeit

def montar_matriz(linha, coluna):
    matriz = []
    for i in range(int(linha)):
        linha_matriz = []
        for j in range(int(coluna)):
            num = randint(0, 100)
            linha_matriz.append(num)
        matriz.append(linha_matriz)
    return matriz

def multiplicar_matriz(matriz_a, matriz_b):
    produto = []
    linha = len(matriz_a)
    coluna = len(matriz_b[0])
    for i in range(int(linha)):
        linha_matriz = []
        for j in range(int(coluna)):
            val = 0
            for k in range(int(len(matriz_b))):
                val = val + matriz_a[i][k] * matriz_b[k][j]
            linha_matriz.append(val)
        produto.append(linha_matriz)
    return produto

def imprime_matriz(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            print(matriz[i][j], end='\t')
        print()


if __name__ == '__main__':

    if len(sys.argv) == 3:
        linha = sys.argv[1]
        coluna = sys.argv[2]
        inicio = timeit.default_timer()
        matriz = montar_matriz(linha, coluna)
        fim = timeit.default_timer()
        imprime_matriz(matriz)
        print(fim - inicio)

    if len(sys.argv) == 5:
        linha_a = sys.argv[1]
        coluna_a = sys.argv[2]
        linha_b = sys.argv[3]
        coluna_b = sys.argv[4]
        if coluna_a == linha_b:
            matriz_A = montar_matriz(linha_a, coluna_a)
            matriz_B = montar_matriz(linha_b, coluna_b)
            imprime_matriz(matriz_A)
            imprime_matriz(matriz_B)
            inicio = timeit.default_timer()
            matriz = multiplicar_matriz(matriz_A, matriz_B)
            fim = timeit.default_timer()
            imprime_matriz(matriz)
            print(fim - inicio)
        else:
            sys.stderr.write('Erro, é preciso que o número de colunas de A seja igual ao número de linhas de B.\n')
            sys.exit()

    else:
        sys.stderr.write('Erro na chamada do comando.\n')
        sys.stderr.write('Para executar digite: \'python matriz_time.py [TAM_LINHA_A] [TAM_COLUNA_A]\' para criar uma matriz,\n')
        sys.stderr.write('ou utilize: \'python matriz_time.py [TAM_LINHA_a] [TAM_COLUNA_a] [TAM_LINHA_b] [TAM_COLUNA_b]\' para multiplicar matrizes.\n')
        sys.exit()
