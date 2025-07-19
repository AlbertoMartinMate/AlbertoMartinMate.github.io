file_name = "/home/alberto/MASTER EN DESARROLLO WEB FULL STACK/PREWORK/PYTHON/Practicas phyton/clase_8/pruebas_archivos.txt"
f = open(file_name, "w+")
f.write("Comenzamos...")


f=open(file_name)
contenido=f.read()
print(contenido)