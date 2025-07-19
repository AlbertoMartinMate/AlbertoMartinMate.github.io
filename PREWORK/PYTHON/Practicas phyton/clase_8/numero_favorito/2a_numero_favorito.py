"""Escribe un programa que solicite al usuario su número favorito. Utiliza json.dump() para 
almacenar este número en un archivo. Escribe un programa separado que lea este valor e imprima el 
mensaje: "Sé cuál es tu número favorito… Es ____.” Combina ambos programas en un solo archivo 
(puedes crear tantas funciones como necesites). Si el número ya está almacenado, muestra el número
 favorito al usuario. Si no lo está, solicita al usuario su número favorito y guárdalo en un 
 archivo. Ejecuta el programa al menos dos veces para asegurarte de que funciona correctamente."""

import json

#pedir el numero favorito
#guardar el numero favorito
#comprobar si tenemos guardado el numero favorito
#imprimir el numero favorito

def comprobar_num_fav():
    """Comprobar si existe un archivo con el numero favorito,
    y si existe va a devolver dicho numero"""
    try:
        with open("numero_fav.json", "r") as file:
            num_fav= json.load(file)
            return(num_fav)

    except FileNotFoundError:
        return None



def guardar_num_favorito(numero_favorito):
    """guarda el numero favorito introducido por el usuario"""
    #abrimos archivo
    with open("numero_fav.json", "w") as file:
        #guardamos numero favorito en archivo
        json.dump(numero_favorito, file)


def preguntar_num_fav():
    num_fav=int(input("Introduce tu numero favorito"))
    guardar_num_favorito(num_fav)
    return(num_fav)

def print_num_fav(numero_favorito):
    print(f"Se cual es tu numero favorito... es {numero_favorito}")


#Programa principal

numero_favorito= comprobar_num_fav()

if numero_favorito:
    print_num_fav(numero_favorito)
else:
    numero_favorito=preguntar_num_fav()
    print_num_fav(numero_favorito)

