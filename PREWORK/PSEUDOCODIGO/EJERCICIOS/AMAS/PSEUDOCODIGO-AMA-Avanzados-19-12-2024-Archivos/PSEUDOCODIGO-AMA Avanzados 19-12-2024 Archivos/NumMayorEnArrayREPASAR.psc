Funcion VMA = Mayor(NumerosArray)
	
	Definir i, VMA Como Entero
	i = 0
	VMA = 0

	Para i = 0 Hasta (10-1) Con Paso 1 Hacer
		Si NumerosArray[i] > VMA Entonces
			VMA = NumerosArray[i]
			
		FinSi
	FinPara
FinFuncion

Algoritmo NumMayorEnArray
	
//Crear un algoritmo que:
//a. Crea un array de dimensión 10 de números aleatorios (1-50)
//b. Llame a una función que recorre el array y devuelve el número más alto del array
	
//c. El algoritmo imprime el array y el valor devuelto por la función
//Resultado:
//17 11 5 20 34 2 45 36 8 12
//El número más alto es el 45
	
	
	Definir array, i, masAlto Como Entero
	Dimension array[10]
	i = 0
	masAlto = 0
	
	Para i = 0 Hasta (10-1) Con Paso 1 Hacer
		array[i] = azar(50)+1
	FinPara
	
	masAlto = Mayor(array)
	
	Para i = 0 Hasta (10-1) con paso 1 Hacer
		Escribir array[i] " " Sin Saltar
	FinPara
	Escribir ""
	Escribir "El numero más alto del array es " masAlto
	
FinAlgoritmo
