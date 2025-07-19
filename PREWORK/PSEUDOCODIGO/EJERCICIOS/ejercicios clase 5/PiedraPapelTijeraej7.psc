Algoritmo PiedraPapelTijera
	// Juego "Piedra, Papel, Tijera". Vamos a enfrentarnos contra el ordenador en el juego d piedra, papel o tijera. Reglas:
	//- Piedra gana a Tijera y pierde con Papel
	//Papel gana a Piedra y pierde con Tijera
	//- Tijera gana a Papel y pierde con Piedra
	//Pedir al jugador que escoja entre "Piedra | Papel | Tijera" (texto); el ordenador hará su elección al azar. 
	//Y se comparan las dos elecciones para ver quién gana. Al terminar una partida, se pedirá si se quiere jugar 
	//de nuevo (texto) y, en caso afirmativo, se reinicia el juego (sin que acabe el programa).
		//Recordatorio: hay que controlar que el jugador introduzca una de las 3 opciones
			//(Piedra | Papel | Tijera), y no otra.
		//Pista: la función "azar(3)" devuelve un número al azar entre 0, 1 y 2. Cada una de estas
	//opciones podríamos asociarla a "piedra", "papel" o "tijera": "Si numAzar = 0 Entonces ordenador = "Piedra" SiNo ?"
	
	//1.- vamos definiendo e inicializando
	Definir respuesta, jugar como texto
	Definir numAzar, respuestanum Como Entero
	
	respuesta = " "
	jugar = " "
    respuestanum = 3
	numAzar = azar (3)
	
	//2.- pedimos al jugador que escoga una opcíon. lo hacemos dentro del buble repetir para que pida una vez finalizado el proceso
	
	
	Repetir
		
		Escribir " Escoge una de las tres opciones para jugar contra el ordenador." 
		Escribir "Piedra, papel o tijera"
		Leer respuesta
		
		
		//damos valor numerico a las respuesta pedida para obtener resultado de empate/victoria/derrota
		
		Si(respuesta ="piedra")
			respuestanum= 0
			
		SiNo
			Si (respuesta ="papel") Entonces
				respuestanum = 1
				
			SiNo
				Si (respuesta = "tijera") Entonces
					
					respuestanum = 2
					
			FinSi
			FinSi
		FinSi
		
		//pedimos número al azar y le damos valor texto para calcular resultado final
	
	Si numAzar= 0 Entonces 
		Escribir " El ordenador elige piedra"
		
	SiNo
		Si numAzar = 1 Entonces
			
			Escribir " El ordenador elige papel"
			
		SiNo
			Si numAzar= 2 Entonces
				
				Escribir "El ordenador elige tijera"
			FinSi
			
		FinSi
		
	FinSi
	
	//calculamos resultado y todas las opciones. incluso si se ha dado una respuesta erronea por parte del usuario
	
	Si numAzar = respuestanum Entonces
		Escribir "Se ha producido un empate"
		
	Sino 
		Si (numAzar = 0 ) y (respuestanum = 2) Entonces
			Escribir "El ordenador gana"
			
		Sino 
			Si (numAzar = 1) y (respuestanum = 0) Entonces
				
				Escribir "El ordenador gana"
				
			Sino 
				Si (numAzar = 2) y (respuestanum = 1) Entonces
					Escribir "El ordenador gana"
				
			Sino 
				Si (numAzar = 1) y (respuestanum = 2) Entonces
					Escribir "Ganaste!"
					
				Sino 
					Si (numAzar = 2 ) y (respuestanum = 0) Entonces
						Escribir "Ganaste!"
						
					Sino 
						Si (numAzar = 0) y (respuestanum = 1) Entonces
							
							Escribir "Ganaste!"
							
						
				SiNo
					Escribir "Tu respuesta es incorrecta "
				FinSi
			FinSi
		FinSi
	FinSi
	FinSi
		FinSi
	FinSi
	
	//pedimos si quiere volver a jugar. si se escribe otra cosa diferente al si terminamos, sino se vuelve a empezar
	
	Escribir "¿Quieres jugar otra vez? si o no "
	Leer jugar
	
	Hasta que (jugar <> "si")
	
	
	//salimos y nos despedimos
	
	Escribir "De acuerdo, entiendo que no quieras jugar mas conmigo, nos vemos otro dia."
FinAlgoritmo
