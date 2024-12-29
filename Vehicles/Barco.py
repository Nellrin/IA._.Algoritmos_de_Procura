from .Veiculo import Veiculo

class Barco(Veiculo):

    def __init__(self,quantidadeDeGasolinaAtual,quantidadeDeRecursosAtual):
        super().__init__(quantidadeDeGasolinaAtual,quantidadeDeRecursosAtual)