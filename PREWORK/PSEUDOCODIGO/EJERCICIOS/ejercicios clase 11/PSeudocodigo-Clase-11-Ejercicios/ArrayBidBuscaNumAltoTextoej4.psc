//Crear un algoritmo que: a. Crea un array bidimensional 5 las y 7 columnas, de números aleatorios (10-50) 
//b. Llame a una función que recorre el array y devuelve la posición del número más alto en formato texto 
     //i. Parámetros: array bidimensional 5x7, con números aleatorios (10-50) 
     //ii. Variable de retorno: la posición del array con el número más alto (texto) 
//c. El algoritmo imprime el array y la posición del array con el número más alto 
//Nota: Si el número más alto aparece en varias posiciones, devolver únicamente la primera en la que aparece 
//Resultado (ejemplo, para el caso de un array bidimensional 2x3): 562 695 
//La posición del array en la que aparece el número más alto es la [1,1]


Funcion BuscaNum = BuscaNum(posicion)
	
	Definir fila, columna, array, num Como Entero
	Definir lugar, filaPosicion, columnaPosicion como texto
	Dimension array[5,7]
	
	fila=0
	columna=0
	lugar = ""
	num=0
	
	Para fila=0 hasta 4 Con paso 1 Hacer            //No me salia al poner la estructura de escribir el array en el Algoritmo y la de calculo en la Funcion 
		Para columna=0 hasta 6 Con paso 1 Hacer
			
			array[fila,columna] = azar(41) + 10 //Para q salga entre el 10 y el 50
			
			Escribir array[fila,columna]  " " Sin Saltar
			
		FinPara
		
		Escribir " "
	FinPara
	
	//1. Recorrer el array y ver en qué posición está el número más alto
	
	Para fila=0 hasta 4 con paso 1 Hacer
		Para columna=0 hasta 6 con paso 1 Hacer
			
			Si array[fila,columna] > num Entonces
			    num = array[fila,columna] 
				filaPosicion = ConvertirATexto(fila)
				columnaPosicion= ConvertirATexto(columna)
				
			FinSi
			
		FinPara
		
	FinPara
	
	//2. Guardar la fila y columna de la posición en formato texto, mediante concatenación --> [X,Y
	lugar = "["
	lugar = Concatenar(lugar, filaPosicion)
	lugar = Concatenar(lugar, ",")
	lugar = Concatenar(lugar, columnaPosicion)
	lugar = Concatenar(lugar, "]")
	
	Escribir "La posición del array en la que aparece el número más alto es la ", lugar
	
	
FinFuncion

Algoritmo ArrayBidBuscaNumAltoTexto
	
	Definir posArray Como Entero
	
	posArray=0
	
	
	posArray = BuscaNum(posArray)
	
	
	
FinAlgoritmo
