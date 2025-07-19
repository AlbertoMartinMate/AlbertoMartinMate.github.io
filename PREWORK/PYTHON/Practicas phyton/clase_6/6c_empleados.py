"""GESTIÓN DE EMPLEADOS:
Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento."""

#inicializamos nuestra base de datos con un diccionario vacio

bbdd={}

#programa para poder ingresar: agregar empleado, actualizar salario y departamento

continuar = True


while continuar:
    opcion = input("1. Añadir empleado, salario y departamento\n2. Actualizar salario\n3.Mostrar lista completa de empleados\n4. Calcular el salario promedio del deparamento\n5. Salir\nElige una opción: ")

    # Registrar empleado
    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")

        if nombre not in bbdd: #para asegurarno que no esta registrado ya
            
            salario = int(input("Ingrese el salario del empleado: "))
            departamento=input("Introduce el departamento del empleado ")
            bbdd[nombre]=[salario,departamento] #corregio pone bbdd[nombre] ={"salario": x, "departamento":x}
            print(bbdd)
    

        else: #si esta registrado...
           print("Este usuario ya esta registrado")

    # Actualizar salario
    elif opcion == "2":
        # Ingresar el nombre del empleado al que queremos actualizar el salario
        nombre=input("Introduce el nombre al que le quieres actualizar el salario ")

        if nombre in bbdd: #nos aseguramos q esta en la bbdd

         salario = input("Ingrese el nuevo salario ")
         bbdd[nombre][0] =salario    #modificamos la posicion donde esta el salario

         print(bbdd)

        else:
            print("Este usuario no esta dado de alta")

    # Mostar el listado de empleados
    elif opcion == "3":
       
        # recorremos los valores del diccionario
        for empleado, datos in bbdd.items():
            print(empleado, ":")
            print("Salario:", datos[0], ".Departamento:", datos[1])

  
    elif opcion =="4": #calculamos salario promedio
     seccion=input("¿De que departamento quieres saber la media del salario? ")
     salario_departamento=0
     empleados_departamento=0
     for empleado, datos in bbdd.items():
            if datos[1]==seccion:
                sueldo=int(datos[0])
                salario_departamento+=sueldo
                empleados_departamento+=1

     if empleados_departamento>0:  #hacemos este if para poder impriirlo correctamente, xa q no se meta en un bucle
          media_salario=salario_departamento/empleados_departamento
          print("El salario medio del departamento", seccion, "es de:", media_salario)
     else:
          print("Introduce un departamento válido")
            

        
    # Salir del programa
    elif opcion == "5":
        print("Saliendo del programa...")
        continuar = False

    # Si el numero introducido no es 1,2,3,4 pedimos que se elija
    # una opcion valida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")