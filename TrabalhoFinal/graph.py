# coding: utf-8

class Graph(object):
    '''Definiçoes da estrutura do grafo e funções de algoritmos auxiliares'''
    def __init__(self):
        self.n = 0      # numero de vertices
        self.m = 0      # numero de arestas
        self.d = 0      # desvio medio
        self.arestas = {}
        self.pesos = {}

    def read_file(self, arquivo):
        self.n = int(arquivo.readline())
        for line in arquivo:
            u, v, p = map(str, line.split())
            key = str(u) + str(v)
            if u not in self.arestas:
                self.arestas[u] = [v]
                self.pesos[key] = [p]
                self.m = self.m + 1
            else:
                self.arestas[u].append(v)
                self.pesos[key] = [p]
                self.m = self.m + 1
        self.d = 2 * self.m/self.n

    def write_file(self, arquivo):
        output = '# n = ' + str(self.n) + '\n'
        output += '# m = ' + str(self.m) + '\n'
        output += '# d_medio = ' + str(self.d) + '\n'
        arquivo.write(output)

    def bfs(self, inicio):
        q = []
        visitado = []
        pais = {}
        q.append(inicio)
        visitado.append(inicio)
        print(inicio, end='\t')
        while len(q) != 0:
            u = q.pop(0)
            for vertice in self.arestas[u]:
                if vertice not in visitado:
                    pais.update({vertice: u})
                    visitado.append(vertice)
                    q.append(vertice)
                    print(vertice, end='\t')
        print('\n')

    def dfs(self, visitado=[], ordem=[]):
        for vertice in self.arestas:
            if vertice not in visitado:
                print(vertice, end='\t')
                self.dfs_visita(vertice, visitado, ordem)
        print('\n')

    def dfs_visita(self, vertice, visitado, ordem):
        visitado.append(vertice)
        if vertice in self.arestas:
            for vertice_aux in self.arestas[vertice]:
                if vertice_aux not in visitado:
                    print(vertice_aux, end='\t')
                    self.dfs_visita(vertice_aux, visitado, ordem)
            ordem.insert(0, vertice)
        else:
            ordem.append(vertice)

    def ordenacao_topologica(self):
        visitado = []
        ordem = []
        self.dfs(visitado, ordem)
        print(ordem)

    def print_graph(self):
        print('*** GRAFO DETALHADO ***')
        print('# n = ' + str(self.n))
        print('# m = ' + str(self.m))
        print('# d_medio = ' + str(self.d) + '\n')
        print('# conjunto arestas:')
        print(self.arestas)
        print('\n')
        print('# relação arestas e peso:')
        print(self.pesos)
        print('\n')
