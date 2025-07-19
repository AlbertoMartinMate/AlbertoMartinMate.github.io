Algoritmo PalabraClave
	
	//Pedir una frase por consola (texto) y obtener la palabra formada por la primera letra de cada palabra de la frase. 
    //Resultado (ejemplo "Hola, soy nuevo en programación"): La nueva palabra es: Hsnep
	
	Definir frase, letraTexto, palabra  como texto
	Definir long, i, numPalabra, numEspacio Como Entero
	
	palabra= " "
	
	frase = " "
	letraTexto = " "
	i = 0
	long =0
	numPalabra = 0
	numEspacio = 0
	
	
	Escribir "Introduce una frase "
	Leer frase
	
	long = Longitud(frase)  //importante poner este comando despues de leer la frase. obtiene el numero de caracteres para recorrerlos en bucle
	
	Para i = 0 hasta long -1 Hacer
		
		letraTexto = Subcadena(frase, i, i) //PASO CLAVE, para analizar los caracteres y quedarse con uno
		
		Si letraTexto= " " Entonces
			
			numEspacio= numEspacio + 1
		SiNo
			Si (numEspacio=numPalabra) Entonces         //Comprobamos si estamos aún en la misma palabra o si ya hemos dado paso a la siguiente (ha aparecido un
				
				palabra = Concatenar(palabra, letraTexto)  // un espacio). En caso de que ya estemos en la siguiente,
				numPalabra= numPalabra +1                    //podemos volver a coger la primera letra
				
			FinSi
			
		Finsi
		
	FinPara
	
      Escribir  "La nueva palabra es " palabra
		
	
	
	
FinAlgoritmo
