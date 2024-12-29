#from .Algoritmos.Aest import procura_aStar
#from .Algoritmos.BFS import procura_BFS
#from .Algoritmos.DFS import procura_DFS
#from .Algoritmos.Greedy import greedy

from .Search import getNodes, get_arc_cost, calcula_custo, getNeighbours, calcula_est, getH
from .Event import eventoAleatorio, atualizaEvento, decrement_life
from .Generate import get_node_by_name, add_edge, add_heuristica, heuristica
from .Draw import _str_, imprime_aresta, desenha

class Graph:

    def __init__(self, recursos, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para heuristicas e tempo de vida dos nodos
        self.m_recursos = recursos

    def __str__(self):                                          return _str_(self)
    def get_node_by_name(self, name):                           return get_node_by_name(self,name)
    def imprime_aresta(self):                                   return imprime_aresta(self)
    def add_edge(self, node1, node2, weight):                   add_edge(self,node1,node2,weight)
    def eventoAleatorio(self):                                  return eventoAleatorio(self)
    def atualizaEvento(self, nodo_inicial, nodo_final):         atualizaEvento(self, nodo_inicial, nodo_final)
    def getNodes(self):                                         return getNodes(self)
    def get_arc_cost(self, node1, node2):                       return get_arc_cost(self, node1, node2)
    def calcula_custo(self, caminho):                           return calcula_custo(self, caminho)
    #def procura_DFS(self, start, end, path=[], visited=set()):  return procura_DFS(self, start, end, path=[], visited=set())
    #def procura_BFS(self, start, end):                          return procura_BFS(self, start, end)
    def getNeighbours(self, nodo):                              return getNeighbours(self, nodo)
    def desenha(self):                                          desenha(self)
    def add_heuristica(self, n, estima):                        add_heuristica(self, n, estima)
    def decrement_life(self, cidadesVisitadas):                 decrement_life(self, cidadesVisitadas)
    def heuristica(self):                                       return heuristica(self)
    def calcula_est(self, estima):                              return calcula_est(self, estima)
    #def procura_aStar(self, start, end):                        return procura_aStar(self, start, end)
    def getH(self, nodo):                                       return getH(self, nodo)
    #def greedy(self, start, end):                               return greedy(self,start,end)