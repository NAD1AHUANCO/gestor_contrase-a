
#IMPORTAMOS LIBRERIAS
import random
import string #str

import tkinter as tk
from tkinter import messagebox
import re # Importamos la librería re para usar expresiones regulares

#IMPORTAR CLASES
import datosprivados
import usuario

#importamos el conector
import conector
import datosprivados

class Usuario:
    def __init__(self, nombre=None, apellido=None, dni=None, contrasena=None):
        #Inicializa la clase Usuario con los datos básicos y la contraseña maestra.
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni if dni is not None else "" # Asegura que self.dni no sea None 
        self.contrasena = contrasena if contrasena is not None else "" # Asegura que self.contrasena no sea None
        # self.contrasenas = {}  # Diccionario para almacenar contraseñas
        # self.carpetas = {}  # Diccionario para organizar contraseñas por carpetas
        print(f"Usuario creado con DNI: {self.dni}, Contraseña: {self.contrasena}") # Impresión de depuración
    
    ###################### VALIDACIONES DE LOGUEO ######################
    def validar_entrada(self):
        print(f"Validando entrada con DNI: {self.dni}, Contraseña: {self.contrasena}") # Impresión de depuración
        #Valida las entradas de usuario y contraseña.
        print("El contenido de dni es: ", self.dni)
        #if not self.dni:
        #    print("entrada1")
        #    messagebox.showerror("Error", "El campo de usuario no puede estar vacío o contener números")  # Verifica que el campo de usuario no esté vacío
        #    print("entrada2")
        #    return False
        print("entrada3")
        if not re.fullmatch(r'\d{8}', self.dni): 
            print("entrada4")
            messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos") # Verifica que el DNI tenga exactamente 8 dígitos 
            print("entrada5")
            return False
        print("entrada6")
        if not self.contrasena:
            print("entrada7")
            messagebox.showerror("Error", "El campo de contraseña no puede estar vacío")  # Verifica que el campo de contraseña no esté vacío
            print("entrada8")
            return False
        print("entrada9")
        if len(self.contrasena) < 6:
            print("entrada10")
            messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres")  # Verifica que la contraseña tenga al menos 6 caracteres
            print("entrada11")
            return False
        print("entrada12")
        return True  # Si todas las validaciones pasan, retorna True

    def autenticar(self, usuarios_registrados):
        """
        Autentica el usuario contra un diccionario de usuarios registrados.
        """
        if self.dni in usuarios_registrados and usuarios_registrados[self.dni] == self.contrasena:
            return True  # Retorna True si el usuario y la contraseña coinciden
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")  # Muestra un error si las credenciales no coinciden
            return False


    #CREAMOS LA BASE DE DATOS: inserta los datos privados y los datos del usuario en la base de datos
    def crear_usuario(self): #datos: datosprivados.DatosPrivados que tipo de datos estamos recibiendo
        con=conector.DataBase().conectar() #me conecto a la base de datos
        cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
        try:
            query_usuario="""INSERT INTO usuario (nombre, apellido, dni, contraseña) 
            values (?,?,?,?)"""
            cursor.execute(query_usuario, (self.nombre, self.apellido, self.dni, self.contrasena))
            con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
            return True
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(f'error, {error}')
            return False


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
            con.close()
            return user
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(error)
            return None
        

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