################################################################################
# Procura DFS
####################################################################################

def procura_DFS(self, start, end, path=[], visited=set()):
    path.append(start)
    visited.add(start)

    if start == end:
        # calcular o custo do caminho funçao calcula custo.
        custoT = self.calcula_custo(path)
        return (path, custoT)
    if start in self.m_graph and end in self.m_graph:
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited and self.m_h[adjacente] > 0: #se ainda é possivel visitar esse nodo
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
    path.pop()  # se nao encontra remover o que está no caminho..
    return None