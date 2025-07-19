//a. Crea un array de dimensión 10 de números aleatorios (1-50) 
//b. Llame a una función que recorre el array y devuelve el número más alto del array 
//i. Parámetros: array con 10 números aleatorios (1-50) 
//ii. Variable de retorno: el valor más alto (entero) 
//c. El algoritmo imprime el array y el valor devuelto por la función 
//Resultado: 17 11 5 20 34 2 45 36 8 12 El número más alto es el 45

Funcion NumMayor = NumMayor (numAleatorio) //funcion con parametro y con variable de retorno. parametro (hay q inicializar un proceso) hay q operar y variable de retorno
	
	Definir mayor,i Como Entero
	
	mayor = 0
	i=0
	
	Para i=0 Hasta 9 con paso 1 hacer
		Si numAleatorio[i] > mayor Entonces
			mayor = numAleatorio[i]               //Importante este orden de mayor antes. sino no es valido
		FinSi
	FinPara
	
	Escribir " El número mayor es " mayor
	
	
FinFuncion

Algoritmo NumMasAlto
	
	//1.- definimos e iniciqlizamos
	
	Definir num, numAleatorio,i, mayor como entero
	Dimension numAleatorio[10]
	
	mayor=0
	num=0
	i=0
	
	//2.- rellenamos array con numeros aleatorios del 1 al 50
	
	Para i=0 Hasta 9 Con Paso 1 Hacer
		
		numAleatorio[i]= azar(50) +1
		
	FinPara
	
	//3.- lo escribimos
	
	Para i=0 Hasta 9 con paso 1 Hacer
		Escribir numAleatorio[i] " "Sin Saltar
		
		
	FinPara
	
	//4.- Para saber que número es mas alto, llamamos la funcion
	
	mayor = NumMayor(numAleatorio)
	

	
FinAlgoritmo
