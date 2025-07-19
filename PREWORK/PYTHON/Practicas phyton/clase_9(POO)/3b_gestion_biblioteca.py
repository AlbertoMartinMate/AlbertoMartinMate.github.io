"""Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario."""

class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo=titulo
        self.autor=autor
        self.ejemplares=ejemplares

class Usuario:
    def __init__(self, nombre, num_id):
        self.nombre = nombre
        self.num_id = num_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no tiene el libro '{libro}'.")

class Biblioteca:
    def __init__(self):
        self.libros = {}   # clave = título, valor = Libro
        self.usuarios = {} # clave = ID, valor = Usuario

    def agregar_libro(self, libro):
        if libro.titulo in self.libros:
            self.libros[libro.titulo].ejemplares += libro.ejemplares
        else:
            self.libros[libro.titulo] = libro

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.num_id] = usuario

    def prestar_libro(self, id_usuario, titulo_libro):
        if id_usuario in self.usuarios and titulo_libro in self.libros:
            libro = self.libros[titulo_libro]
            if libro.ejemplares > 0:
                self.usuarios[id_usuario].prestar_libro(titulo_libro)
                libro.ejemplares -= 1
                print(f"Se prestó '{titulo_libro}' a {self.usuarios[id_usuario].nombre}")
            else:
                print(f"No hay ejemplares disponibles de '{titulo_libro}'")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, titulo_libro):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if titulo_libro in usuario.libros_prestados:
                usuario.devolver_libro(titulo_libro)
                self.libros[titulo_libro].ejemplares += 1
                print(f"'{titulo_libro}' ha sido devuelto por {usuario.nombre}")
            else:
                print(f"{usuario.nombre} no tiene el libro '{titulo_libro}'")
        else:
            print("Usuario no encontrado.")

    def mostrar_inventario(self):
        print("\nInventario de la biblioteca:")
        for libro in self.libros.values():
            print(f"{libro.titulo} - {libro.autor} - {libro.ejemplares} ejemplar(es)")


#ejemplo de uso

# Crear biblioteca
biblio = Biblioteca()

# Crear libros
libro1 = Libro("1984", "George Orwell", 3)
libro2 = Libro("El Quijote", "Cervantes", 2)

# Agregar libros a la biblioteca
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)

# Crear y registrar usuarios
usuario1 = Usuario("Ana", 101)
usuario2 = Usuario("Luis", 102)
biblio.registrar_usuario(usuario1)
biblio.registrar_usuario(usuario2)

# Prestar libros
biblio.prestar_libro(101, "1984")
biblio.prestar_libro(101, "El Quijote")
biblio.prestar_libro(102, "1984")

# Mostrar inventario
biblio.mostrar_inventario()

# Devolver un libro
biblio.devolver_libro(101, "1984")

# Mostrar inventario actualizado
biblio.mostrar_inventario()
