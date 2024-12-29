from Map import Selection
from Vehicles import Aviao, Barco, Carro
from build import startGraph, startRecursos

import random
import subprocess
import sys



def install_requirements():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            stdout=subprocess.DEVNULL,  # Suppress standard output
            stderr=subprocess.DEVNULL   # Suppress error output
            )
        print("[Dependências instaladas]\n\n")
    except subprocess.CalledProcessError as e:
        print(f"[Erro ao instalar dependências]: {e}\n\n")



def main():
        
    install_requirements()

    aviao = Aviao(45,80)
    carro = Carro(100,100)
    barco = Barco(65,50)

    selection = Selection()

    gCarro_climaBasico, gCarro_climaRegular,gCarro_climaExtremo,gAviao_climaBasico,gAviao_climaRegular,gAviao_climaExtremo,gBarco_climaBasico,gBarco_climaRegular,gBarco_climaExtremo = startGraph()
    recursos = startRecursos()


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
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_BFS(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].procura_BFS(inicio, fim)

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_BFS(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].procura_BFS(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_BFS(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].procura_BFS(inicio, fim)

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
                aviao.restauraRecursos()
                aviao.restauraGasolina()
                carro.restauraRecursos()
                carro.restauraGasolina()
                barco.restauraRecursos()
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
