Algoritmo SumaNumeros
	
	//Enunciado Pedir dos n�meros por consola (enteros) y sumar (entero) todos los n�meros que hay entre ellos.
     //Nota: vamos a suponer que el primer n�mero que introduce el usuario SIEMPRE es menor que el segundo
	//Ejemplo: si los n�meros introducidos son el 4 y el 11, el resultado ser�a: 5 + 6 + 7 + 8 + 9 + 10 = 45
	
	//1.- Definimos e inicializamos
	
	Definir num1, num2, suma, numInicial Como Entero
	
	
	num2 = 0
	suma = 0
	numInicial = 0
	num1 = 0
	
	
	//2.- Pido los n�meros para hacer la suma
	
	Escribir "Introduce un numero. Desde dicho n�mero comenzar� la suma"
	Leer num1
	Escribir "Introduce un segundo n�mero. Hasta dicho n�mero se realizar� la suma"
	Leer num2
	
	
	numInicial = num1 +1 // Para comenzar la cuenta desde el el siguiente n�mero q nos dan. ANTES DEL MIENTRAS
	
	
	//3.- Hago un condicional para asegurarme de q numInicial es menor que num2
	
	Si numInicial<num2 Entonces
		
	
		
	Mientras numInicial<num2 Hacer //4.- Pasamos a realizar un bucle para q vaya sumando hasta q llegue a num2!
		
			suma = suma + numInicial      //en la operacion de arriba ponemos lo q queremos hacer y en la segunda como queremos q se vaya modificando la variable
			numInicial = numInicial +1
			
		FinMientras
		
		Escribir "El resultado de la suma entre los n�meros citados   " num1 "  y  " num2 "   Es : "  suma  //pongo espacios para al ejecutar se vea bien
		
SiNo
		Escribir "La operaci�n no se puede hacer por un error en los n�meros dados, ya que entre dichos n�meros no se puede hacer una suma"
		
	FinSi
	
FinAlgoritmo
