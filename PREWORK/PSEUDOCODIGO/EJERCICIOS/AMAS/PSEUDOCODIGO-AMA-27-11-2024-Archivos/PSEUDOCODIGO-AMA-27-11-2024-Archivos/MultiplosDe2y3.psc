//Pedir un número (entero) y calcular qué números desde el 1 hasta el propio número
//son múltiplos de 2 y 3.
//Recordatorio: un número es múlplo de 2 si al dividir por 2, el resto es 0; y es múlplo
//de 3 si al dividir por 3, el resto es 0
//Ejemplo: dado el número 15, los números múlplos de 2 y 3 hasta 15 son 6 y 12 (resto
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
