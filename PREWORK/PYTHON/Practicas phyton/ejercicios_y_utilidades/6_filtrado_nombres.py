"""Problema de Transformación y Filtrado de Nombres:
Imagina que te encuentras desarrollando una herramienta de procesamiento de
nombres para una aplicación de gestión de contactos. Tienes una lista de
nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:
1. Utiliza la función lambda para transformar una lista de nombres completos
al nuevo formato.
2. Filtra la lista para incluir solo los nombres que contienen al menos dos
vocales y tienen una longitud mayor a 10 caracteres.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada Salida
- Lista de nombres, ej: ["Pérez, Juan",
"López, María"]
Nombres filtrados, ej: ['María López',
'José García']"""

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

def filtra_nombre_completo(nombres_ordenados):
  def nombre_valido(nombre):
    vocales= "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in nombre if letra in vocales) >=6 and len(nombre)>10
  return [nombre for nombre in nombres_ordenados if nombre_valido(nombre)]
   

if __name__ == "__main__":
 
 nombres=[
    "García, Laura",
    "Fernández, Marcos",
    "Ruiz, Andrea",
    "Torres, Daniel",
    "Sánchez, Paula",
    "Moreno, Javier",
    "Ramírez, Lucía",
    "Ortega, Sergio",
    "Delgado, Elena",
    "Navarro, Miguel"
]

#transformar una lista de nombres completos al nuevo formato.
nombres_ordenados= [
    (lambda n: n.split(', ')[1] + " " + n.split(', ')[0])(nombre_original)
    for nombre_original in nombres
]

# con chat gpt: list(map(lambda n: f"{n.split(', ')[1]} {n.split(', ')[0]}", nombres))

filtrado1=filtrar_nombres(nombres_ordenados) #nombres de mayor de 5 letras y 3 o mas vocales
print(f"Listado de nombres con mas de 5 letras y 3 o mas vocales: \n{filtrado1}")

filtrado2=filtra_nombre_completo(nombres_ordenados) #nombres completos de mayor de 10 letras y 6 vocales
print(f"Listado de nombres completos con mas de 10 letras y 6 o mas vocales: \n{filtrado2}")



