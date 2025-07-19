//Crear un algoritmo que: a. Crea un array bidimensional 5 las y 7 columnas, de números aleatorios (10-50) 
//b. Llame a una función que recorre el array y devuelve un texto con la suma de los valores de cada fila 
//i. Parámetros: array bidimensional 5x7, con números aleatorios (10-50) 
//ii. Variable de retorno: la suma de los valores de cada la (texto) 
//c. El algoritmo imprime el array y la suma de los valores de cada fila 
//Resultado (ejemplo, para el caso de un array bidimensional 2x3): 562 695 La suma de cada la es: 13 20

Funcion sumaFila= sumaFilaTexto(array)
	
	Definir sumaFila, totalFilaTexto como cadena
	Definir i, j, totalFila como Entero
	
	totalFila = 0
	sumaFila= " "
	i=0
	j=0
	
	Para i=0 hasta 5-1 con paso 1 Hacer
		Para j=0 hasta 7-1 con paso 1 hacer
			
			totalFila = totalFila + array[i,j]
			
			
		FinPara
		
		totalfilaTexto = ConvertirATexto(totalFila)
		sumaFila = Concatenar(sumaFila, totalFilaTexto)
		sumaFila = Concatenar(sumaFila, " ")
		totalFila = 0
		
	FinPara	
	
FinFuncion



Algoritmo ejercicio5IIParte
	
	Definir arrayBidimensional, fila, columna Como Entero
	definir totalFilaTexto como cadena
	dimension arrayBidimensional[5,7]
	
	fila=0
	columna=0
	totalFilaTexto= " "
	
	
	Para fila = 0 hasta 5-1 con paso 1 Hacer
		Para columna = 0 hasta 7-1 con paso 1 Hacer
			
			arrayBidimensional[fila,columna] = azar(41) + 10
			
			Escribir arrayBidimensional[fila,columna]  " " sin saltar
			
		FinPara
		
		 Escribir " "
	FinPara
	
	totalFilaTexto = sumaFilaTexto(arrayBidimensional)
	
	
	Escribir "La suma de los valores de cada fila son " totalFilaTexto
	
FinAlgoritmo
