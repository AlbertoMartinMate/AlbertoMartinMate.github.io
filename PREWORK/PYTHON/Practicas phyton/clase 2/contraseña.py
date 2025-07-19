"""Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla."""

# pedimos una contraseña al usuario

contraseña = input(
    "Ingrese una contraseña que contenga al menos una vocal en minuscula,\
        y dos simbolos especiales (# o *): "
)

# creamos variable para definir lo q es vocales y simbolos raros
vocales = "aeiou"
simbolos = "#*"

# creamos variables para contar las vocales y los simbolos
contador_vocales = 0
contador_simbolos = 0

# creamos un condicional para ver si tenemos vocales y simbolos

for caracter in contraseña:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in simbolos:
        contador_simbolos += 1

# ahora tenemos que ver si la contraseña tiene al menos una vocal y dos simbolos difentes
if contador_vocales >= 1 and contador_simbolos >= 2:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")
