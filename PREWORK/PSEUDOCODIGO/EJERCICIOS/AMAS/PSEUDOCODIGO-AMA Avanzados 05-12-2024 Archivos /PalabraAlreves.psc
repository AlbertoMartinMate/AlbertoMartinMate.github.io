Algoritmo PalabraAlreves
	Definir palabra, palabraNueva como Cadena
	Definir i Como Entero
	
	palabra = ""
	palabraNueva = ""
	i = 0
	
	Escribir "Dame una palabra"
	Leer palabra
	
	// palabra = "CONQUER"
	// palabraNueva = "REUQNOC"
	Para i = 0 Hasta Longitud(palabra)-1 Con Paso 1 Hacer
		// i = 0
		//Subcadena(palabra, i, i) = "C"
		//palabraNueva = "C"
		palabraNueva = Concatenar(Subcadena(palabra, i, i), palabraNueva)
		
		// i = 1
		//Subcadena(palabra, i, i) = "O"
		// palabraNueva = "O" + "C" = "OC"
		
		// i = 2
		// Subcadena(palabra, i, i) = "N"
		// palabraNueva = "N" + "OC" = "NOC"
		
		
	FinPara
	
	Para i = Longitud(palabra)-1 Hasta 0 Con Paso -1 Hacer
		palabraNueva = Concatenar( palabraNueva, Subcadena(palabra, i, i))
	FinPara
	
	
FinAlgoritmo
