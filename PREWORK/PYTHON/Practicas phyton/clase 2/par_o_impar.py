"""Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
"""

# pedimos al usuario que ingrese un numero y una potencia
numero = float(input("Ingresa un número: "))
potencia = float(
    input("Ingresa otro número, al cual, le vamos a dar valor de potencia: ")
)

# calculamos el resultado de elevar el numero a la potencia
resultado = numero**potencia


# calculamos el resultado de la division entre 2 para saber si el resto es 0

resultado_final = resultado % 2

# comprobamos si el resultado es par o impar con un condicional

if resultado_final == 0:
    print(
        "El resultado es par, ya que ",
        resultado,
        "al dividirlo entre 2, su resto es de",
        resultado_final,
    )
else:
    print(
        "El resultado es impar ya que ",
        resultado,
        "al dividirlo entre 2, su resto es de",
        resultado_final,
    )
