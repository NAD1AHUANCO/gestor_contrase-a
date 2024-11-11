
# usuario.py
#IMPORTAMOS LIBRERIAS
import random
import string #str

#importamos el conector
import conector

import datosprivados

class Usuarios:
    def __init__(self, id=None, nombre=None, apellido=None, dni=None, logueo=False, contrasena=None):
        """
        Inicializa la clase Usuario con los datos básicos y la contraseña maestra.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.logueo = False  # Indica si el usuario está logueado
        self.contrasena = contrasena  # Contraseña maestra
        self.contrasenas = {}  # Diccionario para almacenar contraseñas
        self.carpetas = {}  # Diccionario para organizar contraseñas por carpetas

    #Creamos el objeto de base de datos
    def crear_usuario(self, usuario, datos): #datos: datosprivados.DatosPrivados que tipo de datos estamos recibiendo
        con=conector.DataBase().conectar() #me conecto a la base de datos
        try:
            cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
            query_datos="""INSERT INTO datosprivados (tipo_tarjeta, nombre_tarjeta, numero_tarjeta, fecha_vencimiento, codigo_seguridad, nombre_titular) values
                        (?,?,?,?,?,?)""" #instrucción para ejecución el insertar los parametros en la base de datos
            cursor.execute(query_datos, (datos.tipo_tarjeta, datos.nombre_tarjeta, datos.numero_tarjeta, datos.fecha_vencimiento, datos.codigo_seguridad, datos.nombre_titular))  #ejecutamos la sentencia creado
            con.commit() #ejecutame el guardado de la instrucción
            id_datos=cursor.lastrowid #me trae el id del objeto que acabo de crear
            query_usuario="""INSERT INTO usuario (nombre, apellido, dni, logueo, contraseña, id_datosprivados) values
                        (?,?,?,?,?,?)"""
            cursor.execute(query_usuario, (usuario.nombre, usuario.apellido, usuario.dni, usuario.logueo, usuario.contrasena, id_datos))
            con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(error)

    def loguear(self, dni, contrasena):
        """
        Permite el logueo del usuario si la contraseña ingresada es correcta.
        """
        con=conector.DataBase().conectar() 
        try:
            cursor=con.cursor() 
            query_inicio="""SELECT * FROM usuario WHERE dni= (?) AND contraseña= (?)""" 
            cursor.execute(query_inicio, (dni,contrasena)) 
            user=cursor.fetchone()
            if user:
                query_islogin="""UPDATE usuario set logueo = '1' WHERE id=(?)""" 
                cursor.execute(query_islogin, (user[0],))
                con.commit()
            con.close()
            return user
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(error)
            return

    def verificar_logueo(self):
        """
        Verifica si el usuario está logueado para permitir el acceso a las funcionalidades.
        """
        if not self.logueo:
            print("Por favor, inicia sesión para acceder a esta funcionalidad.")
        return self.logueo

    def agregar_contrasena(self, cuenta, contrasena, carpeta=None):
        """
        Agrega una nueva contraseña al usuario, con una carpeta opcional para organización.
        """
        if carpeta:
            if carpeta not in self.carpetas:
                self.carpetas[carpeta] = []
            self.carpetas[carpeta].append((cuenta, contrasena))
        else:
            self.contrasenas[cuenta] = contrasena
        print(f"Contraseña para {cuenta} agregada exitosamente.")

    def ver_contrasenas(self):
        """
        Muestra todas las contraseñas guardadas, organizadas por carpeta.
        """
        print("\nContraseñas guardadas:")
        for cuenta, contrasena in self.contrasenas.items():
            print(f"Cuenta: {cuenta}, Contraseña: {contrasena}")
        for carpeta, contras in self.carpetas.items():
            print(f"\nCarpeta: {carpeta}")
            for cuenta, contrasena in contras:
                print(f"Cuenta: {cuenta}, Contraseña: {contrasena}")

    def buscar_contrasena(self, cuenta):
        """
        Busca una contraseña específica por nombre de cuenta.
        """
        contrasena = self.contrasenas.get(cuenta)
        if contrasena:
            print(f"Contraseña para {cuenta}: {contrasena}")
        else:
            print("Cuenta no encontrada.")

    def actualizar_contrasena(self, cuenta, nueva_contrasena):
        """
        Actualiza la contraseña de una cuenta existente.
        """
        if cuenta in self.contrasenas:
            self.contrasenas[cuenta] = nueva_contrasena
            print(f"Contraseña para {cuenta} actualizada.")
        else:
            print("Cuenta no encontrada.")

    def eliminar_contrasena(self, cuenta):
        """
        Elimina una contraseña de la lista.
        """
        if cuenta in self.contrasenas:
            del self.contrasenas[cuenta]
            print(f"Contraseña para {cuenta} eliminada.")
        else:
            print("Cuenta no encontrada.")

    def crear_carpeta(self, carpeta):
        """
        Crea una nueva carpeta para organizar contraseñas.
        """
        if carpeta not in self.carpetas:
            self.carpetas[carpeta] = []
            print(f"Carpeta '{carpeta}' creada exitosamente.")
        else:
            print("La carpeta ya existe.")

    def mover_contrasena(self, cuenta, carpeta_destino):
        """
        Mueve una contraseña a una carpeta especificada.
        """
        if cuenta in self.contrasenas:
            if carpeta_destino not in self.carpetas:
                self.crear_carpeta(carpeta_destino)
            self.carpetas[carpeta_destino].append((cuenta, self.contrasenas.pop(cuenta)))
            print(f"Contraseña para {cuenta} movida a la carpeta '{carpeta_destino}'.")
        else:
            print("Cuenta no encontrada.")

    def generar_contrasena_segura(self, longitud=12):
        """
        Genera una contraseña segura de longitud especificada.
        """
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena_segura = ''.join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña generada: {contrasena_segura}")
        return contrasena_segura

    def cambiar_contrasena(self, nueva_contrasena):
        """
        Cambia la contraseña maestra del usuario.
        """
        self.contrasena = nueva_contrasena
        print("Contraseña maestra actualizada.")

    def recuperar_acceso(self, metodo, respuesta):
        """
        Permite la recuperación de la cuenta mediante un método y respuesta.
        """
        print("Método de recuperación configurado.")


################################################################################################
#CONEXIÓN CON LA BASES DE DATOS
#consulta para agregar un campo
query_receta='''INSERT INTO usuario (nombre,apellido,dni,logueo,contraseña,id_datosprivados)
                        values(%s,%s,%s,%s,%s,%s)'''
"""
cursor.execute(query_usuario,(usuario['Nombre'],usuario['Preparacion'],receta['Imagen'],receta['Tiempo_preparacion'],
                                        usuario['Tiempo_coccion'],usuario['Favorita']))  
            conn.commit() #guarda los datos
"""

#me relaciona las dos tablas
#ultimo_id = cursor.lastrowid solo para la tabla de datos personales porque ahi comienza la relacion de datos
# ultimo_id = cursor.lastrowid 