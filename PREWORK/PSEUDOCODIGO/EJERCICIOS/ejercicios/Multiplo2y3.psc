Algoritmo Multiplo2y3
	
	//Pedir un número (entero) por pantalla y decir si es múltiplo de 2 y de 3 a la vez (texto). 
    //Recordatorio: un número (número 1) es múltiplo de otro (número2) si al dividir el primero por el segundo, el RESTO de la división es 0.
	
	Definir numeroDefinir Como Entero
	Definir expresionLogica Como Logico
	
	numeroDefinir = 0
	
	
	Escribir "Introduce un número que sea múltiplo de 2 y de 3 a la vez"
	Leer numeroDefinir
	
	//Pido un número para comprobar si es múltiplo de 2 y de 3
	
	
	Si  (numeroDefinir mod 2 = 0) y (numeroDefinir mod 3 = 0) Entonces
		Escribir "El número es múltiplo de 2 y de 3"
		
	Sino 
		Escribir "El numero no es múltiplo de 2 y de 3"
	FinSi
	
	//Hago un operando lógico de Y para comprobar que se cumplen ambas condiciones
	
FinAlgoritmo
