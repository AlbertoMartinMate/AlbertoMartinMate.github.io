Algoritmo Gym
	
	// Enunciado: Un gimnasio ene las siguientes tarifas: 
	//mañanas, 1h cuesta 10 euros, 2h cuestan 20 euros y 3h (o más) cuestan 30 euros
	//tardes, 1h cuesta 20 euros, 2h cuestan 30 euros y 3h (o más) cuestan 40 euros. 
	//Pedir en qué momento del día irás, "mañanas" o "tardes" (texto), y el número de horas que asistirás (entero)Pedir en qué momento del día irás, "mañanas" o "tardes" (texto),
	//número de horas que asistirás (entero)
	//devolver la tarifa correcta (entero).
	
	//1.- definir e inicializar
	
	Definir jornada como texto
	Definir horas, tarifa Como Entero
	
	//2.- pedimos el momento del día y las horas que se van a ir al gimnasio
	
	Escribir " ¿En que momento del día iras al gimnasio? ¿Por las mañana o por la tarde? "
	Leer jornada
	
	Escribir "¿Cuantas horas asistiras? "
	Leer horas
	
	jornada = "mañana
	horas = 0
	tarifa = 0
	
	
	//3.- segun los datos obtenidos pasamos a dar tarifas
	
	Si (jornada = "mañana") Entonces
		tarifa = horas *10
		Escribir "La tarifa es: " tarifa
		
	SiNo
		Si (jornada = "mañana") y (horas>=3) Entonces
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
