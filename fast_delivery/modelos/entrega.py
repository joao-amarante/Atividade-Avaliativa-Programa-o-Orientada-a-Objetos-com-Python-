from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaComum(CalculoFreteInterface):
    """Implementa o cálculo para entrega comum"""
    def __init__(self, distancia: float):
        self.__distancia = distancia

    def calcular_frete(self) -> float:
        return self.__distancia * 1.5

class EntregaExpressa(CalculoFreteInterface):
    """Implementa o cálculo para entrega expressa"""
    def __init__(self, distancia: float):
        self.__distancia = distancia

    def calcular_frete(self) -> float:
        return self.__distancia * 3.0

class EntregaPremium(CalculoFreteInterface):
    """Implementa o cálculo para entrega premium"""
    def __init__(self, distancia: float):
        self.__distancia = distancia

    def calcular_frete(self) -> float:
        return (self.__distancia * 5.0) + 20.0