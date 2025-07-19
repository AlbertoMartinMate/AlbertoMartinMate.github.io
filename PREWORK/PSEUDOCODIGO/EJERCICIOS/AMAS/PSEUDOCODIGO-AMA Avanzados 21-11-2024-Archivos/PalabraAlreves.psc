Algoritmo PalabraAlreves
	Definir palabra, palabra2, palabra3 como Cadena
	Definir i, j, long Como Entero
	
	palabra = ''
	palabra2 = ''
	palabra3 =""
	i=0
	j=0
	long = 0
	
	Escribir "Dame una palabra"
	Leer palabra
	
	long = Longitud(palabra)
	
	Para i = 0 Hasta long-1 Con Paso 1 Hacer
		//cadena1 = "CONQUER"
		//cadena2 = "BLOCKS"
		
		//Concatenar(cadena1, cadena2) = "CONQUERBLOCKS"
		
		palabra2 = Concatenar(Subcadena(palabra, i,i), palabra2) 

		// palabra = "HOLA" palabra2 = "ALOH"
		
		// i = 0
		// palabra2 = Concatenar(Subcadena(palabra, i,i), palabra2) 
		// "" = Concatenar("H", "") = "H"
		
		// i = 1
		// palabra2 = Concatenar(Subcadena(palabra, 1,1), palabra2) 
		// Concatenar("O", "H") = "OH"
		
		Escribir "i = ", i
		Escribir "palabra2: ", palabra2
	FinPara
	
	Para i = long-1 Hasta 0 Con Paso -1 Hacer
		palabra3 = Concatenar(palabra3, Subcadena(palabra, i,i) ) 
		
		// i = 0
		// palabra3 = Concatenar(palabra3, Subcadena(palabra, i,i)) 
		// "" = Concatenar("A", "") = "A"
		
		// i = 1
		// palabra3 = Concatenar(palabra3, Subcadena(palabra, i,i)) 
		// "A" = Concatenar("A", "L") = "AL"
	FinPara
	
	
	
FinAlgoritmo
