//Pedir una frase por consola texto y contar el n�mero de vocales y consonantes que
//tiene la frase ( No vamos a tener en cuenta los acentos, s�mbolos, ni las
//may�sculas y min�sculas (el texto ser� en min�sculas).


Algoritmo CuentaVocalesyConsonantes
	Definir  frase como Cadena
	Definir vocales, consonantes, i Como Entero
	
	frase = ""
	vocales = 0
	consonantes = 0
	i = 0
	
	Escribir "Dame una frase"
	Leer frase
	
	Para i = 0 Hasta Longitud(frase)-1 Con Paso 1 Hacer
		Si Subcadena(frase, i, i) <> 'a' Y  Subcadena(frase, i, i) <> 'e' Y Subcadena(frase, i, i) <> 'i' Y Subcadena(frase, i, i) <> 'o' Y Subcadena(frase, i, i) <> 'u' Entonces
			Si Subcadena(frase, i,i) <> " " Entonces
				//No tenemos en cuenta numeros, signos de puntuacion etc
				consonantes = consonantes +1
			FinSi
		SiNo
			vocales = vocales + 1
		FinSi
	FinPara
	
	Escribir "El numero de vocales es: ", vocales
	Escribir "El n�mero de consonantes es:", consonantes
	
FinAlgoritmo
