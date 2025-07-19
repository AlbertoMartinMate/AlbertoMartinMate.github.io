"""Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y en que posición. 
Puedes usar finnd()). Puedes usar el archivo pi_10000.txt"""

def buscando_pi(filename, fecha):
    #leer el archivo pi_10000, guardar contenido y buscar string
    try:

        with open(filename, "r") as file: #abre archivo
            num_pi=file.read() #lee archivo

            if fecha in num_pi:
                print("Tu fecha de nacimiento esta en el numero pi")
                posicion=num_pi.find(fecha) #si esta devolvemos la posicion
                print("En la posicion", posicion)

            else:
                print("Tu fecha de nacimiento, no esta en el numero pi")
    except FileNotFoundError:
        msj="Lo siento, el archivo " + filename + " no existe"
        print(msj)

nacimiento=input("Introduce la fecha de tu nacimiento, sin espacios ni signos de puntuacion: ")
numero_pi=("/home/alberto/MASTER EN DESARROLLO WEB FULL STACK/PREWORK/PYTHON/Practicas phyton/clase_8/pi_10000.txt")

buscando_pi(numero_pi,nacimiento)