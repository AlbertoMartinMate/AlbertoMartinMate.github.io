"""REGISTRO DE ASISTENCIAS:
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas) """

#creamos un diccionario vacio

asistencia={}

#rellenamos el diccionario con algunos registros

asistencia["Alumno1"]= ["06/01/2025", "07/01/2025"]
asistencia["Alumno2"]= ["06/01/2025", "08/01/2025"]
asistencia["Alumno3"]= ["07/01/2025", "09/01/2025"]



#añadimos fechas

asistencia["Alumno1"].append("17/02/2025")
asistencia["Alumno2"].append("07/02/2025")
asistencia["Alumno2"].append("27/02/2025")


#mostramos todos los datos ordenados por alumno

for dato,fecha in asistencia.items():
    print(dato, "asistio en las siguientes fechas:")
    print("Fechas:", "," .join(fecha)) #.join() nos lo convierte a string(quita corchetes), y nos lo separa por lo q le indiquemos antes