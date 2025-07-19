Algoritmo Sorteo
	
	// Enunciado Par cipación en un sorteo. Para participar en un sorteo, tienes q cumplir los siguientes requisitos: 
    //tener más de 1000 seguidores, seguir a la cuenta "sorteo_conquer_blocks" y residir en Francia, Alemania o Italia. 
	//Pedir, como datos, el número de seguidores que tienes (entero) ,si sigues la cuenta "sorteo_conquer_blocks" (lógico) y el país de residencia (texto),
	// y devolver si puedes participar en el sorteo o no (texto)
	
	//1.- Definimos e inicializamos
	
	Definir seguidores Como Entero
	Definir cuentaConquer Como Logico
	Definir paisResidencia, participacionSorteo como texto
	
	seguidores = 0
	cuentaConquer = Verdadero
	paisResidencia = "si"
	participacionsorteo= "si"
	
	//2.- pedimos los datos
	
	Escribir "Número de seguidores en Instagram"
	Leer seguidores
	
	Escribir "¿Sigues la cuenta en Instagram de sorteo_conquer_blocks? Verdadero o Falso"
	Leer cuentaConquer
	
	Escribir "¿Reside en Francia, Alemania o Italia? Si/No"
	Leer paisResidencia
	
	
	//3.- pasamos a calcular las variables, teniendo q darse las tres variables. Con el comando "Y" / SiNo. y  ha devolver si puede partcipar en el sorteo
	
	Si (seguidores >1000) y (cuentaConquer = Verdadero) y (paisResidencia = "si") Entonces
		Escribir "Eres apto para participar en el sorteo"
		
	Sino 
		Escribir "No eres apto para participar en el sorteo"
		
	FinSi
	
	
FinAlgoritmo
