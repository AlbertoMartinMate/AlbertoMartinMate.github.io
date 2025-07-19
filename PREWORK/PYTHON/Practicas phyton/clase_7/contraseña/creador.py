"""función llamada generar_contrasena que 
   genere contraseñas seguras de forma aleatoria. La función debe permitir especificar la longitud de 
   la contraseña y qué tipos de caracteres deben incluirse (por ejemplo, letras mayúsculas, 
   letras minúsculas, números y caracteres especiales). (Para el generador de contraseñas puedes 
   probar a usar los modulos random y string)"""

import random
import string

def generar_contraseña(): #9 caracteres q tenga mayus, minus, numero y simbolo
    #genera una contraseña segura dada una longitud(9)
    mayus= random.choice(string.ascii_uppercase)
    minus= random.choice(string.ascii_lowercase)
    nums= random.choice(string.digits)
    simbolos= random.choice(string.punctuation)
    resto= random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits \
                          + string.punctuation, k=5) #los otros 5 caracteres lo crea desde aqui


    password=[mayus, minus, nums, simbolos] + resto
    random.shuffle(password) 
    #coge un elemnto de cada, 5 del resto, y lo mezcla todo, dentro de la misma variable
    
    password="".join(password)
    #lo une para que no haya espacios

    return password #importante return y no imprimir
