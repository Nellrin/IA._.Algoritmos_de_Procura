from Map import Selection, startGraph, startRecursos, startHeuristicas
from Vehicles import Aviao, Barco, Carro
from time import sleep
import os
import platform

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

def clear():
    system_name = platform.system().lower()
    if system_name == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def main():
        
    install_requirements()

    aviao = Aviao(45,80)
    carro = Carro(65,50)
    barco = Barco(100,100)

    selection = Selection()

    recursosDeCadaCidade = startRecursos()
    heuristicas = startHeuristicas()
    gAviao_climaBasico,gAviao_climaRegular,gAviao_climaExtremo,gBarco_climaBasico,gBarco_climaRegular,gBarco_climaExtremo,gCarro_climaBasico, gCarro_climaRegular,gCarro_climaExtremo = startGraph(recursosDeCadaCidade,heuristicas)


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


    GasolinaDisponivel = 300
    RecursosDisponiveis = 200

    GasolinaInicial = GasolinaDisponivel
    RecursosInicial = RecursosDisponiveis
    

    recursosPedidosInicialmente = 0
    for recursos in g[0].m_recursos.values():
        recursosPedidosInicialmente += recursos


    posiçõesAtuais = {
        "Avião": None,
        "Carro": None,
        "Barco": None,
    }

    GasolinaComoCriterioDeDecisao = True

    saida = -1
    while saida != 0:

        print('\033[1m==================================================================\033[0m')
        print("\033[1m( 0)\033[0m Saír")
        print("\033[1m( 1)\033[0m Imprimir Grafo")
        print("\033[1m( 2)\033[0m Desenhar Grafo")
        print("\033[1m( 3)\033[0m Imprimir nodos do Grafo")
        print("\033[1m( 4)\033[0m Imprimir arestas do Grafo")
        print("\033[1m( 5)\033[0m Ver Recursos Requisitados pelas cidades")
        print("\033[1m( 6)\033[0m Ver Tempo de Vida restante das cidades")
        print("\033[1m( 7)\033[0m Ver Estatísticas")
        print("\033[1m( 8)\033[0m Definir o Critério de Decisão")
        print("\033[1m( 9)\033[0m Procura DFS")
        print("\033[1m(10)\033[0m Procura BFS")
        print("\033[1m(11)\033[0m Procura A*")
        print("\033[1m(12)\033[0m Procura Gulosa")
        print('\033[1m==================================================================\n\033[0m')


        saida = int(input("\033[1m[Introduza a sua opcao]:\033[0m "))
        
        clear()

        if saida == 0:
            print('\033[1m==================================================================\033[0m')
            print("Saindo...")
            print('\033[1m==================================================================\n\033[0m')
        elif saida == 1:
            print('\033[1m==================================================================\033[0m')
            print('\033[1mOrigem\033[0m: [(\033[1mVizinho1\033[0m, \033[1mCusto1\033[0m), ... , (\033[1mVizinhoN\033[0m, \033[1mCustoN\033[0m)]\n')
            print(g[0].m_graph) #selecionamos o grafo dos aviões que é o maior/global o mapa
            print('\033[1m==================================================================\n\033[0m')

            sleep(0.1)
        elif saida == 2:
            saida_grafo = -1
            
            while saida_grafo != 0:
                clear()
                print('\033[1m==================================================================\033[0m')
                print("\033[1m(1)\033[0m Grafo dos Aviões")
                print("\033[1m(2)\033[0m Grafo dos Carros")
                print("\033[1m(3)\033[0m Grafo dos Barcos")
                print("\n\033[1m(0)\033[0m Sair")
                print('\033[1m==================================================================\n\033[0m')
                saida_grafo = int(input("\033[1m[Introduza a sua opcao]:\033[0m "))

                if saida_grafo == 1: g[0].desenha()
                elif saida_grafo == 2: g[1].desenha()
                elif saida_grafo == 3: g[2].desenha()
                elif saida_grafo == 0: saida_grafo = 0
        elif saida == 3:
            print('\033[1m==================================================================\033[0m')
            print(list(g[0].m_graph.keys()))
            print('\033[1m==================================================================\n\033[0m')
            sleep(0.1)
        elif saida == 4:
            print('\033[1m==================================================================\033[0m')
            print('(\033[1mCidadeA\033[0m -> \033[1mCidadeB\033[0m) {\033[1mCusto\033[0m}\n')
            print(g[0].imprime_aresta())
            print('\033[1m==================================================================\n\033[0m')
            sleep(0.1)
        elif saida == 5:
            print('\033[1m==================================================================\033[0m')
            print('{\033[1mCidade\033[0m: \033[1mRecursos Requisitados\033[0m}\n')
            print(g[0].m_recursos)
            print('\033[1m==================================================================\n\033[0m')
            sleep(0.1)

        elif saida == 6:
            print('\033[1m==================================================================\033[0m')
            print('{\033[1mCidade\033[0m: \033[1mTempo de Vida\033[0m}\n')
            print(g[0].m_h)
            print('\033[1m==================================================================\n\033[0m')
            sleep(0.1)

        elif saida == 7:

            listaTiposDeCidadesEmRisco = [0,0,0,0,0,0,0]
            recursosAtendidos = recursosPedidosInicialmente
            
            for cidades in (g[0].m_graph.keys()):
                listaTiposDeCidadesEmRisco[0] += 1
                recursosAtendidos -= g[0].m_recursos[cidades]

                if g[0].m_recursos[cidades] == 0: listaTiposDeCidadesEmRisco[1] += 1
                elif g[0].m_h[cidades] == 0:      listaTiposDeCidadesEmRisco[2] += 1
                elif g[0].m_h[cidades] <= 2:      listaTiposDeCidadesEmRisco[3] += 1
                elif g[0].m_h[cidades] == 3:      listaTiposDeCidadesEmRisco[4] += 1
                elif g[0].m_h[cidades] == 4:      listaTiposDeCidadesEmRisco[5] += 1
                elif g[0].m_h[cidades] == 5:      listaTiposDeCidadesEmRisco[6] += 1

            print('\033[1m==================================================================\033[0m')
            print(f"Avião {{Recursos:\033[1m[{aviao.getRecursos()}/{aviao.getRecursosMAX()}]\033[0m   \033[1m({((100*aviao.getRecursos())/aviao.getRecursosMAX()):.2f}%)\033[0m}}")
            print(f"      {{Gasolina:\033[1m[{aviao.getGasolina()}/{aviao.getGasolinaMAX()}]\033[0m   \033[1m({((100*aviao.getGasolina())/aviao.getGasolinaMAX()):.2f}%)\033[0m}}")
            print(f"Barco {{Recursos:\033[1m[{barco.getRecursos()}/{barco.getRecursosMAX()}]\033[0m   \033[1m({((100*barco.getRecursos())/barco.getRecursosMAX()):.2f}%)\033[0m}}")
            print(f"      {{Gasolina:\033[1m[{barco.getGasolina()}/{barco.getGasolinaMAX()}]\033[0m   \033[1m({((100*barco.getGasolina())/barco.getGasolinaMAX()):.2f}%)\033[0m}}")
            print(f"Carro {{Recursos:\033[1m[{carro.getRecursos()}/{carro.getRecursosMAX()}]\033[0m   \033[1m({((100*carro.getRecursos())/carro.getRecursosMAX()):.2f}%)\033[0m}}")
            print(f"      {{Gasolina:\033[1m[{carro.getGasolina()}/{carro.getGasolinaMAX()}]\033[0m   \033[1m({((100*carro.getGasolina())/carro.getGasolinaMAX()):.2f}%)\033[0m}}\n\n")
            print(f"                Recursos Disponíveis: \033[1m[{RecursosDisponiveis}/{RecursosInicial}]\033[0m   \033[1m({((100*RecursosDisponiveis)/RecursosInicial):.2f}%)\033[0m")
            print(f"                 Gasolina Disponível: \033[1m[{GasolinaDisponivel}/{GasolinaInicial}]\033[0m   \033[1m({((100*GasolinaDisponivel)/GasolinaInicial):.2f}%)\033[0m\n")
            print(f"     Recursos Requisitados Entregues: \033[1m[{recursosAtendidos}/{recursosPedidosInicialmente}]\033[0m   \033[1m({((100*recursosAtendidos)/recursosPedidosInicialmente):.2f}%)\033[0m")
            print(f"                  Cidades Socorridas: \033[1m[{listaTiposDeCidadesEmRisco[1]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[1]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m")
            print(f"                    Cidades Perdidas: \033[1m[{listaTiposDeCidadesEmRisco[2]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[2]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m\n")
            print(f"         Cidades em Estado Emergente: \033[1m[{listaTiposDeCidadesEmRisco[6]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[6]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m")
            print(f"           Cidades em Estado Estável: \033[1m[{listaTiposDeCidadesEmRisco[5]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[5]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m")
            print(f"         Cidades em Estado Alarmante: \033[1m[{listaTiposDeCidadesEmRisco[4]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[4]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m")
            print(f"           Cidades em Estado Crítico: \033[1m[{listaTiposDeCidadesEmRisco[3]}/{listaTiposDeCidadesEmRisco[0]}]\033[0m   \033[1m({(100*listaTiposDeCidadesEmRisco[3]/listaTiposDeCidadesEmRisco[0]):.2f}%)\033[0m")
            print('\033[1m==================================================================\n\033[0m')

            sleep(0.1)

        elif saida == 8:

            opcaoGasolina = "(1) Menor quantidade de Gasolina Gasta"
            opcaoRecursos = "(2) Maior quantidade de Recursos Distribuidos"

            if GasolinaComoCriterioDeDecisao: opcaoGasolina = f"\033[1m{opcaoGasolina}\033[0m"
            else:                             opcaoRecursos = f"\033[1m{opcaoRecursos}\033[0m"

            print('\033[1m==================================================================\033[0m')
            print('Qual deve ser o Critério de Decisão caso mais de um veículo')
            print('seja capaz de efetuar a viagem proposta?\n')
            print(f"         {opcaoGasolina}")
            print(f"         {opcaoRecursos}\n")
            
            saida_CD = int(input("\033[1m[Introduza a sua opcao]:\033[0m "))

            if saida_CD == 1: GasolinaComoCriterioDeDecisao = True
            elif saida_CD == 2: GasolinaComoCriterioDeDecisao = False

        elif saida == 9:

            check = True
            while (check):
                print('\033[1m==================================================================\033[0m')
                inicio = input("Este só será usado na primeira viagem\n\033[1m[Nodo Inicial]:\033[0m ")
                fim =    input("  \033[1m[Nodo final]:\033[0m ")
                print('\033[1m==================================================================\n\033[0m')
                
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


                    print('\033[1m==================================================================\033[0m')
                    print("A cidade que pretende alcançar não se encontra disponível.")
                    print("Insira um novo destino")
                    print('\033[1m==================================================================\n\033[0m')

            (melhor_path, melhor_custo, recursosgastos, melhor_vehiculo) = selection.selecionaTheBest(GasolinaComoCriterioDeDecisao, resAviao, resCarro, resBarco, aviao, carro, barco, recursosDeCadaCidade, heuristicas)

        elif saida == 10:

            check = True
            while (check):
                print('\033[1m==================================================================\033[0m')
                inicio = input("Este só será usado na primeira viagem\n\033[1m[Nodo Inicial]:\033[0m ")
                fim =    input("  \033[1m[Nodo final]:\033[0m ")
                print('\033[1m==================================================================\n\033[0m')

                
                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_BFS(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].procura_BFS(inicio, fim)

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_BFS(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].procura_BFS(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_BFS(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].procura_BFS(inicio, fim)

                    check = False
                else:
                    print('\033[1m==================================================================\033[0m')
                    print("A cidade que pretende alcançar não se encontra disponível.")
                    print("Insira um novo destino")
                    print('\033[1m==================================================================\n\033[0m')

            (melhor_path, melhor_custo, recursosgastos, melhor_vehiculo) = selection.selecionaTheBest(GasolinaComoCriterioDeDecisao, resAviao, resCarro, resBarco, aviao, carro, barco, recursosDeCadaCidade,heuristicas)
        
        
        elif saida == 11:

            check = True
            while (check):
                
                print('\033[1m==================================================================\033[0m')
                inicio = input("Este só será usado na primeira viagem\n\033[1m[Nodo Inicial]:\033[0m ")
                fim =    input("  \033[1m[Nodo final]:\033[0m ")
                print('\033[1m==================================================================\n\033[0m')

                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].procura_aStar(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].procura_aStar(inicio, fim)


                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].procura_aStar(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].procura_aStar(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].procura_aStar(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].procura_aStar(inicio, fim)

                    check = False
                
                else:
                    print('\033[1m==================================================================\033[0m')
                    print("A cidade que pretende alcançar não se encontra disponível.")
                    print("Insira um novo destino")
                    print('\033[1m==================================================================\n\033[0m')

            
            (melhor_path, melhor_custo, recursosgastos, melhor_vehiculo) = selection.selecionaTheBest(GasolinaComoCriterioDeDecisao, resAviao, resCarro, resBarco, aviao, carro, barco, recursosDeCadaCidade,heuristicas)


        elif saida == 12:

            check = True
            while (check):

                print('\033[1m==================================================================\033[0m')
                inicio = input("Este só será usado na primeira viagem\n\033[1m[Nodo Inicial]:\033[0m ")
                fim =    input("  \033[1m[Nodo final]:\033[0m ")
                print('\033[1m==================================================================\n\033[0m')

                if g[0].getH(fim) > 0: #so vamos ir ao nodo fim se ainda esta disponivel
                    if posiçõesAtuais["Avião"] != None: resAviao = g[0].greedy(posiçõesAtuais["Avião"], fim)
                    else: resAviao = g[0].greedy(inicio, fim)

                    if posiçõesAtuais["Carro"] != None: resCarro = g[1].greedy(posiçõesAtuais["Carro"], fim)
                    else: resCarro = g[1].greedy(inicio, fim)
                    
                    if posiçõesAtuais["Barco"] != None: resBarco = g[2].greedy(posiçõesAtuais["Barco"], fim)
                    else: resBarco = g[2].greedy(inicio, fim)

                    check = False
                
                else:
                    print('\033[1m==================================================================\033[0m')
                    print("A cidade que pretende alcançar não se encontra disponível.")
                    print("Insira um novo destino")
                    print('\033[1m==================================================================\n\033[0m')

            (melhor_path, melhor_custo, recursosgastos, melhor_vehiculo) = selection.selecionaTheBest(GasolinaComoCriterioDeDecisao, resAviao, resCarro, resBarco, aviao, carro, barco, recursosDeCadaCidade, heuristicas)
        

        else:
            print('\033[1m==================================================================\033[0m')
            print("Não foi selecionada uma opção válida")
            print('\033[1m==================================================================\n\033[0m')

            sleep(0.1)
        
        ##response##

        if saida >= 9 and saida <= 12:
            if melhor_path:

                if melhor_custo == "Carro": 
                    carro.decrementaGasolina(melhor_custo)
                    carro.decrementaRecursos(recursosgastos)

                if melhor_custo == "Barco": 
                    barco.decrementaGasolina(melhor_custo)
                    barco.decrementaRecursos(recursosgastos)

                if melhor_custo == "Aviao": 
                    aviao.decrementaGasolina(melhor_custo)
                    aviao.decrementaRecursos(recursosgastos)

                print('\033[1m==================================================================\033[0m')
                print("O melhor veículo para esta viagem é o \033[1m[", melhor_vehiculo, "]\033[0m\n")
                print("{Recursos Distribuídos:\033[1m", recursosgastos, "\033[0m}")
                print("{Gasolina Gasta:\033[1m", melhor_custo, "\033[0m}")
                print("\nCaminho solução")
                print(melhor_path)
                print('\033[1m==================================================================\n\033[0m')


                #ja foi atualizado a gasolina/capacidade do vehiculo
                #guardar cidades visitadas numa lista
                selection.atualiza_cidades(cidadesVisitadas, melhor_path)


            else:
                print('\033[1m==================================================================\033[0m')
                print("De momento não é possível percorrer a viagem inserida.")
                print("Nenhum dos veículos possui \033[1mgasolina suficiente\033[0m para")
                print("efetuar o melhor caminho determinado.\n")
                print("\033[1mSerão restaurados os recursos e gasolina dos veículos\033[0m")
                print('\033[1m==================================================================\033[0m\n')

                RecursosDisponiveis -= aviao.restauraRecursos(RecursosDisponiveis)
                GasolinaDisponivel -= aviao.restauraGasolina(GasolinaDisponivel)
                RecursosDisponiveis -= carro.restauraRecursos(RecursosDisponiveis)
                GasolinaDisponivel -= carro.restauraGasolina(GasolinaDisponivel)
                RecursosDisponiveis -= barco.restauraRecursos(RecursosDisponiveis)
                GasolinaDisponivel -= barco.restauraGasolina(GasolinaDisponivel)


            
            if melhor_vehiculo: 
                posiçõesAtuais[melhor_vehiculo] = fim
                #print(posiçõesAtuais[melhor_vehiculo])

            #diminuir heuristica/Tempo de vida das cidades no visitadas
            g[0].decrement_life(cidadesVisitadas)
            g[1].decrement_life(cidadesVisitadas)
            g[2].decrement_life(cidadesVisitadas)

            #informar do novo Tempo de vida das cidades

            print('\033[1m==================================================================\033[0m')
            print("\033[1mNovos Tempos de Vida das cidades\033[0m")
            print(g[0].m_h)
            print('\033[1m==================================================================\n\033[0m')


            #é suposto o vehiculo ficar na cidade objetivo (oseja que esse vai ser o proximo Nodo Inicial para ele)
            if melhor_vehiculo:
                print('\033[1m==================================================================\033[0m')
                print("Nodo Inicial para a próxima viagem do\033[1m",melhor_vehiculo,"\033[0m:\033[1m",fim,"\033[0m")
                print('\033[1m==================================================================\n\033[0m')

            #evento aleatorio
            check, nodoA, nodoB = g[0].eventoAleatorio()
            if check:
                g[1].atualizaEvento(nodoA, nodoB)
                g[2].atualizaEvento(nodoA, nodoB)
                print('\033[1m==================================================================\033[0m')
                print("Aconteceu um evento entre\033[1m", nodoA, "\033[0me\033[1m", nodoB, "\033[0m")
                print('\033[1m==================================================================\n\033[0m')

                #print(g[0].m_graph)
        
        sleep(0.1)


if __name__ == "__main__":
    main()
