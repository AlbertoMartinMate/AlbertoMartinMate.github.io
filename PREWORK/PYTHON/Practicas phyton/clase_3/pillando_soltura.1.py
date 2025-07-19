

#-->1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
#añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
#elementos únicos. 

# ESTE SALE OK, PERO AL PEDIR YO LOS PRODUCTOS ME DA ERROR, POR EL REMOVE, EN EL
#PRIMER CASO NO ENTIENDO XQ SALE

#creamos una lista vacia y pedimos al usuario que introduzca valores.


lista_compra=["setas", "pan", "huevos", "leche", "galletas", "pan"]

productos_duplicados=[]  #creamos una lista vacia para los duplicado
vistos=[]  #creamos un conjunto vacio para rastrear los elementos vistos

#buscamos elementos duplicados. recorremos la lista de string


for palabra in lista_compra:
  if palabra in vistos and palabra not in productos_duplicados:
    productos_duplicados.append(palabra) #agregamos a la lista de duplicados

  else:
   vistos.append(palabra) #agregamos al conjunto de vistos

print("Los productos repetidos son: ", productos_duplicados)

lista_compra.remove(palabra) #lo borramos de la lista. me ha funcionado con este metodo, pero yo creo q se podria hacer como la forma anterior y en vez de agragarlo a lista, borrarlo

print(lista_compra)

lista_compra = []
productos_duplicados = []  # creamos una lista vacia para los duplicado
vistos = []  # creamos un conjunto vacio para rastrear los elementos vistos

for i in range(0, 4):

    producto = input("Introduce un producto a comprar: ")
    lista_compra.append(producto)

for palabra in lista_compra:
    if palabra in vistos and palabra not in productos_duplicados:
        productos_duplicados.append(palabra)  # agregamos a la lista de duplicados

    else:
        vistos.append(palabra)  # agregamos al conjunto de vistos

print("Los productos repetidos son: ", productos_duplicados)

lista_compra.remove(palabra)

print(lista_compra)






# -->4. Crea un script que cuente el número de elementos más grandes que un determinado número
# dado por el usuario (supón una lista numérica).


# -->5. Crea un script dado un número introducido por el usuario o determinado al inicio del
# programa, realice la suma de aquellos números que sean divisibles por este.


# -->6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
# que es inferior al número introducido o determinado al inicio del programa.



# -->8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
# (P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)


# -->9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.


# -->10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
# los strings de la lista original.

# -->11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en mayúscula.
