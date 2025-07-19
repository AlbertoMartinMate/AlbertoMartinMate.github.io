"""Decorador de Control de Acceso:
Imagina que estás trabajando en el desarrollo de un sistema para una
aplicación de gestión de documentos en un entorno empresarial. Deseas
implementar un decorador llamado verificar_acceso_entorno que permita
controlar el acceso a funciones según el entorno de ejecución.
El decorador debe realizar las siguientes acciones:
1. Antes de ejecutar la función, verificar si el entorno de ejecución es
"producción".
2. Si el entorno es "producción", permitir la ejecución de la función y mostrar
un mensaje indicando que el acceso fue permitido en el entorno de
producción.
3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar
un mensaje indicando que el acceso está restringido a entornos de
producción.
Luego, aplica este decorador a dos funciones, subir_documento y
eliminar_documento . Intenta ejecutar estas funciones con diferentes entornos y
observa el comportamiento del decorador.
A continuacion un ejemplo de una posible entrada y salida de la solucion:
Entrada      
- entorno : ‘produccion’ / ‘desarrollo’
- subir_documento("Documento1")
-eliminar_documento("Documento1")
Salida
- Acceso permitido / rechazado :
- Documento subido
- Documento eliminado"""

def verificar_acceso_entorno(funcion):
#permita controlar el acceso a funciones según el entorno de ejecución.
    def wrapper(nombre_documento,entorno):
        # verificar si el entorno de ejecución es "producción"
        #Si el entorno es "producción", permitir la ejecución de la función y mostrar
        #un mensaje indicando que el acceso fue permitido en el entorno de producción.
        if entorno=="produccion":
            print("\nAcceso permitido al entorno de producción")
            return funcion(nombre_documento)
            
        else: #Si el entorno no es "producción", evitar la ejecución de la función y mostrar...
            print("\nAcceso restringido a entorno de producción.")
    return wrapper

@verificar_acceso_entorno      
def subir_documento (nombre_documento):
    print(f"Documento {nombre_documento} subido")

@verificar_acceso_entorno      
def eliminar_documento (nombre_documento):
    print(f"Documento {nombre_documento} eliminado")

# Pruebas
print("\n--- Prueba en entorno de PRODUCCIÓN ---")
subir_documento("Documento1", "produccion")
eliminar_documento("Documento1", "produccion")

print("\n--- Prueba en entorno de DESARROLLO ---")
subir_documento("Documento2", "desarrollo")
eliminar_documento("Documento2", "desarrollo")