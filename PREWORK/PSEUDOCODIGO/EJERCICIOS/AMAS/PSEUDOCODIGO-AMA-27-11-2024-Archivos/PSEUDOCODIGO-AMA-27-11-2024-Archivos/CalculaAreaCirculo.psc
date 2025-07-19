
Funcion resultado = AreaCirculo(radio)
	Definir resultado Como Real
	resultado = PI * (radio^2) 
FinFuncion

Algoritmo CalculaAreaCirculo
	Definir r, area Como Real
	
	r = 0
	area = 0
	
	Escribir "Dame el radio y calculo el area de tu circulo"
	Leer r
	
	area = AreaCirculo(r)
	
	Escribir "El area de tu circulo es: ", area
	
FinAlgoritmo
