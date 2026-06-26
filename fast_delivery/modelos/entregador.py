from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    """Classe Entregador herdando de Pessoa"""
    
    def __init__(self, nome: str, veiculo: str, cnh: str):
        super().__init__(nome)
        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self) -> str:
        return self.__veiculo

    @property
    def cnh(self) -> str:
        return self.__cnh