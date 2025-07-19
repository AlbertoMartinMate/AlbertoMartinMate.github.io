
#-->6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.

numero = int((input)("Introduce un número y te dire justo el inferior de mi lista: "))
lista = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
numeros_inferiores=[]

for num in lista:
  if numero > num:
    numeros_inferiores.append(num)

print (max(numeros_inferiores))