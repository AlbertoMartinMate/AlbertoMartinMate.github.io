#1. Crea un array con 15 números enteros aleatorios entre 1 y 100

import numpy as np

array_1= np.random.randint(1,101,15)
print(array_1)


#2. Multiplica todos los elementos del array usando un bucle y después usando un
#método de numpy. Compara los resultados

resultado=1

for n in array_1:
    resultado = resultado * n
print(resultado)

resultado_2=array_1.prod()
print(resultado_2)

#3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
array_2= np.random.random(15)

array_2decim=[f"{value:.2f}" for value in array_2] #utilizamos esta funcion de este modo para q
                                       #imprima solo dos decimales. hacierndo un for lo hace pero 
                                       #cada num en una linea..haciendolo asi como lista en otra
                                       #variable, lo imprime de seguido

print(array_2decim)


#4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
#operador y después con una función de numpy
 #(Pista: busca en google que función de numpy hace esto)

resultado_suma=array_1+array_2 #con el array_2_decim me sale error, xq es de tipo string
print(resultado_suma)
print("")

resultado_np= np.add(array_1, array_2) #si quisieramos con dos decimales y en formato lista,
                                    #tendriamos q hacer algo parecido al ejercicio anterior
print(resultado_np)
print("")

#5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
#(Pista: busca en google que función de numpy hace esto)

resultado_resta=array_1-array_2
print(resultado_resta)
print("")

resultado_resta_np=np.subtract(array_1,array_2)
print(resultado_resta_np)
print("")


#6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
#después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

resultado_multip=array_1*array_2
print(resultado_multip)
print("")

resultado_multip_np=np.multiply(array_1,array_2)
print(resultado_multip_np)
print("")


#7. Encuentra el valor más alto del primer array que has creado.

array_1_max= array_1.max()  #tb np.max()
print(array_1_max)
print("")


#8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard
#deviation) de los arrays (Nota: No nos importa el significado matemático de estos
#valores, lo importante es que encuentres que función de numpy necesitas. Puedes
#hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
#haber más resultados).
media_array_1=array_1.mean()
print("\n", media_array_1)


media_array_2=array_2.mean()
print("\n", media_array_2)


mediana_array_1=np.median(array_1)
print("\n", mediana_array_1)

mediana_array_2=np.median(array_2)
print("\n", mediana_array_2)


desviacion_array_1=np.std(array_1)
print("\n", desviacion_array_1)

desviacion_array_2=np.std(array_2)
print("\n", desviacion_array_2)
