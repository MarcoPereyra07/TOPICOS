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
ventana.title("Categorías")
ventana.geometry("640x480")

# Funciones CRUD
def guardar_categoria():
    id_categoria = txtId.get()
    nombre = txtNombre.get()
    descripcion = txtDescripcion.get()
    if id_categoria and nombre and descripcion:
        try:
            cursor.execute("INSERT INTO Categorias (id_categoria, nombre, descripcion) VALUES (%s, %s, %s)",
                           (id_categoria, nombre, descripcion))
            conn.commit()
            messagebox.showinfo("Éxito", "Categoría guardada correctamente.")
            limpiar_campos()
            mostrar_categorias()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar categoría: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_categoria():
    seleccionado = tree.selection()
    if seleccionado:
        id_categoria = tree.item(seleccionado[0], "values")[0]
        try:
            cursor.execute("DELETE FROM Categorias WHERE id_categoria = %s", (id_categoria,))
            conn.commit()
            messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
            mostrar_categorias()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar categoría: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una categoría para eliminar.")

def actualizar_categoria():
    seleccionado = tree.selection()
    if seleccionado:
        id_categoria = tree.item(seleccionado[0], "values")[0]
        nombre = txtNombre.get()
        descripcion = txtDescripcion.get()
        if nombre and descripcion:
            try:
                cursor.execute("UPDATE Categorias SET nombre = %s, descripcion = %s WHERE id_categoria = %s",
                               (nombre, descripcion, id_categoria))
                conn.commit()
                messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
                limpiar_campos()
                mostrar_categorias()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar categoría: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una categoría para actualizar.")

def mostrar_categorias():
    try:
        cursor.execute("SELECT * FROM Categorias")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar categorías: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtNombre.delete(0, tk.END)
    txtDescripcion.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="CATEGORÍAS")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_CATEGORÍA")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblNombre = tk.Label(ventana, text="NOMBRE")
lblNombre.place(x=20, y=90, width=100, height=20)
txtNombre = tk.Entry(ventana, bg="#f4a261")
txtNombre.place(x=150, y=90, width=200, height=20)

lblDescripcion = tk.Label(ventana, text="DESCRIPCIÓN")
lblDescripcion.place(x=20, y=130, width=100, height=20)
txtDescripcion = tk.Entry(ventana, bg="#2a9d8f")
txtDescripcion.place(x=150, y=130, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_categoria)
btnGuardar.place(x=20, y=170, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_categoria)
btnEliminar.place(x=150, y=170, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_categoria)
btnActualizar.place(x=280, y=170, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=170, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_categorias)
btnMostrar.place(x=540, y=170, width=100, height=30)

# Configuración del Treeview
tree = ttk.Treeview(ventana, columns=("id_categoria", "nombre", "descripcion"), show="headings")
tree.heading("id_categoria", text="ID_CATEGORÍA")
tree.heading("nombre", text="NOMBRE")
tree.heading("descripcion", text="DESCRIPCIÓN")
tree.column("id_categoria", width=100)
tree.column("nombre", width=200)
tree.column("descripcion", width=300)
tree.place(x=20, y=220, width=600, height=240)

ventana.mainloop()