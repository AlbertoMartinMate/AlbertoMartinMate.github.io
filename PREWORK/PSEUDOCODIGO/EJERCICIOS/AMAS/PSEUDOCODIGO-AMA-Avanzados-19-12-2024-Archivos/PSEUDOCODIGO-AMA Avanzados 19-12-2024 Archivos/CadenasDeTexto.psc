//A las cadenas de caracteres las tratamos como si fueran arrays

Algoritmo CadenasDeTexto
	
	Definir palabra1, palabra2, frase, letra como Cadena
	Definir num, i, dimen Como Entero
	
	frase = ""
	palabra1 = ""
	palabra2 = ""
	letra = ""
	num = 0
	i = 0
	
	Escribir "Dame una palabra"
	Leer palabra1
	
	Escribir "Dame otra palabra"
	Leer palabra2
	
	frase = Concatenar(palabra1, palabra2)
	Escribir "He formado esta frase: ", frase
	
	frase = Concatenar(palabra2, palabra1)
	Escribir "He formado otra frase: ", frase
	
	//Convertir numero a texto
	num = 12
	palabra1= ConvertirATexto(num) // "12"
	
	//Recorrer cadena de caracteres
	// Subcadena("CONQUER BLOCKS", 3, 6) = "QUER"
	dimen = Longitud(frase)
	Para i = 0 Hasta dimen-1 Con Paso 1
		letra = Subcadena(frase, i, i)
		Escribir "La i: ", i
		Escribir "Letra: ", letra
	FinPara
	
	
	
FinAlgoritmo
