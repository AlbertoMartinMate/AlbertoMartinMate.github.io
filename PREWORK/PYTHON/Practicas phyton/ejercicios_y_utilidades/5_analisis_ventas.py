"""Problema de Análisis de Datos de Ventas:
Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el
monto de la venta y la ubicación del comprador. Realiza un análisis avanzado
de estas ventas.

1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500 (100).
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada 
- Registro de ventas (json,dic,etc)
Salida
Ubicaciones por promedio, ej. : [Chile,
Ecuador]"""

from itertools import groupby  
from collections import OrderedDict
#1
def ventas_ultimo_trimestre(mis_ventas):
    """Filtra las ventas realizadas en el último trimestre del año."""
    return list(filter(lambda venta: int(venta["fecha_venta"].split("-")[1]) in [10, 11, 12],
        mis_ventas
    ))
#2
def ventas_mayores(mis_ventas):
    """Selecciona solo las ventas de productos con un monto superior a 100"""
    return list(filter(lambda venta: venta["monto"] >100, mis_ventas))
#3
def ubicacion_ventas(mis_ventas):
    """Agrupa las ventas por ubicación del comprador"""
    # ordenar primero por la clave
    ordenadas = sorted(mis_ventas, key=lambda e: e["ubicacion"])
    # agrupar
    productos_ordenados_ubicacion = OrderedDict({ubicacion: list(grupo)
        for ubicacion, grupo in groupby(ordenadas, key=lambda e: e["ubicacion"])})
    return productos_ordenados_ubicacion
#4
def promedio_monto_ubicacion(productos_ordenados_ubicacion):
    """Calcula el promedio del monto de venta para cada ubicación."""
    promedios = {}
    for ciudad, ventas in productos_ordenados_ubicacion.items():
        montos = [venta["monto"] for venta in ventas]
        if montos:
            promedio = sum(montos) / len(montos)
        else:
            promedio = 0
        promedios[ciudad] = promedio
    return promedios

#5
def orden_ciudad_promedio(promedios):
    """
    Ordena las ubicaciones por el promedio del monto de venta de forma descendente.
    """
    # Creamos una lista de tuplas (ciudad, promedio) ordenada de mayor a menor
    listado_ordenado = sorted(
        promedios.items(),                  # [('Madrid', 120.47), ('Barcelona', 127.85), ...]
        key=lambda item: item[1],           # Ordenamos por el promedio (que es el valor, item[1])
        reverse=True                        # De mayor a menor
    )
    return listado_ordenado


if __name__ == "__main__":

    ventas = [
    {
        "producto": "Auriculares Bluetooth X200",
        "fecha_venta": "2024-01-18",
        "monto": 379.99,
        "ubicacion": "Madrid"
    },
    {
        "producto": "Teclado Mecánico Pro",
        "fecha_venta": "2024-02-05",
        "monto": 129.50,
        "ubicacion": "Barcelona"
    },
    {
        "producto": "Ratón Inalámbrico Silent",
        "fecha_venta": "2024-03-22",
        "monto": 39.90,
        "ubicacion": "Valencia"
    },
    {
        "producto": "Monitor 27'' Ultra HD",
        "fecha_venta": "2024-04-14",
        "monto": 299.99,
        "ubicacion": "Madrid"
    },
    {
        "producto": "Altavoz Inteligente Mini",
        "fecha_venta": "2024-05-09",
        "monto": 59.95,
        "ubicacion": "Barcelona"
    },
    {
        "producto": "Smartwatch Fit 2",
        "fecha_venta": "2024-06-27",
        "monto": 159.00,
        "ubicacion": "Valencia"
    },
    {
        "producto": "Disco Duro Externo 1TB",
        "fecha_venta": "2024-07-15",
        "monto": 79.00,
        "ubicacion": "Madrid"
    },
    {
        "producto": "Tablet 10'' Pro",
        "fecha_venta": "2024-08-03",
        "monto": 249.99,
        "ubicacion": "Barcelona"
    },
    {
        "producto": "Cámara Web HD",
        "fecha_venta": "2024-09-21",
        "monto": 49.95,
        "ubicacion": "Valencia"
    },
    {
        "producto": "Cargador Rápido USB-C",
        "fecha_venta": "2024-10-12",
        "monto": 24.90,
        "ubicacion": "Madrid"
    },
    {
        "producto": "Auriculares Deportivos Pro",
        "fecha_venta": "2024-11-06",
        "monto": 69.99,
        "ubicacion": "Barcelona"
    },
    {
        "producto": "Ebook Reader Light",
        "fecha_venta": "2024-12-19",
        "monto": 119.95,
        "ubicacion": "Valencia"
    }
]

productos_ciudad= ubicacion_ventas(ventas) #3 lo saco fuera para que no tenga q calcular, ya q es una funcion q no cambia
media_monto_ubicacion= promedio_monto_ubicacion(productos_ciudad) #4
ciudades_ordenadas= orden_ciudad_promedio(media_monto_ubicacion) #5
continuar = True

while continuar:
    opcion = input("\n1. Mostrar ventas del ultimo trimestre\n2. Mostrar ventas superiores a 100 euros" \
    "\n3. Mostrar las ventas por ciudad\n4. Calcular la media por ciudad\n5. Ordenar las ciudades segun promedio de venta" \
    "\n6 Salir\nElige una opción: ")

    
    if opcion == "1": #Mostrar ventas del ultimo trimestre
        ultimo_trimestre=ventas_ultimo_trimestre(ventas)
        for venta in ultimo_trimestre:
                print(f"\n📍 {venta['producto']}:")
                print(f"  - {venta['ubicacion']} | Fecha: {venta['fecha_venta']} | Monto: €{venta['monto']:.2f}")
    
    elif opcion=="2": #Mostrar ventas superiores a 100 euros
        producto_mas_100= ventas_mayores(ventas)  
        for venta in producto_mas_100:
                print(f"\n📍 {venta['producto']}:")
                print(f"  - {venta['ubicacion']} | Fecha: {venta['fecha_venta']} | Monto: €{venta['monto']:.2f}")

    elif opcion=="3": #Mostrar las ventas por ciudad

        for ciudad, lista_ventas in productos_ciudad.items():
            print(f"\n📍 {ciudad}:")
            for venta in lista_ventas:
                print(f"  - {venta['producto']} | Fecha: {venta['fecha_venta']} | Monto: €{venta['monto']:.2f}")

    elif opcion=="4": #Calcular la media por ciudad
        for ciudad in media_monto_ubicacion:
            print(f"\n📍 {ciudad} {media_monto_ubicacion[ciudad]:.2f} €")
    
    elif opcion=="5": #Ordenar las ciudades segun promedio
        for ciudad, promedio in ciudades_ordenadas: #desempaqueta cada tupla
            print(f"\n📍 {ciudad}: {promedio:.2f} €")

        # Salir del programa
    elif opcion == "6":
        print("Saliendo del programa...")
        continuar = False

    # Si el numero introducido no es 1,2,3,4,5,6 pedimos que se elija
    # una opcion valida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
