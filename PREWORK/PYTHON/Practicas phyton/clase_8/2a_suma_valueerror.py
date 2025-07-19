"""Un problema común al solicitar una entrada numérica ocurre cuando las personas ingresan texto 
en lugar de números. Cuando intentas convertir la entrada a un entero (int), obtendrás un ValueError.
 Escribe un programa que solicite dos números. Suma los números y muestra el resultado. Captura el 
 ValueError si alguno de los valores de entrada no es un número e imprime un mensaje de error 
 amigable. Prueba tu programa ingresando dos números y luego ingresando texto en lugar de un número. 
 Envuelve tu código del en un bucle while para que el usuario pueda continuar ingresando números 
 incluso si comete un error ingresando texto en lugar de un número."""

print("Dame dos numeros para sumar")

while True: #para q lo pida hasta q se introducen bien los numeros
    
    numero1=input("Introduce el primer numero: ")
    numero2=input("Introduce el segundo numero: ")
    #comprobamos q son los numeros enteros y hacemos suma
    try:
        resultado=int(numero1) + int(numero2)
        print(resultado)
        break #imprimimos y salimos
    except ValueError: #controlar el error de string en vez de int
        print("Respuesta incorrecta, por favor, introduce un valor numérico")
    