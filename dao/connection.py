
import mysql.connector

class Conexion:
    def conectar(self):
        dic = {"host" : "127.0.0.1",
               "port":"3307",
                "user" :"root",
                "passwd" :"1234",
                "database":"bookstore"}
        conectarDB = None
        try:
            conectarDB= mysql.connector.connect(**dic)

        except(mysql.connector.DatabaseError, mysql.connector.OperationalError, mysql.connector.IntegrityError) as e:
            print("Error de conexion"+ str(e))
        return conectarDB




