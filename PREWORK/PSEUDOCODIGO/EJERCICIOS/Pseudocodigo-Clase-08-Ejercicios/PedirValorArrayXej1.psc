Algoritmo PedirValorArrayX
	
	//Crear un array de dimensión 5, inicializado con números aleatorios (función azar), del 0 al 19. 
	//Pedir por consola un valor de 0 a 4, y mostrar el número guardado en esa posición del array (entero). 
	//Escribir en consola también el array. Nota: si el número que introduce el usuario es mayor a 4, 
	//el programa debería mostrar el array y avisar del error: 
	//"La longitud del array es de 0 a 4, por lo que la posición [5] no es válida"
	
	//definimos
	
	Definir numAzar, i, num Como Entero
	Dimension numAzar[5]     //dimension de 0 a 4. sin espacios entre variable y []
	
	i= 0
	num=0
	
	//inicializamos
	
	Para i=0 Hasta 4 Con paso 1 Hacer
		
		numAzar[i] = azar(20)
		
	FinPara
	
	//pedimos el número por pantalla
	
	Escribir "Introduce un número del 0 al 4"
	Leer num
	
	 
	

		//Escribir todos los número del array
		
		
	 Para i=0 Hasta 4 Con paso 1 Hacer
		 		 
		 Escribir  numAzar[i] " " Sin Saltar
		 
	 FinPara
	 
	 Escribir "" //para q salte de linea
	 
	 Si (num>=0) y (num<5) Entonces           //hago una estrucutra si -enctonces por que si no da el numero pedido no escriba el array
		 Escribir "El número del array en la posicion : " num " es " numAzar[num]
		 

		 
	 SiNo       //cierro estructura si-entonces
		 
		 Escribir "El número dado no es correcto al no comprenderse entre el 0 y el 4"
		 
	 FinSi
	
FinAlgoritmo
