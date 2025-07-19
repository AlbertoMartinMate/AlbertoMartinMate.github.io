Algoritmo TiendaRopa
	
	//Rebajas en tienda de ropa. Si compramos una prenda desc. 15%, 3, 25% , +de 3, 20% y nos regalan una prenda
	//precio prenda es de 10 ?
	//pedir cuantas prendas queremos comprar
	//calcular precio
	//calcular el numero de prendas total que nos llevamos
	
	Definir prendasCompradas Como Entero
	Definir precioPrenda, precioTotal Como Real
	
	prendasCompradas = 0
	precioPrenda = 10
	precioTotal = 0
	
	
	Escribir "¿Cuantas prendas has comprado?"
	Leer prendasCompradas
	
	Si prendasCompradas = 0 Entonces
		Escribir " El precio a pagar es de 0, ya que no has comprado nada"
		Escribir  "Total de prendas compradas es igual 0" 
		
	Sino 
		Si prendasCompradas <= 2  Entonces
			Escribir "El precio a pagar es: " precioPrenda * prendasCompradas * 0.85
			Escribir "Total de prendas compradas es: " prendasCompradas
			
		SiNo
			Si prendasCompradas = 3 Entonces
				Escribir "El precio a pagar es: " precioPrenda * prendasCompradas * 0.75
				Escribir "Total de prendas compradas es: " prendasCompradas
				
			SiNo
				
				Si prendasCompradas >= 3 Entonces
					Escribir "El precio a pagar es: " precioPrenda * prendasCompradas * 0.8
					Escribir "Total de prendas compradas es: " prendasCompradas + 1
				FinSi
				
			FinSi
		FinSi
	FinSi
	
	
	
FinAlgoritmo
