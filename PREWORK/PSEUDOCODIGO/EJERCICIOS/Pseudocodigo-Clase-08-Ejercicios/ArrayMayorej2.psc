Algoritmo ArrayMayor
	
	//Crear un array e inicializarlo con 5 números pedidos por consola (enteros). 
    //Una vez guardados, buscar cuál es el número mayor. 
	//Escribir en consola el array, y devolver cuál es el número mayor (entero). 
	//Resultado (ejemplo): 6 23 9 45 18 El número mayor del array es el 45
	
	//1. Definir e inicializar variables
	Definir i, mayor, array Como Entero
	Dimension array[5]
	
	i= 0
	mayor=0
	
	//2. Inicializar el array con números pedidos por consola
	
	Para i = 0 Hasta 4 Con paso 1 Hacer
		
		Escribir "Introduce un número"
		Leer array[i]
		
	FinPara
	
	//3. Buscar cuál es el número mayor
	
	Para i = 0 Hasta 4 con paso 1 Hacer
		
		Si (array[i] > mayor) Entonces
			mayor = array[i]
			
		FinSi
		
	FinPara
	
	//4. Escribir todos los números del array
	
	Para i = 0 Hasta 4 con paso 1 Hacer
		
		Escribir array[i], " " Sin Saltar
	
		
	FinPara
	
	Escribir " "
	
	Escribir " El número mayor es " mayor
	
	
	
FinAlgoritmo
