
#1. Crea un array_1 lleno ceros con una longitud de 8 elementos.


import numpy as np

array_1= np.zeros(8)

#2. Haz que todos los elementos de este array sean igual a 2

array_1[:]=2

#3. Crea un array_2 que contenga todos los números pares del 1 al 10.

array_2=np.arange(2,11,2)
print(array_2)

#4. Suma todos los elementos del array_2 usando un bucle y después usando un método
#de numpy. Compara los resultados

resultado=0

for n in array_2:
  resultado +=n

print("La suma del bucle: ", resultado)

resultado_2= array_2.sum()

print("El resultado con metodo numpy es: ", resultado_2)

#5. Revierte array_2 y guárdalo en una variable independiente.

array_reverse = np.flip(array_2) #tambien se puede utilizar arrayreverse[:]= array_2[::-1]
                                  #[:]para que no modifique el original.
                                  #me da error al imprimir, me sale [np.int64(10), np.ont64(8),...]

print("El array 2 al reves: ", array_reverse)

#6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_2_revertido
 #(Pista: Investiga el uso de intersect1d() de numpy)

interseccion= np.intersect1d(array_1, array_2)

print("Los elementos comunes entre el array_1 y el array_2, son: ", interseccion)

interseccion_2= np.intersect1d(array_2, array_reverse)

print("Los elementos comunes entre el array_2 y el array_2 revertido, son: ", interseccion_2)


#7. Crea un arrays lleno de 1s con una longitud dada por el usuario

longitud_usuario= int(input("Introduce la longitud del array que quieres: "))

array_3=np.ones(longitud_usuario)

print("El array es de la siguiente manera: ", array_3)