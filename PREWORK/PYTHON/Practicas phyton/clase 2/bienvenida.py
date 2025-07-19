"""Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada.
Crea el script de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?
¿Y si lo introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?
¿Y si se le cuela una almohadilla (p.e se#rgio)?"""

# pedimos el nombre de usuario

usuario = input("Introduce tu nombre de usuario: ")

# intentamos corregir el nombre ante los posibles errores de escritura (.,#)
usuario = usuario.replace(".", "")
usuario = usuario.replace("#", "")
usuario = usuario.replace(" ", "")
usuario = usuario.replace(",", "")

# convertimos el nombre a minusculas
usuario = usuario.lower()

# comprobamos si el nombre es uno de los tres usuarios
if usuario == "alejandro":
    print("Bienvenido Alejandro")

elif usuario == "naomi":
    print("Bienvenida Naomi")
elif usuario == "sergio":
    print("Bienvenido Sergio")
else:
    print("Bienvenido")
