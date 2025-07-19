"""Problema de Organización de Datos Empresariales:
Imagina que trabajas en una empresa internacional con equipos distribuidos en
diferentes países. Cada equipo tiene una lista de empleados, representados
como diccionarios, con información sobre el nombre, la edad y el rendimiento
en proyectos recientes.
Tu tarea es organizar una lista consolidada de todos los empleados de la
empresa. La organización debe seguir ciertas reglas:
1. Los empleados se deben ordenar por el rendimiento en proyectos recientes
de forma descendente.
2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de
forma ascendente. Además, deseas agrupar a los empleados por país para
un análisis más efectivo. Utiliza funciones lambda.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada                                      Salida
- Registro de empleados (json,dic,etc) Empleados agrupados"""

import json
from itertools import groupby  


def ordenar_por_rendimiento(empleados):
    #ordenamos por rendimiento y si es igual por edad ascendente
    empleados_ordenados=sorted(empleados, key=lambda e: (-e["rendimiento"], e["edad"]))
    return empleados_ordenados

def ordenar_por_ciudad(empleados_ordenados):
    #ordenamos por ciudad
    empleados_ordenados_ciudad= {ciudad: list(grupo_ciudad) for ciudad, grupo_ciudad 
                                 in groupby(empleados_ordenados, key=lambda e:(e["ciudad"]))}
    return empleados_ordenados_ciudad

def mostrar_empleados_agrupados(empleados_ordenados_ciudad):
        
    for ciudad, grupos_ciudad in empleados_ordenados_ciudad.items():
        print(f"\nCiudad: {ciudad}")
        for empleado in grupos_ciudad:
            print(empleado)

# Leer empleados del archivo JSON
with open("empleados.json", "r", encoding="utf-8") as f:
    empleados = json.load(f)

empleados_ordenados= ordenar_por_rendimiento(empleados)
empleados_ordenados_ciudad= ordenar_por_ciudad(empleados_ordenados)
mostrar_empleados_agrupados(empleados_ordenados_ciudad)