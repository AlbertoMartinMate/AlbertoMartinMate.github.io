Algoritmo ArrayMayor
	
	//Crear un array e inicializarlo con 5 n�meros pedidos por consola (enteros). 
    //Una vez guardados, buscar cu�l es el n�mero mayor. 
	//Escribir en consola el array, y devolver cu�l es el n�mero mayor (entero). 
	//Resultado (ejemplo): 6 23 9 45 18 El n�mero mayor del array es el 45
	
	//1. Definir e inicializar variables
	Definir i, mayor, array Como Entero
	Dimension array[5]
	
	i= 0
	mayor=0
	
	//2. Inicializar el array con n�meros pedidos por consola
	
	Para i = 0 Hasta 4 Con paso 1 Hacer
		
		Escribir "Introduce un n�mero"
		Leer array[i]
		
	FinPara
	
	//3. Buscar cu�l es el n�mero mayor
	
	Para i = 0 Hasta 4 con paso 1 Hacer
		
		Si (array[i] > mayor) Entonces
			mayor = array[i]
			
		FinSi
		
	FinPara
	
	//4. Escribir todos los n�meros del array
	
	Para i = 0 Hasta 4 con paso 1 Hacer
		
		Escribir array[i], " " Sin Saltar
	
		
	FinPara
	
	Escribir " "
	
	Escribir " El n�mero mayor es " mayor
	
	
	
FinAlgoritmo
