import tkinter as tk
from tkinter import messagebox
import re

#IMPORTAR CLASES
import datosprivados
import usuario


###################### FORMULARIO ######################
#Validaciones de Texto
def es_texto_valido(texto):
    """Verifica si el texto contiene solo letras."""
    return texto.isalpha()


def texto_valido(texto):
    """Verifica si el texto contiene solo letras y espacios."""
    return all(char.isalpha() or char.isspace() for char in texto)

# Función para mostrar los datos registrados en una nueva ventana
def mostrar_datos(nombre, apellido, dni, tipo_tarjeta, numero_tarjeta, fecha_vencimiento, codigo_seguridad, nombre_titular):
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Registrados")
    ventana_datos.geometry("600x600") #tamaño de la ventana

    tk.Label(ventana_datos, text=f"Nombre: {nombre}").pack()
    tk.Label(ventana_datos, text=f"Apellido: {apellido}").pack()
    tk.Label(ventana_datos, text=f"DNI: {dni}").pack()
    tk.Label(ventana_datos, text=f"Tipo de Tarjeta: {tipo_tarjeta}").pack()
    tk.Label(ventana_datos, text=f"Número de Tarjeta: {numero_tarjeta}").pack()
    tk.Label(ventana_datos, text=f"Fecha de Vencimiento: {fecha_vencimiento}").pack()
    tk.Label(ventana_datos, text=f"Código de Seguridad: {codigo_seguridad}").pack()
    tk.Label(ventana_datos, text=f"Nombre del Titular: {nombre_titular}").pack()

################### REGISTRO - FORMULARIO DE DATOS ###################
# Función para procesar y validar los datos ingresados
def registrar_datos():
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    dni = entry_dni.get().strip()
    contraseña = entry_contraseña.get().strip()
    tipo_tarjeta = tipo_tarjeta_var.get().strip()
    numero_tarjeta = entry_numero_tarjeta.get().strip()
    fecha_vencimiento = entry_fecha_vencimiento.get().strip()
    codigo_seguridad = entry_codigo_seguridad.get().strip()
    nombre_titular = entry_nombre_titular.get().strip()

    # Validaciones
    if not es_texto_valido(nombre):
        messagebox.showerror("Error", "El nombre debe contener solo letras.")
        return
    if not es_texto_valido(apellido):
        messagebox.showerror("Error", "El apellido debe contener solo letras.")
        return
    if not es_texto_valido(tipo_tarjeta):
        messagebox.showerror("Error", "El tipo de tarjeta debe contener solo letras.")
        return
    if not texto_valido(nombre_titular):
        messagebox.showerror("Error", "El nombre del titular debe contener solo letras.")
        return
    if not nombre or not apellido or not dni or not contraseña:
        messagebox.showwarning("Error", "Nombre, Apellido, DNI y Contraseña son obligatorios.")
        return

    if not re.match(r'^\d{7,8}$', dni):
        messagebox.showwarning("Error", "DNI debe tener entre 7 y 8 dígitos.")
        return

    if not re.match(r'^\d{16}$', numero_tarjeta):
        messagebox.showwarning("Error", "El número de tarjeta debe tener 16 dígitos.")
        return

    if not re.match(r'^\d{2}/\d{2}$', fecha_vencimiento):
        messagebox.showwarning("Error", "Fecha de vencimiento debe ser en formato MM/AA.")
        return

    if not re.match(r'^\d{3}$', codigo_seguridad):
        messagebox.showwarning("Error", "Código de seguridad debe tener 3 dígitos.")
        return

    #IMPO
    user = usuario.Usuario(nombre, apellido, dni, contraseña)
    data = datosprivados.DatosPrivados(tipo_tarjeta, numero_tarjeta, fecha_vencimiento, codigo_seguridad, nombre_titular)
    usuario.Usuario().crear_usuario(user, data)

    # Mostrar los datos en una nueva ventana
    mostrar_datos(nombre, apellido, dni, tipo_tarjeta, numero_tarjeta, fecha_vencimiento, codigo_seguridad, nombre_titular)

    # Mensaje de confirmación
    messagebox.showinfo("Registro Exitoso", "Los datos han sido registrados exitosamente.")


# Función para cerrar sesión y finalizar el programa
def cerrar_sesion():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
    tipo_tarjeta_var.delete(0, tk.END)
    entry_numero_tarjeta.delete(0, tk.END)
    entry_fecha_vencimiento.delete(0, tk.END)
    entry_codigo_seguridad.delete(0, tk.END)
    entry_nombre_titular.delete(0, tk.END)
    
    messagebox.showinfo("Cerrar Sesión", "Has cerrado sesión exitosamente. \nFin del programa.")
    ventana.destroy()  # Cierra la ventana principal

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Datos")
ventana.geometry("600x600") #tamaño de la ventana

####### CENTRAR VENTANA ####### 
# Obtener el tamaño de la pantalla
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()

# Obtener el tamaño de la ventana
ventana_ancho = 600  # Ancho de la ventana
ventana_alto = 600   # Alto de la ventana

# Calcular la posición para centrar la ventana
posicion_x = (pantalla_ancho - ventana_ancho) // 2
posicion_y = (pantalla_alto - ventana_alto) // 2

# Establecer la posición de la ventana
ventana.geometry(f"{ventana_ancho}x{ventana_alto}+{posicion_x}+{posicion_y}")

####### Etiquetas y campos de entrada para cada dato ####### 
#CAMPO NOMBRE
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

#CAMPO APELLIDO
tk.Label(ventana, text="Apellido:").pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

#CAMPO DNI
tk.Label(ventana, text="DNI:").pack()
entry_dni = tk.Entry(ventana)
entry_dni.pack()

#CAMPO CONTRASEÑA
tk.Label(ventana, text="Contraseña:").pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

#CAMPO TIPO DE TARJETA
# Menú desplegable para Tipo de Tarjeta
tk.Label(ventana, text="Tipo de Tarjeta:").pack()
tipo_tarjeta_var = tk.StringVar(value="Crédito")  # Valor por defecto es "Crédito"
tipo_tarjeta_menu = tk.OptionMenu(ventana, tipo_tarjeta_var, "Crédito", "Débito")
tipo_tarjeta_menu.pack()

#CAMPO NÚMERO DE TARJETA
tk.Label(ventana, text="Número de Tarjeta:").pack()
entry_numero_tarjeta = tk.Entry(ventana)
entry_numero_tarjeta.pack()

#CAMPO FECHA DE VENCIMIENTO
tk.Label(ventana, text="Fecha de Vencimiento (MM/AA):").pack()
entry_fecha_vencimiento = tk.Entry(ventana)
entry_fecha_vencimiento.pack()

#CAMPO CÓDIGO DE SEGURIDAD
tk.Label(ventana, text="Código de Seguridad:").pack()
entry_codigo_seguridad = tk.Entry(ventana)
entry_codigo_seguridad.pack()

#CAMPO NOMBRE DEL TITULAR
tk.Label(ventana, text="Nombre del Titular:").pack()
entry_nombre_titular = tk.Entry(ventana)
entry_nombre_titular.pack()

# Botones de registro y cerrar sesión
boton_registrar = tk.Button(ventana, text="Registrar", command=registrar_datos)
boton_registrar.pack(pady=20)

boton_cerrar_sesion = tk.Button(ventana, text="Cerrar Sesión", command=cerrar_sesion)
boton_cerrar_sesion.pack(pady=10)

# Ejecuta la ventana principal
ventana.mainloop()
###################### FIN FORMULARIO ######################