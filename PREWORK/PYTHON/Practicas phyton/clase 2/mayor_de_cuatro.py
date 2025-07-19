"""Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los
cuatro por pantalla."""

# pedimos al usuario q introduzca 4 números, dándole a cada número una variable diferentes

numero_1 = int(input("Introduce el primer número "))
numero_2 = int(input("Segundo número "))
numero_3 = int(input("Tercer número "))
numero_4 = int(input("Cuarto número "))

# creamos una variable para guardar el número mayor

numeromayor = numero_1

# tambien podriamos hacerlo asi.... numeromayor = max(numero_1, numero_2, numero_3, numero_4)

# hacemos un condicional para ver si el número 2 es mayor que el número 1, y asi sucesivamente con todos
if numero_2 > numeromayor:
    numeromayor = numero_2
if numero_3 > numeromayor:
    numeromayor = numero_3
if numero_4 > numeromayor:
    numeromayor = numero_4

# imprimimos el resultado

print("El número mayor es: ", numeromayor)

# otra forma que se puede hacer. visto en clase para ordenar los numeros como para poder ver el mayor,
# en este caso lo hacemos para ver el mayor

# pd: lo hago tres veces para que terminen de ordenarse los números.. ya que dado 2,5,3,1 no se ordenaban del todo

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1

if numero_2 > numero_3:
    numero_2, numero_3 = numero_3, numero_2

if numero_3 > numero_4:
    numero_3, numero_4 = numero_4, numero_3


if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1

if numero_2 > numero_3:
    numero_2, numero_3 = numero_3, numero_2

if numero_3 > numero_4:
    numero_3, numero_4 = numero_4, numero_3


if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1

if numero_2 > numero_3:
    numero_2, numero_3 = numero_3, numero_2

if numero_3 > numero_4:
    numero_3, numero_4 = numero_4, numero_3


print("El número mayor es ", numero_4)

print(
    "El orden de los números de menor a mayor es ",
    numero_1,
    numero_2,
    numero_3,
    numero_4,
)
