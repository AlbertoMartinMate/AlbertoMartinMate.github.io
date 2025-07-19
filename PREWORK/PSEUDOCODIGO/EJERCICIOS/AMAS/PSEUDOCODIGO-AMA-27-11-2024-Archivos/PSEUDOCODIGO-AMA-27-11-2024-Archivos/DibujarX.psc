//Dibuja la X del cuadrado. Pedir el tamaño del lado de un cuadrado (entero) 
//y dibujar la
//"X" de ese cuadrado mediante "*"


Algoritmo DibujarX
	Definir tam, i, j Como Entero
	Definir array como Cadena
	
	tam = 0
	i = 0 //filas
	j = 0 // columnas
	
	Escribir "Dame el tamaño y dibujo una X"
	Leer tam
	
	Dimension array[tam, tam]
	
	Para i = 0 Hasta tam-1 Con Paso 1 Hacer
		Para j = 0 Hasta tam-1 Con Paso 1 Hacer
			Si i = j O i+j = tam-1 Entonces
				array[i,j] = "*"
				
			SiNo
				array[i,j] = " "
			FinSi
			Escribir array[i,j] Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
	
FinAlgoritmo
