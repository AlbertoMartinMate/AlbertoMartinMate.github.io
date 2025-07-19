//Máximo Común Divisor. Crear un algoritmo que: a. Pide dos números por pantalla (enteros) 
//b. Llame a una función que calcula el máximo común divisor de esos dos números (MCD) 
//i. Parámetros: los dos números introducidos por el usuario (enteros) 
//ii. Variable de retorno: el MCD de los dos números (entero) 
//c. El algoritmo imprime el MCD de los dos números 
//Nota1: El MCD de dos números es el mayor de los divisores comunes de esos dos números. 
//Por ejemplo, para el 20 y el 12: Divisores del 20: 1, 2, 4, 5, 10, 20 (resto de la división 20/X es igual a 0) 
//Divisores del 12: 1, 2, 3, 4, 6, 12( resto de la división 12/X es igual a 0) 
//Por tanto, el MCD de 20 y 12 es 4. Nota2: Podéis tomar como ejemplo el del Mínimo Común Múl plo (MCM) visto en clase 
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
	
	
	Escribir "Introduce los dos números para sacar el máximo comun divisor de ambos"
	Leer num1
	Leer num2
	
	resultado= maximoComun (num1, num2)
	
	Escribir "El máximo comun divisor de ambos numeros es "  resultado
	
FinAlgoritmo
