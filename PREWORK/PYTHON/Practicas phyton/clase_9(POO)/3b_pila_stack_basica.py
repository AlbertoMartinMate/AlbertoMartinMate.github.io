"""PILA (STACK) BÁSICA
En programación, un "stack" es una estructura de datos que sigue el principio de LIFO (Last In, First Out), 
lo que significa que el último elemento agregado a la pila es el primero en ser retirado. Imagina una 
pila de platos:cuando apilas un nuevo plato, este se coloca en la parte superior de la pila, y cuando 
retiras un plato, siempre tomas el de arriba primero.
En Python, puedes implementar un stack utilizando una lista. Puedes agregar elementos a la pila 
utilizando el método `append()`, y puedes retirar elementos de la pila utilizando el método `pop()` 
sin ningún índice especificado, ya que `pop()` por defecto elimina y devuelve el último elemento de la lista.
Los stacks son útiles en muchas situaciones, como algoritmos de búsqueda y recorrido, manejo de llamadas 
a funciones (con la pila de llamadas), manejos de historial y navegación y más.
Crea una clase "Pila" que represente una pila (stack) básica. Implementa métodos para agregar elementos 
a la pila, quitar elementos y mostrar elcontenido actual.
Por supuesto, estaré encantado de explicarte qué es un "stack" en el contexto de la programación y cómo se utiliza en Python."""

class Pila:
    
    #pila(stack) básica
    def __init__(self):
        self.elementos=[]

    #metodo para agregar elementos a la pila
    def añadir_elementos(self, elemento):
        self.elementos.append(elemento)
        return f"Añadiendo elemento {elemento} ..."

    #metodo para quitar elementos a la pila
    def quitar_elementos(self):   #corregido crea def esta_vacia(self):
        if self.elementos:                         # return len(self.elementos)==0
            self.elementos.pop()     # y aqui... if not self.esta_vacia():
            return f"Quitando el ultimo elemento..."  #return self.elementos.pop()
                                                       #else igual
        else:
            return "La pila de elementos esta vacia, por lo que no puedo eliminar"

    #mostrar contenido

    def mostrar_contenido(self):
        print (f"Mi lista de elementos es el siguiente: {self.elementos}")

mis_elementos= Pila()
mis_elementos.mostrar_contenido()
print(mis_elementos.quitar_elementos())
print(mis_elementos.añadir_elementos("Sodio"))
mis_elementos.mostrar_contenido()

print(mis_elementos.añadir_elementos("Potasio"))
mis_elementos.mostrar_contenido()

print(mis_elementos.quitar_elementos())
mis_elementos.mostrar_contenido()