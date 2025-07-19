# -->2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.

# creamos dos listas

lista_1=["setas", "huevos", "leche", "galletas", "pan"]
lista_2=["cerveza", "ron", "whisky", "vino"]

lista_completa= lista_1 + lista_2  #unimos las dos listas

lista_completa.sort() #ordenamos la lista de forma alfabetica

for palabra in lista_completa: #utilizamos esto para que imprima palabra a palabra cada una en una linea
  print(palabra)
