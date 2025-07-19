//M�ximo Com�n Divisor. Crear un algoritmo que: a. Pide dos n�meros por pantalla (enteros) 
//b. Llame a una funci�n que calcula el m�ximo com�n divisor de esos dos n�meros (MCD) 
//i. Par�metros: los dos n�meros introducidos por el usuario (enteros) 
//ii. Variable de retorno: el MCD de los dos n�meros (entero) 
//c. El algoritmo imprime el MCD de los dos n�meros 
//Nota1: El MCD de dos n�meros es el mayor de los divisores comunes de esos dos n�meros. 
//Por ejemplo, para el 20 y el 12: Divisores del 20: 1, 2, 4, 5, 10, 20 (resto de la divisi�n 20/X es igual a 0) 
//Divisores del 12: 1, 2, 3, 4, 6, 12( resto de la divisi�n 12/X es igual a 0) 
//Por tanto, el MCD de 20 y 12 es 4. Nota2: Pod�is tomar como ejemplo el del M�nimo Com�n M�l plo (MCM) visto en clase 
//Resultado (ejemplo anterior): El MCD de 20 y 12 es: 4

Funcion resultado= maximoComun(num1, num2)
	
	Definir  a, b, numAux, mcd, resultado Como Entero
	
	numAux=0
	a=0
	b=0
	resultado=0
	
	
	si num1>num2 Entonces
		
		a = num1
		b = num2
		
	SiNo
		a= num2
		b= num1
		
	FinSi
	
	
	Repetir
		numAux = a mod b
		a = b
		b = numAux
	Hasta Que b = 0
	
	resultado = a
	
FinFuncion
	
	
Algoritmo MaximoComunDivisor
	
	Definir num1, num2, resultado como entero
	
	num1=0
	num2=0
	resultado=0
	
	
	Escribir "Introduce los dos n�meros para sacar el m�ximo comun divisor de ambos"
	Leer num1
	Leer num2
	
	resultado= maximoComun (num1, num2)
	
	Escribir "El m�ximo comun divisor de ambos numeros es "  resultado
	
FinAlgoritmo
