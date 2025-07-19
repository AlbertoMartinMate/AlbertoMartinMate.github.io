# Separar objetos de un entorno y quedarnos con lo principal o ocultar los detalles
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod  # No podemos instanciar o llamar a clases abstractas
    def area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


rectangulo = Rectangulo(2, 2)
print(rectangulo.area())

# figura = Figura()
# figura.area() ERROR
