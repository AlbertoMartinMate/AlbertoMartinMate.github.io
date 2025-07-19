Algoritmo ArrayBidBuscaNum
	
	//Crear un array bidimensional de 5 filas y 5 columnas, inicializado con n�meros aleatorios (funci�n azar), de 0 a 9. 
	//Pedir por consola un valor de 0 a 9, y mostrar cu�ntas veces aparece ese n�mero en el array (entero). 
	//Escribir en consola tambi�n el array. Resultado (ejemplo, con el n�mero 5): 
	//56205 
	//69546 
	//30873 
	//01826 
	//09867 
	//El n�mero 5 aparece 3 veces
	
	//1.- Definimos e inicializamos
	
	Definir num, numsAzar, fila, columna, numTotal, numRepe como entero
	Dimension numsAzar[5,5]
	
	numRepe=0
	num =0 
	numTotal = 0
	
	//2.- inicializamos el array bidimensional y rellenamos con numeros al azar del 0 al 9
	
	Para fila = 0 Hasta 4 Con paso 1 Hacer
		Para columna = 0 hasta 4 con paso 1 Hacer
			num = azar (10)
			numsAzar[fila,columna] = num
			
		FinPara
	FinPara
	
	Escribir " Introduce un n�mero entre el 0 y el 9 que quieres buscar en el listado"
	Leer numRepe
	
	//3.- imprimir numeros del array bid. si se da la condicion que el n�mero dado esta entra las opciones marcadas
	
	Si (numRepe>=0) y (numRepe <=9) Entonces
		
	
	Para fila =0 Hasta 4 Con paso 1 Hacer
		Para columna=0 hasta 4 con paso 1 Hacer
			
			Escribir numsAzar[fila,columna] " " Sin Saltar
			
		FinPara
		
		Escribir " "
		
	FinPara
	
	//4.- buscamos el n�mero pedido por consola
	
	Para fila =0 Hasta 4 Con paso 1 Hacer
		Para columna=0 hasta 4 con paso 1 Hacer
			
			Si numRepe = numsAzar[fila,columna] Entonces
				
				numTotal = numTotal +1
				
			FinSi
			
		FinPara
		
		
	FinPara
	
	Escribir " El n�mero " numRepe " Aparece " numTotal " veces."
	
SiNo
	
	Escribir "El n�mero introducido no esta entre los valores 0 y 9 "
	
FinSi

	
FinAlgoritmo
