"""El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que pida
el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
"""

# pedimos al usuario que ingrese su nombre, edad y nota media

nombre = input("Introduce tu nombre ")
edad = float(input("Introduce tu edad "))
nota_media = float(input("Introduce tu nota media "))

# hacemos un condicional para saber si cumple con los requisitos

if (nota_media >= 8) and (edad >= 17) and (edad <= 21):

    print("Puedes optar a la beca", (nombre.title()))

else:

    print("Lo siento, "(nombre.title()), "no puedes optar a la beca")
