"""STRING A LISTA:
Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.
Supón ahora que tu input es un string como este:
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string."""

#primero lo vamos a hacer con un alumno
base_datos=[]

#añadimos la inf como string todo junto
alumno1="David Fernandez 12311267A 43527 2 9.1 7.6 2.4"
alumno2="Maria Garcia 12316487A 43527 2 7.1 8.6 5.4"
alumno3="Juan Perez 647829236A 43527 2 8.1 8.5 8.4"

#vamos separando cada dato x cada alumno y lo guardamos en otra variable y luego lo añadimos a la bbdd
datos_alumnos = alumno1.split() 
base_datos.append(datos_alumnos)
datos_alumnos2= alumno2.split()
base_datos.append(datos_alumnos2)
datos_alumnos3= alumno3.split()
base_datos.append(datos_alumnos3)

#2.-separamos cada lista
for alumno in base_datos:
    dni=alumno[2] #el dni esta n la pos.2
    suma_notas=0
    n_notas=0
    nota_media=0

    #analizamos cada lista desde 5 hasta el final (las notas)
    for dato in range(5,len(alumno)):
        suma_notas= suma_notas + float(alumno[dato]) #las vamos sumando
        n_notas=n_notas +1 #cade vez va sumando una nota mas, para luego hacer la media
    nota_media=suma_notas/n_notas

    print(f"{dni}, nota media {nota_media:.2f}" )

    """
Supón ahora que tu input es un string como este: 
"David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n 
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n "



# base de datos (lista de listas con los datos de los alumnos)
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# nos dan de input esta cadena con informacion de los alumnos
cadena_alumnos = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n \
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n \
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n"

# --- formatear datos de entrada

# convertir la cadena en una serie del listas diferentes para cada alumno
alumnos = cadena_alumnos.split('\n') # creamos una lista de tres strings, uno para cad alumno, separado x \n
for alumno in alumnos:  # recorremos todos los strings de la lista
    alumno = alumno.strip() # quitamos espacios en el string que sobren al comienzo y al final
    datos_alumno = alumno.split() # split separara la cadena en una lista de valores individuales

    if datos_alumno: # comprobamos que la lista tiene contenido 
                     # para librarnos de cualquier error de formato
        # añadimos las listas a la base de datos
        base_datos.append(datos_alumno)

Y DESPUES PASAMOS AL PUNTO 2 """
