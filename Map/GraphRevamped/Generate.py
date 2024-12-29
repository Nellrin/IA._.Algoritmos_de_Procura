from .Node import Node

################################
# Encontrar nodo pelo nome
################################

def get_node_by_name(self, name):
    search_node = Node(name)
    for node in self.m_nodes:
        if node == search_node:
            return node
        else:
            return None

#############################
# Adicionar   aresta no grafo
#############################

def add_edge(self, node1, node2, weight):
    n1 = Node(node1)
    n2 = Node(node2)
    if (n1 not in self.m_nodes):
        self.m_nodes.append(n1)
        self.m_graph[node1] = list()
    else:
        n1 = self.get_node_by_name(node1)

    if (n2 not in self.m_nodes):
        self.m_nodes.append(n2)
        self.m_graph[node2] = list()
    else:
        n2 = self.get_node_by_name(node2)

    self.m_graph[node1].append((node2, weight))


    if not self.m_directed:
        self.m_graph[node2].append((node1, weight))

##########################################################################
#  add_heuristica   -> define heuristica para cada nodo
##########################################################################

def add_heuristica(self, n, estima):
    n1 = Node(n)
    if n1 in self.m_nodes:
        self.m_h[n] = estima

#######################################################################
#    heuristica   -> define heuristica para cada nodo 1 por defeito....
#    apenas para teste de pesquisa informada
#######################################################################

def heuristica(self):
    nodos = self.m_graph.keys
    for n in nodos:
        self.m_h[n] = 1
    return (True)