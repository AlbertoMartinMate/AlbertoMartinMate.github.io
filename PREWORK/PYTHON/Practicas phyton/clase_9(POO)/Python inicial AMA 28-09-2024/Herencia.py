# Herencia de clases
# Moto es un Vehiculo
# Avion es un vehiculo
# Leon es un animal


class Vehiculo:
    def __init__(self, marca) -> None:
        self.marca = marca

    def conducir(self):
        print(f"Conduciendo el vehiculo de marca {self.marca}")

    def apagar(self):
        print("Apagando vehiculo")


# Clase hija de vehiculo
class Moto(Vehiculo):
    def __init__(self, marca) -> None:
        super().__init__(marca)

    def caballito(self):
        print("Encendiendo motor de moto a pedal")


class Auto(Vehiculo):
    def __init__(self, marca) -> None:
        super().__init__(marca)

    def abrir_puertas(self):
        print("Abriendo puertas del auto")


moto = Moto("Yamaha")
moto.caballito()
moto.conducir()
moto.apagar()

auto = Auto("Toyota")
auto.conducir()
auto.abrir_puertas()
