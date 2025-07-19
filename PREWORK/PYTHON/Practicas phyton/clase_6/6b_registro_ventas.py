"""REGISTRO DE VENTAS: 
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias de tus productos. 
Cada producto tiene un nombre y una cantidad vendida. Implementa un programa en Python que utilice 
un diccionario para almacenar la información de las ventas. El programa debe permitir registrar las
 ventas de productos, actualizar la cantidad vendida de un producto existente y calcular el total 
 de ventas diarias. (Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada producto"""

#creamos un diccionario vacio
ventas_diarias={}

#añadimos productos. Su nombre y cantidad vendida
ventas_diarias["Balon"]= 5 
ventas_diarias["Pelotas"]= 7 
ventas_diarias["Deportivas"]= 3 
ventas_diarias["Camiseta"]= 10


#crear un programa para registrar ventas del producto, actualizar cantidades y calcular el total de
#ventas diarias

#analizo cantidades vendidas en total. tb se puede sum(ventas_diarias.values()) y nos quitamos for

cantidad_total=0

for clave, cantidad in ventas_diarias.items():
    
    cantidad_total+=cantidad

print("Se han vendido", cantidad_total, "productos")




#actulizo cantidades preguntando y calculando el total de ventas diarias

venta=True    #booleano para salir del bucle

while (venta==True):
    respuesta=input("Has realizado una venta? si o no: ")
    if respuesta=="si":
        producto_vendido=input("Que producto has vendido?: ")
        cantidades_vendidas=int(input("Cuantas unidades?: "))
        
        if producto_vendido in ventas_diarias:      #si el producto esta en ventas_diarias, la cantidad
         ventas_diarias[producto_vendido] += cantidades_vendidas  #la sumo
        else:
         ventas_diarias[producto_vendido] = cantidades_vendidas  #sino añado producto y cantidad
        
        print(ventas_diarias)   #imprimo todo actualizado
        cantidad_total+=cantidades_vendidas   #calculo el total actualizado
        print("Se han vendido", cantidad_total, "productos")
    
    else:
        print("De acuerdo, cuando realices una venta, reinicia el programa")  #si no hay venta salgo
        venta=False      #y se vuelve a inicializar todo al principio
