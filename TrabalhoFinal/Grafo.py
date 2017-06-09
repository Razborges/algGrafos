# coding: utf-8

class Grafo(object):
    '''Definiçoes da estrutura do grafo e funções de algoritmos auxiliares'''
    def __init__(self):
        self.n = 0      # numero de vertices
        self.m = 0      # numero de arestas
        self.d = 0      # desvio medio
        self.arestas = {}
        self.pesos = {}
        self.distribuicao_graus = {}

    def ler_arquivo(self, arquivo):
        self.n = int(arquivo.readline())
        for line in arquivo:
            u, v, p = map(str, line.split())
            key = str(u) + '-' + str(v)
            if u not in self.arestas:
                self.arestas[u] = [v]
                self.pesos[key] = [p]
                self.m = self.m + 1
            else:
                self.arestas[u].append(v)
                self.pesos[key] = [p]
                self.m = self.m + 1

            if v not in self.arestas:
                self.arestas[v] = [u]
            else:
                self.arestas[v].append(u)
        self.d = 2 * self.m/self.n
        self.graus_empiricos()
        print('----------- FINALIZANDO LEITURA DO GRAFO ----------------')

    def escrever_arquivo(self, arquivo):
        texto = '# n = ' + str(self.n) + '\n'
        texto += '# m = ' + str(self.m) + '\n'
        texto += '# d_medio = ' + str(self.d) + '\n'
        for m in self.distribuicao_graus:
            grau = self.distribuicao_graus[m]/self.n
            texto += str(m) + ' ' + str(grau) + '\n'
        arquivo.write(texto)

    def lista(self, arquivo=None):
        texto = ''
        for u in self.arestas:
            texto += u + ' '
            for v in self.arestas.get(u):
                texto += '->' + v + ' '
            texto += '\n'
        if arquivo:
            arquivo.write(texto)
        else:
            print(texto)

    def matriz(self, arquivo=None):
        texto = ''
        texto += '  '
        for u in self.arestas:
            texto += u + ' '
        texto += '\n'
        for u in self.arestas:
            texto += u + ' '
            for v in self.arestas:
                if v in self.arestas[u]:
                    texto += '1' + ' '
                else:
                    texto += '0' + ' '
            texto += '\n'
        if arquivo:
            arquivo.write(texto)
        else:
            print(texto)

    def bfs(self, inicio):
        q = []
        visitado = []
        pais = {}
        arvore = {}
        count = 0
        q.append(inicio)
        arvore[inicio] = count
        visitado.append(inicio)
        #print(inicio, end='\t')
        while len(q) != 0:
            u = q.pop(0)
            count += 1
            for vertice in self.arestas[u]:
                if vertice not in visitado:
                    pais.update({vertice: u})
                    arvore[vertice] = count
                    visitado.append(vertice)
                    q.append(vertice)
                    #print(vertice, end='\t')
        #print('\n')
        #print(pais)
        #print(arvore)
        print('-------------- FINALIZANDO O BFS ---------------')
        return pais, arvore

    def bfs_arquivo(self, arquivo, inicio):
        pais, arvore = self.bfs(inicio)
        texto = 'Pais dos vértices do Grafo:\n'
        for chave in pais:
            texto += 'Vertice ' + str(chave) + ': pai = ' + str(pais[chave]) + '\n'
        texto += '\n' + 'Nível dos vértices na árvore:\n'
        for chave in arvore:
            texto += 'Vertice ' + str(chave) + ': está no nível ' + str(arvore[chave]) + '\n'
        arquivo.write(texto)
        print('---------- FINALIZANDO ESCRITA DO ARQUIVO DE SAIDA ------------')

    def dfs(self, inicio, visitado=[], ordem=[]):
        visitado.append(inicio)
        print(inicio, end='\t')
        for vertice in self.arestas:
            if vertice not in visitado:
                print(vertice, end='\t')
                self.dfs_visita(vertice, visitado, ordem)
        print('\n')
        ordem.insert(0, inicio)

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

    def ordenacao_topologica(self, inicio):
        visitado = []
        ordem = []
        self.dfs(inicio, visitado, ordem)
        print(ordem)

    def graus_empiricos(self):
        for m in self.arestas:
            grau = len(self.arestas[m])
            if grau not in self.distribuicao_graus:
                self.distribuicao_graus[grau] = 1
            else:
                self.distribuicao_graus[grau] = self.distribuicao_graus[grau] + 1


    def imprimir_grafo(self):
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
        print('# distribuiçao dos graus:')
        print(self.distribuicao_graus)
