# 9. Crea un arrays lleno de 1s con una longitud dada por el usuario 


import numpy as np

longitud= int(input("Introduce la longitud del array: "))

array_1= np.ones(longitud)

print(array_1)
print("")

# 10. Cambia la forma del array para que tenga una estructura de tipo ( filas, columnas) 

array_2=array_1.reshape((3,3))

print(array_2)
print("")


# 11. Crea una “matriz identidad” con la misma forma que el array anterior ( filas, columnas) 

array_matriz=np.eye(3)
print(array_matriz)

# 12. Concatena ambas estructuras horizontalmente y verticalmente 
# (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)

concatena_1=np.concatenate((array_2, array_matriz), axis=0) #concatenamos x filas (6*3) (verticalmente)
print("concatenamos")
print(concatena_1)
print("")

concatena_2=np.concatenate((array_2, array_matriz), axis=1) #concatenamos x columnas (3*6) (horizontalmente)
print(concatena_2)
print("")

array_vstack=np.vstack((array_2, array_matriz)) #igual a concatenar x fila
print(array_vstack)
print("")

array_hstack=np.hstack((array_2, array_matriz)) #igual q concatenar x columnas
print(array_hstack)
print("")