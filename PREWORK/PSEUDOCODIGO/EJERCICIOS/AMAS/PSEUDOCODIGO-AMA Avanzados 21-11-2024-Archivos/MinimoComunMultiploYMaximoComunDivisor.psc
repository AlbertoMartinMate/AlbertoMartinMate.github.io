
Funcion resultado = CalculaMaximoComunDivisor(num1, num2)
	Definir resultado, a, b, numAux Como Entero
	//a > b
	resultado = 0
	a  = 0
	b = 0
	numAux = 0
	
	Si num1>num2 Entonces
		a = num1 
		b = num2
	SiNo
		a = num2
		b = num1
	FinSi
	
	//Algoritmo de Euclides
	// a mod b (el resto de a dvidido por b)
	// a = b
	// b = a mod b
	
	Repetir
		numAux = a mod b
		a = b
		b = numAux
	Hasta Que b = 0
	
	resultado = a
	
FinFuncion

//MCM(a,b) = (a*b) / MCD

Funcion resultado = CalculaMinimoComunMultiplo(num1, num2)
	Definir resultado, mcd Como Entero
	resultado = 0
	mcd = 0
	
	mcd = CalculaMaximoComunDivisor(num1, num2)
	
	resultado = (num1*num2) / mcd
	
FinFuncion


Algoritmo MinimoComunMultiploYMaximoComunDivisor
	
	Definir numero1, numero2, mcm, mcd Como Entero
	numero1 = 0
	numero2= 0
	mcm  = 0
	mcd = 0
	
	Escribir "dame el primer número"
	Leer numero1
	
	Escribir "Dame el segundo número"
	Leer numero2
	
	mcm = CalculaMinimoComunMultiplo(numero1, numero2)
	mcd = CalculaMaximoComunDivisor(numero1, numero2)
	
	Escribir "El minimo comun multiplo es: ", mcm
	Escribir "El maximo comun divisor es: ", mcd
	
FinAlgoritmo
















