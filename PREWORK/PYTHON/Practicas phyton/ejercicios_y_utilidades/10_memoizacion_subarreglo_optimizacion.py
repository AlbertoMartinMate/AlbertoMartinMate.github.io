
"""Problema de Optimización de Subarreglo:
Imagina que estás trabajando en un sistema de análisis de datos y te han
proporcionado una lista de números enteros. Tu tarea es desarrollar una
función llamada max_subarray_sum que encuentre y devuelva la suma máxima de
un subarreglo contiguo en la lista.
Por ejemplo, considera la lista [1, -2, 3, 10, -4, 7, 2, -5] . El subarreglo
contiguo con la suma máxima es [3, 10, -4, 7, 2] , y la suma de esos elementos
es 18 . Por lo tanto, la función debería devolver 18 para esta lista.
Implementa la función max_subarray_sum y, además, aplica memoización para
mejorar su eficiencia en el cálculo de subarreglos de suma máxima en listas
previamente procesadas.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada                                          Salida
- arreglo: [1, -2, 3, 10, -4, 7, 2, -5] -          18"""

import functools

@functools.lru_cache(maxsize=None)
def max_subarray_sum(arr):
  if not arr:
    return 0

  current_sum=max_sum=arr[0]
  max_subarray=[arr[0]]
  best_subarray = max_subarray.copy() #x siencontremos varios subarreglos q suman + q los anteriores

  for num in arr[1:]:
    if num >current_sum+num:
      current_sum = num       #Si num por sí solo es mejor que current_sum + num → empezamos un 
      max_subarray=[num]      #subarreglo nuevo que solo contiene num. Si current_sum + num es mejor 
    else:                    #→ seguimos sumando num al subarreglo que teníamos.
      current_sum+=num
      max_subarray.append(num)
    if current_sum > max_sum:         #xa asegurarnos q no haya otro sub arreglo q mayor valor  
            max_sum = current_sum
            best_subarray = max_subarray.copy()

  return max_sum, best_subarray         

arreglo = tuple([21, 2, -2, 3, -3, -20, 10, -4, 7, -5, 6])
resultado, subarray = max_subarray_sum(arreglo)
print("Suma máxima del subarreglo contiguo es de:", resultado)
print("Subarreglo contiguo con la suma máxima es:", subarray)