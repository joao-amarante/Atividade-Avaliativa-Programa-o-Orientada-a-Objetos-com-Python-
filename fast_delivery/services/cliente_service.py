from modelos.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.__clientes = [] # Banco de dados em memória

    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str, endereco: str):
        novo_cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(novo_cliente)
        return novo_cliente

    def listar_clientes(self) -> list:
        return self.__clientes

    def buscar_cliente_por_cpf(self, cpf: str) -> Cliente:
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None