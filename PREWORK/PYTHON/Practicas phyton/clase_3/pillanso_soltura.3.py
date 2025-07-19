# -->3. Escribe un script que encuentre el segundo número más grande de una lista.

#creamos una lista vacia. pedimos por pantalla una serie de numeros

lista=[4, 5, 6, 1, 3]

#lista=input("Introduce una serie de numeros: ") #tengo q escribirlos seguidos...
#SI NO LOS PIDO YO SI ME SALE...SI PIDO NUMEROS ME DA ERROR

 #ordeno la lista    
lista.sort()

#imprimo el penultimo
print(lista[-2])