# 1.- Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
# imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
# es el 4532 por pantalla deberá imprimirse:
# 4
# 5
# 3
# 2

# pedimos numero
num = (input)("Introduce un número de mas de una cifra ")

# hacemos condicional para asegurarnos de que el numero es de mas de 1 digito

if len(num) > 1:

    for digito in num:
        print(digito)  # imprimir cada digito en una linea (xq num es un string)

else:
    print("Por favor, introduce un número de mas de una cifra.")

    # . 2.- dar la vuelta al número. Por ejemplo si el número introducido  es 4532, el output deberá ser 2354


num_reves = num[::-1]
print(" ")
print("El número escrito al reves es ", (num_reves))
