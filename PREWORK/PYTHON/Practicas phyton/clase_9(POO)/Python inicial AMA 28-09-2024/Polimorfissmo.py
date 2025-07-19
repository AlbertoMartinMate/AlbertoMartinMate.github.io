# Permite a diferentes clases con el mismo metodo actuar diferente a su llamado
# el metodo de una subclase sustituye al metodo de la superclase
#podemos reescribir metodos(polimorfismo)
class Animal:
    def hacer_sonido(self):
        print("Hola estoy haciendo sonidos")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")


class Objea(Animal):
    def hacer_sonido(self):
        print("beee")


class Auto:
    def hacer_sonido(self):
        print("rum")


animal = Animal()
animal.hacer_sonido()
peroo = Perro()
peroo.hacer_sonido()
gato = Gato()
gato.hacer_sonido()
obeja = Objea()
obeja.hacer_sonido()
