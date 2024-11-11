#conexión a la bd y al mismo tiempo corre la tabla si no esta creada
import sqlite3

#se conecta a la bd si no exite la crea
#conexion=sqlite3.connect("gestor_c")

#manejamos clase
class DataBase:
    def conectar(self):
        try:
            conexion=sqlite3.connect("gestor_c")
        except Exception:
            print("error")
        else:
            return conexion  #si no paso nada te devuelve una conexión vacia NO SE CONECTA
        
 
    def create_if_not_exists(self):
        #crear_database = "CREATE DATABASE IF NOT EXISTS %s" %'gestor_c'
        tabla_datosprivados = '''CREATE TABLE IF NOT EXISTS datosprivados (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo_tarjeta TEXT NOT NULL,
                            nombre_tarjeta TEXT NOT NULL,
                            numero_tarjeta TEXT NOT NULL,
                            fecha_vencimiento TEXT NOT NULL,
                            codigo_seguridad TEXT NOT NULL,
                            nombre_titular TEXT NOT NULL
                            )'''

        # Crear tabla usuario
        tabla_usuario = '''CREATE TABLE IF NOT EXISTS usuario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        dni TEXT UNIQUE NOT NULL,
                        logueo TEXT UNIQUE NOT NULL,
                        contraseña TEXT NOT NULL,
                        id_datosprivados INTEGER,
                        FOREIGN KEY (id_datosprivados) REFERENCES datosprivados(id)
                        )'''

        # Crear tabla cuentas
        tabla_cuentas = '''CREATE TABLE IF NOT EXISTS cuentas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo_cuenta TEXT NOT NULL,
                        usuario_cuenta TEXT NOT NULL,
                        contraseña_cuenta TEXT NOT NULL,
                        id_usuario INTEGER,
                        id_categoria INTEGER,
                        FOREIGN KEY (id_usuario) REFERENCES usuario(id),
                        FOREIGN KEY (id_categoria) REFERENCES categoria(id)
                        )'''

        # Crear tabla categoria
        tabla_categoria = '''CREATE TABLE IF NOT EXISTS categoria (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT UNIQUE
                        )'''
        
        try:
            conn= self.conectar()
            cur = conn.cursor()
            #cur.execute(crear_database)
            #cur.execute("USE %s" %'gestor_c')
            cur.execute(tabla_datosprivados)
            cur.execute(tabla_usuario)
            cur.execute(tabla_categoria)
            cur.execute(tabla_cuentas)
            #CREAR SOLO UNA SOLA VEZ LA TABLA CATEGORÍA
            try:
                cur.execute("INSERT INTO categoria (nombre) values ('todos')")
                conn.commit()
            except:
                print("La categoria ya existe")
            conn.close()
        except Exception:
            print("Error al conectar o crear la base de datos.")
            raise