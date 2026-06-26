from modelos.pedido import Pedido
from modelos.cliente import Cliente
from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class PedidoService:
    def __init__(self):
        self.__pedidos = []

    def criar_pedido(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo: int) -> Pedido:
        # Define a estratégia de frete (Polimorfismo)
        if tipo == 1:
            entrega = EntregaComum(distancia)
        elif tipo == 2:
            entrega = EntregaExpressa(distancia)
        elif tipo == 3:
            entrega = EntregaPremium(distancia)
        else:
            raise ValueError("Tipo de entrega inválido.")

        novo_pedido = Pedido(codigo, cliente, peso, distancia, entrega)
        self.__pedidos.append(novo_pedido)
        return novo_pedido

    def listar_pedidos(self) -> list:
        return self.__pedidos

    def atualizar_status(self, codigo: str, novo_status: str):
        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                pedido.status = novo_status
                return True
        return False