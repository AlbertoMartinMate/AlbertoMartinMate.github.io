"""Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la
suma de los otros dos."""

# enunciamos lo q vamos hacer

print(
    "Vamos a pedir tres números diferentes y a adivinar si alguno de ellos es la suma\
        de los otros dos"
)

# pedimos numeros

numero_1 = int(input("Introduce el primer número "))
numero_2 = int(input("Introduce el segundo número "))
numero_3 = int(input("Introduce el tercer número "))

# hacemos las comprobaciones con los cuatro casos posibles e imprimimos

if numero_1 == numero_2 + numero_3:
    print("El primer número es la suma de los otros dos")

elif numero_2 == numero_1 + numero_3:
    print("El segundo número es la suma de los otros dos")

elif numero_3 == numero_1 + numero_2:
    print("El tercer número es la suma de los otros dos")

else:
    print("Ningun número es la suma de los otros dos")
