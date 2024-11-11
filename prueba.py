import tkinter as tk
from tkinter import messagebox
import re

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

    def get_data(self):
        return self.data

# Formulario 1 con validaciones de tipo y número
class Formulario1(FormularioBase):
    def __init__(self):
        fields = {
            "Nombre": str,
            "Apellido": str,
            "DNI (entero)": int,
            "Logueo": str,
            "Contraseña": str
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

# Crear funciones para abrir cada formulario
def open_form1():
    global form1
    form1 = Formulario1()

def open_form2():
    global form2
    form2 = Formulario2()

def open_form3():
    global form3
    form3 = Formulario3()

def open_form4(form1_data, form2_data, form3_data):
    global form4
    form4 = Formulario4(form1_data, form2_data, form3_data)

# Menú principal
def main_menu():
    root = tk.Tk()
    root.title("Menú Principal")
    root.geometry("300x300")

    form1_data, form2_data, form3_data = [], [], []

    # Botones para abrir los formularios
    tk.Button(root, text="Formulario 1", command=open_form1).pack(pady=10)
    tk.Button(root, text="Formulario 2", command=open_form2).pack(pady=10)
    tk.Button(root, text="Formulario 3", command=open_form3).pack(pady=10)
    tk.Button(root, text="Formulario 4", command=lambda: open_form4(form1_data, form2_data, form3_data)).pack(pady=10)

    root.mainloop()

# Ejecutar el menú principal
if __name__ == "__main__":
    main_menu()
