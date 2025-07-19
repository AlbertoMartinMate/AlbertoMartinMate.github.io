"""Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
 - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
 - Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales."""

class Vuelo:
    """Vamos a crear un tipo de vuelo con diferentes caracteristicas"""
    def __init__(self, numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo= numero_vuelo
        self.origen= origen
        self.destino= destino
        self.capacidad=capacidad
        self.lista_pasajeros=[]
    
    def disponibilidad_asientos(self):
        #valoramos la disponibilidad de asientos
        return self.capacidad - len(self.lista_pasajeros)
            
    def agregar_pasajero(self, pasajero):
        #agregamos pasajeros al vuelo si hay plazas
        self.pasajero=pasajero
        if self.disponibilidad_asientos()>0:
            self.lista_pasajeros.append(self.pasajero)
            print(f"{self.pasajero} añadido al vuelo")
            print(f"Plazas vacantes restantes: {self.capacidad - len(self.lista_pasajeros)}")
        else:
            print(f"No hay plazas disponibles. No se puede añadir el pasajero {pasajero}.")
            
    
    def imprimir_vuelo(self):
        #muestro caracteristicas del vuelo y listado pasajeros
        print(f"El vuelo {self.numero_vuelo}, con origen {self.origen},"
            f" y destino {self.destino}, con una capacidad de {self.capacidad} pasajeros.\n"
            f"Tiene los siguientes pasajeros: {self.lista_pasajeros}")


class VueloEspecial(Vuelo):
    """Creamos una subclass de vuelo de otro tipo de vuelos"""
    def __init__(self, numero_vuelo, origen, destino, capacidad, motivo):
        super().__init__(numero_vuelo, origen, destino, capacidad)
        self.motivo = motivo

    def imprimir_vuelo_especial(self):
        #muestro caracteristicas del vuelo y listado pasajeros
        print(f"El vuelo {self.numero_vuelo}, con origen {self.origen},"
            f" y destino {self.destino}, con un motivo de vuelo {self.motivo},"
            f" con una capacidad de {self.capacidad} pasajeros.\n"
            f"Tiene los siguientes pasajeros: {self.lista_pasajeros}")



#Ejemplo se uso

vuelo1=Vuelo(1234,"Madrid", "Cuba", 2)
vuelo1.agregar_pasajero("Alberto")
vuelo1.agregar_pasajero("Maria")
vuelo1.agregar_pasajero("Rodrigo")
vuelo1.imprimir_vuelo()

vuelo2=VueloEspecial(4231, "Oviedo", "Santiago", 5, "Trabajo")
vuelo2.agregar_pasajero("Gonzalo")
vuelo2.agregar_pasajero("Lucas")
vuelo2.imprimir_vuelo_especial()
