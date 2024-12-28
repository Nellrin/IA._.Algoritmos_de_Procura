from Graph import Graph
from Selection import Selection
from Node import Node

from Aviao import Aviao
from Carro import Carro
from Barco import Barco

import random


def main():

    aviao = Aviao()
    carro = Carro()
    barco = Barco()

    selection = Selection()

    recursos = {
        "alcacer": 5,
        "barcheta": 5,
        "calles": 10,
        "dos aguas": 5,
        "enova": 15,
        "fontanares": 10,
        "gandia": 15,
        "liria": 5,
        "jarafuel": 5,
        "luchente": 5,
        "masamagrell": 5,
        "oliva": 15,
        "picaña": 5,
        "requena": 5,
        "rocafort": 15,
        "serra": 10,
        "torrente": 10,
        "valencia": 10
    }

    gBarco_climaBasico = Graph(recursos)
    gBarco_climaRegular = Graph(recursos)
    gBarco_climaExtremo = Graph(recursos)


    gBarco_climaBasico.add_edge("serra", "rocafort", 10)
    gBarco_climaBasico.add_edge("rocafort", "requena", 15)
    gBarco_climaBasico.add_edge("requena", "picaña", 15)
    gBarco_climaBasico.add_edge("picaña", "oliva", 10)

    gBarco_climaRegular.add_edge("serra", "rocafort", 15)
    gBarco_climaRegular.add_edge("rocafort", "requena", 20)
    gBarco_climaRegular.add_edge("requena", "picaña", 20)
    gBarco_climaRegular.add_edge("picaña", "oliva", 15)

    gBarco_climaExtremo.add_edge("serra", "rocafort", 20)
    gBarco_climaExtremo.add_edge("rocafort", "requena", 25)
    gBarco_climaExtremo.add_edge("requena", "picaña", 25)
    gBarco_climaExtremo.add_edge("picaña", "oliva", 20)





    gCarro_climaBasico = Graph(recursos)
    gCarro_climaRegular = Graph(recursos)
    gCarro_climaExtremo = Graph(recursos)

    gCarro_climaBasico.add_edge("fontanares", "gandia", 5)
    gCarro_climaBasico.add_edge("fontanares", "liria", 4)
    gCarro_climaBasico.add_edge("fontanares", "jarafuel", 7)
    gCarro_climaBasico.add_edge("jarafuel", "serra", 3)
    gCarro_climaBasico.add_edge("jarafuel", "torrente", 3)
    gCarro_climaBasico.add_edge("jarafuel", "luchente", 3)
    gCarro_climaBasico.add_edge("liria", "masamagrell", 4)
    gCarro_climaBasico.add_edge("masamagrell", "oliva", 5)
    gCarro_climaBasico.add_edge("masamagrell", "valencia", 3)
    gCarro_climaBasico.add_edge("valencia", "picaña", 4)
    gCarro_climaBasico.add_edge("torrente", "requena", 3)
    gCarro_climaBasico.add_edge("torrente", "rocafort", 4)
    gCarro_climaBasico.add_edge("luchente", "valencia", 5)
    gCarro_climaBasico.add_edge("luchente", "masamagrell", 5)
    gCarro_climaBasico.add_edge("masamagrell", "gandia", 4)

    gCarro_climaRegular.add_edge("fontanares", "gandia", 10)
    gCarro_climaRegular.add_edge("fontanares", "liria", 6)
    gCarro_climaRegular.add_edge("fontanares", "jarafuel", 9)
    gCarro_climaRegular.add_edge("jarafuel", "serra", 5)
    gCarro_climaRegular.add_edge("jarafuel", "torrente", 5)
    gCarro_climaRegular.add_edge("jarafuel", "luchente", 5)
    gCarro_climaRegular.add_edge("liria", "masamagrell", 6)
    gCarro_climaRegular.add_edge("masamagrell", "oliva", 6)
    gCarro_climaRegular.add_edge("masamagrell", "valencia", 4)
    gCarro_climaRegular.add_edge("valencia", "picaña", 6)
    gCarro_climaRegular.add_edge("torrente", "requena", 5)
    gCarro_climaRegular.add_edge("torrente", "rocafort", 5)
    gCarro_climaRegular.add_edge("luchente", "valencia", 6)
    gCarro_climaRegular.add_edge("luchente", "masamagrell", 6)
    gCarro_climaRegular.add_edge("masamagrell", "gandia", 7)

    gCarro_climaExtremo.add_edge("fontanares", "gandia", 15)
    gCarro_climaExtremo.add_edge("fontanares", "liria", 7)
    gCarro_climaExtremo.add_edge("fontanares", "jarafuel", 11)
    gCarro_climaExtremo.add_edge("jarafuel", "serra", 7)
    gCarro_climaExtremo.add_edge("jarafuel", "torrente", 6)
    gCarro_climaExtremo.add_edge("jarafuel", "luchente", 7)
    gCarro_climaExtremo.add_edge("liria", "masamagrell", 7)
    gCarro_climaExtremo.add_edge("masamagrell", "oliva", 7)
    gCarro_climaExtremo.add_edge("masamagrell", "valencia", 5)
    gCarro_climaExtremo.add_edge("valencia", "picaña", 8)
    gCarro_climaExtremo.add_edge("torrente", "requena", 9)
    gCarro_climaExtremo.add_edge("torrente", "rocafort", 6)
    gCarro_climaExtremo.add_edge("luchente", "valencia", 9)
    gCarro_climaExtremo.add_edge("luchente", "masamagrell", 9)
    gCarro_climaExtremo.add_edge("masamagrell", "gandia", 9)





    gAviao_climaBasico = Graph(recursos)
    gAviao_climaRegular = Graph(recursos)
    gAviao_climaExtremo = Graph(recursos)

    gAviao_climaBasico.add_edge("serra", "rocafort", 8)
    gAviao_climaBasico.add_edge("rocafort", "requena", 13)
    gAviao_climaBasico.add_edge("requena", "picaña", 13)
    gAviao_climaBasico.add_edge("picaña", "oliva", 8)
    gAviao_climaBasico.add_edge("fontanares", "gandia", 3)
    gAviao_climaBasico.add_edge("fontanares", "liria", 2)
    gAviao_climaBasico.add_edge("fontanares", "jarafuel", 5)
    gAviao_climaBasico.add_edge("jarafuel", "serra", 1)
    gAviao_climaBasico.add_edge("jarafuel", "torrente", 1)
    gAviao_climaBasico.add_edge("jarafuel", "luchente", 1)
    gAviao_climaBasico.add_edge("liria", "masamagrell", 2)
    gAviao_climaBasico.add_edge("masamagrell", "oliva", 3)
    gAviao_climaBasico.add_edge("masamagrell", "valencia", 1)
    gAviao_climaBasico.add_edge("valencia", "picaña", 2)
    gAviao_climaBasico.add_edge("torrente", "requena", 1)
    gAviao_climaBasico.add_edge("torrente", "rocafort", 2)
    gAviao_climaBasico.add_edge("fontanares", "barcheta", 1)
    gAviao_climaBasico.add_edge("barcheta", "alcacer", 1)
    gAviao_climaBasico.add_edge("alcacer", "dos aguas", 1)
    gAviao_climaBasico.add_edge("dos aguas", "enova", 1)
    gAviao_climaBasico.add_edge("enova", "calles", 1)
    gAviao_climaBasico.add_edge("calles", "barcheta", 1)
    gAviao_climaBasico.add_edge("gandia", "enova", 1)
    gAviao_climaBasico.add_edge("luchente", "valencia", 3)
    gAviao_climaBasico.add_edge("luchente", "masamagrell", 3)
    gAviao_climaBasico.add_edge("masamagrell", "gandia", 2)

    gAviao_climaRegular.add_edge("serra", "rocafort", 9)
    gAviao_climaRegular.add_edge("rocafort", "requena", 14)
    gAviao_climaRegular.add_edge("requena", "picaña", 14)
    gAviao_climaRegular.add_edge("picaña", "oliva", 9)
    gAviao_climaRegular.add_edge("fontanares", "gandia", 4)
    gAviao_climaRegular.add_edge("fontanares", "liria", 3)
    gAviao_climaRegular.add_edge("fontanares", "jarafuel", 6)
    gAviao_climaRegular.add_edge("jarafuel", "serra", 2)
    gAviao_climaRegular.add_edge("jarafuel", "torrente", 2)
    gAviao_climaRegular.add_edge("jarafuel", "luchente", 2)
    gAviao_climaRegular.add_edge("liria", "masamagrell", 3)
    gAviao_climaRegular.add_edge("masamagrell", "oliva", 4)
    gAviao_climaRegular.add_edge("masamagrell", "valencia", 2)
    gAviao_climaRegular.add_edge("valencia", "picaña", 3)
    gAviao_climaRegular.add_edge("torrente", "requena", 2)
    gAviao_climaRegular.add_edge("torrente", "rocafort", 3)
    gAviao_climaRegular.add_edge("fontanares", "barcheta", 2)
    gAviao_climaRegular.add_edge("barcheta", "alcacer", 2)
    gAviao_climaRegular.add_edge("alcacer", "dos aguas", 2)
    gAviao_climaRegular.add_edge("dos aguas", "enova", 2)
    gAviao_climaRegular.add_edge("enova", "calles", 2)
    gAviao_climaRegular.add_edge("calles", "barcheta", 2)
    gAviao_climaRegular.add_edge("gandia", "enova", 2)
    gAviao_climaRegular.add_edge("luchente", "valencia", 4)
    gAviao_climaRegular.add_edge("luchente", "masamagrell", 4)
    gAviao_climaRegular.add_edge("masamagrell", "gandia", 3)

    gAviao_climaExtremo.add_edge("serra", "rocafort", 10)
    gAviao_climaExtremo.add_edge("rocafort", "requena", 15)
    gAviao_climaExtremo.add_edge("requena", "picaña", 15)
    gAviao_climaExtremo.add_edge("picaña", "oliva", 10)
    gAviao_climaExtremo.add_edge("fontanares", "gandia", 5)
    gAviao_climaExtremo.add_edge("fontanares", "liria", 4)
    gAviao_climaExtremo.add_edge("fontanares", "jarafuel", 7)
    gAviao_climaExtremo.add_edge("jarafuel", "serra", 3)
    gAviao_climaExtremo.add_edge("jarafuel", "torrente", 3)
    gAviao_climaExtremo.add_edge("jarafuel", "luchente", 3)
    gAviao_climaExtremo.add_edge("liria", "masamagrell", 4)
    gAviao_climaExtremo.add_edge("masamagrell", "oliva", 5)
    gAviao_climaExtremo.add_edge("masamagrell", "valencia", 3)
    gAviao_climaExtremo.add_edge("valencia", "picaña", 4)
    gAviao_climaExtremo.add_edge("torrente", "requena", 3)
    gAviao_climaExtremo.add_edge("torrente", "rocafort", 4)
    gAviao_climaExtremo.add_edge("fontanares", "barcheta", 3)
    gAviao_climaExtremo.add_edge("barcheta", "alcacer", 3)
    gAviao_climaExtremo.add_edge("alcacer", "dos aguas", 3)
    gAviao_climaExtremo.add_edge("dos aguas", "enova", 3)
    gAviao_climaExtremo.add_edge("enova", "calles", 3)
    gAviao_climaExtremo.add_edge("calles", "barcheta", 3)
    gAviao_climaExtremo.add_edge("gandia", "enova", 3)
    gAviao_climaExtremo.add_edge("luchente", "valencia", 5)
    gAviao_climaExtremo.add_edge("luchente", "masamagrell", 5)
    gAviao_climaExtremo.add_edge("masamagrell", "gandia", 4)


    gBarco_climaBasico.add_heuristica("alcacer", 3)
    gBarco_climaRegular.add_heuristica("alcacer", 3)
    gBarco_climaExtremo.add_heuristica("alcacer", 3)
    gCarro_climaBasico.add_heuristica("alcacer", 3)
    gCarro_climaRegular.add_heuristica("alcacer", 3)
    gCarro_climaExtremo.add_heuristica("alcacer", 3)
    gAviao_climaBasico.add_heuristica("alcacer", 3)
    gAviao_climaRegular.add_heuristica("alcacer", 3)
    gAviao_climaExtremo.add_heuristica("alcacer", 3)


    gBarco_climaBasico.add_heuristica("barcheta", 3)
    gBarco_climaRegular.add_heuristica("barcheta", 3)
    gBarco_climaExtremo.add_heuristica("barcheta", 3)
    gCarro_climaBasico.add_heuristica("barcheta", 3)
    gCarro_climaRegular.add_heuristica("barcheta", 3)
    gCarro_climaExtremo.add_heuristica("barcheta", 3)
    gAviao_climaBasico.add_heuristica("barcheta", 3)
    gAviao_climaRegular.add_heuristica("barcheta", 3)
    gAviao_climaExtremo.add_heuristica("barcheta", 3)


    gBarco_climaBasico.add_heuristica("calles", 2)
    gBarco_climaRegular.add_heuristica("calles", 2)
    gBarco_climaExtremo.add_heuristica("calles", 2)
    gCarro_climaBasico.add_heuristica("calles", 2)
    gCarro_climaRegular.add_heuristica("calles", 2)
    gCarro_climaExtremo.add_heuristica("calles", 2)
    gAviao_climaBasico.add_heuristica("calles", 2)
    gAviao_climaRegular.add_heuristica("calles", 2)
    gAviao_climaExtremo.add_heuristica("calles", 2)


    gBarco_climaBasico.add_heuristica("dos aguas", 5)
    gBarco_climaRegular.add_heuristica("dos aguas", 5)
    gBarco_climaExtremo.add_heuristica("dos aguas", 5)
    gCarro_climaBasico.add_heuristica("dos aguas", 5)
    gCarro_climaRegular.add_heuristica("dos aguas", 5)
    gCarro_climaExtremo.add_heuristica("dos aguas", 5)
    gAviao_climaBasico.add_heuristica("dos aguas", 5)
    gAviao_climaRegular.add_heuristica("dos aguas", 5)
    gAviao_climaExtremo.add_heuristica("dos aguas", 5)


    gBarco_climaBasico.add_heuristica("enova", 2)
    gBarco_climaRegular.add_heuristica("enova", 2)
    gBarco_climaExtremo.add_heuristica("enova", 2)
    gCarro_climaBasico.add_heuristica("enova", 2)
    gCarro_climaRegular.add_heuristica("enova", 2)
    gCarro_climaExtremo.add_heuristica("enova", 2)
    gAviao_climaBasico.add_heuristica("enova", 2)
    gAviao_climaRegular.add_heuristica("enova", 2)
    gAviao_climaExtremo.add_heuristica("enova", 2)


    gBarco_climaBasico.add_heuristica("fontanares", 2)
    gBarco_climaRegular.add_heuristica("fontanares", 2)
    gBarco_climaExtremo.add_heuristica("fontanares", 2)
    gCarro_climaBasico.add_heuristica("fontanares", 2)
    gCarro_climaRegular.add_heuristica("fontanares", 2)
    gCarro_climaExtremo.add_heuristica("fontanares", 2)
    gAviao_climaBasico.add_heuristica("fontanares", 2)
    gAviao_climaRegular.add_heuristica("fontanares", 2)
    gAviao_climaExtremo.add_heuristica("fontanares", 2)


    gBarco_climaBasico.add_heuristica("gandia", 3)
    gBarco_climaRegular.add_heuristica("gandia", 3)
    gBarco_climaExtremo.add_heuristica("gandia", 3)
    gCarro_climaBasico.add_heuristica("gandia", 3)
    gCarro_climaRegular.add_heuristica("gandia", 3)
    gCarro_climaExtremo.add_heuristica("gandia", 3)
    gAviao_climaBasico.add_heuristica("gandia", 3)
    gAviao_climaRegular.add_heuristica("gandia", 3)
    gAviao_climaExtremo.add_heuristica("gandia", 3)


    gBarco_climaBasico.add_heuristica("liria", 4)
    gBarco_climaRegular.add_heuristica("liria", 4)
    gBarco_climaExtremo.add_heuristica("liria", 4)
    gCarro_climaBasico.add_heuristica("liria", 4)
    gCarro_climaRegular.add_heuristica("liria", 4)
    gCarro_climaExtremo.add_heuristica("liria", 4)
    gAviao_climaBasico.add_heuristica("liria", 4)
    gAviao_climaRegular.add_heuristica("liria", 4)
    gAviao_climaExtremo.add_heuristica("liria", 4)


    gBarco_climaBasico.add_heuristica("jarafuel", 3)
    gBarco_climaRegular.add_heuristica("jarafuel", 3)
    gBarco_climaExtremo.add_heuristica("jarafuel", 3)
    gCarro_climaBasico.add_heuristica("jarafuel", 3)
    gCarro_climaRegular.add_heuristica("jarafuel", 3)
    gCarro_climaExtremo.add_heuristica("jarafuel", 3)
    gAviao_climaBasico.add_heuristica("jarafuel", 3)
    gAviao_climaRegular.add_heuristica("jarafuel", 3)
    gAviao_climaExtremo.add_heuristica("jarafuel", 3)


    gBarco_climaBasico.add_heuristica("luchente", 2)
    gBarco_climaRegular.add_heuristica("luchente", 2)
    gBarco_climaExtremo.add_heuristica("luchente", 2)
    gCarro_climaBasico.add_heuristica("luchente", 2)
    gCarro_climaRegular.add_heuristica("luchente", 2)
    gCarro_climaExtremo.add_heuristica("luchente", 2)
    gAviao_climaBasico.add_heuristica("luchente", 2)
    gAviao_climaRegular.add_heuristica("luchente", 2)
    gAviao_climaExtremo.add_heuristica("luchente", 2)


    gBarco_climaBasico.add_heuristica("masamagrell", 3)
    gBarco_climaRegular.add_heuristica("masamagrell", 3)
    gBarco_climaExtremo.add_heuristica("masamagrell", 3)
    gCarro_climaBasico.add_heuristica("masamagrell", 3)
    gCarro_climaRegular.add_heuristica("masamagrell", 3)
    gCarro_climaExtremo.add_heuristica("masamagrell", 3)
    gAviao_climaBasico.add_heuristica("masamagrell", 3)
    gAviao_climaRegular.add_heuristica("masamagrell", 3)
    gAviao_climaExtremo.add_heuristica("masamagrell", 3)


    gBarco_climaBasico.add_heuristica("oliva", 2)
    gBarco_climaRegular.add_heuristica("oliva", 2)
    gBarco_climaExtremo.add_heuristica("oliva", 2)
    gCarro_climaBasico.add_heuristica("oliva", 2)
    gCarro_climaRegular.add_heuristica("oliva", 2)
    gCarro_climaExtremo.add_heuristica("oliva", 2)
    gAviao_climaBasico.add_heuristica("oliva", 2)
    gAviao_climaRegular.add_heuristica("oliva", 2)
    gAviao_climaExtremo.add_heuristica("oliva", 2)


    gBarco_climaBasico.add_heuristica("picaña", 3)
    gBarco_climaRegular.add_heuristica("picaña", 3)
    gBarco_climaExtremo.add_heuristica("picaña", 3)
    gCarro_climaBasico.add_heuristica("picaña", 3)
    gCarro_climaRegular.add_heuristica("picaña", 3)
    gCarro_climaExtremo.add_heuristica("picaña", 3)
    gAviao_climaBasico.add_heuristica("picaña", 3)
    gAviao_climaRegular.add_heuristica("picaña", 3)
    gAviao_climaExtremo.add_heuristica("picaña", 3)


    gBarco_climaBasico.add_heuristica("requena", 3)
    gBarco_climaRegular.add_heuristica("requena", 3)
    gBarco_climaExtremo.add_heuristica("requena", 3)
    gCarro_climaBasico.add_heuristica("requena", 3)
    gCarro_climaRegular.add_heuristica("requena", 3)
    gCarro_climaExtremo.add_heuristica("requena", 3)
    gAviao_climaBasico.add_heuristica("requena", 3)
    gAviao_climaRegular.add_heuristica("requena", 3)
    gAviao_climaExtremo.add_heuristica("requena", 3)


    gBarco_climaBasico.add_heuristica("rocafort", 3)
    gBarco_climaRegular.add_heuristica("rocafort", 3)
    gBarco_climaExtremo.add_heuristica("rocafort", 3)
    gCarro_climaBasico.add_heuristica("rocafort", 3)
    gCarro_climaRegular.add_heuristica("rocafort", 3)
    gCarro_climaExtremo.add_heuristica("rocafort", 3)
    gAviao_climaBasico.add_heuristica("rocafort", 3)
    gAviao_climaRegular.add_heuristica("rocafort", 3)
    gAviao_climaExtremo.add_heuristica("rocafort", 3)


    gBarco_climaBasico.add_heuristica("serra", 3)
    gBarco_climaRegular.add_heuristica("serra", 3)
    gBarco_climaExtremo.add_heuristica("serra", 3)
    gCarro_climaBasico.add_heuristica("serra", 3)
    gCarro_climaRegular.add_heuristica("serra", 3)
    gCarro_climaExtremo.add_heuristica("serra", 3)
    gAviao_climaBasico.add_heuristica("serra", 3)
    gAviao_climaRegular.add_heuristica("serra", 3)
    gAviao_climaExtremo.add_heuristica("serra", 3)


    gBarco_climaBasico.add_heuristica("torrente", 4)
    gBarco_climaRegular.add_heuristica("torrente", 4)
    gBarco_climaExtremo.add_heuristica("torrente", 4)
    gCarro_climaBasico.add_heuristica("torrente", 4)
    gCarro_climaRegular.add_heuristica("torrente", 4)
    gCarro_climaExtremo.add_heuristica("torrente", 4)
    gAviao_climaBasico.add_heuristica("torrente", 4)
    gAviao_climaRegular.add_heuristica("torrente", 4)
    gAviao_climaExtremo.add_heuristica("torrente", 4)


    gBarco_climaBasico.add_heuristica("valencia", 3)
    gBarco_climaRegular.add_heuristica("valencia", 3)
    gBarco_climaExtremo.add_heuristica("valencia", 3)
    gCarro_climaBasico.add_heuristica("valencia", 3)
    gCarro_climaRegular.add_heuristica("valencia", 3)
    gCarro_climaExtremo.add_heuristica("valencia", 3)
    gAviao_climaBasico.add_heuristica("valencia", 3)
    gAviao_climaRegular.add_heuristica("valencia", 3)
    gAviao_climaExtremo.add_heuristica("valencia", 3)

    gBasico = [gAviao_climaBasico, gCarro_climaBasico, gBarco_climaBasico]
    gRegular = [gAviao_climaRegular, gCarro_climaRegular, gBarco_climaRegular]
    gExtremo = [gAviao_climaExtremo, gCarro_climaExtremo, gBarco_climaExtremo]

    cidadesVisitadas = []

    numAleatorio = random.randint(0, 2)

    #escolhemos o clima
    match numAleatorio:
        case 0:
            g = gBasico
        case 1:
            g = gRegular
        case 2:
            g = gExtremo

    posiçõesAtuais = {
        "Avião": None,
        "Carro": None,
        "Barco": None,
    }

    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-Ver recursos necessarios por cidade")
        print("6-DFS")
        print("7-BFS")
        print("8-A*")
        print("9-Gulosa")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(g[0].m_graph) #selecionamos o grafo dos aviões que é o maior/global o mapa
            l = input("prima enter para continuar")
        elif saida == 2:
            saida_grafo = -1
            while saida_grafo != 0:
                print("1-Grafo dos Aviões")
                print("2-Grafo dos Carros")
                print("3-Grafo dos Barcos")
                print("0-Sair")
                saida_grafo = int(input("introduza a sua opcao-> "))

                if saida_grafo == 1: g[0].desenha()
                elif saida_grafo == 2: g[1].desenha()
                elif saida_grafo == 3: g[2].desenha()
                elif saida_grafo == 0: saida_grafo = 0
        elif saida == 3:
            print(g[0].m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(g[0].imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            print(g[0].m_recursos)
            l = input("prima enter para continuar")
                    
        elif saida == 6:

            check = True
            while (check):
                inicio = input("\nNodo inicial (vai ser usado caso seja a primeira viagem)->")
                fim = input("Nodo final->")
                
                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    # Definir las tres posibles opciones
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_DFS(posiçõesAtuais["Avião"], fim, path=[], visited=set())
                    else: resAviao = g[0].procura_DFS(inicio, fim, path=[], visited=set())

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_DFS(posiçõesAtuais["Carro"], fim, path=[], visited=set())
                    else: resCarro = g[1].procura_DFS(inicio, fim, path=[], visited=set())
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_DFS(posiçõesAtuais["Barco"], fim, path=[], visited=set())
                    else: resBarco = g[2].procura_DFS(inicio, fim, path=[], visited=set())

                    check = False
                else:
                    print("O nodo ao qual esta a tentar ir ja não esta disponivel!, tente novamente")
            
            
            (melhor_path, melhor_custo, melhor_vehiculo) = selection.selecionaTheBest(resAviao, resCarro, resBarco, aviao, carro, barco, recursos)
            
        elif saida == 7:

            check = True
            while (check):
                inicio = input("\nNodo inicial (vai ser usado caso seja a primeira viagem)->")
                fim = input("Nodo final->")
                
                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_BFS(posiçõesAtuais["Avião"], fim, path=[], visited=set())
                    else: resAviao = g[0].procura_BFS(inicio, fim, path=[], visited=set())

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_BFS(posiçõesAtuais["Carro"], fim, path=[], visited=set())
                    else: resCarro = g[1].procura_BFS(inicio, fim, path=[], visited=set())
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_BFS(posiçõesAtuais["Barco"], fim, path=[], visited=set())
                    else: resBarco = g[2].procura_BFS(inicio, fim, path=[], visited=set())

                    check = False
                else:
                    print("O nodo ao qual esta a tentar ir ja não esta disponivel!, tente novamente")

            (melhor_path, melhor_custo, melhor_vehiculo) = selection.selecionaTheBest(resAviao, resCarro, resBarco, aviao, carro, barco, recursos)
        
        
        elif saida == 8:

            check = True
            while (check):
                inicio = input("\nNodo inicial (vai ser usado caso seja a primeira viagem)->")
                fim = input("Nodo final->")

                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_aStar(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].procura_aStar(inicio, fim)

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_aStar(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].procura_aStar(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_aStar(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].procura_aStar(inicio, fim)

                    check = False
                
                else:
                    print("O nodo ao qual esta a tentar ir ja não esta disponivel!, tente novamente")
            
            (melhor_path, melhor_custo, melhor_vehiculo) = selection.selecionaTheBest(resAviao, resCarro, resBarco, aviao, carro, barco, recursos)


        elif saida == 9:

            check = True
            while (check):
                inicio = input("\nNodo inicial (vai ser usado caso seja a primeira viagem)->")
                fim = input("Nodo final->")

                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].greedy(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].greedy(inicio, fim)

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].greedy(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].greedy(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].greedy(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].greedy(inicio, fim)

                    check = False
                
                else:
                    print("O nodo ao qual esta a tentar ir ja não esta disponivel!, tente novamente")

            (melhor_path, melhor_custo, melhor_vehiculo) = selection.selecionaTheBest(resAviao, resCarro, resBarco, aviao, carro, barco, recursos)
        

        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")
        
        ##response##

        if saida == 6 or saida == 7 or saida == 8 or saida == 9:
            if melhor_path:
                print("\nO melhor vehiculo para estas circunstancias era:", melhor_vehiculo)
                print("Caminho solução:", melhor_path)

                #ja foi atualizado a gasolina/capacidade do vehiculo
                #guardar cidades visitadas numa lista
                selection.atualiza_cidades(cidadesVisitadas, melhor_path)


            else:
                print("Atualmente ninhum dos vehiculos consegue fazer a viagem seja por causa da gasolina ou recursos, vão ser restaurado os recursos e gasolina dos vehiculos")
                aviao.restauraCapacidade()
                aviao.restauraGasolina()
                carro.restauraCapacidade()
                carro.restauraGasolina()
                barco.restauraCapacidade()
                barco.restauraGasolina()


            
            if melhor_vehiculo: 
                posiçõesAtuais[melhor_vehiculo] = fim
                #print(posiçõesAtuais[melhor_vehiculo])

            #diminuir heuristica/tempo de vida das cidades no visitadas
            g[0].decrement_life(cidadesVisitadas)
            g[1].decrement_life(cidadesVisitadas)
            g[2].decrement_life(cidadesVisitadas)

            #informar do novo tempo de vida das cidades
            print("\nNovos tempos de vida das cidades")
            print(g[0].m_h)

            #é suposto o vehiculo ficar na cidade objetivo (oseja que esse vai ser o proximo nodo inicial para ele)
            if melhor_vehiculo: print("Nodo inicial para a proxima viagem do", melhor_vehiculo, ": ", fim)

            #evento aleatorio
            check, nodoA, nodoB = g[0].eventoAleatorio()
            if check:
                g[1].atualizaEvento(nodoA, nodoB)
                g[2].atualizaEvento(nodoA, nodoB)
                print("\nAconteceu um evento entre", nodoA, "e", nodoB)
                #print(g[0].m_graph)
        
        l = input("prima enter para continuar\n")


if __name__ == "__main__":
    main()
