Algoritmo MenorMayor10fin0
	
	//Enunciado : Pedir un número por consola (entero) y decir si es menor, igual o mayor a 10. 
	//Hacer que el programa continúe pidiendo un número hasta que introduzcamos el 0, y entonces, terminará.
    //Ejemplo:
    //1) Introduce número: 23
	 //2) 23 es mayor que 10
      //1) Introduce número: 10
	   //2) 10 es igual a 10
       //1) Introduce número: 2
	//2) 2 es menor que 10
      //1) Introduce número: 0
	   //2) 0 es menor que 10
	//3) Adios!
	
	//1.- definimos e inicializamos
	
	Definir num Como Entero
	
	num = 0
	
	Escribir "Introduce un número "
	Leer num
	
	//2.- Comenzamos estructura. Pedimos número, porque sino el resultado seria infinito
	
	Mientras no num=0 Hacer
		
		Si num>10 Entonces
			Escribir " " num " es mayor que 10 "
			
			Escribir "Introduce un número "
			Leer num
			
		SiNo
			
			Si num<10 Entonces
				Escribir  " " num " es menor que 10 "
				
				Escribir "Introduce un número "
				Leer num
			SiNo
				
				Si num = 10 Entonces
					
					Escribir " " num " es igual a 10 "
					Escribir "Introduce un número "
					Leer num
					
				FinSi
				
			FinSi
		FinSi
		
		
		
		
	FinMientras 
	
	Escribir "0 es menor que 10" 
	Escribir "Adios!"
	             
	

	
	
FinAlgoritmo
