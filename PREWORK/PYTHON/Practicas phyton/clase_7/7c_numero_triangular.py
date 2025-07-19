"""NUMERO TRIANGULAR
Crea una función recursiva llamada numero_triangular que calcule el n-ésimo
número triangular. Un número triangular se obtiene al sumar todos los
números naturales desde 1 hasta n."""

def numero_triangular(n):
    """Calcular el valor del numero triangular n"""
    #es un num de la suma del triangulo de todos los puntos hasta n
    if n==1:
        return 1
    else: #recursividad
        return n + numero_triangular(n-1) #formula para obtener el num. triangular. 
    
num=int(input("Introduce un número para calcular el número triangular: "))

resultado=numero_triangular(num)
print(resultado)

"""ej con 5
5+numero_triangular(4)
5+4+numero_triangular(3)
5+4+3+numero_triangular(2)
5+4+3+2+numero_triangular(1) 
5+4+3+2+1 caso base
"""