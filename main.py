import tkinter as tk
from tkinter import messagebox
import conector
import re
#IMPORTAMOS LAS CLASES
from usuario import Usuario
# Diccionario de usuarios registrados (para pruebas, puedes cambiar esto a una base de datos) 
usuarios_registrados = {}

#IMPORTAR CLASES
import datosprivados
import usuario

#INTACIAMOS LAS CLASES
#color_1=Prueba("rojo")
# Diccionario para almacenar usuarios registrados y contraseñas (solo como ejemplo)
usuarios_registrados = {}
contraseñas_guardadas = {}
carpetas = {}  # Almacenará las carpetas de credenciales

################################################################################################
# Función para abrir una ventana de submenú  / PARA PROBAR PROGRAMA
def abrir_ventana(titulo, mensaje):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry("300x150")
    label = tk.Label(ventana, text=mensaje, font=("Arial", 12))
    label.pack(pady=30)

# Clase base para los formularios
class FormularioBase(tk.Toplevel):
    def __init__(self, title, fields):
        super().__init__()
        self.title(title)
        self.geometry("300x400")
        self.data = []
        self.entries = {}

        # Crear los campos de entrada
        for field_name, field_type in fields.items():
            if isinstance(field_type, list):  # Si el campo es una lista, se crea un menú desplegable
                self.entries[field_name] = self.create_dropdown(field_name, field_type)
            else:  # Si no, se crea un campo de texto normal
                self.entries[field_name] = self.create_entry(field_name)

        # Botón de guardar
        tk.Button(self, text="Guardar", command=self.save_data).pack(pady=5)

    # Método para crear un campo de texto
    def create_entry(self, label_text):
        tk.Label(self, text=label_text).pack(pady=5)
        entry = tk.Entry(self)
        entry.pack(pady=5)
        return entry

    # Método para crear un menú desplegable con OptionMenu
    def create_dropdown(self, label_text, options):
        tk.Label(self, text=label_text).pack(pady=5)
        variable = tk.StringVar(self)
        variable.set(options[0])  # Opción predeterminada
        dropdown = tk.OptionMenu(self, variable, *options)
        dropdown.pack(pady=5)
        return variable  # Se guarda la variable para obtener su valor

    # Método para validar campos
    def validate_input(self, field_name, value, field_type):
        if not value:
            return False
        if field_type == int:  # Validar que sea un número entero
            if field_name == "DNI (entero)" and len(value) != 8:
                messagebox.showerror("Error", "El DNI debe tener 8 dígitos.")
                return False
            if field_name == "Código de seguridad (CVV)" and len(value) != 3:
                messagebox.showerror("Error", "El código de seguridad debe tener 3 dígitos.")
                return False
            if field_name == "Número de tarjeta (entero)" and len(value) != 16:
                messagebox.showerror("Error", "El número de tarjeta debe tener 16 dígitos.")
                return False
        else:
            #field_type == str:  # Validar que sea una cadena de texto
            if field_name == "Nombre del titular" and not re.match("^[a-zA-Z\s]+$", value):
                messagebox.showerror("Error", "El nombre del titular debe ser texto y puede incluir espacios.")
                return False
        return True

    # Método para guardar datos
    def save_data(self):
        record = {}
        for field_name, entry in self.entries.items():
            value = entry.get() if not isinstance(entry, tk.StringVar) else entry.get()
            if not self.validate_input(field_name, value, str if isinstance(entry, tk.StringVar) else int):
                return
            record[field_name] = value
        self.data.append(record)
        messagebox.showinfo("Guardado", "Los datos fueron guardados exitosamente.")
        for entry in self.entries.values():
            if isinstance(entry, tk.StringVar):  # Si es desplegable, restablece al valor predeterminado
                entry.set(entry.get())
            else:
                entry.delete(0, tk.END)
        self.withdraw()
    # Método para obtener los datos guardados
    def get_data(self):
        return self.data

# Formularios específicos
class Formulario1(FormularioBase):
    def __init__(self):
        fields = {
            "Ingrese su nombre": str,
            "Ingrese su apellido": str,
            "Ingrese su dni": int,
            "Ingrese su dni nuevamente (logueo)": str,
            "Ingrese su Ingrese su contraseña": str
        }
        super().__init__("Formulario 1", fields)

# Formulario 2 con menú desplegable para el tipo de cuenta
class Formulario2(FormularioBase):
    def __init__(self):
        fields = {
            "Tipo de cuenta": ["redes sociales", "correo electrónico", "plataformas de trabajo", "plataformas de estudio", "plataformas de entretenimiento"],
            "Nombre de cuenta": str,
            "Usuario de cuenta": str,
            "Contraseña de cuenta": str
        }
        super().__init__("Formulario 2", fields)

# Formulario 3 con campos de tarjeta
class Formulario3(FormularioBase):
    def __init__(self):
        fields = {
            "Empresa": str,
            "Tipo de tarjeta": ["Crédito", "Débito"],
            "Nombre de tarjeta": str,
            "Número de tarjeta (entero)": int,
            "Fecha de vencimiento (MM/AA)": str,
            "Código de seguridad (CVV)": int,
            "Nombre del titular": str
        }
        super().__init__("Formulario 3", fields)

# Formulario 4 para mostrar datos guardados
# Formulario 4 para mostrar los datos de los formularios
class Formulario4(tk.Toplevel):
    def __init__(self, form1_data, form2_data, form3_data):
        super().__init__()
        self.title("Formulario 4 - Mostrar Datos")
        self.geometry("500x400")

        # Crear una lista para mostrar los datos
        tk.Label(self, text="Seleccionar Formulario para Mostrar Datos").pack(pady=10)

        # Crear el menú de selección de formulario
        self.formulario_var = tk.StringVar(self)
        self.formulario_var.set("Formulario 1")  # Opción predeterminada
        tk.OptionMenu(self, self.formulario_var, "Formulario 1", "Formulario 2", "Formulario 3").pack(pady=5)

        # Botón para mostrar los datos seleccionados
        tk.Button(self, text="Mostrar Datos", command=self.show_data).pack(pady=10)

        # Área de texto para mostrar los datos
        self.text_area = tk.Text(self, height=10, width=50)
        self.text_area.pack(pady=10)

        # Guardar los datos de los formularios
        self.form1_data = form1_data
        self.form2_data = form2_data
        self.form3_data = form3_data

    def show_data(self):
        selected_form = self.formulario_var.get()

        if selected_form == "Formulario 1":
            data_to_display = self.form1_data
        elif selected_form == "Formulario 2":
            data_to_display = self.form2_data
        else:
            data_to_display = self.form3_data

        self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto
        for record in data_to_display:
            display_text = "\n".join([f"{key}: {value}" for key, value in record.items()])
            self.text_area.insert(tk.END, display_text + "\n\n")
################################################################################################
# Funciones para abrir cada formulario
def open_form1():
    global form1
    form1 = Formulario1()

def open_form2():
    global form2
    form2 = Formulario2()

def open_form3():
    global form3
    form3 = Formulario3()

def open_form4():
    forms_data = {
        "Formulario 1": form1.get_data() if form1 else [],
        "Formulario 2": form2.get_data() if form2 else [],
        "Formulario 3": form3.get_data() if form3 else []
    }
    Formulario4(forms_data)
################################################################################################
# Función para abrir el submenú 1 de Gestión de Contraseñas
def gestion_contraseñas(menu_principal):
    ventana_gestion = tk.Toplevel(root)
    ventana_gestion.title("Gestión de Contraseñas")
    ventana_gestion.geometry("400x400")
    
    label_gestion = tk.Label(ventana_gestion, text="Gestión de Contraseñas", font=("Arial", 14))
    label_gestion.pack(pady=10)

    button_agregar = tk.Button(ventana_gestion, text="1. Agregar una nueva cuenta y contraseña", command=lambda: open_form2())
    #tk.Button(root, text="Formulario 1", command=open_form1).pack(pady=10)
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
# Función para abrir el submenú 2 Gestión de tarjetas
def gestion_tarjeta(menu_principal):
    ventana_organizacion = tk.Toplevel(root)
    ventana_organizacion.title("Gestión tarjetas")
    ventana_organizacion.geometry("400x400")
    
    label_organizacion = tk.Label(ventana_organizacion, text="Gestión tarjetas", font=("Arial", 14))
    label_organizacion.pack(pady=10)

    button_crear_carpeta = tk.Button(ventana_organizacion, text="1. Agregar una nueva tarjeta", command=lambda: open_form3())
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

################################################################################################
"""
# Función para iniciar sesión
def iniciar_sesion(form):
    # Obtiene los valores de dni y contraseña del formulario
    dni = form.entries["dni"].get()  # Asumiendo que 'formulario.entries' es un diccionario con los campos
    contrasena = form.entries["contraseña"].get()
    
    # Verifica si el DNI está registrado y si la contraseña coincide
    if dni in usuarios_registrados and usuarios_registrados[dni] == contrasena:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
        root.withdraw()  # Oculta la ventana de login
        abrir_menu()  # Abre el menú principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


"""
# Función para iniciar sesión
def iniciar_sesion():
    dni = entry_dni.get()
    contrasena = entry_contrasena.get()
    
    #usuario = Usuario().loguear(dni, contrasena)
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
    dni = entry_dni.get()
    contrasena = entry_contrasena.get()
    
    if dni in usuarios_registrados:
        messagebox.showerror("Error", "Este usuario ya está registrado")
    else:
        usuarios_registrados[dni] = contrasena
        messagebox.showinfo("Registro", "Registro exitoso. Ahora puedes iniciar sesión.")
"""

# Función para registrarse
def registrarse(form):
    # Obtiene los valores de dni y contraseña del formulario 1
    dni = form.entries["dni"].get()
    contrasena = form.entries["contraseña"].get()
    
    # Verifica si el DNI ya está registrado
    if dni in usuarios_registrados:
        messagebox.showerror("Error", "Este usuario ya está registrado")
    else:
        usuarios_registrados[dni] = contrasena  # Guarda el DNI y contraseña
        messagebox.showinfo("Registro", "Registro exitoso. Ahora puedes iniciar sesión.")
        """

# Configuración de la ventana principal
root = tk.Tk()  # Crea la ventana principal de tkinter
root.title("Sistema de Login")  # Establece el título de la ventana
root.geometry("300x300")  # Establece el tamaño de la ventana
root.configure(bg="#f0f0f0")  # Establece el color de fondo de la ventana

# Etiqueta y entrada para el DNI
label_dni = tk.Label(root, text="DNI:", bg="#f0f0f0")  # Crea una etiqueta para el DNI
label_dni.pack(pady=(20, 5))  # Añade un margen vertical
entry_dni = tk.Entry(root)  # Crea un campo de entrada para el DNI
entry_dni.pack()  # Añade el campo de entrada a la ventana

# Etiqueta y entrada para la contraseña
label_contrasena = tk.Label(root, text="Contraseña:", bg="#f0f0f0")  # Crea una etiqueta para la contraseña
label_contrasena.pack(pady=(10, 5))  # Añade un margen vertical
entry_contrasena = tk.Entry(root, show="*")  # Crea un campo de entrada para la contraseña
entry_contrasena.pack()  # Añade el campo de entrada a la ventana

# Botón de inicio de sesión
button_login = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, bg="#4CAF50", fg="white")  # Crea un botón para iniciar sesión
button_login.pack(pady=(20, 5))  # Añade un margen vertical

# Botón de registro
button_register = tk.Button(root, text="Registrarse", command=open_form1, bg="#2196F3", fg="white")  # Crea un botón para registrarse en un formulario
button_register.pack(pady=(5, 20))  # Añade un margen vertical

# IMPORTAR LA BASE DE DATOS - CONEXIÓN A LA BD
conector.DataBase().conectar()
conector.DataBase().create_if_not_exists()

# Iniciar el loop principal
root.mainloop()  # Inicia el loop principal de tkinter para mostrar la ventana y esperar interacciones del usuario




