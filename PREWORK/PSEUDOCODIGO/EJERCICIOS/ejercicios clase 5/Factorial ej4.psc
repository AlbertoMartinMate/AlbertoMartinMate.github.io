Algoritmo Factorial
	
	//Enunciado : Pedir un número (entero) y calcular su factorial (entero)
     //Recordatorio: el factorial de un número se calcula multiplicando los números desde el
	//1 hasta el propio número, incluidos los números intermedios
	//Ejemplo: el factorial de 6 sería 1 * 2 * 3 * 4 * 5 * 6 = 720
	
	//1.- Definimos e inicializamos
	
	Definir num, i, resultado Como Entero
	num = 0
	i = 1
	resultado = 1
	
	//2.- pedimos por consola numero
	
	Escribir "Introduce un número, del cual, vamos a sacar su factorial"
	Leer num
	
	//3.- utilizamos estructura para...
	Para  i = 1 Hasta num Con paso 1
		
		resultado = resultado * i
		
	fin para
	
	Escribir " El resultado del factorial es " resultado
	
FinAlgoritmo
