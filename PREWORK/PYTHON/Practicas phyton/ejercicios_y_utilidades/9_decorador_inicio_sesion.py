"""Ejercicio: Verificación de Inicio de Sesión con Decorador
Estás desarrollando un sistema de autenticación para una aplicación web y
deseas implementar un sistema de inicio de sesión que verifique si las
credenciales proporcionadas por el usuario son válidas antes de permitir el
acceso a ciertas funciones. Además, deseas que una vez que el usuario haya
iniciado sesión correctamente, se le proporcione información personal.
Implementa lo siguiente:
1. Un registro de usuarios que contenga información adicional, como el
nombre completo y el correo electrónico.
2. Un decorador llamado verificar_inicio_sesion que acepte el nombre de
usuario y la contraseña como argumentos. Este decorador verificará si las
credenciales proporcionadas son válidas comparándolas con el registro de
usuarios. Si las credenciales son válidas, la función decorada se ejecutará y
se le pasará como argumento la información personal del usuario.
3. Una función llamada informacion_usuario que imprima la información personal
del usuario después de que haya iniciado sesión correctamente.

Implementa este sistema de inicio de sesión utilizando decoradores.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada 
- informacion_usuario("usuario1",
"contrasena123")
Salida
- Inicio de sesión exitoso para el
usuario usuario1.

* Información personal del usuario:
* Nombre completo: Juan Pérez
- Inicio de sesión fallido. Verifica tu
nombre de usuario y contraseña."""

def verificar_inicio_sesion(funcion):
    #Este decorador verificará si las credenciales proporcionadas son válidas comparándolas 
    # con el registro de usuarios.
    def wrapper(nombre_usuario,contrasena):
        nombre_usuario_lower = nombre_usuario.lower() #case sensitive
        if nombre_usuario_lower in usuarios:
            datos_usuario=usuarios[nombre_usuario_lower]
            if datos_usuario["password"] == contrasena:
                print(f"\n✅ Inicio de sesión exitoso para el usuario '{nombre_usuario}'.\n")
                return funcion(datos_usuario)
        else:
            print("\n⛔ Inicio de sesión fallido. Verifica tu nombre de usuario y contraseña.")
    return wrapper

# Función que muestra la info personal
@verificar_inicio_sesion
def informacion_usuario(info_usuario):
    print("* Información personal del usuario:")
    print(f"- Nombre completo: {info_usuario['nombre_completo']}")
    print(f"- Email: {info_usuario['email']}")


# Registro de usuarios (diccionario)
usuarios = {
    "usuario1": {
        "password": "contrasena123",
        "nombre_completo": "Juan Pérez",
        "email": "juanperez@gmail.com"
    },
    "pepito": {
        "password": "1234",
        "nombre_completo": "Pepito Grillo",
        "email": "pepitogrillo@gmail.com"
    }
}

#Ejemplo de uso
usuario1=input("Introduce tu nombre de usuario: ")
contrasenia1=input("Introduce tu contraseña: ")
informacion_usuario(usuario1, contrasenia1)

