"""Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de gatos en el primer 
archivo y tres nombres de perros en el segundo archivo. Escribe un programa que intente leer estos 
archivos e imprima el contenido de cada archivo en la pantalla. Envuelve tu código en un bloque 
try-except para capturar el error de FileNotFoundError, e imprime un mensaje amigable si falta 
algún archivo. Mueve uno de los archivos a una ubicación diferente en tu sistema y asegúrate de que 
el código en el bloque except se ejecute correctamente. Modifica tu bloque except para que falle en 
silencio si falta alguno de los archivos."""

#programa q lee los archivos e imprima el contenido


def archivos(filename):
    #para leer los diferentes archivos

    try:
        with open(filename) as f_obj:
            contenido=f_obj.read()
    except FileNotFoundError:
        msj="Lo siento, el archivo " + filename + " no existe"
        print(msj)
        #pass (si queremos error en silencio)
        #tb se podria poner otro except
    else:
        print("El contenido del archivo " +filename+ " contiene los sieguiente:\n" + contenido )
        
filenames=["cats.txt","dogs.txt"] 
#rutas absolutas o cambiar con cd en la terminal y situarnos en la carpeta del script, de esta forma 

for filename in filenames:
    archivos(filename)