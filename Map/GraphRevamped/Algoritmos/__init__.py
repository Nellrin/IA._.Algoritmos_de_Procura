from .Aest import procura_aStar
from .BFS import procura_BFS
from .DFS import procura_DFS
from .Greedy import greedy

from ..Graph import Graph

Graph.procura_BFS = procura_BFS
Graph.procura_aStar = procura_aStar
Graph.procura_DFS = procura_DFS
Graph.greedy = greedy