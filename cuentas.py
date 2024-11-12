import conector


class Cuentas:
    def __init__(self, id = None, tipo_cuenta = None, nombre_cuenta = None, usuario_cuenta = None, contraseña_cuenta = None):
        self.id = id
        self.tipo_cuenta = tipo_cuenta
        self.nombre_cuenta = nombre_cuenta
        self.usuario_cuenta = usuario_cuenta
        self.contraseña_cuenta = contraseña_cuenta
        

    def agregar_cuenta(self, user_id):
        con=conector.DataBase().conectar() #me conecto a la base de datos
        try:
            cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
            query_cuenta="""INSERT INTO cuentas (tipo_cuenta, nombre_cuenta, usuario_cuenta, contraseña_cuenta, id_usuario) 
            values (?,?,?,?,?)"""
            cursor.execute(query_cuenta, (self.tipo_cuenta, self.nombre_cuenta, self.usuario_cuenta, self.contraseña_cuenta, user_id))
            con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
            return True
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(f'error, {error}')
            return False
        
        
    #AGREGAR CONTRASEÑA - MENÚ 1.1
    #verifica si la cuenta ya existe, pedir confirmación antes de guardar y confirmar la acción al usuario.
    def agregar_contrasena(self):
        tipo_cuenta = input("Ingrese el tipo de cuenta (ej: email, social, bancaria): ")
        usuario_cuenta = input("Ingrese el nombre de usuario o ID de la cuenta: ")

        if usuario_cuenta in self.contrasenas:
            print("Esta cuenta ya existe. ¿Desea actualizar la contraseña en su lugar? (s/n)")
            if input().lower() != 's':
                print("No se realizó ninguna acción.")
                return

        contrasena_cuenta = input("Ingrese la contraseña para la cuenta: ")
        self.contrasenas[usuario_cuenta] = {'tipo': tipo_cuenta, 'contraseña': contrasena_cuenta}
        print("Contraseña agregada correctamente.")


    #MUESTRA LOS DATOS DE LA CUENTA - MENÚ 1.2
    #Permite que el usuario elija si desea ver todas o por categoría.
    def ver_cuentas(self, user_id):
        con=conector.DataBase().conectar() #me conecto a la base de datos
        try:
            cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
            query_cuenta="""SELECT * FROM cuentas WHERE id_usuario = (?)"""
            cursor.execute(query_cuenta, (user_id,))
            cuentas = cursor.fetchall()
            # con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
            return cuentas
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(f'error, {error}')
            return []


    #BUSCAR CONTRASEÑA - MENÚ 1.3
    #Confirma si la cuenta buscada no existe y mostrar un mensaje de error si el nombre ingresado es incorrecto.
    def ver_contrasenas(self):
        if not self.contrasenas:
            print("No tienes contraseñas guardadas.")
            return

        print("¿Deseas ver todas las contraseñas o solo de un tipo específico?")
        opcion = input("1. Todas\n2. Filtrar por tipo\nElige una opción: ")

        if opcion == '1':
            for usuario, datos in self.contrasenas.items():
                print(f"\nCuenta: {usuario}")
                print(f" - Tipo: {datos['tipo']}")
                print(f" - Contraseña: {datos['contraseña']}")
        elif opcion == '2':
            tipo_filtro = input("Ingresa el tipo de cuenta que deseas ver (ej: email, social): ")
            for usuario, datos in self.contrasenas.items():
                if datos['tipo'] == tipo_filtro:
                    print(f"\nCuenta: {usuario}")
                    print(f" - Contraseña: {datos['contraseña']}")
        else:
            print("Opción no válida.")


    #ACTUALIZAR CONTRASEÑA - MENÚ 1.4
    #Este método puede pedir al usuario que ingrese la nueva contraseña dos veces para evitar errores tipográficos.
    def actualizar_contrasena(self):
        usuario_cuenta = input("Ingrese el nombre de la cuenta cuya contraseña desea actualizar: ")
        
        if usuario_cuenta in self.contrasenas:
            nueva_contrasena = input("Ingrese la nueva contraseña: ")
            confirmacion = input("Confirme la nueva contraseña: ")
            
            if nueva_contrasena == confirmacion:
                self.contrasenas[usuario_cuenta]['contraseña'] = nueva_contrasena
                print("Contraseña actualizada correctamente.")
            else:
                print("Las contraseñas no coinciden. Intente de nuevo.")
        else:
            print("Cuenta no encontrada.")


    #ELIMINAR UNA CUENTA - MENÚ 1.5
    #Este método puede pedir confirmación antes de eliminar una cuenta para evitar que el usuario borre datos accidentalmente.
    def eliminar_cuenta(self, id):
        con=conector.DataBase().conectar() #me conecto a la base de datos
        try:
            cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
            query_cuenta="""DELETE FROM cuentas WHERE id = (?)"""
            cursor.execute(query_cuenta, (id,))
            con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
            return True
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(f'error, {error}')
            return False
        
    def editar_cuenta(self):
        con=conector.DataBase().conectar() #me conecto a la base de datos
        try:
            cursor=con.cursor() #Con el cursos realizamos los cambio en la bs
            query_cuenta="""UPDATE cuentas SET tipo_cuenta = (?), nombre_cuenta = (?), usuario_cuenta = (?), contraseña_cuenta = (?) WHERE id = (?)"""
            cursor.execute(query_cuenta, (self.tipo_cuenta, self.nombre_cuenta, self.usuario_cuenta, self.contraseña_cuenta, self.id,))
            con.commit()
            con.close() #cierro la base de datos despues de crear los objetos
            return True
        except Exception as error:
            con.close() #si hubo algun error me cierra la conección
            print(f'error, {error}')
            return False

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