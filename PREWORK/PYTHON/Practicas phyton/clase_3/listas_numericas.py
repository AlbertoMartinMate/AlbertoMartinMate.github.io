

#-->1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].

#numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros=(range(1, 11))

#-->2. Crea una nueva lista con los números pares de la lista anterior en orden inverso

pares = [numero for numero in numeros if numero % 2 ==0] # si añadimos [::-1], nos ahorramos el paso siguiente 
pares.reverse()
print(pares)
print("----------------")


#-->3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola.

for numero in numeros:
 print (numero, numero**2)

print("-------------")

#-->4. Intenta rehacer los pasos 2 y 3  con el menor número de lineas posible (método de compresión).

#-->5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla

numero_menor = min(numeros) #utilizo esta funcion para que imprima el valor minimo
print(numero_menor) 
print("------------------")

#-->6. Haz lo mismo con el número más alto
numero_mayor = max(numeros)
print(numero_mayor)
print("----------------")

#-->7. Suma todos los elementos de la lista con y sin un bucle.

#con bucle
numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma=0

for numero in numeros:
  suma+=numero

print (suma) #tabular a la altura de for...sino imprime los correlativos
print("---------------------")

#sin bucle
sumatorio= sum(numeros)
print(sumatorio)
print("-----------------")

#-->8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras el punto 2.

indice_8=numeros.index(8)
print(indice_8)
print("------------------")

numeros.reverse() #le doy la vuelta otra vez como en el punto 2

indice_8=numeros.index(8)
print(indice_8)
print("--------------")
