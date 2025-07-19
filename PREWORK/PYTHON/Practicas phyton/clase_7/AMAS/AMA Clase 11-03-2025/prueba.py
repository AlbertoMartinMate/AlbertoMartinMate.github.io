# REGISTRO DE VENTAS: 
# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias 
# de tus productos. Cada producto tiene un nombre y una cantidad 
# vendida. Implementa un programa en Python que utilice un diccionario 
# para almacenar la informaciÃ³n de las ventas. El programa debe permitir 
# registrar las ventas de productos, actualizar la cantidad vendida de un 
# producto existente y calcular el total de ventas diarias
ventas ={}
#producto, cantidad vendida
ventas["Producto1"] = 7
ventas["Producto2"] = 10
ventas["Producto3"] = 15
## print(ventas)
#Actualizar cantidad vendida de un producto
ventas["Producto2"] = ventas["Producto2"]+2
print(ventas)

# Calcular total de ventas diarias
total_ventas_1 = 0
total_ventas_2 = 0
for producto, venta in ventas.items():
    total_ventas_1 = total_ventas_1 + venta
    total_ventas_2 = sum(ventas.values())

print("Total ventas sin sum: ",total_ventas_1)
print("Total ventas con sum: ",total_ventas_2)