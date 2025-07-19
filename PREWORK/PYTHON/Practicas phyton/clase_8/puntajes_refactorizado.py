"""REGISTRO DE PUNTAJES:
Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores."""

def agregar_puntaje(registros, nombre, puntaje):
    """Agrega o actualiza el puntaje de un jugador en el diccionario."""
    registros[nombre] = puntaje

def obtener_mas_alto(registros):
    """Devuelve una tupla (nombre, puntaje) del jugador con puntaje más alto."""
    if not registros:
        return None, None
    jugador = max(registros, key=registros.get)
    return jugador, registros[jugador]

def calcular_promedio(registros):
    """Calcula y devuelve el promedio de los puntajes."""
    if not registros:
        return 0
    return sum(registros.values()) / len(registros)

def imprimir_estadisticas(registros):
    """Imprime el puntaje más alto, promedio y cantidad de jugadores."""
    jugador, puntaje = obtener_mas_alto(registros)
    if jugador:
        print(f"Puntaje más alto: {jugador} → {puntaje}")
    else:
        print("No hay registros aún.")
    promedio = calcular_promedio(registros)
    print(f"Promedio de puntajes: {promedio:.2f}")
    print(f"Cantidad de jugadores: {len(registros)}\n")

def main():
    registros = {}
    while True:
        nombre = input("Ingrese nombre del jugador (o 'salir' para terminar): ").strip()
        if nombre.lower() == 'salir':
            break

        try:
            puntaje = int(input("Ingrese el puntaje del jugador: ").strip())
        except ValueError:
            print("Puntaje inválido. Debe ser un número entero.\n")
            continue

        agregar_puntaje(registros, nombre, puntaje)
        imprimir_estadisticas(registros)

if __name__ == "__main__":
    main()

    """Qué hace cada parte: by chatgpt

-Funciones de lógica

agregar_puntaje centraliza la actualización del diccionario.

obtener_mas_alto y calcular_promedio devuelven datos concretos sin imprimirlos.

-Función de presentación

imprimir_estadisticas usa las dos anteriores para mostrar los resultados.

-Bucle principal (main)

Gestiona la entrada del usuario, validación básica y controla el flujo de “salir”.

Tras cada inserción imprime las estadísticas actualizadas.

Así queda el código más modular, fácil de probar y de extender si quieres, por ejemplo, guardar registros en un archivo o añadir más métricas."""