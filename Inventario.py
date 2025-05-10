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
ventana.title("Inventario")
ventana.geometry("640x480")

# Funciones CRUD
def guardar_inventario():
    id_inventario = txtId.get()
    stock_actual = txtStock.get()
    ubicacion = txtUbicacion.get()
    if id_inventario and stock_actual and ubicacion:
        try:
            cursor.execute("INSERT INTO Inventario (id_inventario, stock_actual, ubicacion) VALUES (%s, %s, %s)",
                           (id_inventario, stock_actual, ubicacion))
            conn.commit()
            messagebox.showinfo("Éxito", "Inventario guardado correctamente.")
            limpiar_campos()
            mostrar_inventario()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar inventario: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_inventario():
    seleccionado = tree.selection()
    if seleccionado:
        id_inventario = tree.item(seleccionado[0], "values")[0]
        try:
            cursor.execute("DELETE FROM Inventario WHERE id_inventario = %s", (id_inventario,))
            conn.commit()
            messagebox.showinfo("Éxito", "Inventario eliminado correctamente.")
            mostrar_inventario()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar inventario: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un inventario para eliminar.")

def actualizar_inventario():
    seleccionado = tree.selection()
    if seleccionado:
        id_inventario = tree.item(seleccionado[0], "values")[0]
        stock_actual = txtStock.get()
        ubicacion = txtUbicacion.get()
        if stock_actual and ubicacion:
            try:
                cursor.execute("UPDATE Inventario SET stock_actual = %s, ubicacion = %s WHERE id_inventario = %s",
                               (stock_actual, ubicacion, id_inventario))
                conn.commit()
                messagebox.showinfo("Éxito", "Inventario actualizado correctamente.")
                limpiar_campos()
                mostrar_inventario()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar inventario: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un inventario para actualizar.")

def mostrar_inventario():
    try:
        cursor.execute("SELECT * FROM Inventario")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar inventario: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtStock.delete(0, tk.END)
    txtUbicacion.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="INVENTARIO")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_INVENTARIO")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblStock = tk.Label(ventana, text="STOCK ACTUAL")
lblStock.place(x=20, y=90, width=100, height=20)
txtStock = tk.Entry(ventana, bg="#f4a261")
txtStock.place(x=150, y=90, width=200, height=20)

lblUbicacion = tk.Label(ventana, text="UBICACIÓN")
lblUbicacion.place(x=20, y=130, width=100, height=20)
txtUbicacion = tk.Entry(ventana, bg="#2a9d8f")
txtUbicacion.place(x=150, y=130, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_inventario)
btnGuardar.place(x=20, y=170, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_inventario)
btnEliminar.place(x=150, y=170, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_inventario)
btnActualizar.place(x=280, y=170, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=170, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_inventario)
btnMostrar.place(x=540, y=170, width=100, height=30)

# Configuración del Treeview
tree = ttk.Treeview(ventana, columns=("id_inventario", "stock_actual", "ubicacion"), show="headings")
tree.heading("id_inventario", text="ID_INVENTARIO")
tree.heading("stock_actual", text="STOCK ACTUAL")
tree.heading("ubicacion", text="UBICACIÓN")
tree.column("id_inventario", width=100)
tree.column("stock_actual", width=100)
tree.column("ubicacion", width=300)
tree.place(x=20, y=220, width=600, height=240)

ventana.mainloop()