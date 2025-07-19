"""ADMINISTRACION DE PROYECTOS: Eres un gerente de proyectos y necesitas un programa para 
administrar las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, una 
descripción y un responsable asignado. Implementa un programa en Python que utilice un diccionario
 para almacenar la información de las tareas. El programa debe permitir agregar nuevas tareas, 
 asignar responsables a las tareas existentes, actualizar las descripciones de las tareas y mostrar
   la lista completa de tareas y responsables. (Pista: puedes comenzar con un diccionario vacío y 
   construir un diccionario de diccionarios)"""

#construimos un diccionario vacio

info_tareas={}

#introduccimos info al diccionario (tarea, descripcion, responsable)

info_tareas["baños"]={"responsable":"luisa", "descripcion": "urinarios y espejos"}
info_tareas["oficinas"]={"responsable":"mario", "descripcion": "mesas y suelos"}
info_tareas["jardines"]={"responsable":"pedro", "descripcion": "cesped y riego"}


#agregamos nuevas tareas. asignar responsables a las tareas existentes. actualizar descripciones.

tarea=True    #booleano para salir del bucle

while (tarea==True):
    respuesta=input("¿Quieres añadir o modificar alguna tarea? si o no: ")
    if respuesta=="si":
        nueva_tarea=input("Que tarea quieres cambiar o añadir?: ")
        nuevo_responsable=input("Quien es o va a ser el responsable?: ")
        nueva_descripcion=input("Introduce la descripcion de la actividad: ")
        
        if nueva_tarea in info_tareas:    
         info_tareas[nueva_tarea]= {"responsable": nuevo_responsable, "descripcion": nueva_descripcion}  
        else:
         info_tareas[nueva_tarea]= {"responsable": nuevo_responsable, "descripcion": nueva_descripcion}
    
        for clave, valor in info_tareas.items():    #mostar lista completa y actualizada
          print("La tarea: ", clave)
          print("Su responsables es: ", info_tareas[clave]["responsable"])
          print("y debe realizar: ", info_tareas[clave]["descripcion"])
    else:
        print("De acuerdo, si luego quisieras, reinicia el programa")  #si no hay accion salgo
        tarea=False      #y se vuelve a inicializar todo al principio

