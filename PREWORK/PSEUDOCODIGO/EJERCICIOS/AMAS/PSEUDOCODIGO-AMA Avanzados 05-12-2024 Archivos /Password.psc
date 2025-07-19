Algoritmo Password
	Definir pass, passwordUsuario como Cadena
	Definir numIntentos Como Entero
	
	pass = "conquer123!"
	passwordUsuario = ""
	
	numIntentos = 0
	
	//Escribir "Define una nueva contraseña."
	//Leer pass
	
	Escribir "Introduce la contraseña."
	
	Repetir
		Escribir "Te quedan ", 3-numIntentos," intentos"
		
		numIntentos = numIntentos+1
		
		Leer passwordUsuario
	Hasta Que (numIntentos==3 O pass==passwordUsuario)
	
	//doble = para comparar
	
	//Mientras (numIntentos < 4 O pass<>passwordUsuario) Hacer 
	//	Escribir "Te quedan ", 3-numIntentos," intentos" 
	//	numIntentos = numIntentos+1
	//	Leer passwordUsuario
	//FinMientras
	
	
	Si pass = passwordUsuario Entonces
		Escribir "Contraseña correcta"
	SiNo
		Escribir "Contraseña bloqueada"
	FinSi
	
FinAlgoritmo
