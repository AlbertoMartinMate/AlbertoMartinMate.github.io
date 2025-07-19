Algoritmo AdivinaMiNumero
	
	//Juego "Adivina mi n�mero". Pedir al jugador que piense un n�mero (entero) del 1 al 10, 
	//y dejarle 5 segundos para pensar ("Esperar 5 Segundos"). A partir de ah�, el
		//ordenador tratar� de adivinar el n�mero, preguntando al jugador si su n�mero es "X".
			//En caso de que no lo sea, volver� a preguntar por otro n�mero. Tiene 5 intentos para tratar de adivinarlo.
			//Nota: Utilizar las funci�n "azar" para que el ordenador pregunte de forma aleatoria.
	//	Recordatorio: el juego acaba cuando el "n�mero es acertado" O "se han hecho 5 intentos"
	
	Definir numAzar, numIntentos como Entero
	Definir respuesta como texto
	
	numAzar = azar (10) +1 //+1 para que la respuesta no sea 0
	numIntentos = 1
	respuesta = "no"
	
	Escribir "Piensa un n�mero del 1 al 10 "
	Esperar 5 Segundos
	
	
	Mientras (respuesta = "no" ) y (numIntentos <= 5) Hacer // respuesta inicializado con no xq sino no entra en el bucle, numintentos 4, xq ya hace el primero x defecto
		
		Escribir "�Tu n�mero es el " numAzar "? si o no"
		Leer respuesta
		
		Si respuesta = "si" Entonces
			
			Escribir "�Acertado! Soy una maquina:)"
			
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
		
		Escribir "Me has ganado, excedi el n�mero de intentos"
	FinSi
	
	
	
FinAlgoritmo
