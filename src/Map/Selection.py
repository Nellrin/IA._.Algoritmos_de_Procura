class Selection:            

    def atualiza_cidades(self, listaTotal, cidades_visitadas):
        for ciudad in cidades_visitadas:
            if ciudad not in listaTotal:
                listaTotal.append(ciudad)

    def recursosUsados(self, gastar, path, recursos, recursosDisponiveis, temposDeVida):
        totalRec = 0

        destino = path[-1]

        dictH = dict(temposDeVida)
        del dictH[destino]

        caminhoOrdenadoPorHeuristica = path.copy()
        caminhoOrdenadoPorHeuristica.remove(destino)

        caminhoOrdenadoPorHeuristica.sort(key=lambda cidade: dictH.get(cidade))
        caminhoOrdenadoPorHeuristica.insert(0,destino)

        print(f"Recursos: {recursos}")
        
        for cidade in caminhoOrdenadoPorHeuristica:
            if (totalRec + recursos[cidade]) < recursosDisponiveis:
                totalRec += recursos[cidade]

                if gastar:
                    recursos[cidade] = 0

            else:
                totalToTakeOut = recursosDisponiveis - totalRec
                if gastar:
                    recursos[cidade] -= totalToTakeOut
                
                totalRec += totalToTakeOut
                break

        return totalRec

    def selecionaTheBest(self, GasolinaComoPrioridade, resAviao, resCarro, resBarco, aviao, carro, barco, recursos,temposDeVida):
        # Inicializar la mejor opción como None y el mejor custo como infinito

        # print(aviao.getGasolina(), carro.getGasolina(), barco.getGasolina())
        # print(aviao.getRecursos(), carro.getRecursos(), barco.getRecursos())
        # print(resAviao)
        # print(resCarro)
        # print(resBarco)

        melhor_path = None
        melhor_custo = float('inf')
        melhor_veiculo = None  # Variable para almacenar el nombre del mejor vehículo
        recursosGastosMAX = 0

        # Verificar y comparar los custos
        if resBarco is not None:
            path_barco, custo_barco = resBarco
            recursosGastos = self.recursosUsados(False,path_barco, recursos, barco.getRecursos(),temposDeVida)
            if custo_barco <= barco.getGasolina() and ((GasolinaComoPrioridade and custo_barco < melhor_custo) or (not GasolinaComoPrioridade and recursosGastos > recursosGastosMAX)):
                recursosGastosMAX = recursosGastos
                melhor_path = path_barco
                melhor_custo = custo_barco
                melhor_veiculo = 'Barco'  # Guardamos el nombre del vehículo

        if resAviao is not None:
            path_aviao, custo_aviao = resAviao
            recursosGastos = self.recursosUsados(False,path_aviao, recursos, aviao.getRecursos(),temposDeVida)
            if custo_aviao <= aviao.getGasolina() and ((GasolinaComoPrioridade and custo_aviao < melhor_custo) or (not GasolinaComoPrioridade and recursosGastos > recursosGastosMAX)):
                recursosGastosMAX = recursosGastos
                melhor_path = path_aviao
                melhor_custo = custo_aviao
                melhor_veiculo = 'Avião'  # Guardamos el nombre del vehículo

        if resCarro is not None:
            path_carro, custo_carro = resCarro
            recursosGastos = self.recursosUsados(False,path_carro, recursos, carro.getRecursos(),temposDeVida)
            if custo_carro <= carro.getGasolina() and ((GasolinaComoPrioridade and custo_carro < melhor_custo) or (not GasolinaComoPrioridade and recursosGastos > recursosGastosMAX)):
                recursosGastosMAX = recursosGastos
                melhor_path = path_carro
                melhor_custo = custo_carro
                melhor_veiculo = 'Carro'  # Guardamos el nombre del vehículo
        
        if melhor_veiculo == 'Avião':
            recursosGastosMAX = self.recursosUsados(True,path_aviao, recursos, aviao.getRecursos(),temposDeVida)
            aviao.decrementaRecursos(recursosGastos)
            aviao.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Carro':
            recursosGastosMAX = self.recursosUsados(True,path_carro, recursos, carro.getRecursos(),temposDeVida)
            carro.decrementaRecursos(recursosGastos)
            carro.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Barco':
            recursosGastosMAX = self.recursosUsados(True,path_barco, recursos, barco.getRecursos(),temposDeVida)
            barco.decrementaRecursos(recursosGastos)
            barco.decrementaGasolina(melhor_custo)

        return (melhor_path, melhor_custo, recursosGastosMAX, melhor_veiculo)