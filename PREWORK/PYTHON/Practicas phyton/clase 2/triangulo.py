"""En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir este
 estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo con
 esas piezas.
 (Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así
 para todas las posibles combinaciones)"""

# pedimos el tamaño de todas las piezas
pieza1 = int((input)("Introduce el tamaño de la primera pieza "))
pieza2 = int((input)("Introduce el tamaño de la segunda pieza "))
pieza3 = int((input)("Introduce el tamaño de la tercera pieza "))

if (
    (pieza1 + pieza2 > pieza3)
    and (pieza1 + pieza3 > pieza2)
    and (pieza2 + pieza3 > pieza1)
):
    print("Puede contruirse el tejado con esta pieza")

else:
    print("La estructura no es válida")
