import tkinter as tk
from tkinter import messagebox
import conector
#import Usuario 
#IMPORTAMOS LAS CLASES
from usuario import Usuario


#INTACIAMOS LAS CLASES
#color_1=Prueba("rojo")
# Diccionario para almacenar usuarios registrados y contraseñas (solo como ejemplo)
usuarios_registrados = {}
contraseñas_guardadas = {}
carpetas = {}  # Almacenará las carpetas de credenciales

# Función para abrir una ventana de submenú  / PARA PROBAR PROGRAMA
def abrir_ventana(titulo, mensaje):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("300x150")
    label = tk.Label(ventana, text=mensaje, font=("Arial", 12))
    label.pack(pady=30)

################################################################################################
# Función para abrir el submenú 1 de Gestión de Contraseñas
def gestion_contraseñas(menu_principal):
    ventana_gestion = tk.Toplevel(root)
    ventana_gestion.title("Gestión de Contraseñas")
    ventana_gestion.geometry("400x400")
    
    label_gestion = tk.Label(ventana_gestion, text="Gestión de Contraseñas", font=("Arial", 14))
    label_gestion.pack(pady=10)
    #Intaciamos la clase
    #pedir_color=input("Ingrese el nombre de un color")
    
    #llamamos a la clase prueb
    button_agregar = tk.Button(ventana_gestion, text="1. Agregar una nueva contraseña", command=lambda: abrir_ventana("rojo"))
    button_agregar.pack(pady=5)

    button_ver = tk.Button(ventana_gestion, text="2. Ver todas las contraseñas", command=lambda: abrir_ventana("Ver Contraseñas", "Aquí puedes ver todas las contraseñas guardadas"))
    button_ver.pack(pady=5)

    button_buscar = tk.Button(ventana_gestion, text="3. Buscar una contraseña", command=lambda: abrir_ventana("Buscar Contraseña", "Aquí puedes buscar una contraseña por cuenta o categoría"))
    button_buscar.pack(pady=5)

    button_actualizar = tk.Button(ventana_gestion, text="4. Actualizar una contraseña", command=lambda: abrir_ventana("Actualizar Contraseña", "Aquí puedes actualizar una contraseña existente"))
    button_actualizar.pack(pady=5)

    button_eliminar = tk.Button(ventana_gestion, text="5. Eliminar una contraseña", command=lambda: abrir_ventana("Eliminar Contraseña", "Aquí puedes eliminar una contraseña"))
    button_eliminar.pack(pady=5)

    # Botón para volver al menú principal
    button_volver_menu = tk.Button(ventana_gestion, text="Volver al Menú Principal", command=lambda: volver_menu(menu_principal, ventana_gestion))
    button_volver_menu.pack(pady=20)

################################################################################################
# Función para abrir el submenú 2 de Organización de Credenciales
def gestion_tarjeta(menu_principal):
    ventana_organizacion = tk.Toplevel(root)
    ventana_organizacion.title("Gestión tarjetas")
    ventana_organizacion.geometry("400x400")
    
    label_organizacion = tk.Label(ventana_organizacion, text="Gestión tarjetas", font=("Arial", 14))
    label_organizacion.pack(pady=10)

    button_crear_carpeta = tk.Button(ventana_organizacion, text="1. Agregar una nueva tarjeta", command=lambda: abrir_ventana("Crear Carpeta", "Aquí puedes crear una nueva carpeta o grupo"))
    button_crear_carpeta.pack(pady=5)

    button_mover_contraseña = tk.Button(ventana_organizacion, text="2. Ver todas las tarjetas", command=lambda: abrir_ventana("Mover Contraseña", "Aquí puedes mover una contraseña a una carpeta"))
    button_mover_contraseña.pack(pady=5)

    button_ver_carpeta = tk.Button(ventana_organizacion, text="3. Buscar una tarjeta por nombre o categoría", command=lambda: abrir_ventana("Ver Carpeta", "Aquí puedes ver las contraseñas organizadas por carpeta o grupo"))
    button_ver_carpeta.pack(pady=5)

    button_eliminar_carpeta = tk.Button(ventana_organizacion, text="4. Actualizar una datos de una tarjeta existente", command=lambda: abrir_ventana("Eliminar Carpeta", "Aquí puedes eliminar una carpeta tras confirmar que no contiene contraseñas"))
    button_eliminar_carpeta.pack(pady=5)

    button_eliminar_carpeta = tk.Button(ventana_organizacion, text="5. Eliminar una tarjeta")
    button_eliminar_carpeta.pack(pady=5)

    # Botón para volver al menú principal
    button_volver_menu = tk.Button(ventana_organizacion, text="Volver al Menú Principal", command=lambda: volver_menu(menu_principal, ventana_organizacion))
    button_volver_menu.pack(pady=20)

################################################################################################
# Función para abrir el submenú 3 de Generación de Contraseñas Seguras
def organizar_contrasenas(menu_principal):
    ventana_organizacion = tk.Toplevel(root)
    ventana_organizacion.title("Organizar Contraseñas")
    ventana_organizacion.geometry("400x400")
    
    label_organizacion = tk.Label(ventana_organizacion, text="Organizar Contraseñas", font=("Arial", 14))
    label_organizacion.pack(pady=10)

    button_crear_carpeta = tk.Button(ventana_organizacion, text="1. Crear categoría de cuenta")
    button_crear_carpeta.pack(pady=5)

    button_mover_contraseña = tk.Button(ventana_organizacion, text="2. Buscar y Mover una cuenta a otra categoría", command=lambda: abrir_ventana("Mover Contraseña", "Aquí puedes mover una contraseña a una carpeta"))
    button_mover_contraseña.pack(pady=5)

    button_ver_carpeta = tk.Button(ventana_organizacion, text="3. Ver cuentas por categoría", command=lambda: abrir_ventana("Ver Carpeta", "Aquí puedes ver las contraseñas organizadas por carpeta o grupo"))
    button_ver_carpeta.pack(pady=5)

    button_ver_carpeta = tk.Button(ventana_organizacion, text="4. Eliminar una cuenta de una categoría", command=lambda: abrir_ventana("Ver Carpeta", "Aquí puedes ver las contraseñas organizadas por carpeta o grupo"))
    button_ver_carpeta.pack(pady=5)

    # Botón para volver al menú principal
    button_volver_menu = tk.Button(ventana_organizacion, text="Volver al Menú Principal", command=lambda: volver_menu(menu_principal, ventana_organizacion))
    button_volver_menu.pack(pady=20)

################################################################################################
# Función para abrir el submenú 4 de Monitoreo de Seguridad
def contrasena_segura(menu_principal):
    ventana_organizacion = tk.Toplevel(root)
    ventana_organizacion.title("Generación de Contraseña Segura")
    ventana_organizacion.geometry("400x400")
    
    label_organizacion = tk.Label(ventana_organizacion, text="Generación de Contraseña Segura", font=("Arial", 14))
    label_organizacion.pack(pady=10)

    button_crear_carpeta = tk.Button(ventana_organizacion, text="1. Generar una contraseña con requisitos específicos", command=lambda: abrir_ventana("Crear Carpeta", "Aquí puedes crear una nueva carpeta o grupo"))
    button_crear_carpeta.pack(pady=5)

    button_mover_contraseña = tk.Button(ventana_organizacion, text="2. Guardar la contraseña generada", command=lambda: abrir_ventana("Mover Contraseña", "Aquí puedes mover una contraseña a una carpeta"))
    button_mover_contraseña.pack(pady=5)

    button_mover_contraseña = tk.Button(ventana_organizacion, text="3. Eliminar contraseña y cuenta", command=lambda: abrir_ventana("Mover Contraseña", "Aquí puedes mover una contraseña a una carpeta"))
    button_mover_contraseña.pack(pady=5)

    # Botón para volver al menú principal
    button_volver_menu = tk.Button(ventana_organizacion, text="Volver al Menú Principal", command=lambda: volver_menu(menu_principal, ventana_organizacion))
    button_volver_menu.pack(pady=20)

################################################################################################
# Función para abrir el submenú 5 de Configuración
def configuracion(menu_principal):
    ventana_organizacion = tk.Toplevel(root)
    ventana_organizacion.title("Configuración")
    ventana_organizacion.geometry("400x400")
    
    label_organizacion = tk.Label(ventana_organizacion, text="Configuración", font=("Arial", 14))
    label_organizacion.pack(pady=10)

    button_crear_carpeta = tk.Button(ventana_organizacion, text="1. Cambiar contraseña maestra", command=lambda: abrir_ventana("Crear Carpeta", "Aquí puedes crear una nueva carpeta o grupo"))
    button_crear_carpeta.pack(pady=5)

    button_mover_contraseña = tk.Button(ventana_organizacion, text="2. restauración de contraseñas", command=lambda: abrir_ventana("Mover Contraseña", "Aquí puedes mover una contraseña a una carpeta"))
    button_mover_contraseña.pack(pady=5)

    # Botón para volver al menú principal
    button_volver_menu = tk.Button(ventana_organizacion, text="Volver al Menú Principal", command=lambda: volver_menu(menu_principal, ventana_organizacion))
    button_volver_menu.pack(pady=20)

# Función para cerrar el submenú y volver al menú principal
def volver_menu(menu_principal, ventana_submenu):
    ventana_submenu.destroy()  # Cierra la ventana del submenú
    menu_principal.deiconify()  # Muestra nuevamente la ventana del menú principal


################################################################################################
# Función para la ventana del MENÚ PRINCIPAL
def abrir_menu():
    menu = tk.Toplevel(root)
    menu.title("Menú Principal del Gestor de Contraseñas")
    menu.geometry("400x400")
    menu.configure(bg="#e0f7fa")
    
    label_menu = tk.Label(menu, text="Menú Principal del Gestor de Contraseñas", bg="#e0f7fa", font=("Arial", 14))
    label_menu.pack(pady=10)

    # Opción 1: Gestión de Contraseñas
    button_gestion = tk.Button(menu, text="1. Gestión de Contraseñas", command=lambda: gestion_contraseñas(menu))
    button_gestion.pack(pady=5)

    # Opción 2: Organización de Credenciales
    button_organizar = tk.Button(menu, text="2. Gestión de Tarjetas", command=lambda: gestion_tarjeta(menu))
    button_organizar.pack(pady=5)

    # Opción 3:
    button_generar = tk.Button(menu, text="3. Organizar contraseñas", command=lambda: organizar_contrasenas(menu))
    button_generar.pack(pady=5)

    ## Opción 4: Monitoreo de Seguridad
    button_seguridad = tk.Button(menu, text="4. Monitoreo de Seguridad", command=lambda: contrasena_segura(menu))
    button_seguridad.pack(pady=5)

    # Opción 5: Recuperación de Cuenta
    button_configuracion = tk.Button(menu, text="5. Configuración", command=lambda: configuracion(menu))
    button_configuracion.pack(pady=5)

    button_cerrar_sesion = tk.Button(menu, text="Cerrar sesión", command=menu.quit)
    button_cerrar_sesion.pack(pady=20)

# Función para iniciar sesión
def iniciar_sesion():
    username = entry_username.get()
    password = entry_password.get()
    
    usuario = Usuario().loguear(username, password)
    #verificación de autenticidad
    # if username in usuarios_registrados and usuarios_registrados[username] == password:
    if usuario:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
        root.withdraw()  # Oculta la ventana de login
        abrir_menu()  # Abre el menú principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para registrarse
def registrarse():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in usuarios_registrados:
        messagebox.showerror("Error", "Este usuario ya está registrado")
    else:
        usuarios_registrados[username] = password
        messagebox.showinfo("Registro", "Registro exitoso. Ahora puedes iniciar sesión.")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Login")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Etiqueta y entrada para el usuario
label_username = tk.Label(root, text="Usuario:", bg="#f0f0f0")
label_username.pack(pady=(20, 5))
entry_username = tk.Entry(root)
entry_username.pack()

# Etiqueta y entrada para la contraseña
label_password = tk.Label(root, text="Contraseña:", bg="#f0f0f0")
label_password.pack(pady=(10, 5))
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botón de inicio de sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, bg="#4CAF50", fg="white")
button_login.pack(pady=(20, 5))

# Botón de registro
button_register = tk.Button(root, text="Registrarse", command=registrarse, bg="#2196F3", fg="white")
button_register.pack(pady=(5, 20))

#IMPORTAR LA BASE DE DATOS - CONEXIÓN A LA BD
conector.DataBase().conectar()
conector.DataBase().create_if_not_exists()


# Iniciar el loop principal
root.mainloop()






