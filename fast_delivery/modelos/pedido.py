from modelos.cliente import Cliente
from interfaces.calculo_frete_interface import CalculoFreteInterface

class Pedido:
    """Classe que representa um pedido no sistema"""
    def __init__(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo_entrega: CalculoFreteInterface):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__status = "Em preparação"
        self.__valor_frete = self.__tipo_entrega.calcular_frete() # Polimorfismo aplicado aqui

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, novo_status: str):
        status_permitidos = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]
        if novo_status in status_permitidos:
            self.__status = novo_status
        else:
            raise ValueError("Status inválido.")

    @property
    def valor_frete(self) -> float:
        return self.__valor_frete