Algoritmo Multiplos2y3
	
	
	//Pedir un n�mero (entero) y calcular qu� n�meros desde el 1 hasta el propio n�mero son m�ltiplos de 2 y 3.
	//Recordatorio: un n�mero es m�ltiplo de 2 si al dividir por 2, el resto es 0; y es m�ltiplo
	//de 3 si al dividir por 3, el resto es 0
	//Ejemplo: dado el n�mero 15, los n�meros m�ltiplos de 2 y 3 hasta 15 son 6 y 12 (resto 0 en ambas divisiones)
	
	//1.- Definimos, inicializamos y pedimos n�mero
	
	Definir num, i, resultado, modulo Como entero
	
	num = 0
	i = 0
	resultado = 0
	modulo = 0
	
	Escribir "Enuncia un n�mero, del cual, obtendremos los n�meros multiplos de 2 y 3, desde el 1 hasta dicho n�mero "
	leer num
	
	Escribir " Dado el numero " num, " los numeros multiplos de de 2 y 3 hasta " num " son: "
	
	Para i = 1 Hasta num con paso 1 // Inicializamos con 1 porque el 0 no es multiplo de 2 y 3
		Si (i mod 2 = 0) y (i mod 3 = 0) Entonces
			
			Escribir " " i
		FinSi
	FinPara
FinAlgoritmo
