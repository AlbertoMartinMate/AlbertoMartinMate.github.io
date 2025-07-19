"""ANÁLISIS DE VOTACIONES: 
Supongamos que tienes los resultados de una elección con los nombres de los candidatos y la cantidad 
de votos obtenidos por cada uno. Implementa un programa en Python que permita registrar los votos, 
mostrar la lista completa de candidatos y sus votos, encontrar al candidato ganador (con más votos) y 
calcular el porcentaje de votos que obtuvo cada candidato."""

votaciones={}

continuar=True
votos=0

while continuar:
   opcion = input("Introduce la opcion que quieres realizar: \n 1. Añadir candidato y votos\n2. Añadir votos a candidato existente\n3.Mostrar lista completa de candidatos y votos\n4.Mostrar porcentajes de votos\n5.Salir y mostrar ganador\nOpcion: ")





   if opcion=="1":   #registrar votos/candidatos
    nombre=input("Introduce el nombre del candidato y los votos obtenidos ")

    if nombre not in votaciones:
       votos= int(input("Ingrese el numero de votos contados: "))
       votaciones[nombre]=votos
    else:
       print("Este candidato, ya esta registrado. Si quieres sumar votos, marque la opción 2")

   elif opcion=="2": #sumar votos
     nombre=input("Introduce el nombre del candidato al que añadir los votos ")

     if nombre in votaciones:
       votos= int(input("Ingrese el numero de votos que hay que añadir: "))
       votaciones[nombre]= votaciones[nombre] + votos

   elif opcion=="3": #mostrar lista de candidatos y votos
       for candidatos, datos in votaciones.items():
        print("El candidato:", candidatos, "tiene:", datos, "votos")

   elif opcion=="4":  #mostrar porcentaje de votos
     votos_totales=0   #corregido: votos_totales=sum(votaciones.values())
     porcentaje=0
     for candidatos, datos in votaciones.items():#con el corregido, nos evitariamos este for
      votos_totales+=datos
     for candidatos, datos in votaciones.items():
         porcentaje=(datos*100)/votos_totales
         print(f"El candidato: {candidatos}, ha obtenido un porcentaje de {porcentaje:.2f} votos")


   elif opcion=="5": #mostrar candidato ganador
                     #corregido:ganador=max(votaciones, key=votaciones.get)
    if len(votaciones) ==0:
     print("No hay candidatos registrados")
     continuar=False

   else:

    puntos=0
    candidato_ganador=""
    for candidatos, datos in votaciones.items():
        if datos > puntos:
         candidato_ganador = candidatos
    print("El candidato ganador es:", candidato_ganador)

    continuar=False

else:
  print("Opción invalida")