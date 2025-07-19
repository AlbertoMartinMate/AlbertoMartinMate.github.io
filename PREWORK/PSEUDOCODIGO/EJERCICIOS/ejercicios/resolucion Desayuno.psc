Algoritmo Desayuno
	
	Definir precioCafe, precioTostada, precioZumo Como Real
	Definir precioTotalDesayuno Como Real
	Definir cambioDesayuno Como Real
	Definir dinero Como Real
	precioCafe = 0
	precioTostada = 0
	precioZumo = 0
	precioTotalDesayuno = 0
	cambioDesayuno = 0
	dinero = 10
	
	Escribir "Precio Cafe"
	Leer precioCafe
	Escribir "Precio Tostada"
	Leer precioTostada
	Escribir "Precio Zumo"
	Leer precioZumo
	
	
	
	
	//1. Preguntar por el precio del café, de la tostada y del zumo de naranja
	
	
	precioTotalDesayuno = precioCafe + precioTostada + precioZumo 
	
	Escribir "Precio total del desayuno: " precioTotalDesayuno
	
	
	//2. Hacer la suma para calcular el precio total del desayuno
	
	cambioDesayuno = dinero - precioTotalDesayuno
	
	Escribir "Cambio del desayuno es: " cambioDesayuno
	
	//3. Suponiendo que tenemos solo un billete de 10 euros, calcular cuánto nos tienen que
	//devolver
	//--> PISTA: el coste total del desayuno puede ser mayor, igual o menor a 10 euros :-)
	
	
	Si cambioDesayuno >= 0 Entonces
		Escribir "Tienes dinero suficiente"
	SiNo
		Escribir "No tienes dinero suficiente"
	FinSi
	
	//4. Mostrar el precio total del desayuno y la cantidad a devolver
	
FinAlgoritmo
