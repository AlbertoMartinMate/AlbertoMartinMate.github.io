Algoritmo Multiplos2y3
	
	
	//Pedir un número (entero) y calcular qué números desde el 1 hasta el propio número son múltiplos de 2 y 3.
	//Recordatorio: un número es múltiplo de 2 si al dividir por 2, el resto es 0; y es múltiplo
	//de 3 si al dividir por 3, el resto es 0
	//Ejemplo: dado el número 15, los números múltiplos de 2 y 3 hasta 15 son 6 y 12 (resto 0 en ambas divisiones)
	
	//1.- Definimos, inicializamos y pedimos número
	
	Definir num, i, resultado, modulo Como entero
	
	num = 0
	i = 0
	resultado = 0
	modulo = 0
	
	Escribir "Enuncia un número, del cual, obtendremos los números multiplos de 2 y 3, desde el 1 hasta dicho número "
	leer num
	
	Escribir " Dado el numero " num, " los numeros multiplos de de 2 y 3 hasta " num " son: "
	
	Para i = 1 Hasta num con paso 1 // Inicializamos con 1 porque el 0 no es multiplo de 2 y 3
		Si (i mod 2 = 0) y (i mod 3 = 0) Entonces
			
			Escribir " " i
		FinSi
	FinPara
FinAlgoritmo
