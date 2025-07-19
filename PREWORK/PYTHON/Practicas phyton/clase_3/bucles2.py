"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta"""

contraseña = "alberto"

passw = input("Introduzca la contraseña: ")
passw = passw.lower()

while contraseña != passw:
    print("Por favor, introduce la contraseña de nuevo")
    passw = input(
        "Introduzca la contraseña: "
    )  # ponemos condicion xq sino sale del bucle
    passw = passw.lower()

print("Contraseña correcta")
