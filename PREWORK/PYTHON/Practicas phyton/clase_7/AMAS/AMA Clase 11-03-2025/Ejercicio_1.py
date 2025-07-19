# Enunciado:
# Desarrollar un programa en Python que permita gestionar las notas de estudiantes.
# El programa debe permitir al usuario:
# 1. Agregar estudiantes con sus respectivas notas (solo valores entre 0 y 10).
# 2. Ver la lista de estudiantes ingresados, mostrando su estado (Aprobado o Reprobado).
# 3. Calcular y mostrar el promedio de notas de los estudiantes registrados.
# 4. Salir del programa.

# Lista para almacenar los estudiantes
estudiantes = []

# Funcion sin parametros de entrada ni salida, solo muestra un mensaje de bienvenida
def mostrar_bienvenida():
    print("Bienvenido al sistema de gestion de notas")
    print("Podras ingresar las notas de varios estudiantes y calcular el promedio")

# Funcion con parametros de entrada pero sin salida
# Agrega un estudiante con su nombre y nota si la nota esta en el rango permitido
def agregar_estudiante(nombre, nota):
    if 0 <= nota <= 10:  # Verifica si la nota está entre 0 y 10
        estudiantes.append({"nombre": nombre, "nota": nota})
        print(f"Estudiante {nombre} agregado con nota {nota}")
    else:
        print("Error! La nota debe estar entre 0 y 10")

# Funcion con salida pero sin entrada
# Devuelve la lista de estudiantes registrados
def obtener_estudiantes():
    return estudiantes

# Funcion con entrada y salida
# Calcula el promedio de notas de los estudiantes registrados
def calcular_promedio(lista_estudiantes):
    if not lista_estudiantes:  # Verifica si la lista está vacía
        return 0
    
    suma_notas = sum(estudiante["nota"] for estudiante in lista_estudiantes)  # Suma las notas
    promedio = suma_notas / len(lista_estudiantes)  # Calcula el promedio
    return promedio

# Funcion principal del programa
mostrar_bienvenida()

while True:
    # Menu de opciones
    print("\nMenu de Opciones")
    print("1. Agregar estudiante")
    print("2. Ver la lista de estudiantes")
    print("3. Calcular el promedio de notas")
    print("4. Salir")
    
    opcion = input("Selecciona una opcion (1-4): ")
    
    if opcion == "1":
        nombre = input("Introduce el nombre del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante (0-10): "))
        agregar_estudiante(nombre, nota)
    
    elif opcion == "2":
        lista = obtener_estudiantes()
        if lista:
            print("\nLista de estudiantes:")
            for estudiante in lista:
                estado = "Aprobado" if estudiante["nota"] >= 6 else "Reprobado"  # Determina si aprobó o reprobó
                print(f"{estudiante['nombre']} - Nota: {estudiante['nota']} ({estado})")
        else:
            print("No hay estudiantes registrados")
    
    elif opcion == "3":
        resultado = calcular_promedio(obtener_estudiantes())
        print("El promedio de notas es:", resultado)
    
    elif opcion == "4":
        print("Gracias por usar el sistema")
        break  # Termina el bucle y sale del programa
    
    else:
        print("Opcion Invalida. Intente de nuevo.")