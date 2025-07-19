//Pedir por pantalla un numero de tres cifras (de 100 a 999)(Entero). 
//Devolver cual es la cifra mas baja del numero introducido. Nota: 
//Hay que verificar que el numero sea de tres cifras. 
//Ejemplo: Si introducimos el numero 272, el algoritmo debe devolver : 
//"La cifra mas baja para el numero 272 es 2" Pista: Hay que utilizar el operador 
//MOD y la funcion trunc(valor). Esta funcion devuelve la parte entera de un 
//numero real (Ejemplo 23.45, devuelve 23)

// EJEMPLO: 123
// MODULO: el resto de la division entera de dos números
// TRUNCAR: quitar la parte decimal 
// Operaciones con 1 seguido de ceros
// 123/100 = 1.23 (movemos la coma hacia la izquiera tantos ceros como tenga el 1 detrás)
// 1.23 * 10 = 12.3 (movemos la coma hacia la derecha tantos ceros como tenga el 1 detrás)


Algoritmo SepararCifras
	Definir num, cifra1, cifra2, cifra3 Como Entero
	num = 0
	cifra1 = 0
	cifra2 = 0
	cifra3 = 0
	
	Repetir
		Escribir "Dame un numero de tres cifras (100-999) "
		Leer num
	Hasta Que (num >=100 Y num<= 999)
	
	//123
	
	cifra1 = trunc(num/100) //123/100 = 1.23 -> truncado = 1
	cifra2 = trunc(num/10) MOD 10 // 123 / 10 = 12.3 truncamos =>  12- 12 MOD 10 = 2 ( el resto)
	cifra3 = num MOD 10 //123 / 10 -> el resto es 3 (la parte decimal)
	
	Si cifra1 < cifra2 Y cifra1 < cifra3 Entonces
		Escribir "La cifra más pequeña es: ", cifra1
	SiNo
		Si cifra2 < cifra1 Y cifra2 < cifra3 Entonces
			Escribir "La cifra más pequeña es: ", cifra2
		SiNo
			Si cifra3 < cifra2 Y cifra3< cifra1 Entonces
				Escribir "La cifra más pequeña es: ", cifra3
			FinSi
		FinSi
	FinSi
	
	
FinAlgoritmo
