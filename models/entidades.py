class Usuario:
    def __init__(self, nombre, apellido, email, usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.usuario = usuario
        self.contrasena = contrasena

class Libro:
    def __init__(self, autor,nombre,precio):
        self.autor = autor
        self.nombre = nombre
        self.precio = precio