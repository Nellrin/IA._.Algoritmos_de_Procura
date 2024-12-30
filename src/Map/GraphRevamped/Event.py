
import random

#############################
# Geração aleatoria de evento
#############################

def eventoAleatorio(self):
    numeroRandom = random.randint(1, 3)
    if numeroRandom == 3: #33% de acontecer um evento
        nodo_inicial = random.choice(list(self.m_graph.keys()))
        
        # Verifica si la lista de vecinos no está vacía
        if self.m_graph[nodo_inicial]:
            # Selecciona un vecino aleatorio del nodo inicial
            nodo_adyacente, _ = random.choice(self.m_graph[nodo_inicial])
            
            # Actualiza el peso del nodo adyacente en el nodo inicial
            for i, (vecino, valor) in enumerate(self.m_graph[nodo_inicial]):
                if vecino == nodo_adyacente:
                    self.m_graph[nodo_inicial][i] = (vecino, 999)
                    break
            
            # Verifica si el nodo adyacente existe en el grafo
            if nodo_adyacente in self.m_graph:
                # Actualiza el peso del nodo inicial en el nodo adyacente
                for i, (vecino, valor) in enumerate(self.m_graph[nodo_adyacente]):
                    if vecino == nodo_inicial:
                        self.m_graph[nodo_adyacente][i] = (vecino, 999)
                        break
            else:
                print(f"Advertencia: El nodo adyacente '{nodo_adyacente}' no está en el grafo.")
        else:
            print(f"Advertencia: El nodo inicial '{nodo_inicial}' no tiene vecinos.")
            nodo_adyacente = None

        return True, nodo_inicial, nodo_adyacente
    else: return False, None, None


def atualizaEvento(self, nodo_inicial, nodo_final):
    if nodo_inicial in self.m_graph and nodo_final in self.m_graph:
        for i, (vecino, valor) in enumerate(self.m_graph[nodo_inicial]):
            if vecino == nodo_final:
                self.m_graph[nodo_inicial][i] = (vecino, 999)
                break
        
        # Realiza lo mismo para el nodo adyacente
        for i, (vecino, valor) in enumerate(self.m_graph[nodo_final]):
            if vecino == nodo_inicial:
                self.m_graph[nodo_final][i] = (vecino, 999)
                break

##########################################################################
#  decrement_life   -> atualiza o tempo de vida dos nodos
##########################################################################

def decrement_life(self, cidadesVisitadas):
    for nodo in self.m_h:
        if nodo not in cidadesVisitadas: 
            var = self.m_h[nodo]
            if var -1 >= 0: self.m_h[nodo] -= 1 