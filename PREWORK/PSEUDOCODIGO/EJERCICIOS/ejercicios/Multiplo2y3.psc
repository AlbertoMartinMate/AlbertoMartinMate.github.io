Algoritmo Multiplo2y3
	
	//Pedir un n�mero (entero) por pantalla y decir si es m�ltiplo de 2 y de 3 a la vez (texto). 
    //Recordatorio: un n�mero (n�mero 1) es m�ltiplo de otro (n�mero2) si al dividir el primero por el segundo, el RESTO de la divisi�n es 0.
	
	Definir numeroDefinir Como Entero
	Definir expresionLogica Como Logico
	
	numeroDefinir = 0
	
	
	Escribir "Introduce un n�mero que sea m�ltiplo de 2 y de 3 a la vez"
	Leer numeroDefinir
	
	//Pido un n�mero para comprobar si es m�ltiplo de 2 y de 3
	
	
	Si  (numeroDefinir mod 2 = 0) y (numeroDefinir mod 3 = 0) Entonces
		Escribir "El n�mero es m�ltiplo de 2 y de 3"
		
	Sino 
		Escribir "El numero no es m�ltiplo de 2 y de 3"
	FinSi
	
	//Hago un operando l�gico de Y para comprobar que se cumplen ambas condiciones
	
FinAlgoritmo
