Funcion DimenTablero = TableroDeJuego(dificultad)  //funcion para calcular la dimension que va a tener el tablero
	
	Definir dimen, DimenTablero Como Entero
	dimen = 0
	DimenTablero = 0
	
	Si (dificultad = 1) entonces 
		DimenTablero = 3
		
	SiNo
		Si (dificultad = 2) Entonces
			DimenTablero= 4
			
		Sino 
			DimenTablero = 5
		FinSi
	FinSi
FinFuncion

Funcion juego = HundirBarcos(tablero,dimen)
	
	Definir intentos, filaUsuario, columnaUsuario, barcoHundido, juego Como Entero
	
	juego = 0
	intentos = 0
	filaUsuario = 0
	columnaUsuario = 0
	barcoHundido = 0
	
	Escribir "Tienes 5 intentos para intentar hundir mis barcos!!"

	Mientras (intentos<5) Hacer
		
		Escribir " "
		Escribir "Intento número " intentos+1
		
    Escribir "Introduce una fila " " 0- " dimen-1
	Leer filaUsuario
	Escribir "Introduce una columna " " 0- " dimen-1
	Leer columnaUsuario
	
	Si tablero[filaUsuario,columnaUsuario] = " B " Entonces
		tablero[filaUsuario,columnaUsuario] = " H "
		
		Escribir "BARCO HUNDIDO"
		barcoHundido = barcoHundido +1
	Sino 
		
		Escribir "AGUA"
	FinSi
	
	intentos = intentos + 1
	
	Si barcoHundido = 3 Entonces
		intentos = 5
	FinSi
	
     FinMientras

     Si barcoHundido =3 Entonces
	Escribir "HAS GANADO, HAS HUNDIDO TODOS MIS BARCOS "
     SiNo
	Escribir "SE ACABARON TUS INTENTOS, PERDISTE. ME QUEDARON BARCOS A FLOTE"
    FinSi
	
		
FinFuncion

   

Algoritmo HundirLaFlota
	
	
	Definir tablero como texto
	Definir fila, columna, dimen, barcos, barcoHundido, dificultad, filaBarco, columnaBarco Como Entero
	                   
	fila = 0
	columna = 0
	dimen = 0
	barcos = 0
	barcoHundido = 0
	dificultad = 0
	filaBarco = 0
	columnaBarco = 0
	
	//1.- letrero inicial
	
	Escribir " ------------------------------ "
	Escribir " BIENVENIDO A HUNDIR LA FLOTA "
	Escribir " ------------------------------ "
	
    //2.- pedimos la dificultad del juego
	
	Escribir "Introduce la dificultad del juego : 1 (fácil), 2 (intermedio) y 3 (dificil) "
	Leer dificultad
	
	//3.- llamamos a la funcion,  en funcion de la dificultad elegida. 1 (3x3), 2 (4x4), y 3 (5x5)
	
	dimen = TableroDeJuego(dificultad)
	
	
	Dimension tablero[dimen,dimen]
	
	//4.- Rellenamos tablero con agua. (Con la funcion nos da error en la dimension de tablero) Tanto aqui como en la de los barcos
	
	
	Para fila = 0 hasta (dimen -1) con paso 1 Hacer
		Para columna = 0 Hasta (dimen -1) con paso 1 Hacer
			
			tablero[fila, columna] = " X " 
		FinPara
	
	FinPara
	
	
	
	//5.- Prepara los barcos el sistema . ponemos barcos en juegos (con funcion no nos sale)
	
	Escribir " ------------------------------- "
	Escribir "   SALIENDO LOS BARCOS A LA MAR  "
	Escribir " -------------------------------- "
	
	
	
	Mientras (barcos<3) Hacer
		
		filaBarco = azar(dimen)
		columnaBarco = azar(dimen)
		
		Si tablero[filaBarco, columnaBarco] = " X "
			tablero[filaBarco, columnaBarco] = " B "
			
			barcos = barcos + 1
		FinSi
	FinMientras
	
	//6.- Pasamos a proceder al juego. 
	
	Escribir "--------------------"
	Escribir "PROCEDEMOS A JUGAR "
	Escribir "--------------------"
	
	barcoHundido = HundirBarcos(tablero,dimen)
	
	
	Para fila = 0 hasta (dimen -1) con paso 1 Hacer
		Para columna = 0 Hasta (dimen -1) con paso 1 Hacer
			
			Escribir tablero[fila, columna] " " sin saltar 
		FinPara
		
		Escribir " "
	FinPara
FinAlgoritmo
