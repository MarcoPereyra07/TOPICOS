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
ventana.title("Cajas")
ventana.geometry("640x480")

# Funciones CRUD
def guardar_caja():
    id_caja = txtId.get()
    nombre = txtNombre.get()
    if id_caja and nombre:
        try:
            cursor.execute("INSERT INTO Cajas (id_caja, nombre) VALUES (%s, %s)", (id_caja, nombre))
            conn.commit()
            messagebox.showinfo("Éxito", "Caja guardada correctamente.")
            limpiar_campos()
            mostrar_cajas()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar caja: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_caja():
    seleccionado = tree.selection()
    if seleccionado:
        id_caja = tree.item(seleccionado[0], "values")[0]
        try:
            cursor.execute("DELETE FROM Cajas WHERE id_caja = %s", (id_caja,))
            conn.commit()
            messagebox.showinfo("Éxito", "Caja eliminada correctamente.")
            mostrar_cajas()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar caja: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una caja para eliminar.")

def actualizar_caja():
    seleccionado = tree.selection()
    if seleccionado:
        id_caja = tree.item(seleccionado[0], "values")[0]
        nombre = txtNombre.get()
        if nombre:
            try:
                cursor.execute("UPDATE Cajas SET nombre = %s WHERE id_caja = %s", (nombre, id_caja))
                conn.commit()
                messagebox.showinfo("Éxito", "Caja actualizada correctamente.")
                limpiar_campos()
                mostrar_cajas()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar caja: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una caja para actualizar.")

def mostrar_cajas():
    try:
        cursor.execute("SELECT * FROM Cajas")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar cajas: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtNombre.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="CAJAS")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_CAJA")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblNombre = tk.Label(ventana, text="NOMBRE")
lblNombre.place(x=20, y=90, width=100, height=20)
txtNombre = tk.Entry(ventana, bg="#f4a261")
txtNombre.place(x=150, y=90, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_caja)
btnGuardar.place(x=20, y=130, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_caja)
btnEliminar.place(x=150, y=130, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_caja)
btnActualizar.place(x=280, y=130, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=130, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_cajas)
btnMostrar.place(x=540, y=130, width=100, height=30)

# Configuración del Treeview
tree = ttk.Treeview(ventana, columns=("id_caja", "nombre"), show="headings")
tree.heading("id_caja", text="ID_CAJA")
tree.heading("nombre", text="NOMBRE")
tree.column("id_caja", width=100)
tree.column("nombre", width=500)
tree.place(x=20, y=180, width=600, height=240)

ventana.mainloop()