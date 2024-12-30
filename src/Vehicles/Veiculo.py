class Veiculo:

    def __init__(self, capacidadeDeGasolina, capacidadeDeRecursos):
        self.gasolinaAtual        = capacidadeDeGasolina 
        self.capacidadeDeGasolina = capacidadeDeGasolina
        self.recursosAtuais       = capacidadeDeRecursos
        self.capacidadeDeRecursos = capacidadeDeRecursos

    def getGasolina(self):
        return self.gasolinaAtual
    
    def getRecursos(self):
        return self.recursosAtuais

    def restauraGasolina(self):
        self.gasolinaAtual = self.capacidadeDeGasolina

    def restauraRecursos(self):
        self.recursosAtuais = self.capacidadeDeRecursos


    def decrementaRecursos(self, valor):
        quantidadeRetirada = min(self.recursosAtuais, valor)
        self.recursosAtuais -= quantidadeRetirada

    def decrementaGasolina(self, valor):
        quantidadeRetirada = min(self.gasolinaAtual, valor)
        self.gasolinaAtual -= quantidadeRetirada