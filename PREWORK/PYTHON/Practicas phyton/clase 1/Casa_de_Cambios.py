# 1.-  # pedir al usuario que ingrese el dinero

euros = input("Ingresa la cantidad de euros que deseas comvertir: ")  # tipo string

# convertimos la cantidad ingresada a float

euros = float(euros)
# se podria hacer en una paso poniendo float justo delante de input con parentesis

# convertir la cantidad de euros a dolares

dolares = euros * 1.2

# imprimir el resultado de la conversión

print(euros, "euros son", dolares, "dolares")

# 2.-# hacemos el calculo de lo que se queda la casa de cambio y lo que le queda al usuario

intereses = dolares * 0.1
usuario = dolares - intereses

# imprimimos el resultado
print("Cantidad en euros:", euros, "euros")
print("Cantidad en dolares:", dolares, "dolares")
print("Intereses de la casa de cambio:", intereses, "dolares")
print("Cantidad que le queda al usuario:", usuario, "dolares")
