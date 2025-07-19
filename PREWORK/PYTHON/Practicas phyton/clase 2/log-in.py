"""Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la contraseña.
  Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse. Cambia el script para
    que no distinga entre mayúsculas y minúsculas. (Pista: Necesitarás in If Statement anidado)
"""

# definimos la contraseña correcta
contraseña_correcta = "alberto"

# pedimos una contraseña al usuario

contraseña = input("Introduce la cotraseña: ")

# convertimos la contraseña a minusculas para no distinguir entre mayusculas y minusculas
contraseña = contraseña.lower()

# comprobamos si la contraseña es correcta, si no es asi, le damos una segunda oportunidad

if contraseña_correcta == contraseña:

    print("La contraseña es correcta")

else:
    contraseña = input("No es correcta, tienes una segunda y última oportunidad: ")
    contraseña = contraseña.lower()

    # comprobamos de nuevo. si la acierta correcta y sino mensaje de error.

    if contraseña_correcta == contraseña:
        print("Ahora si, la contraseña es correcta")

    else:
        print("Lo siento, la contraseña no es correcta")
