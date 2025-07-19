Algoritmo MediaArray
	
	//Pedir por consola el tamaño de un array (entero) y crear un array de esa dimensión 
	//inicializado con números aleatorios entre 5 y 20 (función azar). 
    //Escribir en consola el array, y devolver cuál es la media de todos los números del array (real). 
    //Nota: la media será la suma de todos los números del array dividido entre la dimensión 
    //Resultado (ejemplo con array de dimensión 4): 17 11 5 20 La media de los números del array es 13.25
	
	//1.- definimos e inicializamos
	
	Definir array, dimen, i Como Entero
	Definir media Como Real
	
	dimen= 0
	media = 0
	i = 0
	
	
	//2.- inicializamos array con x y pedimos numero de array por consola. ojo, lo inicializamos depues de pedir el número
	
	Escribir " ¿De cuantos números quieres que hagamos la media? "
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
		media = media + array[i]   //PARA SUMAR TODOS LOS NÚMEROS 
		
	FinPara
	
	media= media / dimen  //calculamos media
	
	
	Escribir "La media de todos los números son " media  //y nos lo gozamos
	
FinAlgoritmo
