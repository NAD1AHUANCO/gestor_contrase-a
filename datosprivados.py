
class DatosPrivados:
    def __init__(self, tipo_tarjeta, numero_tarjeta, fecha_vencimiento, codigo_seguridad, nombre_titular, nombre_tarjeta="a"):
        self.tipo_tarjeta = tipo_tarjeta
        self.nombre_tarjeta = nombre_tarjeta
        self.numero_tarjeta = numero_tarjeta
        self.fecha_vencimiento = fecha_vencimiento
        self.codigo_seguridad = codigo_seguridad
        self.nombre_titular = nombre_titular
        self.tarjetas = []

    def agregar_contrasena_tarjeta(self):
        tarjeta = {
            "tipo_tarjeta": self.tipo_tarjeta,
            "nombre_tarjeta": self.nombre_tarjeta,
            "numero_tarjeta": self.numero_tarjeta,
            "fecha_vencimiento": self.fecha_vencimiento,
            "codigo_seguridad": self.codigo_seguridad,
            "nombre_titular": self.nombre_titular
        }
        self.tarjetas.append(tarjeta)
        print("Contraseña de tarjeta agregada exitosamente.")

    def ver_contrasenas_tarjeta(self):
        if not self.tarjetas:
            print("No hay contraseñas de tarjetas guardadas.")
            return
        for tarjeta in self.tarjetas:
            print("\nTarjeta:", tarjeta)

    def buscar_contrasena_tarjeta(self, nombre_tarjeta):
        for tarjeta in self.tarjetas:
            if tarjeta["nombre_tarjeta"] == nombre_tarjeta:
                print("Contraseña encontrada:", tarjeta)
                return
        print("Tarjeta no encontrada.")

    def actualizar_contrasena_tarjeta(self, nombre_tarjeta, nueva_contrasena):
        for tarjeta in self.tarjetas:
            if tarjeta["nombre_tarjeta"] == nombre_tarjeta:
                tarjeta["numero_tarjeta"] = nueva_contrasena
                print("Contraseña actualizada.")
                return
        print("Tarjeta no encontrada.")

    def eliminar_contrasena_tarjeta(self, nombre_tarjeta):
        for tarjeta in self.tarjetas:
            if tarjeta["nombre_tarjeta"] == nombre_tarjeta:
                self.tarjetas.remove(tarjeta)
                print("Tarjeta eliminada.")
                return
        print("Tarjeta no encontrada.")


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