from .Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self,quantidadeDeGasolinaAtual,quantidadeDeRecursosAtual):
        super().__init__(quantidadeDeGasolinaAtual,quantidadeDeRecursosAtual)