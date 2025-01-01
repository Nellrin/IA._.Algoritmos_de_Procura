class Selection:            

    def atualiza_cidades(self, listaTotal, cidades_visitadas):
        for ciudad in cidades_visitadas:
            if ciudad not in listaTotal:
                listaTotal.append(ciudad)

    def recursosUsados(self, path, recursos, recursosDisponiveis, temposDeVida):
        totalRec = 0

        destino = path[-1]

        dictH = dict(temposDeVida)
        del dictH[destino]

        caminhoOrdenadoPorHeuristica = path.copy()
        caminhoOrdenadoPorHeuristica.remove(destino)

        caminhoOrdenadoPorHeuristica.sort(key=lambda cidade: dictH.get(cidade))
        caminhoOrdenadoPorHeuristica.insert(0,destino)

        
        for cidade in caminhoOrdenadoPorHeuristica:
            if (totalRec + recursos[cidade]) < recursosDisponiveis:
                totalRec += recursos[cidade]
                recursos[cidade] = 0

            else:
                totalToTakeOut = recursosDisponiveis - totalRec
                recursos[cidade] -= totalToTakeOut
                totalRec += totalToTakeOut
                break

        return totalRec

    def selecionaTheBest(self, resAviao, resCarro, resBarco, aviao, carro, barco, recursos,temposDeVida):
        # Inicializar la mejor opción como None y el mejor custo como infinito

        # print(aviao.getGasolina(), carro.getGasolina(), barco.getGasolina())
        # print(aviao.getRecursos(), carro.getRecursos(), barco.getRecursos())
        # print(resAviao)
        # print(resCarro)
        # print(resBarco)

        melhor_path = None
        melhor_custo = float('inf')
        melhor_veiculo = None  # Variable para almacenar el nombre del mejor vehículo

        # Verificar y comparar los custos
        if resAviao is not None:
            path_aviao, custo_aviao = resAviao
            if custo_aviao < melhor_custo and custo_aviao <= aviao.getGasolina():
                melhor_path = path_aviao
                melhor_custo = custo_aviao
                melhor_veiculo = 'Avião'  # Guardamos el nombre del vehículo

        if resCarro is not None:
            path_carro, custo_carro = resCarro
            if custo_carro < melhor_custo and custo_carro <= carro.getGasolina():
                melhor_path = path_carro
                melhor_custo = custo_carro
                melhor_veiculo = 'Carro'  # Guardamos el nombre del vehículo

        if resBarco is not None:
            path_barco, custo_barco = resBarco
            
            if custo_barco < melhor_custo and custo_barco <= barco.getGasolina():
                melhor_path = path_barco
                melhor_custo = custo_barco
                melhor_veiculo = 'Barco'  # Guardamos el nombre del vehículo
        
        if melhor_veiculo == 'Avião':
            aviao.decrementaRecursos(self.recursosUsados(path_aviao, recursos, aviao.getRecursos(),temposDeVida))
            aviao.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Carro':
            carro.decrementaRecursos(self.recursosUsados(path_carro, recursos, carro.getRecursos(),temposDeVida))
            carro.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Barco':
            barco.decrementaRecursos(self.recursosUsados(path_barco, recursos, barco.getRecursos(),temposDeVida))
            barco.decrementaGasolina(melhor_custo)

        return (melhor_path, melhor_custo, melhor_veiculo)