Algoritmo ContarHastaUnNumero
	
	//Enunciado Pedir un n�mero (entero) y escribir por consola todos los n�meros hasta ese n�mero, en orden creciente.
	//Ejemplo: si el n�mero es 12, habr�a que escribir por consola todos los n�meros desde el hasta el 12.
	
	//1.- Definir e inicializar
	
	Definir num, inicio Como Entero
	
	num = 0
	inicio = 1
	
	//2.- Pedir n�mero hasta el que queremos contar
	
	Escribir "Introduce el n�mero hasta donde quieres que contemos"
	Leer num
	
	Escribir "Empezamos a contar..."
	
	//3.- comienza la cuenta
	Repetir 
		Escribir " " inicio
		
		Esperar 1 Segundos
		
		inicio = inicio +1
	Hasta Que inicio = num +1 //Hay q ponerlo en la misma linea (hasta que) Sino, da error. 
	                           //Ponemos +1 para que cuente hasta el numero citado
	Escribir "La cuenta ha terminado " //Cerramos bucle
	
FinAlgoritmo
