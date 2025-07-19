//TRES EN RAYA
//
// ** ** **
// ** ** **
// ** ** **
//
// ** O **
// ** O **
// ** O **
//
// U ** **
// ** U **
// ** ** U

//Función que muestra el tablero que se le pasa como parámetro
Funcion MostrarTablero(tableroJuego, jugada)
	//1. Definir e inicializar variables
	Definir fila, columna Como Entero
	
	fila = 0 
	columna = 0
	
	//2. Letrero
	Escribir ""
	Escribir " --------------------------------"
	Escribir "| TABLERO - JUGADA ", jugada " |"
	Escribir " --------------------------------"
	Escribir ""
	
	//3. Mostrar el tablero de juego
	
	Para fila = 0 hasta (3-1) con paso 1 Hacer
		Para columna = 0 hasta (3-1) con paso 1 Hacer
			
			Escribir tableroJuego[fila,columna] " " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
FinFuncion

//Función que revisa el tablero que se le pasa como parámetro, comprobando si hay algún ganador
Funcion hayGanador = ComprobarGanador(tableroJuego)
	//1. Definir e inicializar variables
	Definir hayGanador, ganador Como Logico
	definir i  Como Entero
	
	i = 0
	hayGanador = Falso
	ganador = falso
	
	//2. Comprobamos si hay alguna fila completa con X's o O's, que no sean "**"
	
		
	Para i= 0  Hasta (3-1) con paso 1 Hacer        
			
			Si (tableroJuego[i,0) <> "X")  y (tableroJuego[i,0] = tableroJuego[i,1]) y (tableroJuego[i,1] = tablerojuego[i,2])
				
				hayGanador = Verdadero
			FinSi
			
		FinPara
		
		Para i= 0  Hasta (3-1) con paso 1 Hacer        
			
			Si (tableroJuego[0,i) <> "X")  y (tableroJuego[0,i] = tableroJuego[1,i]) y (tableroJuego[1,i] = tablerojuego[2,i])
				
				hayGanador = Verdadero
			FinSi
			
		FinPara
	
	
	//3. Comprobamos si hay alguna columna completa con X's o O's, que no sean "**"
	
		//4. Comprobamos si alguna de las dos diagonales está completa con X's o O's, que no sean "**"
			
			Si  (tableroJuego[1,1) <> "X")  y (tableroJuego[0,0] = tableroJuego[1,1]) y (tableroJuego[1,1] = tablerojuego[2,2])
				
				hayGanador = Verdadero
			FinSi
			
			Si (tableroJuego[1,1) <> "X")  y (tableroJuego[0,2] = tableroJuego[1,1]) y (tableroJuego[1,1] = tablerojuego[2,0])
				
				hayGanador = Verdadero
			FinSi
			
		
		
	
FinFuncion

//Juego de las Tres en Raya
Algoritmo TresEnRaya
	//1. Definir e inicializar variables
	Definir numeroJugada, jugador, fila, columna, filaUsuario, columnaUsuario, filaOrdenador, columnaOrdenador Como Entero
	Definir tablero Como Texto
	Definir hayGanador, jugada Como Logico
	Dimension tablero[3,3]
	hayGanador = Falso
	numeroJugada = 0 //Como mucho, habrá 9 jugadas, ya que el tablero tiene 9 posiciones
	jugador = azar(2) //Si el resultado de azar(2) es 0, empezamos nosotros, y si es 1 empieza el ordenador. Vamos alternando de jugador
	//en cada jugada
	fila = 0
	columna = 0
	filaUsuario = 0
	columnaUsuario = 0
	filaOrdenador = 0
	columnaOrdenador = 0
	jugada = Falso
	
	//1.1. Inicializar las posiciones del tablero con texto vacío ("**")
	
	Para fila = 0 Hasta (3-1) con paso 1 Hacer
		Para columna = 0 hasta (3-1) con paso 1 Hacer
			
			tablero[fila,columna] = "X"
		FinPara
	FinPara
	
	//2. Empieza el juego
	
	//2.1. Comenzamos mostrando el tablero vacío
	MostrarTablero(tablero, numeroJugada)
	
	Mientras (numeroJugada < 9) Y (hayGanador = Falso) Hacer
		numeroJugada = numeroJugada + 1
		
		//2.2. En el caso de que sea el turno del jugador... (el usuario pone "U")
		Si (jugador = 0) Entonces
			
			Repetir
				
			
			Escribir "Es el turno del jugador..."
			//2.2.1. Pedir al usuario que elija una fila y una columna, hasta que introduzca una posición vacía (tablero[fila,columna] = "**")
			//y poner la ficha del jugador (tablero[fila,columna] = "U")
			
			Escribir "Introduce la fila y la columna donde colocar tu ficha"
			Leer filaUsuario
			Leer columnaUsuario
			
			Si tablero[filaUsuario, columnaUsuario] = "X" Entonces
				
				tablero[filaUsuario, columnaUsuario] = "U"
				
				jugada = Verdadero
				
			Sino jugada = falso
				
			FinSi
		Hasta Que jugada = Verdadero

		SiNo //2.3. En el caso de que sea el turno del ordenador... (el ordenador pone "O")
			Repetir
				
				Escribir "Es el turno del ordenador..."
			
			
			filaOrdenador = azar(3)
			columnaOrdenador = azar (3)
			
			Si tablero[filaOrdenador, columnaOrdenador] = "X" Entonces
				tablero[filaOrdenador, columnaOrdenador] = "O"
				jugada = Verdadero
				
				sino jugada = Falso
				
				FinSi
				
			Hasta Que jugada = Verdadero
			
			//2.3.1. Hacer que el ordenador elija una fila y una columna al azar, hasta que introduzca una posición vacía (tablero[fila,columna] = "**")
			//y poner la ficha del ordenador (tablero[fila,columna] = "O")
			
		FinSi
		
		//2.4. Mostramos el tablero después de poner la ficha
		MostrarTablero(tablero, numeroJugada)
		
		//2.5. Comprobamos si ha ganado el jugador que acaba de poner ficha, y si es así, lo decimos y terminamos el juego (función ComprobarGanador(tablero))		
		hayGanador = ComprobarGanador(tablero)
		
		Si (hayGanador = verdadero) y (jugador = 0 ) Entonces
			Escribir "ENHORABUENA HAS GANADO EL JUEGO"
			
		SiNo
			sI (hayGanador = verdadero) y (jugador = 1) Entonces
				
				Escribir "SOY EL GANADOR "
			FinSi
		FinSi
	
		
		//2.6. Cambiamos de jugador (Si acaba de jugar el ordenador, ahora le toca al jugador; y viceversa)
		
		Si jugador = 0 Entonces
		   jugador = 1
			
		SiNo
			
			jugador = 0
		FinSi
		
	FinMientras
	
	//3. En el caso de que no haya habido un ganador, mostrar que hemos empatado
	
	Si (numeroJugada = 9 ) y (hayGanador=falso) Entonces
		
		Escribir "HEMOS EMPATADO"
	FinSi
	
FinAlgoritmo
