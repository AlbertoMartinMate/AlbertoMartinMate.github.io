# Clases -> protagonistas en POO (planos para los objetos)
# Clases crean objetos (intancian)
# Clases -> atributos y comportamientos
# Instanciar = inicializar = crear un objeto


class Persona:

    # __init__ se llama automaticamente al instanciar la clase (constructor)
    def __init__(self, nombre, edad, hora_dia) -> None:
        self.nombre = nombre
        self.edad = edad
        self.hora_dia = hora_dia

    def saludar(self):
        print(f"Hola { self.nombre} son las {self.hora_dia}")

    def despedirse(self):
        print("Adios")


persona1 = Persona("Laura", 22)  # 1 instancia (objeto) de la clase Persona
persona2 = Persona("Eduardo", 45)
persona3 = Persona("Sandra", 15)

persona3.saludar("2 pm ")
persona3.despedirse()
