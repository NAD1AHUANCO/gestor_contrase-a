import tkinter as tk
from tkinter import messagebox

# Lista para almacenar las cuentas y contraseñas
cuentas_guardadas = []

# Función para validar si los campos están vacíos
def validar_campos(cuenta, contrasena):
    if cuenta == "" or contrasena == "":
        messagebox.showerror("Error", "Ambos campos son obligatorios")
        return False
    return True

# Función para guardar la información ingresada
def guardar_informacion():
    cuenta = entry_cuenta.get()
    contrasena = entry_contrasena.get()
    
    # Validar los campos antes de guardar
    if validar_campos(cuenta, contrasena):
        cuentas_guardadas.append((cuenta, contrasena))
        messagebox.showinfo("Éxito", "Información guardada correctamente.")
        entry_cuenta.delete(0, tk.END)  # Limpiar campo cuenta
        entry_contrasena.delete(0, tk.END)  # Limpiar campo contraseña

# Función para mostrar la información guardada
def mostrar_informacion():
    if not cuentas_guardadas:
        messagebox.showinfo("Información", "No hay datos guardados")
        return
    
    # Crear una nueva ventana para mostrar los datos
    ventana_info = tk.Toplevel(ventana_principal)
    ventana_info.title("Datos Guardados")
    
    # Crear un texto con la información de las cuentas guardadas
    datos = "\n".join([f"Cuenta: {cuenta}, Contraseña: {contrasena}" for cuenta, contrasena in cuentas_guardadas])
    label_info = tk.Label(ventana_info, text=datos, justify=tk.LEFT)
    label_info.pack(padx=10, pady=10)
    
    # Botón para cerrar la ventana de información
    boton_cerrar_info = tk.Button(ventana_info, text="Cerrar", command=ventana_info.destroy)
    boton_cerrar_info.pack(pady=5)

# Función para volver al menú principal
def volver_menu():
    ventana_formulario.destroy()

# Función para crear la ventana de formulario
def abrir_formulario():
    global ventana_formulario
    ventana_formulario = tk.Toplevel(ventana_principal)
    ventana_formulario.title("Formulario de Ingreso de Datos")
    
    # Etiquetas y campos de texto para ingresar cuenta y contraseña
    label_cuenta = tk.Label(ventana_formulario, text="Cuenta:")
    label_cuenta.pack(pady=5)
    global entry_cuenta
    entry_cuenta = tk.Entry(ventana_formulario)
    entry_cuenta.pack(pady=5)

    label_contrasena = tk.Label(ventana_formulario, text="Contraseña:")
    label_contrasena.pack(pady=5)
    global entry_contrasena
    entry_contrasena = tk.Entry(ventana_formulario, show="*")  # Mostrar asteriscos por la contraseña
    entry_contrasena.pack(pady=5)

    # Botones de acción en la ventana de formulario
    boton_guardar = tk.Button(ventana_formulario, text="Guardar Información", command=guardar_informacion)
    boton_guardar.pack(pady=5)
    
    boton_mostrar = tk.Button(ventana_formulario, text="Mostrar Información", command=mostrar_informacion)
    boton_mostrar.pack(pady=5)

    boton_volver = tk.Button(ventana_formulario, text="Volver al Menú Principal", command=volver_menu)
    boton_volver.pack(pady=5)

# Función para cerrar el programa
def cerrar_programa():
    ventana_principal.quit()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Programa Principal")

# Botones en la ventana principal
boton_ingresar_datos = tk.Button(ventana_principal, text="Ingresar Datos", command=abrir_formulario)
boton_ingresar_datos.pack(pady=20)

boton_cerrar_programa = tk.Button(ventana_principal, text="Cerrar Programa", command=cerrar_programa)
boton_cerrar_programa.pack(pady=20)

# Iniciar el bucle principal de la interfaz
ventana_principal.mainloop()
