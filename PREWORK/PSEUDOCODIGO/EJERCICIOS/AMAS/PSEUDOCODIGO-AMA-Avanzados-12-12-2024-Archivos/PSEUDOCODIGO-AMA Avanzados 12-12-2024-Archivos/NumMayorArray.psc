//Crear un array e inicializarlo con 5 números pedidos por consola (enteros). Una vez
//guardados, buscar cuál es el número mayor. Escribir en consola el array, y devolver cuál
//es el número mayor (entero)

Algoritmo NumMayorArray
	Definir array, numMax, i, numMenor Como Entero
	numMax = 0
	numMenor = 0
	
	i = 0
	
	Dimension array[5]
	
	Escribir "Rellenamos el array: "
	
	Para i = 0 Hasta 4 Con Paso 1 Hacer
		Escribir "Dame un numero"
		Leer array[i]
		
		Si i = 0 Entonces
			numMenor = array[i]
			numMax = array[i]
		FinSi
		
		Si array[i] > numMax Entonces
			numMax = array[i]
		FinSi
		
		Si array[i] < numMenor Entonces
			numMenor = array[i]
		FinSi
		
	FinPara
	
	Para i = 0 Hasta 4 Con Paso 1 Hacer
		Escribir array[i], "     " Sin Saltar
	FinPara
	
	Escribir ""
	
	Escribir "El número más grande es: ", numMax
	Escribir "El número más pequeño es: ", numMenor
	
	
FinAlgoritmo
