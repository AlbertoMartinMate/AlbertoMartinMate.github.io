# -*- coding: utf-8 -*-
"""

VALIDACIÓN DE FORMULARIO
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
 1. Que el nombre tenga una longitud minima de 3 caracteres
 2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
 3. Que el email contenga un “@“ y un “.”
"""

#creamos una funcion

def validar_formulario(nombre, mail, num_telefono):
  #esta funcion verifica q los valores ingresados cumplen con los requisitos. si cumple, true, sino false
   
    if len(nombre)<3:
      print("Por favor introduce un nombre con tres caracteres o mas")
      return False

    if "@" not in mail or "." not in mail:
      print("Por favor, introduce un correo valido")
      return False

    if not num_telefono.isdigit() or len(num_telefono)!=9:
      print("Introduce un número valido")
      return False

    return True

while True:
 name=input("Introduce tu nombre: ")
 correo=input("Introduce un correo electronico: ")
 telefono=input("Introduce tu numero de telefono: ")

 if validar_formulario(name, correo, telefono):

  print("Formulario válido")
  print(f"Nombre:{name.title()}, Correo electronico: {correo}, Numero de telefono: {telefono}")
  break

 else:
  print("Por favor, introduce los datos correctamente")