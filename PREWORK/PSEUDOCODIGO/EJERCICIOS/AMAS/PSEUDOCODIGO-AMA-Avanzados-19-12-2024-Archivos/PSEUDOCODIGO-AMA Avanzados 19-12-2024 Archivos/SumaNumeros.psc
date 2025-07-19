//Pedir dos números por consola (enteros) y sumar (entero) todos los 
//números que hay
//entre ellos.

//Ejemplo: si los números introducidos son el 4 y el 11, el resultado sería:
//5 + 6 + 7 + 8 + 9 + 10 = 45

Funcion resultado = CalculaSuma(num1, num2)
	
	Definir resultado, a, b, i Como Entero
	
	resultado = 0
	a = 0
	b = 0
	i = 0
	
	Si num1 < num2
		a = num1
		b = num2
	SiNo
		a = num2
		b = num1
	FinSi
	
	Si a <> b Entonces
		Para i = a+1 Hasta b-1 Con Paso 1 Hacer
			resultado = resultado + i
		FinPara
	FinSi

FinFuncion

Algoritmo SumaNumeros
	Definir numero1, numero2, suma Como Entero
	
	numero1 = 0
	numero2 = 0
	suma = 0
	
	Escribir "Dame un número"
	Leer numero1
	Escribir "Dame otro numero"
	Leer numero2 
	
	suma = CalculaSuma(numero1, numero2)
	
	Escribir "El resultado de la suma entre ", numero1, " y ", numero2, " es: ", suma
	
FinAlgoritmo
