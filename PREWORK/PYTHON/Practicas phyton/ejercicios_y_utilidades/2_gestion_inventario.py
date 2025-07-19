"""Problema de Gestión de Inventario:
Imagina que trabajas en una empresa de logística y tu tarea es desarrollar un
sistema de gestión de inventario. El inventario está representado como una lista
de productos ordenados por sus códigos. Cada producto se describe como un
diccionario con las claves 'codigo' y 'cantidad' .
Tu objetivo es implementar una función recursiva que realice una búsqueda
binaria en este inventario y devuelva la cantidad disponible para un producto
específico, dado su código.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada                                         
- Inventario de productos (json,dic,etc)
- Codigo de producto buscado

Salida

Cantidad disponible para el producto 307:
80"""


def busqueda_inventario(mi_inventario, codigo_producto, i=0, fin=None):
    if fin==None:
        fin=len(mi_inventario)-1
        #caso base: si el rango no es valido
    if i>fin:
        return 0
    
    medio=(i+fin)//2 #lo dividimos en dos y buscamos en la parte correspondiente

#comparar el codigo del producto con el codigo de la posicion media
    if mi_inventario[medio]["codigo"]==codigo_producto: #caso base PRIMERO
        return mi_inventario[medio]["cantidad"]  #va buscando haste q lo cumple, variando el codigo, 
                                                  #y cuando encuentra...return la cantidad
                                                  
    elif mi_inventario[medio]["codigo"]>codigo_producto:      
        #el codigo va a estar en el lado izquierdo del inventario
        return busqueda_inventario(mi_inventario, codigo_producto, i, fin=medio-1)
    else:
        #el codigo va a estar en el lado derecho del inventario
        return busqueda_inventario(mi_inventario, codigo_producto, medio+1, fin)

mi_inventario=[{"codigo": 101, "cantidad":4 },
               {"codigo": 102, "cantidad":5 },
               {"codigo": 103, "cantidad":4 },
               ]

codigo_producto=103

cantidad_disponible = busqueda_inventario(mi_inventario,codigo_producto)
print(f"Cantidad de stock disponible para el producto {codigo_producto} es de: {cantidad_disponible}")





