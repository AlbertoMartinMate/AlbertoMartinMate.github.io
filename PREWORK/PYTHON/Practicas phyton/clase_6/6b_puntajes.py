"""REGISTRO DE PUNTAJES:
Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores."""

#creamos un diccionario vaciO
puntajes={}

#ingresar nombres y puntajes de jugadores y almacenarlos

puntajes["jugador1"]= {"nombre": "LeBron", "puntos": [24]}
puntajes["jugador2"]= {"nombre": "Magic", "puntos": [12]}
puntajes["jugador3"]= {"nombre": "Doncic", "puntos": [10]}
puntajes["jugador4"]= {"nombre": "Michael", "puntos": [18]}



#proporcionar funcionalidad para mostrar puntajes. puntaje mas alto, promedio puntajes, cantidad total de jugadores

puntajes["jugador1"]["puntos"].append(17)
puntajes["jugador2"]["puntos"].append(21)
puntajes["jugador3"]["puntos"].append(24)
puntajes["jugador4"]["puntos"].append(27)

todos_puntajes=[]
listado_puntos=[]

for clave, valor in puntajes.items():
  nombre=valor["nombre"]
  puntos=valor["puntos"]
  todos_puntajes.append(puntos)
  puntos_jugador=sum(puntos)

  print(nombre, "ha hecho los siguientes puntos", puntos, "Total: ", puntos_jugador)

for punto in todos_puntajes:
  for num in punto:
    listado_puntos.append(num)
print("La puntuacion mas alta en un partido, fue de:", max(listado_puntos))

media_puntos=sum(listado_puntos)/len(listado_puntos)
print("La media de puntos por partidos de estos jugadores, fue de:", media_puntos)
print("En esta competicion individual de jugadores participaron:", len(todos_puntajes), "jugadores") #porque eran 4 listados de puntos