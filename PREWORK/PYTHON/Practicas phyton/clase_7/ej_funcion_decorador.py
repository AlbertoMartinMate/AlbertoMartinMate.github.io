def mi_decorador(func):
    def nueva_funcion(*args, **kwargs):
        print("Antes de ejecutar el codigo")
        resultado=func(*args, **kwargs)
        print("Despues de ejecutar el codigo")
        return resultado
    return nueva_funcion

@mi_decorador

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")
saludar("Luis", saludo="Buenas")