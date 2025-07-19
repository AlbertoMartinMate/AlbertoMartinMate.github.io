"""Problema de Resolución de Laberinto:
Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). Tu tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.
Toma en cuenta los siguientes puntos:
1. La matriz representa el laberinto, donde los valores son:
-0 : Camino permitido.
-1 : Pared, no se puede atravesar.
-9 : Salida del laberinto.
2. Debes implementar la función resolver_laberinto que utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.
3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.
4. Puedes usar una lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0, -1) ), derecha ( (0, 1) ).
A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada 
- Laberinto (matriz)
- Indice de inicio (fila)
- Indice de Inicio (columna)

Salida
Camino para salir del laberinto: (1,1),(1,2),
(),()…"""

def buscar_en_fila(fila, num=9, columna=0):
    """buscamos la columna donde esta la salida"""
    if columna >= len(fila): 
        return None
    if fila[columna]==num: #pos.base
        return columna
    else:   #recursividad, vamos buscando columna
        return buscar_en_fila(fila, num, columna+1)

def buscar_salida(matriz, num=9, fila=0):
    """buscamos fila por fila hasta encontrar el número"""
    if fila>len(matriz):
        return None   #numero no encontrado
    columna=buscar_en_fila(matriz[fila], num) #buscamos la columna dentro de la fila concreta
    if columna is not None:
        return (fila, columna) #aqui paramos la recursion y devolvemos
    else:
        return buscar_salida(matriz, num, fila+1)


def resolver_laberinto(matriz,pos_fila, pos_columna, camino):
    """funcion recursiva para encontrar la salida mas corta"""

    if matriz[pos_fila][pos_columna]==9:
        return camino + [(pos_fila, pos_columna)]
    
    # marcar como visitado
    matriz[pos_fila][pos_columna] = -1

    caminos_encontrados = []

     # explorar direcciones
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in movimientos:
        nueva_fila = pos_fila + dx
        nueva_columna = pos_columna + dy

        if (0 <= nueva_fila < len(matriz) and
            0 <= nueva_columna < len(matriz[0]) and
            (matriz[nueva_fila][nueva_columna]==0 or matriz[nueva_fila][nueva_columna]==9)):

            nuevo_camino = resolver_laberinto(matriz, nueva_fila, nueva_columna, camino + 
                                              [(pos_fila, pos_columna)])
            if nuevo_camino:
                caminos_encontrados.append(nuevo_camino)

    # desmarcar para backtracking
    matriz[pos_fila][pos_columna] = 0

    if caminos_encontrados:
        # devolver el camino más corto
        return min(caminos_encontrados, key=len)
    else:
        return None

matriz=[[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,9,1], [1,1,1,1,1]]
fila_inic=1
columna_inic=1   
camino = resolver_laberinto(matriz, fila_inic, columna_inic, [])

if camino:
    print("Camino para salir del laberinto:", camino)
else:
    print("No hay salida encontrada")

    
    
