"""1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
centro de la estructura.
*
**
***
****
*****
****
***
**
*
"""

# pedimos por pantalla un numero entero al usuario

num = int(input("Introduce un número entero: "))
i = 0

while ( i <= num):  # mayor o igual para q imprima hasta el num, sino haria hasta uno menos... a noser que pusieramos num+1
    print("*" * i)
    i = i + 1


while (i > 0):  # aqui i empieza con el valor de num...x ello tenemos q ir reduciendolo, ponemos la condicion antes del print, para que imprima una menos..ya q solo queremos una fila de * = q num
    i = i - 1
    print("*" * (i - 1))
