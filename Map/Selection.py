from Vehicles import Aviao, Barco, Carro

class Selection:            

    def atualiza_cidades(self, listaTotal, cidades_visitadas):
        for ciudad in cidades_visitadas:
            if ciudad not in listaTotal:
                listaTotal.append(ciudad)

    def recursosUsados(self, path, recursos):
        totalRec = 0
        for cidade in path:
            totalRec += recursos[cidade]
        return totalRec

    def selecionaTheBest(self, resAviao, resCarro, resBarco, aviao, carro, barco, recursos):
        # Inicializar la mejor opción como None y el mejor custo como infinito

        # print(aviao.getGasolina(), carro.getGasolina(), barco.getGasolina())
        # print(aviao.getRecursos(), carro.getRecursos(), barco.getRecursos())
        # print(resAviao)
        # print(resCarro)
        # print(resBarco)

        melhor_path = None
        melhor_custo = float('inf')
        melhor_veiculo = None  # Variable para almacenar el nombre del mejor vehículo
        melhor_recursos = float('inf')

        # Verificar y comparar los custos
        if resAviao is not None:
            path_aviao, custo_aviao = resAviao
            totalRec = self.recursosUsados(path_aviao, recursos)
            if custo_aviao < melhor_custo and custo_aviao <= aviao.getGasolina() and totalRec <= aviao.getRecursos():
                melhor_path = path_aviao
                melhor_custo = custo_aviao
                melhor_recursos = totalRec
                melhor_veiculo = 'Avião'  # Guardamos el nombre del vehículo

        if resCarro is not None:
            path_carro, custo_carro = resCarro
            totalRec = self.recursosUsados(path_carro, recursos)
            if custo_carro < melhor_custo and custo_carro <= carro.getGasolina() and totalRec <= carro.getRecursos():
                melhor_path = path_carro
                melhor_custo = custo_carro
                melhor_recursos = totalRec
                melhor_veiculo = 'Carro'  # Guardamos el nombre del vehículo

        if resBarco is not None:
            path_barco, custo_barco = resBarco
            totalRec = self.recursosUsados(path_barco, recursos)
            if custo_barco < melhor_custo and custo_barco <= barco.getGasolina() and totalRec <= barco.getRecursos():
                melhor_path = path_barco
                melhor_custo = custo_barco
                melhor_recursos = totalRec
                melhor_veiculo = 'Barco'  # Guardamos el nombre del vehículo
        
        if melhor_veiculo == 'Avião':
            aviao.decrementaRecursos(melhor_recursos)
            aviao.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Carro':
            carro.decrementaRecursos(melhor_recursos)
            carro.decrementaGasolina(melhor_custo)

        elif melhor_veiculo == 'Barco':
            barco.decrementaRecursos(melhor_recursos)
            barco.decrementaGasolina(melhor_custo)

        return (melhor_path, melhor_custo, melhor_veiculo)