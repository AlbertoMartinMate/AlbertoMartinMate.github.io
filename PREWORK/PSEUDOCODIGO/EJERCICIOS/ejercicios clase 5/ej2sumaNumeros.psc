Algoritmo SumaNumeros
	
	//Enunciado Pedir dos números por consola (enteros) y sumar (entero) todos los números que hay entre ellos.
     //Nota: vamos a suponer que el primer número que introduce el usuario SIEMPRE es menor que el segundo
	//Ejemplo: si los números introducidos son el 4 y el 11, el resultado sería: 5 + 6 + 7 + 8 + 9 + 10 = 45
	
	//1.- Definimos e inicializamos
	
	Definir num1, num2, suma, numInicial Como Entero
	
	
	num2 = 0
	suma = 0
	numInicial = 0
	num1 = 0
	
	
	//2.- Pido los números para hacer la suma
	
	Escribir "Introduce un numero. Desde dicho número comenzará la suma"
	Leer num1
	Escribir "Introduce un segundo número. Hasta dicho número se realizará la suma"
	Leer num2
	
	
	numInicial = num1 +1 // Para comenzar la cuenta desde el el siguiente número q nos dan. ANTES DEL MIENTRAS
	
	
	//3.- Hago un condicional para asegurarme de q numInicial es menor que num2
	
	Si numInicial<num2 Entonces
		
	
		
	Mientras numInicial<num2 Hacer //4.- Pasamos a realizar un bucle para q vaya sumando hasta q llegue a num2!
		
			suma = suma + numInicial      //en la operacion de arriba ponemos lo q queremos hacer y en la segunda como queremos q se vaya modificando la variable
			numInicial = numInicial +1
			
		FinMientras
		
		Escribir "El resultado de la suma entre los números citados   " num1 "  y  " num2 "   Es : "  suma  //pongo espacios para al ejecutar se vea bien
		
SiNo
		Escribir "La operación no se puede hacer por un error en los números dados, ya que entre dichos números no se puede hacer una suma"
		
	FinSi
	
FinAlgoritmo
