"""Logger con Tiempo de Ejecución
Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. Para asegurarte de que todo funcione correctamente y para
realizar un seguimiento del tiempo de ejecución de estas funciones, decides
implementar un decorador de registro (logger) con tiempo de ejecución.
El decorador debería realizar las siguientes acciones:
1. Antes de llamar a la función original (puedes incluir cualquier función),
debe imprimir un mensaje indicando que la función está a punto de
ejecutarse.
2. Después de que la función se haya ejecutado, debe imprimir un mensaje
que incluya el tiempo que tardó la función en ejecutarse.
3. Si la función original arroja una excepción, el decorador debe manejarla e
imprimir un mensaje adecuado, indicando que se ha producido una
excepción.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada Salida
-
- Invocando a la función 'mi_funcion'...
- La función 'mi_funcion' ha tardado
0.0012459754943847656 segundos en
ejecutarse.
- Resultados de la funcion: [0, 1, 1, 2, 3, 5,
8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181]"""

import time

def decorador_con_args(func):
    #Antes de llamar a la función original (puedes incluir cualquier función), debe 
    # imprimir un mensaje indicando que la función está a punto de ejecutarse.
    def nueva_funcion(*args, **kwargs):
        print(f"📦 Esta funcion esta apunto de ejecutarse")
        inicio=time.time()
        inicio = time.time()
        try:
            resultado = func(*args, **kwargs)
            print(f"✅ Resultado de la función: {resultado}") 
        except Exception as e:
            print(f"⚠️ ¡Ha ocurrido un error al ejecutar '{func.__name__}'!")
            print(f"📌 Tipo de error: {type(e).__name__}")
            print(f"📌 Detalle: {e}")
            resultado = None          #raise #si queremos q interrumpa la ejecucion normal
        
        fin=time.time()
        tiempo_ejecicion=fin-inicio
        print(f"La funcion se ha ejecutado en {tiempo_ejecicion :.10f} segundos")

        return resultado
    return nueva_funcion

@decorador_con_args
def sumar(a, b):
    return a + b

@decorador_con_args
def multiplicar(x, y):
    return x * y

@decorador_con_args
def filtrar_nombres(nombres_ordenados):
  #filtra los nombres q tengan mas de 5 letras y mas o igual de tres vocales
  nombres_filtrados= []

  for palabra in nombres_ordenados:
        partes = palabra.split()            # ['Laura', 'García']
        nombre = ' '.join(partes[:-1])  # todo menos el último → 'Laura' y reconstruye por si fuera compuesto
        vocales= "aeiouáéíóúAEIOUÁÉÍÓÚ"
        num_vocales = sum(1 for letra in nombre if letra in vocales)     
        if len(nombre) > 5 and num_vocales >=3:
            nombres_filtrados.append(palabra)
  return nombres_filtrados


if __name__ == "__main__":

    nombres_ordenados =['Laura García', 'Javier Moreno', 'Lucía Ramírez', 'Sergio Ortega', 'Elena Delgado', 'Miguel Navarro']

ejemplo1=sumar("hola",2100)

ejemplo2=multiplicar(0.00001, 0.023)

ejemplo3=filtrar_nombres(nombres_ordenados)