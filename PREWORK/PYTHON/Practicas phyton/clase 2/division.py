"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error."""

# pedimos dos números, de los cuales vamos a hacer la division

numero1 = float(input("Ingresa el primer número de la división (dividendo) : "))
numero2 = float(input("Ingresa el cociente de la división : "))

# hacemos un condicional, en el cual si número2 es 0, imprima q no se puede dividir entre 0

if numero2 != 0:
    resultado = numero1 / numero2
    print("El resultado de la división es :", resultado)

else:
    print("No se puede dividir entre 0")
