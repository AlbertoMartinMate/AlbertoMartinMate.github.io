Algoritmo Algebraica
	
//Enunciado
//Pedir dos números (enteros) por pantalla
//y pedir ELEGIR entre una operación de "sumar", "restar", "mul plicar" y "dividir" (texto). 
//Una vez tengamos los datos, realizar la operación en función de la operación seleccionada (real). 
//Recordatorio: si se elige "dividir", recordad que no se puede dividir entre 0. 
//Nota: Hay que tener en cuenta que pueden introducir otra operación que no sea la que esperamos, a lo que habría que decir: "No es posible realizar la operación solicitada".

	//1.- Definimos e inicializamos
	
	Definir num1, num2 Como Entero
	Definir Op como texto
	definir resultado Como Real
	
	num1 = 0
	num2 = 0
	Op = " "
	resultado = 0
	
	//2.- Pedimos números a realizar la operación y tipo de operación a realizar
	
	Escribir "Introduce número 1 "
	Leer num1
	
	Escribir "Introduce número 2 "
	Leer num2
	
	Escribir "¿Que operación quieres realizar ? Sumar, restar, multiplicar o dividir "
	Leer Op
	
	//3.- Pasamos a proceder a realizar las distintas operaciones. Segun 
	
	Segun Op Hacer
		
			"sumar" :
			resultado = num1 + num2 
			
			Escribir "El resultado de la operación : " resultado
			
			"restar" :
			resultado = num1 - num2 
			
			Escribir "El resultado de la operación : " resultado
			
			"multiplicar":
			resultado = num1 * num2 
			
			Escribir "El resultado de la operación : " resultado
			
			"dividir" :
			
			Si  no (num2 =0) Entonces
				resultado = num1/num2
				
				Escribir "El resultado de la operación : " resultado
				
			SiNo
				
				si num2=0 Entonces
				Escribir "No es posible realizar la operación, ya que no se puede dividir entre 0"
				
			FinSi
			
			
		FinSi
		
		De Otro Modo:
			
			Escribir "No es posible realizar la operación solicitada"
	FinSegun
	
	
	
FinAlgoritmo
