//a. Crea un array de dimensi�n 10 de n�meros aleatorios (1-50) 
//b. Llame a una funci�n que recorre el array y devuelve el n�mero m�s alto del array 
//i. Par�metros: array con 10 n�meros aleatorios (1-50) 
//ii. Variable de retorno: el valor m�s alto (entero) 
//c. El algoritmo imprime el array y el valor devuelto por la funci�n 
//Resultado: 17 11 5 20 34 2 45 36 8 12 El n�mero m�s alto es el 45

Funcion NumMayor = NumMayor (numAleatorio) //funcion con parametro y con variable de retorno. parametro (hay q inicializar un proceso) hay q operar y variable de retorno
	
	Definir mayor,i Como Entero
	
	mayor = 0
	i=0
	
	Para i=0 Hasta 9 con paso 1 hacer
		Si numAleatorio[i] > mayor Entonces
			mayor = numAleatorio[i]               //Importante este orden de mayor antes. sino no es valido
		FinSi
	FinPara
	
	Escribir " El n�mero mayor es " mayor
	
	
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
	
	//4.- Para saber que n�mero es mas alto, llamamos la funcion
	
	mayor = NumMayor(numAleatorio)
	

	
FinAlgoritmo
