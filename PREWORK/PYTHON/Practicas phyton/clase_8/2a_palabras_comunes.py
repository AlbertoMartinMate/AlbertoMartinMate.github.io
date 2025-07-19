"""Encuentra o crea algunos textos que te gustaría analizar (puedes visitar Project Gutenberg 
(http://gutenberg.org/) o crear textos usando ChatGPT). Copia el texto sin formato desde tu 
navegador en un archivo de texto en tu computadora (o descarga los archivos). Averigua cuántas veces 
aparece una palabra o frase en el texto (puedes usar el método count())."""

import re

def palabras_comunes(filename, elemento):
    #contar aparciocnes de una palabra o frase en difs. textos
    try:
        with open(filename, "r", encoding="utf-8") as f_obj:
            contenido=f_obj.read()
    except FileNotFoundError:
        pass
    else:
         # Todo en minúsculas para que no afecte mayúsculas/minúsculas
        texto = contenido.lower()
        frase = elemento.lower()
        # Quitamos signos de puntuación del texto
        texto = re.sub(r'[^\w\s]', '', texto)
        frase = re.sub(r'[^\w\s]', '', frase)
        conteo = texto.count(frase)
        print("La palabra/frase " + elemento + " en " + filename + " aparece " + str(conteo) + " veces.")

elemento=input("Introduce la palabra o frase que quieres que cuente en los siguientes archivos: ")
filenames=["resumen_dracula.txt", "resumen_robocop.txt", "resumen_300.txt", "resumen_gladiator.txt"]

for filename in filenames:
    palabras_comunes(filename, elemento)
