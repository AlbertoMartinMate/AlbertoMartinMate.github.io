Algoritmo DibujoX
	
	//Dibuja la X del cuadrado. Pedir el tamaño del lado de un cuadrado (entero) y dibujar la "X" de ese cuadrado mediante "*"
    //Pista1: Se necesita un "Para" anidado.
     //Pista2: Se dibuja un "*" cuando:- (altura = ancho) O (lado + 1 = ancho + alto)
	 //En otro caso, se dibuja un " "
	//Nota: al Escribir, recordad que podéis añadir "Sin Saltar" para que siga escribiendo en la misma línea
	
	Definir altura, ancho, lado, alto, array, fila, columna como entero
	
	
	lado = 0
	fila = 0
	columna= 0
	
	Escribir "Escribe el tamaño del lado del cuadrado, de la X a dibujar"
	
	Leer lado
		
	Dimension array[lado,lado]
	
		
		Para fila = 0  Hasta lado-1 con paso 1 Hacer        // Para anidado
			
			Para columna = 0 hasta lado-1 con paso 1 Hacer
			
		Si (fila = columna) o (lado-1 = fila + columna) Entonces
			
			Escribir "*" Sin Saltar // para que lo dibuje en la misma linea
			
		SiNo
			
			Escribir " " Sin Saltar //para que deje hueco en dicha linea
			
		FinSi
		
		
	FinPara
	
	 Escribir " " // salta linea y vuelve a empezar el calculo con los nuevos valores 
FinPara
	
FinAlgoritmo
