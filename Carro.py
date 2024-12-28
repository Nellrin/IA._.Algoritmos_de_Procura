class Carro:

    FINAL_GASOLINA = 65
    FINAL_CAPACIDADE = 50

    def __init__(self):     
        self.gasolina = Carro.FINAL_GASOLINA
        self.capacidade = Carro.FINAL_CAPACIDADE
    
    def getGasolina(self):
        return self.gasolina
    
    def getCapacidade(self):
        return self.capacidade

    def restauraGasolina(self):
        self.gasolina = Carro.FINAL_GASOLINA

    def restauraCapacidade(self):
        self.capacidade = Carro.FINAL_CAPACIDADE

    def decrementaCapacidade(self, valor):
        self.capacidade -= valor

    def decrementaGasolina(self, valor):
        self.gasolina -= valor