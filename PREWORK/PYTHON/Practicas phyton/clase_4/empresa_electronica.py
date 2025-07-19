"""Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres
analizar los datos de calidad de los componentes utilizados en la producción de dichos
dispositivos. Tienes un conjunto de datos que contiene información sobre la fecha de
producción, el tipo de componente, el lote al que pertenece el componente y la
puntuación de calidad del componente (un número entre 0 y 100). Quieres analizar estos
datos para determinar cuál es el tipo de componente con la puntuación de calidad más
alta, cuántos componentes se produjeron en cada mes y cuál es la puntuación de calidad
promedio de cada tipo de componente.
(Pista 1: Tu array de entrada puede tener la forma…)
(Pista 2: puede ser util investigar np.unique y np.argmax)"""

import numpy as np

datos= np.array([
    ["2022-01-01", "Componente 1", "Lote A", 80],
    ["2022-01-15", "Componente 1", "Lote B", 90],
    ["2022-02-01", "Componente 2", "Lote C", 85],
    ["2022-02-15", "Componente 2", "Lote D", 95],
    ["2022-03-01", "Componente 1", "Lote E", 75],
    ["2022-03-15", "Componente 2", "Lote F", 90],
])

#tipo de componente con la puntuación de calidad más alta

componentes=np.array(datos[:,1])
puntuaciones=np.array(datos[:,3], dtype=float)
componente_mas_alto=np.argmax(puntuaciones)

print(f"El tipo de componente con la puntuacion mas alta es: {componentes[componente_mas_alto]}")


#cuántos componentes se produjeron en cada mes

fechas=np.array(datos[:,0])


meses=[fecha[5:7] for fecha in fechas]

valores_unicos, conteos= np.unique(meses, return_counts=True)

for valor in range(len(valores_unicos)):
  
  print(f"En el mes {valores_unicos[valor]}, se realizaron {conteos[valor]} componentes")

#puntuación de calidad promedio de cada tipo de componente.

componentes_unicos=np.unique(componentes)
calidad_media=np.zeros(len(componentes_unicos))

for i in range(len(componentes_unicos)):
  calidad_media[i]=np.mean(puntuaciones[componentes==componentes_unicos[i]])
  print(f"La puntuacion media de cada componenete es:  {componentes_unicos[i]}\
  es de {calidad_media[i]:.2f}")

