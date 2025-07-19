Algoritmo Ejercicio8
	
	//Pedir al jugador que piense un num del 1 al 10, darle cinco segundos para pensar y entonces empezar a decirle números al azar
    //durante cinco turnos. El juego termina cuando el ordenador acierte el número o pasen los 5 turnos.
	
	Definir numIntentos, numOrdenador, numUsados, i Como Entero
	Definir acierto Como Cadena
	Definir numeroNuevo Como Logico
	
	
	acierto = ""
	numIntentos = 0
	numOrdenador = 0
	Dimension numUsados[5]
	numeroNuevo = Falso
	i = 0
	
	Escribir "Piensa en un número del 1 al 10 y trataré de adivinarlo en 5 intentos!"
    Escribir "¿Listo? Vamos allá!"
    Esperar 1 Segundos
	
	Para i = 0 Hasta 4 Con Paso 1 Hacer
		numUsados[i] = 0
	FinPara
	
	Repetir
		numIntentos = numIntentos+1
		
		Repetir
			numOrdenador = azar(10)+1
			Si numUsados[0] <> numOrdenador Y numUsados[1] <> numOrdenador Y numUsados[2] <> numOrdenador Y numUsados[3] <> numOrdenador Y numUsados[4] <> numOrdenador Entonces
				numeroNuevo = Verdadero
			FinSi
		Hasta Que numeroNuevo
		
		numeroNuevo = Falso
		
		Escribir "¿Es ", numOrdenador, " el número que has pensado?"
		Leer acierto
		
		acierto = Minusculas(acierto)
		
		Si acierto = "no" Entonces
			numUsados[numIntentos-1] = numOrdenador
		FinSi
	Hasta Que numIntentos = 5 O acierto = "si"
	
	
FinAlgoritmo
