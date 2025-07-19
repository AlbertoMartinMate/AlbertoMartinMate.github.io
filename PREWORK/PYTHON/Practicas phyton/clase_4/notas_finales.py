""" Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un curso. 
Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una participación en clase. 
Quieres calcular la nota final de cada estudiante, donde los exámenes valen un 30% cada uno, 
el trabajo final vale un 30% y la participación en clase vale un 10%. Para ello, puedes usar NumPy 
para crear un array de 4 columnas y n filas, donde n es el número de estudiantes. Cada columna representa 
una de las calificaciones y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy 
para calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola columna."""

import numpy as np

calificaciones=[]   #inicializamos las listas a utilizar. por un lado las notas
nombres_estudiantes=[]   #y por otro lado los nombre

num_estudiantes=int(input("Introduce el numero de alumnos de la clase: "))  #pedimos el num de estudiantes para trabajar los bucles y para saber longitudes del array


for i in range(num_estudiantes):   #hacemos un bucle para ir guardando los nombres en una lista y en otra las calificaciones

  nombre=input(f"Introduce el nombre del estudiante {i+1}: ")
  nombres_estudiantes.append(nombre)

  calificacion1=float(input(f"Introduce la nota del primer examen de {nombre}: "))
  calificaciones.append(calificacion1)


  calificacion2=float(input(f"Introduce la nota del segundo examen de {nombre}: "))
  calificaciones.append(calificacion2)


  calificacion3=float(input(f"Introduce la nota del trabajo final de {nombre}: "))
  calificaciones.append(calificacion3)


  calificacion4=float(input(f"Introduce la nota de la participacion en clase de {nombre}: "))
  calificaciones.append(calificacion4)

  i+=1  #sumamos para pasar al siguiente estudiante y notas

  print("")

calificaciones_array=np.array(calificaciones)  #lo pasamos a un array
listado_notas= calificaciones_array.reshape((num_estudiantes,4))  #le damos forma al array para que cada fila corresponda a un estudiante

nota_media=(listado_notas.sum(axis=1))/4  #sumamos cada fila y lo dividimos por el numero de notas de cada 
                                           #alumno (no lo pide, pero lo hacemos)

print(listado_notas)

for j in range(num_estudiantes): #hacemos un bucle para imprimir los valores y calculamos la nota final. 
                                  #ya que estan ordenadas por el mismo indice alumno y nota media/final
  nota_final= ((listado_notas[j][0]+listado_notas[j][1]+listado_notas[j][2]) * 0.3) + (
    listado_notas[j][3]*0.1)   
  print(f"La nota media del estudiante {nombres_estudiantes[j]} es de {nota_media[j]} y la nota final de {nota_final:.2f}")