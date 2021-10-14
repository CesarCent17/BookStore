from dao.connection import *
from models.entidades import *

class Crud:

    #Objeto conexion
    def __init__(self):
        self.obj_conexion = Conexion()

    def crearUsuarios(self, tupla):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        sql = f"INSERT INTO usuario (nombre, apellido, email, usuario, contrasena) " \
                f"VALUES(%s,%s,%s,%s,%s)"
        cur.execute(sql, tupla)
        obj = Usuario(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4])
        cnn.commit()
        cur.close()
        return obj

    def autentificacionLogin(self, usuario, contrasena):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        cur.execute(f"SELECT * FROM usuario WHERE usuario = '{usuario}' and contrasena = '{contrasena}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3], datos[0][4])
        cur.close()
        return obj

    #NOMBRE DEL PROCEDIMIENTO Y VALORES
    def resultProcedimiento(self, nombre, tupla):
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        result = cur.callproc(nombre,tupla)
        cnn.commit()
        cur.close()
        return result
    def getLibro(self, autor, nombre):
        obj = None
        cnn = self.obj_conexion.conectar()
        cur = cnn.cursor()
        cur.execute(f"SELECT * FROM libro WHERE autor = '{autor}' and nombre = '{nombre}'")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Libro(datos[0][0], datos[0][1], datos[0][2])
        cur.close()
        return obj





