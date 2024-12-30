from Map import Graph


def startRecursos():
    return {
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


def startHeuristicas():
    return [("alcacer", 3),
            ("barcheta", 3),
            ("calles", 2),
            ("dos aguas", 5),
            ("enova", 2),
            ("fontanares", 2),
            ("gandia", 3),
            ("liria", 4),
            ("jarafuel", 3),
            ("luchente", 2),
            ("masamagrell", 3),
            ("oliva", 2),
            ("picaña", 3),
            ("requena", 3),
            ("rocafort", 3),
            ("serra", 3),
            ("torrente", 4),
            ("valencia", 3)]


def startEdgesBarco():
    return [("serra", "rocafort"),
            ("rocafort", "requena"), 
            ("requena", "picaña"), 
            ("picaña", "oliva")]


def startEdgesCarro():
    return [("fontanares", "gandia"),
            ("fontanares", "liria"),
            ("fontanares", "jarafuel"),
            ("jarafuel", "serra"),
            ("jarafuel", "torrente"),
            ("jarafuel", "luchente"),
            ("liria", "masamagrell"),
            ("masamagrell", "oliva"),
            ("masamagrell", "valencia"),
            ("valencia", "picaña"),
            ("torrente", "requena"),
            ("torrente", "rocafort"),
            ("luchente", "valencia"),
            ("luchente", "masamagrell"),
            ("masamagrell", "gandia")]


def startEdgesAviao():
    return [("serra", "rocafort"),
            ("rocafort", "requena"),
            ("requena", "picaña"),
            ("picaña", "oliva"),
            ("fontanares", "gandia"),
            ("fontanares", "liria"),
            ("fontanares", "jarafuel"),
            ("jarafuel", "serra"),
            ("jarafuel", "torrente"),
            ("jarafuel", "luchente"),
            ("liria", "masamagrell"),
            ("masamagrell", "oliva"),
            ("masamagrell", "valencia"),
            ("valencia", "picaña"),
            ("torrente", "requena"),
            ("torrente", "rocafort"),
            ("fontanares", "barcheta"),
            ("barcheta", "alcacer"),
            ("alcacer", "dos aguas"),
            ("dos aguas", "enova"),
            ("enova", "calles"),
            ("calles", "barcheta"),
            ("gandia", "enova"),
            ("luchente", "valencia"),
            ("luchente", "masamagrell"),
            ("masamagrell", "gandia")]



def combine_edges(nodes, distances):
    return [(node1, node2, distance) for (node1, node2), distance in zip(nodes, distances)]


def edgIng(graph, edges):
    for node1, node2, distance in edges:
        graph.add_edge(node1, node2, distance)


def heuristicaIng(graph, edges):
    for node, distance in edges:
        graph.add_heuristica(node, distance)


def build(recursos,edges,heuristicas):
    gBarco_climaBasico = Graph(recursos)

    edgIng(gBarco_climaBasico, edges)
    heuristicaIng(gBarco_climaBasico, heuristicas)

    return gBarco_climaBasico




def startGraph():
        
    recursos = startRecursos()
    heuristicas = startHeuristicas()
    

    edgesBarco = startEdgesBarco()
    cBarcoClimaBasico  = [10,15,15,10]
    cBarcoClimaRegular = [15,20,20,15]
    cBarcoClimaExtremo = [20,25,25,20]

    edgesCarro = startEdgesCarro()
    cCarroClimaBasico  = [ 5, 4, 7, 3, 3, 3, 4, 5, 3, 4, 3, 4, 5, 5, 4]
    cCarroClimaRegular = [10, 6, 9, 5, 5, 5, 6, 6, 4, 6, 5, 5, 6, 6, 7]
    cCarroClimaExtremo = [15, 7,11, 7, 6, 7, 7, 7, 5, 8, 9, 6, 9, 9, 9]


    edgesAviao = startEdgesAviao()
    cAviaoClimaBasico  = [ 8,13,13, 8, 3, 2, 5, 1, 1, 1, 2, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2]
    cAviaoClimaRegular = [ 9,14,14, 9, 4, 3, 6, 2, 2, 2, 3, 4, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3]
    cAviaoClimaExtremo = [10,15,15,10, 5, 4, 7, 3, 3, 3, 4, 5, 3, 4, 3, 4, 3, 3, 3, 3, 3, 3, 3, 5, 5, 4]


    gBarco_climaBasico = build(recursos,combine_edges(edgesBarco,cBarcoClimaBasico),heuristicas)
    gBarco_climaRegular = build(recursos,combine_edges(edgesBarco,cBarcoClimaRegular),heuristicas)
    gBarco_climaExtremo = build(recursos,combine_edges(edgesBarco,cBarcoClimaExtremo),heuristicas)


    gCarro_climaBasico = build(recursos,combine_edges(edgesCarro,cCarroClimaBasico),heuristicas)
    gCarro_climaRegular = build(recursos,combine_edges(edgesCarro,cCarroClimaRegular),heuristicas)
    gCarro_climaExtremo = build(recursos,combine_edges(edgesCarro,cCarroClimaExtremo),heuristicas)


    gAviao_climaBasico = build(recursos,combine_edges(edgesAviao,cAviaoClimaBasico),heuristicas)
    gAviao_climaRegular = build(recursos,combine_edges(edgesAviao,cAviaoClimaRegular),heuristicas)
    gAviao_climaExtremo = build(recursos,combine_edges(edgesAviao,cAviaoClimaExtremo),heuristicas)


    return gAviao_climaBasico,gAviao_climaRegular,gAviao_climaExtremo,gBarco_climaBasico,gBarco_climaRegular,gBarco_climaExtremo,gCarro_climaBasico, gCarro_climaRegular,gCarro_climaExtremo