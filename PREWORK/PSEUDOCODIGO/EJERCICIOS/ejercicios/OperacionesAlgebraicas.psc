Algoritmo Algebraica
	
//Enunciado
//Pedir dos n�meros (enteros) por pantalla
//y pedir ELEGIR entre una operaci�n de "sumar", "restar", "mul plicar" y "dividir" (texto). 
//Una vez tengamos los datos, realizar la operaci�n en funci�n de la operaci�n seleccionada (real). 
//Recordatorio: si se elige "dividir", recordad que no se puede dividir entre 0. 
//Nota: Hay que tener en cuenta que pueden introducir otra operaci�n que no sea la que esperamos, a lo que habr�a que decir: "No es posible realizar la operaci�n solicitada".

	//1.- Definimos e inicializamos
	
	Definir num1, num2 Como Entero
	Definir Op como texto
	definir resultado Como Real
	
	num1 = 0
	num2 = 0
	Op = " "
	resultado = 0
	
	//2.- Pedimos n�meros a realizar la operaci�n y tipo de operaci�n a realizar
	
	Escribir "Introduce n�mero 1 "
	Leer num1
	
	Escribir "Introduce n�mero 2 "
	Leer num2
	
	Escribir "�Que operaci�n quieres realizar ? Sumar, restar, multiplicar o dividir "
	Leer Op
	
	//3.- Pasamos a proceder a realizar las distintas operaciones. Segun 
	
	Segun Op Hacer
		
			"sumar" :
			resultado = num1 + num2 
			
			Escribir "El resultado de la operaci�n : " resultado
			
			"restar" :
			resultado = num1 - num2 
			
			Escribir "El resultado de la operaci�n : " resultado
			
			"multiplicar":
			resultado = num1 * num2 
			
			Escribir "El resultado de la operaci�n : " resultado
			
			"dividir" :
			
			Si  no (num2 =0) Entonces
				resultado = num1/num2
				
				Escribir "El resultado de la operaci�n : " resultado
				
			SiNo
				
				si num2=0 Entonces
				Escribir "No es posible realizar la operaci�n, ya que no se puede dividir entre 0"
				
			FinSi
			
			
		FinSi
		
		De Otro Modo:
			
			Escribir "No es posible realizar la operaci�n solicitada"
	FinSegun
	
	
	
FinAlgoritmo
