Algoritmo AdivinaMiNumero
	
	//Juego "Adivina mi número". Pedir al jugador que piense un número (entero) del 1 al 10, 
	//y dejarle 5 segundos para pensar ("Esperar 5 Segundos"). A partir de ahí, el
		//ordenador tratará de adivinar el número, preguntando al jugador si su número es "X".
			//En caso de que no lo sea, volverá a preguntar por otro número. Tiene 5 intentos para tratar de adivinarlo.
			//Nota: Utilizar las función "azar" para que el ordenador pregunte de forma aleatoria.
	//	Recordatorio: el juego acaba cuando el "número es acertado" O "se han hecho 5 intentos"
	
	Definir numAzar, numIntentos como Entero
	Definir respuesta como texto
	
	numAzar = azar (10) +1 //+1 para que la respuesta no sea 0
	numIntentos = 1
	respuesta = "no"
	
	Escribir "Piensa un número del 1 al 10 "
	Esperar 5 Segundos
	
	
	Mientras (respuesta = "no" ) y (numIntentos <= 5) Hacer // respuesta inicializado con no xq sino no entra en el bucle, numintentos 4, xq ya hace el primero x defecto
		
		Escribir "¿Tu número es el " numAzar "? si o no"
		Leer respuesta
		
		Si respuesta = "si" Entonces
			
			Escribir "¡Acertado! Soy una maquina:)"
			
		SiNo
			
			Escribir "Voy a intentarlo otra vez"
			
			numIntentos = numIntentos +1
			numAzar = azar (10) +1
			
		FinSi
		
	FinMientras
	
	Escribir "Juego finalizado"
	
	Si respuesta = "si" Entonces
		
		Escribir "Lo acerte en " numIntentos " intentos"
		
	SiNo
		
		Escribir "Me has ganado, excedi el número de intentos"
	FinSi
	
	
	
FinAlgoritmo
