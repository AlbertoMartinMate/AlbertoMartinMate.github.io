
//Crear un algoritmo que: a. Pida 1 n�mero por pantalla (entero) 
//b. Llame a una funci�n que imprima por pantalla si ese n�mero es m�l plo de 2, m�l plo de 3, o m�l plo de 2 y de 3. 
//i. Par�metros: n�mero que ha introducido el usuario (entero) 
//ii. Variable de retorno: ninguna

Funcion Multiplo(num)  //definimos e inicializamos la funcion.
	
	
	
	Si (num mod 2 = 0) y (num mod 3 = 0) Entonces      //Para averiguar si es multiplo de 2 o de 3 o de los dos. 
		Escribir "El n�mero es m�ltiplo de 2 y de 3"
		
	SiNo
		Si num mod 2 = 0 Entonces
			Escribir "El n�mero es m�ltiplo de 2"
			
		Sino 
			Si num mod 3 = 0 Entonces
				Escribir "El n�mero es m�ltiplo de 3"
				
			SiNo
				escribir "El resultado no es m�ltiplo ni de 2 , ni de 3"
			FinSi
		FinSi
		FinSi
FinFuncion

Algoritmo Multiplo2Y3
	
	Definir num Como Entero

	num=0
	
	Escribir "Escribe un n�mero para averiguar si es m�ltiplo de 2, de 3 o de ambos"
	Leer num
	
	multiplo(num)
	
FinAlgoritmo
