from queue import Queue

#####################################################
# Procura BFS
######################################################

def procura_BFS(self, start, end):
    # definir nodos visitados para evitar ciclos

    if start not in self.m_graph or end not in self.m_graph:
        return None

    visited = set()
    fila = Queue()

    # adicionar o nodo inicial à fila e aos visitados
    fila.put(start)
    visited.add(start)

    # garantir que o start node nao tem pais...
    parent = dict()
    parent[start] = None

    path_found = False
    while not fila.empty() and not path_found:
        nodo_atual = fila.get()
        if nodo_atual == end:
            path_found = True
        else:
            for (adjacente, peso) in self.m_graph[nodo_atual]:
                if adjacente not in visited and self.m_h.get(adjacente, 0) > 0: #se a cidade ainda permite acesso
                    fila.put(adjacente)
                    parent[adjacente] = nodo_atual
                    visited.add(adjacente)



    # Reconstruir o caminho

    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
        # funçao calcula custo caminho
        custo = self.calcula_custo(path)
        return (path, custo)
    
    return None