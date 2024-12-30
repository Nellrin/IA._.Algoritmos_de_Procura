import math

#############################
# Devolver nodos do Grafo
############################

def getNodes(self):
    return self.m_nodes

###############################
# Devolver o custo de uma aresta
################################

def get_arc_cost(self, node1, node2):
    custoT = math.inf
    a = self.m_graph[node1]  # lista de arestas para aquele nodo
    for (nodo, custo) in a:
        if nodo == node2:
            custoT = custo

    return custoT

##############################
#  Dado um caminho calcula o seu custo
###############################

def calcula_custo(self, caminho):
    # caminho é uma lista de nodos
    teste = caminho
    custo = 0
    i = 0
    while i + 1 < len(teste):
        custo += self.get_arc_cost(teste[i], teste[i + 1])
        #print(teste[i])
        i = i + 1
    return custo

###################################################
# Função   getneighbours, devolve vizinhos de um nó
####################################################

def getNeighbours(self, nodo):
    lista = []
    if nodo in self.m_graph:
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
    return lista

##########################################3
#
def calcula_est(self, estima):
    l = list(estima.keys())
    min_estima = estima[l[0]]
    node = l[0]
    for k, v in estima.items():
        if v < min_estima:
            min_estima = v
            node = k
    return node

###################################3
# devolve heuristica do nodo
####################################

def getH(self, nodo):
    if nodo not in self.m_h.keys():
        return 1000
    else:
        return (self.m_h[nodo])
