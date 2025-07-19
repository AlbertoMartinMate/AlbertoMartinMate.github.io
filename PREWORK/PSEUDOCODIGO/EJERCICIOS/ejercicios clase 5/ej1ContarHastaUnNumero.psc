Algoritmo ContarHastaUnNumero
	
	//Enunciado Pedir un número (entero) y escribir por consola todos los números hasta ese número, en orden creciente.
	//Ejemplo: si el número es 12, habría que escribir por consola todos los números desde el hasta el 12.
	
	//1.- Definir e inicializar
	
	Definir num, inicio Como Entero
	
	num = 0
	inicio = 1
	
	//2.- Pedir número hasta el que queremos contar
	
	Escribir "Introduce el número hasta donde quieres que contemos"
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
