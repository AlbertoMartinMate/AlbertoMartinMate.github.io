//Pedir un n�mero (entero) y calcular qu� n�meros desde el 1 hasta el propio n�mero
//son m�ltiplos de 2 y 3.
//Recordatorio: un n�mero es m�lplo de 2 si al dividir por 2, el resto es 0; y es m�lplo
//de 3 si al dividir por 3, el resto es 0
//Ejemplo: dado el n�mero 15, los n�meros m�lplos de 2 y 3 hasta 15 son 6 y 12 (resto
//0 en ambas divisiones)

Algoritmo MultiplosDe2y3
	Definir num, i Como Entero
	//Definir multiplos como Cadena
	
	num = 0
	i = 0
	//multiplos = ""
	
	Escribir "Dame un numero"
	Leer num
	
	Para i = 1 Hasta num Con Paso 1 Hacer
		Si i MOD 2 = 0 Y i MOD 3 = 0 Entonces
			Escribir "El numero ", i " es multiplo de 2 y 3"
			//multiplos = Concatenar(Concatenar(multiplos, " "), ConvertirATexto(i))
		FinSi
	FinPara
	
	//Escribir "los multiplos de 2 y 3 son: ", multiplos
FinAlgoritmo
