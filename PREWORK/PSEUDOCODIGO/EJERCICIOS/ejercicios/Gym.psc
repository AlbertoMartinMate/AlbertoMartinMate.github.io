Algoritmo Gym
	
	// Enunciado: Un gimnasio ene las siguientes tarifas: 
	//ma�anas, 1h cuesta 10 euros, 2h cuestan 20 euros y 3h (o m�s) cuestan 30 euros
	//tardes, 1h cuesta 20 euros, 2h cuestan 30 euros y 3h (o m�s) cuestan 40 euros. 
	//Pedir en qu� momento del d�a ir�s, "ma�anas" o "tardes" (texto), y el n�mero de horas que asistir�s (entero)Pedir en qu� momento del d�a ir�s, "ma�anas" o "tardes" (texto),
	//n�mero de horas que asistir�s (entero)
	//devolver la tarifa correcta (entero).
	
	//1.- definir e inicializar
	
	Definir jornada como texto
	Definir horas, tarifa Como Entero
	
	//2.- pedimos el momento del d�a y las horas que se van a ir al gimnasio
	
	Escribir " �En que momento del d�a iras al gimnasio? �Por las ma�ana o por la tarde? "
	Leer jornada
	
	Escribir "�Cuantas horas asistiras? "
	Leer horas
	
	jornada = "ma�ana
	horas = 0
	tarifa = 0
	
	
	//3.- segun los datos obtenidos pasamos a dar tarifas
	
	Si (jornada = "ma�ana") Entonces
		tarifa = horas *10
		Escribir "La tarifa es: " tarifa
		
	SiNo
		Si (jornada = "ma�ana") y (horas>=3) Entonces
			Escribir "La tarifa es de 30 euros"
			
		SiNo
			Si (jornada = "tarde") y (horas = 1) Entonces
				Escribir "La tarifa es de 20 euros"
				
			SiNo
				Si (jornada = "tarde") y (horas = 2) Entonces
					Escribir "La tarifa es de 30 euros"
					
				Sino 
					Si (jornada = "tarde") y (horas >=3) Entonces
						Escribir "La tarifa es de 40 euros"
					FinSi
					
			FinSi
		FinSi
	FinSi
FinSi

FinAlgoritmo
