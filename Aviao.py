class Aviao:

    FINAL_GASOLINA = 45
    FINAL_CAPACIDADE = 80

    def __init__(self):     
        self.gasolina = Aviao.FINAL_GASOLINA
        self.capacidade = Aviao.FINAL_CAPACIDADE
    
    def getGasolina(self):
        return self.gasolina
    
    def getCapacidade(self):
        return self.capacidade

    def restauraGasolina(self):
        self.gasolina = Aviao.FINAL_GASOLINA

    def restauraCapacidade(self):
        self.capacidade = Aviao.FINAL_CAPACIDADE

    def decrementaCapacidade(self, valor):
        self.capacidade -= valor

    def decrementaGasolina(self, valor):
        self.gasolina -= valor