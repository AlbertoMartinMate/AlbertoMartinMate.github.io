//1. Crear un algoritmo que:
//a. Pida 1 n�mero por pantalla (entero)
//b. Llame a una funci�n que imprima por pantalla si ese n�mero es m�ltiplo de 2,
//m�ltiplo de 3, o m�ltiplo de 2 y de 3.

Funcion CalculaMultiplo2y3(_numero)
	Si (_numero MOD 2 = 0 Y _numero MOD 3 = 0) Entonces
		Escribir "El numero es multiplo de 2 y de 3"
	SiNo
		Si _numero MOD 2 = 0 Entonces
			Escribir "El numero es multiplo de 2"
		SiNo 
			Si _numero MOD 3 = 0 Entonces
				Escribir "El numero es multiplo de 3"
			SiNo
				Escribir "No es multiplo ni de 2 ni de 3"
			FinSi
		FinSi
	FinSi
FinFuncion

Algoritmo Multiplos2y3
	
	Definir num Como Entero
	num = 0
	
	Escribir "Dame un numero"
	Leer num
	
	CalculaMultiplo2y3(num)
	
FinAlgoritmo

//
