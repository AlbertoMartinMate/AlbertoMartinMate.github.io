Algoritmo Password
	Definir pass, passwordUsuario como Cadena
	Definir numIntentos Como Entero
	
	pass = "conquer123!"
	passwordUsuario = ""
	
	numIntentos = 0
	
	//Escribir "Define una nueva contrase�a."
	//Leer pass
	
	Escribir "Introduce la contrase�a."
	
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
		Escribir "Contrase�a correcta"
	SiNo
		Escribir "Contrase�a bloqueada"
	FinSi
	
FinAlgoritmo
