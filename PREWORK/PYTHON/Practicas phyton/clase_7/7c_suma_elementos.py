"""SUMA ELEMENTOS DE UNA LISTA Crea una función recursiva llamada suma_lista que calcule la 
suma de todos los elementos de una lista de enteros. Puedes asumir que la lista no está vacía."""

def suma_lista(lista):
    #nos devuelve la suma de los elementos de una lista de enteros
    if len(lista)==1: #caso base
        return lista[0]
    else: #recursivamente
        return lista[0] + suma_lista(lista[1:]) #desde elemento 1 hasta el final
        

mi_lista=[3,4,10,6]
print(suma_lista(mi_lista))

"""
3+suma_lista([4,10,6])
3+4+suma_lista([10,6])
3+4+10+suma_lista([6])
3+4+10+6 (aqui entra en caso base. len=1 devuelve la lista[6])
"""