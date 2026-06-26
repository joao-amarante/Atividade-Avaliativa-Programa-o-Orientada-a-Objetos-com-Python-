from modelos.entregador import Entregador

class EntregaService:
    def __init__(self):
        self.__entregadores = []

    def cadastrar_entregador(self, nome: str, veiculo: str, cnh: str):
        novo_entregador = Entregador(nome, veiculo, cnh)
        self.__entregadores.append(novo_entregador)
        return novo_entregador

    def listar_entregadores(self) -> list:
        return self.__entregadores