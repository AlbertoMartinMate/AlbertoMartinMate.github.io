

"""Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo. """

#--> bucle que recorra todos los numeros del 2 al 100

for num in range(2,101):
  primo = True

  #-->para dicho num, miramos si hay alguno q sea su divisor, recorre i desde 2 hasta el numero a dividir

  for i in range(2,num):
    if num%i==0:
      primo=False
      break #podemos ponerlo o no...si lo ponemos es para q no recorra mas nums. ya q sabemos q no es primo

  #--> si hay primo..imprimimos
  if primo:

    print(num)

    #---> OTRA FORMA DE HACERLO

    """
    for num in range(2,101):
      primo=True
      i=2

      while primo==True and i<num:

        if num% i ==0:
          primo=False
         i+=1

      if primo:
        print(num)

        """