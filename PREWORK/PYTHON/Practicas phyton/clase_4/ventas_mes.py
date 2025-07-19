"""Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año.
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la
venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos,
etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
(Pista 1) Tu array de entrada puede tener un a forma de este tipo: 
(Pista 2: puedes cambiar el tipo de dato del array de string a entero usando
array[:,i].astype(int) )"""

import numpy as np

ventas= np.array([
    ["2025-01-01", 100, "ropa"],
    ["2025-01-02", 200, "alimentos"],
    ["2025-01-03", 150, "ropa"],
    ["2025-02-04", 120, "alimentos"],
    ["2025-02-05", 180, "electronicos"],
    ["2025-02-06", 200, "alimentos"],
    ["2025-03-07", 90, "ropa"],
    ["2025-03-08", 110, "electronicos"],
    ["2025-03-09", 100, "alimentos"]
    ])


ingresos=ventas[:,1].astype(int) #añado a ingresos la columna 1, cambiandolo a tipo int
fechas=np.array(ventas[:,0], dtype="datetime64[D]") #convertir la fechas en formato datetime
meses=fechas.astype("datetime64[M]")#obtenemos los meses de las fechas (como datetime64[M])
meses_unicos=np.unique(meses) #obtenemos los meses unicos


for mes in meses_unicos:   #sumamos las ventas por mes
    ventas_mes=ingresos[meses==mes] #filtramos los ingresos correspondientes a ese mes
    suma_mes=np.sum(ventas_mes)
    print(f"Mes: {mes}, Ventas totales: {suma_mes}")



         