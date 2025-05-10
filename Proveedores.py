import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Conexión a la base de datos
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="07032005Ma",
        database="extra"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error al conectar a la base de datos: {err}")
    exit()

# Crear ventana
ventana = tk.Tk()
ventana.title("Proveedores")
ventana.geometry("640x480")

# Funciones CRUD corregidas
def guardar_proveedor():
    id_proveedor = txtId.get()
    nombre = txtNombre.get()
    telefono = txtTelefono.get()
    if id_proveedor and nombre and telefono:
        try:
            # Cambiado "Proveedores" por "proveedor" o el nombre real de tu tabla
            cursor.execute("INSERT INTO proveedor (id_proveedor, nombre, telefono) VALUES (%s, %s, %s)",
                         (id_proveedor, nombre, telefono))
            conn.commit()
            messagebox.showinfo("Éxito", "Proveedor guardado correctamente.")
            limpiar_campos()
            mostrar_proveedores()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar proveedor: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")


def eliminar_proveedor():
    seleccionado = tree.selection()
    if seleccionado:
        id_proveedor = tree.item(seleccionado[0], "values")[0]
        try:
            # Cambiado "Proveedores" por "proveedor"
            cursor.execute("DELETE FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
            conn.commit()
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
            mostrar_proveedores()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar proveedor: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un proveedor para eliminar.")


def actualizar_proveedor():
    seleccionado = tree.selection()
    if seleccionado:
        id_proveedor = tree.item(seleccionado[0], "values")[0]
        nombre = txtNombre.get()
        telefono = txtTelefono.get()
        if nombre and telefono:
            try:
                # Cambiado "Proveedores" por "proveedor"
                cursor.execute("UPDATE proveedor SET nombre = %s, telefono = %s WHERE id_proveedor = %s",
                             (nombre, telefono, id_proveedor))
                conn.commit()
                messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
                limpiar_campos()
                mostrar_proveedores()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar proveedor: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un proveedor para actualizar.")

def mostrar_proveedores():
    try:
        # Cambiado "Proveedores" por "proveedor"
        cursor.execute("SELECT * FROM proveedor")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar proveedores: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtNombre.delete(0, tk.END)
    txtTelefono.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="PROVEEDORES")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_PROVEEDOR")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblNombre = tk.Label(ventana, text="NOMBRE")
lblNombre.place(x=20, y=90, width=100, height=20)
txtNombre = tk.Entry(ventana, bg="#f4a261")
txtNombre.place(x=150, y=90, width=200, height=20)

lblTelefono = tk.Label(ventana, text="TELÉFONO")
lblTelefono.place(x=20, y=130, width=100, height=20)
txtTelefono = tk.Entry(ventana, bg="#2a9d8f")
txtTelefono.place(x=150, y=130, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_proveedor)
btnGuardar.place(x=20, y=170, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_proveedor)
btnEliminar.place(x=150, y=170, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_proveedor)
btnActualizar.place(x=280, y=170, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=170, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_proveedores)
btnMostrar.place(x=540, y=170, width=100, height=30)

# Configuración del Treeview
tree = ttk.Treeview(ventana, columns=("id_proveedor", "nombre", "telefono"), show="headings")
tree.heading("id_proveedor", text="ID_PROVEEDOR")
tree.heading("nombre", text="NOMBRE")
tree.heading("telefono", text="TELÉFONO")
tree.column("id_proveedor", width=100)
tree.column("nombre", width=200)
tree.column("telefono", width=200)
tree.place(x=20, y=220, width=600, height=240)

ventana.mainloop()