
Funcion resultado = Multiplos2(array, lon)
	Definir resultado Como Cadena
	Definir i Como Entero
	
	i = 0
	resultado = ""
	
	Para i = 0 Hasta lon-1 Con Paso 1 Hacer
		Si array[i] MOD 2 = 0 Entonces
			resultado = Concatenar(Concatenar(resultado , " "), ConvertirATexto(array[i]))
		FinSi
	FinPara
	
	
FinFuncion


Algoritmo Array100
	Definir num100, num, i Como Entero
	Definir multiplos como Cadena
	
	num = 0
	i = 0
	multiplos = ""
	
	Escribir "Elige la dimensión del array"
	Leer num
	
	Dimension num100[num]
	
	Para i = 0 Hasta num-1 Con Paso 1 Hacer
		num100[i] = azar(101)
		Escribir num100[i],"     " Sin Saltar
	FinPara
	
	Escribir ""
	
	multiplos = Multiplos2(num100, num)
	
	Escribir "Los multiplos de 2 son: ", multiplos
FinAlgoritmo
