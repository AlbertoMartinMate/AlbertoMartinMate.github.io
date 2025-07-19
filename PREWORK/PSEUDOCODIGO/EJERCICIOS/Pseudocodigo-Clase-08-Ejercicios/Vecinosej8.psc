Algoritmo Vecinos
	
	//array bidimensional de 3 filas y 4 columnas, q va a representar un edificio de 3 plantas, cada una de ellas con 4 pisos. 
    //Inicializar el array con valores aleatorios (función azar), de 1 a 5 (incluidos). 
	//Mostrar el array por consola, y decir cuántos vecinos hay en cada planta. 
    //Resultado (ejemplo): 1 3 2 2  Esta sería la planta 3 
	              //       1 2 1 5 
	//                     2 4 2 1  Esta sería la planta 1 
	//El número de vecinos en la planta 3 es: 8 
    //El número de vecinos en la planta 2 es: 9    
	//  El número de vecinos en la planta 1 es: 9
	
	Definir edificio, fila, columna, planta1, planta2, planta3 como Entero
	Dimension edificio[3,4]
	
	planta1= 0
	planta2=0
	planta3=0
	fila= 0
	columna = 0
	
	Para fila = 0 Hasta 2 Con paso 1 Hacer
		Para columna = 0 hasta 3 con paso 1 Hacer
			
			edificio[fila,columna] = azar(5) +1
			
			Escribir edificio[fila,columna] " " Sin Saltar
			
		FinPara
		
		Escribir " "
	FinPara
	
	Para fila = 0 hasta 2 con paso 1 Hacer
		
		Para columna = 0 hasta 3 con paso 1 Hacer  //el corregido lo hace con condicional si-entonces, si fila = 0
			                                           //planta 3 = planta 3 + edificio[fila,columna] y asi todas las plantas
			
			planta3 = edificio[0,0] +edificio[0,1] + edificio[0,2] + edificio[0,3]
			planta2 = edificio[1,0] +edificio[1,1] + edificio[1,2] + edificio[1,3]
			planta1= edificio[2,0] +edificio[2,1] + edificio[2,2] + edificio[2,3]
			
			
		FinPara
		
		
	FinPara
	
	Escribir  " El número de vecinos que hay en la planta 3 es de " planta3
	Escribir  " El número de vecinos que hay en la planta 2 es de " planta2
	Escribir " El número de vecinos que hay en la planta 1 es de " planta1
	
	
FinAlgoritmo
