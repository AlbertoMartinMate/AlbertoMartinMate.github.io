
"""
GESTIÓN DE VENTAS
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
 (La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…]
"""

def info_ventas():
  #funcion para confirmar venta y si es asi, agregar ventas
  datos_ventas=[]
  venta="si"
  while venta =="si":
   venta=input("¿Has realizado una venta? si o no ")
   if venta=="si":
     producto=input("Introduce el producto vendido: ")
     precio=input("Introduce su precio: ")
     datos={"Producto": producto, "Precio": precio}
     datos_ventas.append(datos)

   else:
    print("De acuerdo, cuando realices una venta, reinicia el programa")

  return datos_ventas

venta=info_ventas()
print("Los productos vendidos son: ", venta)