class Barco:

    FINAL_GASOLINA = 100
    FINAL_CAPACIDADE = 100

    def __init__(self):     
        self.gasolina = Barco.FINAL_GASOLINA
        self.capacidade = Barco.FINAL_CAPACIDADE
    
    def getGasolina(self):
        return self.gasolina
    
    def getCapacidade(self):
        return self.capacidade

    def restauraGasolina(self):
        self.gasolina = Barco.FINAL_GASOLINA

    def restauraCapacidade(self):
        self.capacidade = Barco.FINAL_CAPACIDADE

    def decrementaCapacidade(self, valor):
        self.capacidade -= valor

    def decrementaGasolina(self, valor):
        self.gasolina -= valor