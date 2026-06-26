class Pessoa:
    """Superclasse que será herdada por Cliente e Entregador"""
    
    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome