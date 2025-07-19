Algoritmo VocalConsonante
	
	//Pedir una frase por consola (texto) y contar el número de vocales y consonantes que tiene la frase (enteros). 
    //No vamos a tener en cuenta los acentos, símbolos, ni las mayúsculas y minúsculas (el texto será en minúsculas). 
    //Resultado (ejemplo "soy nuevo en conquerblocks"): La frase - Hola, soy nuevo - tiene 6 vocales y 6 consonantes
	
	
	
	Definir frase, letraTexto como texto
	Definir vocal, consonante, i, long Como entero
	
	frase = " "
	vocal = 0
	consonante = 0
	letraTexto= " "
	i=0
	long = 0
	
	// 2.- pedimos por consola la frase que queremos analizar e inicializamos el array con la longitud de esta
	
	Escribir "Introduce una frase " 
	Leer frase

	
	long = longitud(frase)  //definimos el array y de la long antes de analizar la frase caracter a caracter
	
	Para i = 0 Hasta long -1 Con Paso 1 Hacer //restamos uno ya q empieza el array por 0
		
		letraTexto = Subcadena(frase, i, i) //PASO CLAVE, para analizar los caracteres y quedarse con uno
		
		Si (letraTexto="a") o (letraTexto="e") o (letraTexto="i") o (letraTexto="o") o (letraTexto="u") Entonces   //analiza si esta la letra en el analisis, y si es asi, la cuenta
			
			vocal = vocal+1
			
		SiNo
			
			Si letraTexto<> " " Entonces  //Para q no cuente los espacios
				
				Consonante= Consonante+1
				
			FinSi
			
			
		FinSi
	FinPara
	
	Escribir "El numero de vocales y consonantes que aparecen en la frase " frase " ,es de " vocal    "  vocales, y de " consonante   " consonantes"
	
	//resultado
	
FinAlgoritmo
