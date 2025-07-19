//Crear un algoritmo que: a. Crea un array bidimensional 5 las y 7 columnas, de números aleatorios (10-50) 
//b. Llame a una función que recorre el array y devuelve un texto con la suma de los valores de cada fila 
     //i. Parámetros: array bidimensional 5x7, con números aleatorios (10-50) 
    //ii. Variable de retorno: la suma de los valores de cada la (texto) 
//c. El algoritmo imprime el array y la suma de los valores de cada fila 
//Resultado (ejemplo, para el caso de un array bidimensional 2x3): 562 695 La suma de cada la es: 13 20


Funcion totalFilaTexto = SumaFila(num)

	Definir columna, fila, array, totalFila Como Entero
	definir  totalTexto, totalFilaTexto como texto
	dimension array[5,7]
	totalFila=0
	columna=0
	fila=0
	totalTexto= " "
	totalFilaTexto= " "
	
	//inicializamos el array con numeros aleatorios
	
	Para fila=0 hasta 5-1 con paso 1 Hacer
		Para columna=0 hasta 7-1 con paso 1 Hacer
			
			array[fila,columna] = azar(41) +10
			
		FinPara
		
	FinPara
	
	//hacemos la suma de cada fila
	
	Para fila = 0 hasta 5-1 con paso 1 Hacer          
		Para columna =0 hasta 7-1 con paso 1 Hacer
			
			totalFila= totalFila + array[fila,columna]
			
		FinPara
		
		totalTexto= ConvertirATexto(totalFila)
		totalFilaTexto= Concatenar[totalFilaTexto, totalTexto)
		totalFilaTexto=Concatenar(totalFilaTexto, " ") //para dejar espacio entre sumas
		totalFila=0 //para q se ponga a 0 y sume la siguiente fila
	FinPara
	
	//escribimos array
	
	Para fila=0 hasta 5-1 con paso 1 Hacer
		Para columna=0 hasta 7-1 con paso 1 Hacer
			
			Escribir array[fila,columna] " " Sin Saltar
			
		FinPara
		Escribir " "
	FinPara
	
FinFuncion

Algoritmo SumaValoresTexto
	
	Definir num Como Entero
	Definir sumatorio como texto

	sumatorio=""
	num=0
	
	//llamamos a la funcion
	sumatorio= SumaFila(num)
	
	Escribir "La suma de cada fila es: " sumatorio
	
FinAlgoritmo
