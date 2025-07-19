# pedir nombre de usuario

nombre = input("¿Cual es tu nombre?")  # es de tipo string

# reformatear nombre
nombre = nombre.replace(".", "")  # quitamos los puntos escritos por error

# escribimos mensaje en una variable
lenguaje = "python"
mensaje = "Hola " + nombre.title() + ". Estas usando " + lenguaje.title() + "!"

# mostramos el mensaje
print(mensaje)
