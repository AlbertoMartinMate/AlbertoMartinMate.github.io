"""Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta
es una mayúscula o una minúscula."""

# pedimos letra al usuario

letra = input("Introduce una letra en mayuscula o minúscula y averiguré que tipo es ")

# comprobamos q tipo es...

if letra == (letra.upper()):
    print("Es una letra mayúscula")

else:
    print("es una letra minuscula")
