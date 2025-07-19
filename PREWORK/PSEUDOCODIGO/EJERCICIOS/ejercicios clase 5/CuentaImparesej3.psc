Algoritmo CuentaImpares
	
	//Enunciado: Pedir un número por consola (entero) y escribir todos los números impares, en orden decreciente, desde ese número hasta el 1.
	//Ejemplo: si el número introducido es el 23, se escribirían el: 23, 21, 19, 17, ?, 5, 3, 1
	
	Definir num, resto Como Entero
	
	num = 0
	resto = 1
	
	Escribir "Introduce un número desde el que comenzar la cuenta atrás, enunciando solo, los números impares"
	Leer  num
	
	Escribir "Comienza la cuenta atrás..."
	

	
	Mientras (num>0) y (resto = num mod 2) Hacer //Para que escriba los numeros impares
		Escribir " " num
		
		Esperar 1 segundos
		
		num = num-1
		
		Mientras (num>0) y (0 = num mod 2) Hacer  //Para que los numeros pares los ignore
			
			Escribir " "
			
			num = num-1
			
		FinMientras
		
		
	FinMientras
	

	
	Escribir "La cuenta atrás de números impares ha finalizado"
	
FinAlgoritmo
