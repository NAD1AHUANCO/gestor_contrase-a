class Cuentas:
    def __init__(self, tipo_cuenta, usuario_cuenta, contraseña_cuenta):
        self.tipo_cuenta = tipo_cuenta
        self.usuario_cuenta = usuario_cuenta
        self.contraseña_cuenta = contraseña_cuenta
        

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
    def eliminar_contrasena(self):
        usuario_cuenta = input("Ingrese el nombre de la cuenta que desea eliminar: ")
        
        if usuario_cuenta in self.contrasenas:
            confirmacion = input(f"¿Está seguro de que desea eliminar la contraseña para {usuario_cuenta}? (s/n): ")
            
            if confirmacion.lower() == 's':
                del self.contrasenas[usuario_cuenta]
                print(f"Contraseña para {usuario_cuenta} eliminada.")
            else:
                print("Acción cancelada.")
        else:
            print("Cuenta no encontrada.")

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