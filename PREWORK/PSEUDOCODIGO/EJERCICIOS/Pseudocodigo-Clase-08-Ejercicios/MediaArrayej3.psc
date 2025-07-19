Algoritmo MediaArray
	
	//Pedir por consola el tama�o de un array (entero) y crear un array de esa dimensi�n 
	//inicializado con n�meros aleatorios entre 5 y 20 (funci�n azar). 
    //Escribir en consola el array, y devolver cu�l es la media de todos los n�meros del array (real). 
    //Nota: la media ser� la suma de todos los n�meros del array dividido entre la dimensi�n 
    //Resultado (ejemplo con array de dimensi�n 4): 17 11 5 20 La media de los n�meros del array es 13.25
	
	//1.- definimos e inicializamos
	
	Definir array, dimen, i Como Entero
	Definir media Como Real
	
	dimen= 0
	media = 0
	i = 0
	
	
	//2.- inicializamos array con x y pedimos numero de array por consola. ojo, lo inicializamos depues de pedir el n�mero
	
	Escribir " �De cuantos n�meros quieres que hagamos la media? "
	Leer dimen
	Dimension array[dimen]
		
	
	
	// 3.- rellenamos el array y lo imprimimos
	
	Para i= 0 hasta dimen -1 con Paso 1 Hacer
		
		array[i] = azar (16) +5   //sumamos 5 para que el numero nuca sea menor q 5 y ponemos 16 xa q no pase del 20
		
		
		Escribir array[i], " " Sin saltar  //lo escribimos dentro de la estructura
		
	FinPara
	
	 
	Escribir " "  //saltamos de linea una vez terminada la estructura
	
	
	//4.- calculamos media y lo imprimimos
	
	Para i= 0 hasta dimen -1 con Paso 1 Hacer
		media = media + array[i]   //PARA SUMAR TODOS LOS N�MEROS 
		
	FinPara
	
	media= media / dimen  //calculamos media
	
	
	Escribir "La media de todos los n�meros son " media  //y nos lo gozamos
	
FinAlgoritmo
