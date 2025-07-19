# 1.- tress finalistas. Creamos un script y pedimos los tiempos por pantalla de cada uno de los tres finalistas.

# pedimos el tiempo del primer finalista

print("¿Cual es el tiempo de Hannah? ")
minutos_hannah = float(input("minutos: "))
segundos_hannah = float(input("segundos: "))
centesimas_hannah = float(input("centésimas: "))
print("El tiempo de Hannah Neisen es: ")
print(minutos_hannah, "minutos ")
print(segundos_hannah, "segundos y")
print(centesimas_hannah, "centesimas")

# pedimos el tiempo del segundo finalista

print("¿Cual es el tiempo de Jackie? ")
minutos_jackie = float(input("minutos: "))
segundos_jackie = float(input("segundos: "))
centesimas_jackie = float(input("centésimas: "))
print("El tiempo de Jackie Narracott es: ")
print(minutos_jackie, "minutos ")
print(segundos_jackie, "segundos y")
print(centesimas_jackie, "centesimas")

# pedimos el tiempo del tercer finalista

print("¿Cual es el tiempo de Kimberley? ")
minutos_kimberley = float(input("minutos: "))
segundos_kimberley = float(input("segundos: "))
centesimas_kimberley = float(input("centésimas: "))
print("El tiempo de Kimberley Boss es: ")
print(minutos_kimberley, "minutos ")
print(segundos_kimberley, "segundos y")
print(centesimas_kimberley, "centesimas")

# 2.- Convertimos los tiempos a segundos. Para ello, multiplicamos los minutos por 60 y sumamos los segundos y las centésimas divididas entre 100.


tiempo_hannah = (minutos_hannah * 60) + (segundos_hannah) + (centesimas_hannah / 60)
# Redondeamos el tiempo a dos decimales
tiempo_hannah = round(tiempo_hannah, 2)
print("El tiempo de Hannah Neisen en segundos es: ", tiempo_hannah, "segundos")


tiempo_jackie = (minutos_jackie * 60) + (segundos_jackie) + (centesimas_jackie / 60)
tiempo_jackie = round(tiempo_jackie, 2)
print("El tiempo de Jackie Narracott en segundos es: ", tiempo_jackie, "segundos")

tiempo_kimberley = (
    (minutos_kimberley * 60) + (segundos_kimberley) + (centesimas_kimberley / 60)
)
tiempo_kimberley = round(tiempo_kimberley, 2)
print("El tiempo de Kimberley Boss en segundos es: ", tiempo_kimberley, "segundos")

# 3.- Sabiendo que la pista es de 100 metros, clacular la velocidad media de cada uno de los finalistas en metros por segundo. Para ello, dividimos la distancia entre el tiempo en segundos.

velocidad_hannah = 100 / tiempo_hannah

# Redondeamos a dos decimales
velocidad_hannah = round(velocidad_hannah, 2)
print("La velocidad media de Hannah Neisen es: ", velocidad_hannah, "m/s")

velocidad_jackie = 100 / tiempo_jackie
velocidad_jackie = round(velocidad_jackie, 2)
print("La velocidad media de Jackie Narracott es: ", velocidad_jackie, "m/s")

velocidad_kimberley = 100 / tiempo_kimberley
velocidad_kimberley = round(velocidad_kimberley, 2)
print("La velocidad media de Kimberley Boss es: ", velocidad_kimberley, "m/s")
