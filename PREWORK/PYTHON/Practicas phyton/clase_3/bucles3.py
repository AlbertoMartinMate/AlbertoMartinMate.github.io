"""Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última."""

# pedimos al usuario una palabra

palabra = input("Introduce una palabra: ")

palabra_reves = palabra[::-1]  #le da la vuelta. quiero q rocarra todo (::) con paso -1 (empezando desde el final)

for (letra) in (palabra_reves):  # esto recorre cada caracter de la palabra (cadena de texto) y lo asigna a la variable letra
    print(letra)
