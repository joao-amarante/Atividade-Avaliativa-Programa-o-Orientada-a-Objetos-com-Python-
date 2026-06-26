from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    """Interface para definir o contrato de cálculo de frete"""
    
    @abstractmethod
    def calcular_frete(self) -> float:
        """Método que deverá possuir comportamentos diferentes em cada tipo de entrega"""
        pass