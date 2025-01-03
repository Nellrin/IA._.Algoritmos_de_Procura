
import matplotlib.pyplot as plt
import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo

#############
# Escrever o grafo como string
#############
def _str_(self):
    out = ""
    for key in self.m_graph.keys():
        out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
    

##############################3
# Imprimir arestas
############################333333

def imprime_aresta(self):
    listaA = ""
    lista = self.m_graph.keys()
    for nodo in lista:
        for (nodo2, custo) in self.m_graph[nodo]:
            listaA = listaA + "(" + nodo.rjust(11) + " -> " + nodo2.ljust(11) + ") {" + str(custo).rjust(2) + "}\n"
    return listaA[:-1]

###############################
#  Desenha grafo  modo grafico
###############################

def desenha(self):
    ##criar lista de vertices
    lista_v = self.m_nodes
    lista_a = []
    g = nx.Graph()
    for nodo in lista_v:
        n = nodo.getName()
        g.add_node(n)
        for (adjacente, peso) in self.m_graph[n]:
            lista = (n, adjacente)
            # lista_a.append(lista)
            g.add_edge(n, adjacente, weight=peso)

    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.draw()
    plt.show()