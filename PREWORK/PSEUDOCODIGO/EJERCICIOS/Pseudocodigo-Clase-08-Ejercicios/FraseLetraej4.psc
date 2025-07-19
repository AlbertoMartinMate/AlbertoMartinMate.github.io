Algoritmo FraseLetra
	
	//Pedir una frase por consola (texto) y una letra (texto). 
    //Decir cuántas veces aparece la letra en el texto (entero). 
	//En este caso, no vamos a tener en cuenta mayúsculas/minúsculas, de forma que el texto será completamente en minúsculas, 
	//al igual que la letra. 
	//Resultado (ejemplo "hola, soy nueva"): La letra - a - aparece 2 veces en la frase ? Hola, soy nueva -
	
	//definimos e inicializamos
	
	Definir frase, letra, letraTexto como texto
	Definir i, num, array, long Como entero
	
	frase = " "
	letra = " "
	num = 0
	i=0
	long = 0
	
	// 2.- pedimos por consola una frase y la letra q queremos analizar e inicializamos el array con la longitud de esta
	
	Escribir "Introduce una frase " 
	Leer frase
	
	
	Escribir  "¿Que letra quieres que te digamos el número de veces que aparece?" 
	Leer letra
	
	long = longitud(frase)  //definimos el array y de la long antes de analizar la frase caracter a caracter
	
	Para i = 0 Hasta long -1 Con Paso 1 Hacer //restamos uno ya q empieza el array por 0
		
		letraTexto = Subcadena(frase, i, i) //PASO CLAVE, para analizar los caracteres y quedarse con uno
		
		Si letra = letraTexto Entonces   //analiza si esta la letra en el analisis, y si es asi, la cuenta
			
			num = num +1
			
		FinSi
	FinPara
	
	Escribir "El numero de veces que aparece la letra " letra  ", en la frase ," frase " ,es de " num  //resultado
	
	
FinAlgoritmo
