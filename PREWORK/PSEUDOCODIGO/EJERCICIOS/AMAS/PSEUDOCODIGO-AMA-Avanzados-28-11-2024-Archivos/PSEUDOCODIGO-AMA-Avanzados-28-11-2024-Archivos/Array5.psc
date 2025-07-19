//Crear un array de dimensi�n 5, inicializado con n�meros aleatorios (funci�n azar), del 0
//al 19. Pedir por consola un valor de 0 a 4, y mostrar el n�mero guardado en esa posici�n
//del array (entero). Escribir en consola tambi�n el array.
//Nota: si el n�mero que introduce el usuario es mayor a 4, el programa deber�a mostrar
//el array y avisar del error: "La longitud del array es de 0 a 4, por lo que la posici�n [5] no
//es v�lida"
//Resultado (ejemplo array 2 0 36 15 9 y posici�n 2):
//2 0 36 15 9

Algoritmo Array5
	
	Definir array, i, num Como Entero
	Dimension array[5] 
	
	i = 0
	num = 0
	
	Para i = 0 Hasta 4 Con Paso 1 Hacer
		array[i] = azar(20)
		Escribir array[i], "     " Sin Saltar
		
		// azar(8) + 8 (numeros aleatorios del 8 al 15)
	FinPara
	
	Escribir "" 
	
	
	Repetir
		Escribir "Dame un numero del 0 al 4 para acceder al array"
		Leer num
		
		Si (num < 0 O num >4) Entonces
			Escribir "ERROR: N�mero incorrecto, repite el procedimiento"
		FinSi
	Hasta Que (num >= 0 Y num<=4) 
	
	Escribir "El numero guardado en la posicion ", num, " es: ", array[num]
	
FinAlgoritmo
