Algoritmo CambioFilasXColumnas
	
    //Crear un array bidimensional de 4 filas y 4 columnas, inicializado con números aleatorios (función azar), de 0 a 9. 
    //Crear un nuevo array bidimensional, donde las filas del array anterior sean ahora las columnas. 
    //Mostrar el array bidimensional inicial por pantalla y, a continuación, el nuevo array. 
    //Resultado (ejemplo): 5620 
						// 6954 
                        // 3087 
	//                     0182 
	
	//                    5630 
	//                    6901 
	//                    2588 
	//                    0472
	
	
	Definir array, fila, columna como entero
	Dimension array[4,4]
	
	
	
	//2.- inicializamos el array bidimensional y rellenamos con numeros al azar del 0 al 9. y lo escribimos
	
	Para fila = 0 Hasta 3 Con paso 1 Hacer
		Para columna = 0 hasta 3 con paso 1 Hacer
			array[fila,columna] = azar(10)
			
			Escribir array[fila,columna] " " Sin Saltar
			
		FinPara
		
		Escribir " "
	FinPara
	
	Escribir " " //para q deje espacio entre ambos array
	
	//Rellenamos el segundo array en el orden inverso
	
	Para columna =0 Hasta 3 Con paso 1 Hacer
		Para fila=0 hasta 3 con paso 1 Hacer
			
			Escribir array[fila,columna] " " Sin Saltar
			
		FinPara
		
		Escribir " "
		
	FinPara
	
	
FinAlgoritmo
