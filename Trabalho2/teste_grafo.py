# coding: utf-8

__author__ = 'Rafael Borges'

'''
Ex. de teste do uso e leitura de grafos
'''

grafo = {
  '1': ['2', '5'],
  '2': ['1', '3', '5'],
  '3': ['2', '4'],
  '4': ['3', '5', '6'],
  '5': ['1', '2', '4'],
  '6': ['4']
}

def encontra_caminho(grafo, inicio, fim, caminho=None):
    if caminho is None:
        caminho = []
    caminho += [inicio]
    if inicio == fim:
        return caminho
    if not inicio in grafo:
        return None
    for aresta in grafo[inicio]:
        if aresta not in caminho:
            novo_caminho = encontra_caminho(grafo, aresta, fim, caminho)
            if novo_caminho:
                return novo_caminho
    return None

if __name__ == '__main__':
    print(grafo)
    caminho = encontra_caminho(grafo, '1', '6')
    print(caminho)
    caminho = encontra_caminho(grafo, '6', '1')
    print(caminho)
    caminho = encontra_caminho(grafo, '5', '3')
    print(caminho)