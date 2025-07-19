"""FACTORIAL Implementa una función recursiva llamada factorial que calcule el factorial de un
 número entero positivo. El factorial de un número n se de ne como el producto de todos los 
 números enteros positivos desde 1 hasta n. (El factorial de 0 y de 1 es igual a 1)"""

from functools import lru_cache #modulo x defecto en python. opcional

@lru_cache(maxsize=None)
#guarda en cache todos los resultados sin limite. opcional

def factorial(n):
    #nos saca los factoriales en funcion de n
    
    if n==0 or n==1:#planteamos el caso base
        return 1
    else:   #planteamos la secuencia recursiva
        return n*factorial(n-1) 
    
#probamos la funcion 
numero=int(input("Introduce un numero: "))
print(f"el factorial de {numero} es de: {factorial(numero)}")