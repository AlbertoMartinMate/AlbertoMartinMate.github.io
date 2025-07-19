//6. Crear un array bidimensional de 4 filas y 4 columnas, 
//inicializado con números aleatorios (función azar), de 0 a 9.
//Crear un nuevo array bidimensional, donde las filas del array 
//anterior sean ahora las columnas. 
//Mostrar el array  bidimensional inicial por pantalla y, a continuación, el nuevo array - Resultado (ejemplo) :
//5 6 2 0     Fila 0
//6 9 5 4
//3 0 8 7
//0 1 8 2

//5 6 3 0
//6 9 0 1
//2 5 8 8
//0 4 7 2


Algoritmo ArrayBiTraspuesto
	
	Definir array, arrayT, i, j Como Entero
	
	Dimension array[4,4]
	Dimension arrayT[4,4]
	
	i = 0
	j = 0
	
	Para i = 0 Hasta 3 Con Paso 1 Hacer //filas
		Para j = 0 Hasta 3 Con Paso 1 Hacer //columnas
			array[i,j] = azar(10)
			arrayT[j, i] = array[i,j]
			Escribir array[i,j], "     " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	Escribir  ""
	
	Para i = 0 Hasta 3 Con Paso 1 Hacer //filas
		Para j = 0 Hasta 3 Con Paso 1 Hacer //columnas
			Escribir arrayT[i,j], "     " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
FinAlgoritmo
