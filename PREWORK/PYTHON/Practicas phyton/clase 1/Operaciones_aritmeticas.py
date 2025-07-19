"""a. Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética:"""

# ((3+2) / (2*5))**2

resultado_a = ((3 + 2) / (2 * 5)) ** 2
print("El resultado de la operación aritmética es: ", resultado_a)

"""B.-Escribe un programa que lea un entero positivo, n, introducido por el usuario y después 
muestre por pantalla el resultado de la siguiente operación:"""

n = int(input("Introduce un número entero positivo: "))
resultado_b = n * (n + 1) / 2
print("El resultado de la operación aritmética es: ", resultado_b)

"""c.- c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla 
los números de entrada, el cociente y el resto."""

num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
cociente = num1 // num2
print("El cociente de los números es: ", cociente)
resto = num1 % num2
print("El resto de los números es: ", resto)
