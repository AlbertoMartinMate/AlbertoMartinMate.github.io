"""En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la M en
el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y R hasta
la Z se les ha asignado al grupo A también, el resto están en el B. Crea un script que pregunte al
usuario si es chica o chico y el nombre. El script debe mostrar por pantalla el grupo que le
corresponde a ese alumno."""

# pedimos al usuario que introduzca su sexo y su nombre

genero = input("Introduce tu género, (femenino/masculino): ")
nombre = input("Introduce tu nombre: ")
nombre = nombre.lower()
letrasA_chicas = "efghijklm"
letrasA_chicos = "abcdefghrstuvwxyz"

primera_letra = nombre[0]


# hacemos la comprobación primero con las chicas.E - M grupo A. resto grupo b

if genero.lower() == "femenino":

    if primera_letra in letrasA_chicas:
        print("Tu grupo, es el grupo A")

    else:
        print("Tu grupo, es el grupo B")

        # vamos con los chicos.A - H y R - Z se les ha asignado al grupo A. resto b

elif genero.lower() == "masculino":

    if primera_letra in letrasA_chicos:
        print("Tu grupo, es el grupo A")

    else:
        print("Tu grupo, es el grupo B")

else:
    print("Introduce un género válido")
