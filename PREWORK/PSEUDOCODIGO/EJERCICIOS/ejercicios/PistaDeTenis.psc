Algoritmo PistaDeTenis
	
	//hemos alquilado una pista de tenis. precio x minuto es de 0.20 ?.
	//si jugamos mas de 90 minutos hay un descuento del 10%
	//pedir el numero de horas (entero) y el número de minutos (entero) que hemos jugado
	//calcular el precio a pagar (real)
	
	Definir precioPista, precioPistaDescuento Como Real
	Definir horas, minutos, tiempoJugado Como Entero
	
	horas = 0
	minutos = 0
	precioPista = 0.2
	precioPistaDescuento = 0.18
	tiempoJugado = 0
	
	Escribir "¿Cuanto tiempo hemos estado jugando? Horas y minutos. Horas: "
	Leer horas
	Escribir " ¿Cuantos minutos?"
	Leer minutos
	
	tiempoJugado = (horas *60) + minutos 
	
	Escribir "Tiempo jugado en minutos : " tiempoJugado
	
	Si tiempoJugado <= 90 Entonces
		Escribir "El precio a pagar en Euros es de : " tiempoJugado * precioPista 
		
	SiNo
		Escribir "El precio a pagar en Euros con el descuento realizado es : " tiempoJugado * precioPistaDescuento
		
	FinSi

	
	
FinAlgoritmo
