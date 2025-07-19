"""Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.
(Pista 1: Tu array de entrada puede tener la forma…)
(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero)"""

import numpy as np

peliculas= np.array([
    ["Peli 1", "Comedia", 120, 1990, 8.5],
    ["Peli 2", "Accion", 110, 2005, 7.8],
    ["Peli 3", "Drama", 95, 2010, 6.9],
    ["Peli 4", "Comedia", 100, 1985, 7.5],
    ["Peli 5", "Accion", 130, 2015, 8.1],
    ["Peli 6", "Drama", 115, 2000, 6.7],
    ["Peli 7", "Comedia", 90, 1995, 8.2],
    ["Peli 8", "Accion", 105, 2010, 7.4],
    ["Peli 9", "Drama", 125, 1980, 6.8],
    ["Peli 10", "Comedia", 95, 2000, 8.0]
])

#guardamos los datos de manera independiente

nombre= peliculas[:,0]
genero= peliculas[:,1]
duracion=np.array(peliculas[:,2], dtype=float)
año=np.array(peliculas[:,3], dtype=float)
valoracion=np.array(peliculas[:,4], dtype=float)
conjunto_valoracion=[] #hacemos una lista con las medias
duracion_genero=[]

#genero de pelicula mas popular (en ejercicio corregido, se refiere a la q mas apariciones tiene)
comedia=[valoracion[i] for i in range(10) if genero[i]=="Comedia"] #hacemos media de valoracion segun genero
valoracion_comedia=np.mean(comedia)
conjunto_valoracion.append(valoracion_comedia)

accion=[valoracion[i] for i in range(10) if genero[i]=="Accion"]
valoracion_accion=np.mean(accion)
conjunto_valoracion.append(valoracion_accion)

drama=[valoracion[i] for i in range(10) if genero[i]=="Drama"]
valoracion_drama=np.mean(drama)
conjunto_valoracion.append(valoracion_drama)

valoracion_alta=conjunto_valoracion.index(max(conjunto_valoracion)) #averiguamos el indice de la valoracion mas alta
popular=genero[valoracion_alta] #en funcion del indice, imprimimos genero
print("El genero mejor valorado es el : ", popular)

#cuantas peliculas se lanzaron en cada decada
ochenta=0
noventa=0
dos_mil=0
dos_mil_diez=0

for valor in año:
    if valor>=1980 and valor<1990:
        ochenta+=1
    elif valor>=1990 and valor<2000:
        noventa+=1
    elif valor>=2000 and valor<2010:
        dos_mil+=1
    else:
        dos_mil_diez+=1
print(f"En los ochenta: {ochenta} peliculas")
print(f"En los noventa: {noventa} peliculas")
print(f"En los dos mil: {dos_mil} peliculas")
print(f"En los dos mil diez: {dos_mil_diez} peliculas")


#duracion promedio de cada genero
tiempos_comedia=[duracion[i] for i in range(10) if genero[i]=="Comedia"] #hacemos media de tiempo segun genero
duracion_comedia=np.mean(tiempos_comedia)
duracion_genero.append(duracion_comedia)

tiempos_accion=[duracion[i] for i in range(10) if genero[i]=="Accion"] #hacemos media de tiempo segun genero
duracion_accion=np.mean(tiempos_accion)
duracion_genero.append(duracion_accion)

tiempos_drama=[duracion[i] for i in range(10) if genero[i]=="Drama"] #hacemos media de tiempo segun genero
duracion_drama=np.mean(tiempos_drama)
duracion_genero.append(duracion_drama)
print(f"La duracion promedio de las peliculas son:")
print(f"Comedia : {duracion_genero[0]:.2f}")
print(f"Accion : {duracion_genero[1]:.2f}")
print(f"Drama : {duracion_genero[2]:.2f}")

