
//Crear un algoritmo que: a. Pida 1 número por pantalla (entero) 
//b. Llame a una función que imprima la tabla de mul plicar de ese número, desde el 1 hasta el 10. 
           //i. Parámetros: número que ha introducido el usuario (entero) 
           //ii. Variable de retorno: ninguna. 
            //Resultado (ejemplo, número 35): Tabla de mul plicar del 35 ???????????? 35 x 1 = 35 35 x 2 = 70 ? 35 x 10 = 350

Funcion TablaMultip(num)
	
	Definir i, resultado como entero
	
	i=1
	resultado=0
	
	Para i=1 hasta 11 Con Paso 1 Hacer
		
		resultado = num * i
		
		Escribir num " x " i " = " resultado
		
	FinPara
	
FinFuncion



Algoritmo TablaMultiplicarEj2
	
	Definir num Como Entero
	
	num = 0
	
	Escribir "Introduce el número del cual quieres sacar la tabla de multiplicar"
	Leer num
	
	
	TablaMultip(num)
	
	
	
	
FinAlgoritmo
