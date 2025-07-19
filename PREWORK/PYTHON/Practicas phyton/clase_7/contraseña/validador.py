"""funcion validar_contrasena 
que reciba una cadena y verifique si cumple con los requisitos mínimos de una contraseña segura 
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras minúsculas, números y caracteres
 especiales). La función debe devolver un valor booleano que indique si la contraseña es válida o no."""

def validar_contraseña(contraseña):
    #funcion q verifica si la contraseña es segura.
    #longitud minima, presencia de letras mayúsculas, letras minúsculas, números y caracteres especiales
    if len(contraseña)<=9:
        return False
    
    #si cumple longitud pasa a esto, sino se sale con el false
    tiene_mayus= any(caracter.isupper() for caracter in contraseña)
    tiene_minus= any(caracter.islower() for caracter in contraseña)
    tiene_num= any(caracter.isdigit() for caracter in contraseña)
    tiene_especial = any(caracter in"@#%$*+-" for caracter in contraseña)
    
    #comprobamos q todo se cumple
    if tiene_mayus and tiene_minus and tiene_num and tiene_especial:  
       return True
    else:
       return False
    
    #aqui termina. no habria q llamarla..pero queremos que imprima booleano si esta ok