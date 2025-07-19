"""Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.
(Pista 1) Tu array de entrada podría ser algo como esto, con daros de temperatura,
humedad, presión y mes del año:"""

import numpy as np

clima=np.array([
    [20, 70, 1009, 1],
    [21, 60, 1011, 1],
    [22, 40, 1010, 1],
    [18, 75, 1012, 2],
    [21, 60, 1008, 3],
    [22, 65, 2008, 3],
    [25, 60, 1010, 4],
    [27, 49, 1007, 5],
    [29, 50, 1007, 5],
    [28, 51, 1007, 5],
    [30, 45, 1005, 6],
    [10, 30, 1005, 6],
    [32, 40, 1002, 7],
    [33, 35, 1001, 8],
    [31, 45, 1003, 9],
    [30, 42, 1001, 9],
    [29, 42, 1002, 9],
    [35, 43, 1001, 9],
    [28, 50, 1006, 10],
    [25, 60, 1010, 10],
    [27, 59, 1012, 11],
    [24, 58, 1011, 11],
    [22, 70, 1011, 12]
])

suma_temperaturas=0
media_temperaturas=0
media_enero=0
suma_humedad=0
media_humedad=0
suma_presion=0
media_presion=0

temperaturas_enero=[]

for i in range(len(clima)):
 suma_temperaturas+=clima[i][0]
 suma_humedad+=clima[i][1]
 suma_presion+=clima[i][2]

 if clima[i][3]==1:  #xa calcular la media de las temperaturas de enero...todos los meses??
  temperaturas_enero.append(clima[i][0])

media_enero=np.mean(temperaturas_enero)
media_temperaturas= suma_temperaturas/(len(clima)) #calculamos la media temperatura anual
media_humedad= suma_humedad/(len(clima))
media_presion= suma_presion/(len(clima))

print(f"La media de la temperatura anual es de: {media_temperaturas:.2f}, y la media de la temperatura en enero es de: {media_enero}")

print(f"La media de la humedad al año es: {media_humedad:.2f}")

print(f"La media de la presion atmosferica al año es: {media_presion:.2f}")