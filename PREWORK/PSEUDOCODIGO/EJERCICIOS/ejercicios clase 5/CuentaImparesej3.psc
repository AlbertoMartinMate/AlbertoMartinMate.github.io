Algoritmo CuentaImpares
	
	//Enunciado: Pedir un n�mero por consola (entero) y escribir todos los n�meros impares, en orden decreciente, desde ese n�mero hasta el 1.
	//Ejemplo: si el n�mero introducido es el 23, se escribir�an el: 23, 21, 19, 17, ?, 5, 3, 1
	
	Definir num, resto Como Entero
	
	num = 0
	resto = 1
	
	Escribir "Introduce un n�mero desde el que comenzar la cuenta atr�s, enunciando solo, los n�meros impares"
	Leer  num
	
	Escribir "Comienza la cuenta atr�s..."
	

	
	Mientras (num>0) y (resto = num mod 2) Hacer //Para que escriba los numeros impares
		Escribir " " num
		
		Esperar 1 segundos
		
		num = num-1
		
		Mientras (num>0) y (0 = num mod 2) Hacer  //Para que los numeros pares los ignore
			
			Escribir " "
			
			num = num-1
			
		FinMientras
		
		
	FinMientras
	

	
	Escribir "La cuenta atr�s de n�meros impares ha finalizado"
	
FinAlgoritmo
