Funcion resultado = AreaCirculo(radio)
	Definir resultado Como Real

	resultado = PI * (radio^2)
FinFuncion

Algoritmo CalculaAreaCirculo
	Definir radioUsuario, areaUsuario Como Real
	
	radioUsuario = 0
	areaUsuario = 0
	
	Escribir "Dame el radio de tu c�rculo y calculo el �rea"
	Leer radioUsuario
	
	areaUsuario = AreaCirculo(radioUsuario)
	
	Escribir "El �rea de tu c�rculo es: ", areaUsuario
	
FinAlgoritmo
