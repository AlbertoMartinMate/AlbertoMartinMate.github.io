"""Recursividad:
Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
apilados en orden descendente, desde el disco N en la parte inferior hasta el
disco 1 en la parte superior.
Tu tarea es implementar una solución recursiva para mover todos los discos
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de
Hanoi:
1. Puedes mover un disco a una torre adyacente.
2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si
el disco superior es más grande que el disco que estás colocando.
Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar)
que, dado el número total de discos n y las torres de origen, destino y auxiliar,
imprima los pasos necesarios para lograr el movimiento de todos los discos
desde la torre A hasta la torre C.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada 
- N de discos
- N de torres
- Torres : origen, desitno, auxiliar
Salida
Mover disco de la torre A a la torre D
Mover disco de la torre A a la torre B"""

def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:  #caso base recursividad
        print(f"Base. Mover disco {n} de la torre {origen} a la torre {destino}")
        return
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de la torre {origen} a la torre {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origen)

torres_de_hanoi(4, "A", "C", "B")

#lo q va haciendo con cada llamada

"""torres_de_hanoi(4, A, C, B)
│
├─ torres_de_hanoi(3, A, B, C)
│   │
│   ├─ torres_de_hanoi(2, A, C, B)
│   │   │
│   │   ├─ torres_de_hanoi(1, A, B, C)   # Mover disco 1 de A a B
│   │   ├─ print disco 2 de A a C
│   │   ├─ torres_de_hanoi(1, B, C, A)   # Mover disco 1 de B a C
│   │
│   ├─ print disco 3 de A a B
│   │
│   ├─ torres_de_hanoi(2, C, B, A)
│       │
│       ├─ torres_de_hanoi(1, C, A, B)   # Mover disco 1 de C a A
│       ├─ print disco 2 de C a B
│       ├─ torres_de_hanoi(1, A, B, C)   # Mover disco 1 de A a B
│
├─ print disco 4 de A a C
│
├─ torres_de_hanoi(3, B, C, A)
    │
    ├─ torres_de_hanoi(2, B, A, C)
    │   │
    │   ├─ torres_de_hanoi(1, B, C, A)   # Mover disco 1 de B a C
    │   ├─ print disco 2 de B a A
    │   ├─ torres_de_hanoi(1, C, A, B)   # Mover disco 1 de C a A
    │
    ├─ print disco 3 de B a C
    │
    ├─ torres_de_hanoi(2, A, C, B)
        │
        ├─ torres_de_hanoi(1, A, B, C)   # Mover disco 1 de A a B
        ├─ print disco 2 de A a C
        ├─ torres_de_hanoi(1, B, C, A)   # Mover disco 1 de B a C"""
    