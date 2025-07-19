Algoritmo DibujoX
	
	//Dibuja la X del cuadrado. Pedir el tamaño del lado de un cuadrado (entero) y dibujar la "X" de ese cuadrado mediante "*"
    //Pista1: Se necesita un "Para" anidado.
     //Pista2: Se dibuja un "*" cuando:- (altura = ancho) O (lado + 1 = ancho + alto)
	 //En otro caso, se dibuja un " "
	//Nota: al Escribir, recordad que podéis añadir "Sin Saltar" para que siga escribiendo en la misma línea
	
	Definir altura, ancho, lado, alto como entero
	
	alto = 0
	ancho = 0
	lado = 0
	
	Escribir "Escribe el tamaño del lado del cuadrado, de la X a dibujar"
	
	Leer lado
	
	Para alto = 1  Hasta lado con paso 1 Hacer        // Para anidado
		
		Para ancho = 1 hasta lado con paso 1 Hacer
			
		
		Si (alto = ancho) o (lado + 1 = ancho + alto) Entonces
			
			Escribir "*" Sin Saltar // para que lo dibuje en la misma linea
			
		SiNo
			
			Escribir " " Sin Saltar //para que deje hueco en dicha linea
			
		FinSi
		
		
	FinPara
	
	 Escribir " " // salta linea y vuelve a empezar el calculo con los nuevos valores 
FinPara
	
FinAlgoritmo
