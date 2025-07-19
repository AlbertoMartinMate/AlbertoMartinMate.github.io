"""Revisa los ejercicios del modulo “Python para Principiantes”. ¿Hay algún ejercicio que pudiese 
dividirse en funciones? ¿Y alguno que podría optimizarse usando bloques try-except? Si es así 
reescríbelos usando estas estructuras."""

#refactorizar codigo biblioteca (practica clase 5)

import re

def busca_libro(lista_libros, palabra):
    #dandole una palabra del titulo o del autor, nos va a decir las coincidencias en nuestra biblioteca
    palabra=palabra.lower()
    conteo=0
        
    for titulo, autor in lista_libros:
        texto = f"{titulo} {autor}".lower()
        texto = re.sub(r'[^\w\s]', '', texto)
        if palabra in texto:
            conteo += 1
    print(f"La palabra '{palabra}' aparece en {conteo} entradas de la biblioteca.")

lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), 
                ('La ciudad y los perros', 'Mario Vargas Llosa')]   

while True:
    palabra = input("Introduce la palabra (o escribe 'salir' para terminar): ")
    if palabra.lower() == 'salir':
        break
    busca_libro(lista_libros, palabra)
