//Crear un algoritmo que: a. Crea un array bidimensional 5 las y 7 columnas, de n�meros aleatorios (10-50) 
//b. Llame a una funci�n que recorre el array y devuelve la posici�n del n�mero m�s alto en formato texto 
     //i. Par�metros: array bidimensional 5x7, con n�meros aleatorios (10-50) 
     //ii. Variable de retorno: la posici�n del array con el n�mero m�s alto (texto) 
//c. El algoritmo imprime el array y la posici�n del array con el n�mero m�s alto 
//Nota: Si el n�mero m�s alto aparece en varias posiciones, devolver �nicamente la primera en la que aparece 
//Resultado (ejemplo, para el caso de un array bidimensional 2x3): 562 695 
//La posici�n del array en la que aparece el n�mero m�s alto es la [1,1]


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
	
	//1. Recorrer el array y ver en qu� posici�n est� el n�mero m�s alto
	
	Para fila=0 hasta 4 con paso 1 Hacer
		Para columna=0 hasta 6 con paso 1 Hacer
			
			Si array[fila,columna] > num Entonces
			    num = array[fila,columna] 
				filaPosicion = ConvertirATexto(fila)
				columnaPosicion= ConvertirATexto(columna)
				
			FinSi
			
		FinPara
		
	FinPara
	
	//2. Guardar la fila y columna de la posici�n en formato texto, mediante concatenaci�n --> [X,Y
	lugar = "["
	lugar = Concatenar(lugar, filaPosicion)
	lugar = Concatenar(lugar, ",")
	lugar = Concatenar(lugar, columnaPosicion)
	lugar = Concatenar(lugar, "]")
	
	Escribir "La posici�n del array en la que aparece el n�mero m�s alto es la ", lugar
	
	
FinFuncion

Algoritmo ArrayBidBuscaNumAltoTexto
	
	Definir posArray Como Entero
	
	posArray=0
	
	
	posArray = BuscaNum(posArray)
	
	
	
FinAlgoritmo
