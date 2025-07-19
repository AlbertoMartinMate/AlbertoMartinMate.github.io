Funcion resultado = AreaCirculo(radio)
	Definir resultado Como Real

	resultado = PI * (radio^2)
FinFuncion

Algoritmo CalculaAreaCirculo
	Definir radioUsuario, areaUsuario Como Real
	
	radioUsuario = 0
	areaUsuario = 0
	
	Escribir "Dame el radio de tu círculo y calculo el área"
	Leer radioUsuario
	
	areaUsuario = AreaCirculo(radioUsuario)
	
	Escribir "El área de tu círculo es: ", areaUsuario
	
FinAlgoritmo
