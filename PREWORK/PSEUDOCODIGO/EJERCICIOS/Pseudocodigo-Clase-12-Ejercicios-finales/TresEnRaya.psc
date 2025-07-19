Funcion TableroJuego(tablero, jugada)  //funcion para mostar tablero
	
	Definir fila, columna Como Entero
	fila = 0
	columna = 0
	
	Escribir " --------------------- "
	Escribir " TABLERO  JUGADA Nº " jugada
	Escribir " --------------------- "
	
	Para fila = 0 hasta (3-1) con paso 1 Hacer
		Para columna = 0 hasta (3-1) con paso 1 Hacer
			
			Escribir tablero[fila,columna] Sin saltar
			
		FinPara
		
		Escribir " "
	FinPara
	
FinFuncion

Funcion  hayGanador = Ganador(tablero)
	
	Definir hayGanador Como Logico
	Definir i Como Entero
	
	i = 0
	
	Para i = 0 hasta 2 con paso 1 Hacer
		
		Si tablero[i,0] <>" X " y (tablero[i,0]) = (tablero[i,1]) y (tablero[i,1] = tablero[i,2]) Entonces
			
			hayGanador = Verdadero
			
		FinSi
	FinPara
	
	Para i = 0 hasta 2 con paso 1 Hacer
		
		Si tablero[0,i] <>" X " y (tablero[0,i]) = (tablero[1,i]) y (tablero[1,i] = tablero[2,i]) Entonces
			
			hayGanador = Verdadero
			
		FinSi
	FinPara
	
	Si (tablero[1,1] <> " X ") y (tablero[0,0]) = (tablero[1,1]) y (tablero[2,2]) = (tablero[1,1]) Entonces
		hayGanador = Verdadero
		
	FinSi
	
	Si (tablero[1,1] <> " X ") y (tablero[0,2]) = (tablero[1,1]) y (tablero[2,0]) = (tablero[1,1]) Entonces
		hayGanador = Verdadero
		
	FinSi
FinFuncion


Algoritmo TresEnRaya
	
	Definir tablero como texto
	Definir fila, columna, filaUsuario, columnaUsuario, filaOrdenador, columnaOrdenador, jugada, jugador Como Entero
	Definir hayGanador Como Logico
	
	Dimension tablero[3,3]
	fila = 0
	columna = 0
	filaUsuario = 0
	columnaUsuario = 0
	filaOrdenador = 0
	columnaOrdenador = 0
	jugada = 0
	jugador = azar(2)
	hayGanador = Falso
	
	Escribir " ----------------- "
	Escribir " COMIENZA EL JUEGO "
	Escribir "    TRES EN RAYA   " 
	Escribir " ----------------- "
	
	//1.- rellenamos tablero con X
	
	Para fila = 0 hasta (3-1) con paso 1 Hacer
		Para columna = 0 hasta (3-1) con paso 1 Hacer
			
			tablero[fila,columna] = " X "
			
		FinPara
	FinPara
	
	// 2.-mostramos tablero de comienzo
	
	TableroJuego(tablero, jugada)
	
	
	//3.- comienza el juego. sorteando el comienzo 
	
	Mientras (jugada<9) y (hayGanador = falso ) Hacer
		
		jugada = jugada +1  //sumamos jugada
		
		Si jugador = 0 Entonces
			
		Repetir
		
		Escribir " Introduce la fila y la columna donde quieres poner la ficha "
		Leer filaUsuario
		Leer columnaUsuario
	    Hasta Que tablero[filaUsuario, columnaUsuario] = " X "
	
	tablero[filaUsuario, columnaUsuario] = " U "
	
        SiNo
			Repetir
				
				filaOrdenador = azar(3)
				columnaOrdenador = azar(3)
				
			Hasta Que tablero[filaOrdenador, columnaOrdenador] = " X "
			
			tablero[filaOrdenador,columnaOrdenador] = " O "
	FinSi
	
	TableroJuego(tablero, jugada) //mostramos tablero despues de jugada
	
	hayGanador = Ganador(tablero) //para comprobar si hay ganador
	
	
	Si (hayGanador = Verdadero) y (jugador = 0) Entonces   //PARA VER QUIEN ES EL GANADOR
		
		Escribir "ENHORABUENA HAS GANADO"
		
	SiNo
		Si (hayGanador = Verdadero) y (jugador = 1) Entonces
			
			Escribir "HE GANADO"
			
		SiNo
			
			Si (hayGanador = falso) y (jugada = 9) Entonces
				
             Escribir " HEMOS QUEDADO EMPATE"
				
			FinSI
		FinSi
	FinSi
	
	Si jugador = 0 Entonces  //cambiamos turno de juego si no hay ganador y jugada<9 y es correcta la jugada
		jugador = 1
	Sino 
		jugador = 0
	FinSi
	
	FinMientras
	
FinAlgoritmo
