
//Crear una calculadora con memoria que registre hasta 20 operaciones 
//realizadas en orden cronológico.
//Las operaciones que puede hacer la calculadora son "suma", "resta", 
//"multiplicación" y "división"
//El registro de memoria es una tabla con 4 columnas: 
//(1) idOperacion ? números correlativos; 
//(2) fechaOperacion; 
//(3) tipoOperacion - Suma/Resta/Multiplicacion/Division; 
//(4) valorOperacion - resultado obtenido

Funcion resultado = Calcular(operacion, a, b)
	Definir resultado Como Real
	resultado = 0
	
	Si operacion = 1 Entonces
		resultado = a + b
	SiNo
		Si operacion = 2 Entonces
			resultado = a - b
		SiNo
			Si operacion = 3 Entonces
				resultado  = a * b
			SiNo
				Si operacion = 4 Entonces
					resultado = a / b
				FinSi
			FinSi
		FinSi
	FinSi
	
	Escribir "El  resultado es: ", resultado
FinFuncion

Funcion BorrarPosicion(memoria, fila)
	
FinFuncion


Algoritmo CalculadoraInfinita
	Definir memoria como Cadena
	Definir operacion, i, j Como Entero
	Definir num1, num2, resultado Como Real
	Definir seguir como Cadena
	
	Dimension memoria[4, 5]
	
	operacion = 0
	num1 = 0
	num2 = 0
	resultado = 0
	i = 0
	j = 0
	seguir = ""

	Repetir
		Escribir "OPERACIÓN NÚMERO: ", i+1
		
		Repetir
			Escribir "Elige una operacion: suma(1)|resta(2)|multiplicación(3)|división(4)"
			Leer operacion
		Hasta Que (operacion>=1 Y operacion<=4)
		
		Escribir "Dame el primer número"
		Leer num1
		
		Escribir "Dame el segundo número"
		Leer num2
		
		resultado = Calcular(operacion, num1, num2)
		
		memoria[i, 0] = ConvertirATexto(i)
		memoria[i, 1] = "12-12-24"
		
		Segun operacion
			1: memoria[i, 2] = "suma"
			2: memoria[i, 2] = "resta"
			3: memoria[i, 2] = "multiplicación"
			4: memoria[i, 2] = "división"
		FinSegun
		
		memoria[i,3] = Concatenar(Concatenar(ConvertirATexto(num1), " , "), ConvertirATexto(num2))
		
		memoria[i, 4] = ConvertirATexto(resultado)
		
		i = i +1
		
		Si i = 4 Entonces
			i = 0
		FinSi
		
		Escribir "¿quieres seguir operando? (si|no)"
		Leer seguir
		
	Hasta Que seguir = "no"
	
	
	Para i = 0 Hasta 3 Con Paso 1 Hacer
		Para j = 0 Hasta 4 Con Paso 1 Hacer
			Escribir  memoria[i,j], "        " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
	
	
FinAlgoritmo
