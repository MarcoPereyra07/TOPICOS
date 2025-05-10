import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Crear ventana
ventana = tk.Tk()
ventana.title("Empleados")
ventana.geometry("640x480")

# Conexión a MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Cambiar por tu usuario de MySQL
        password="07032005Ma",  # Cambiar por tu contraseña de MySQL
        database="extra"  # Cambiar por el nombre de tu base de datos
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a MySQL: {err}")
    ventana.destroy()

# Funciones CRUD corregidas
def guardar_empleado():
    id_empleado = txtId.get()
    nombre = txtNombre.get()
    usuario = txtUsuario.get()
    contrasena = txtContraseña.get()  # Nota: el widget puede mantener el nombre con ñ
    
    if id_empleado and nombre and usuario and contrasena:
        try:
            # Cambiado "contraseña" por "contrasena" para coincidir con la BD
            cursor.execute("INSERT INTO Empleados (id_empleado, nombre, usuario, contrasena) VALUES (%s, %s, %s, %s)",
                         (id_empleado, nombre, usuario, contrasena))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado guardado correctamente.")
            limpiar_campos()
            mostrar_empleados()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar empleado: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")


def eliminar_empleado():
    seleccionado = tree.selection()
    if seleccionado:
        id_empleado = tree.item(seleccionado[0], "values")[0]
        try:
            cursor.execute("DELETE FROM Empleados WHERE id_empleado = %s", (id_empleado,))
            conn.commit()
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            mostrar_empleados()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar empleado: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar.")


def actualizar_empleado():
    seleccionado = tree.selection()
    if seleccionado:
        id_empleado = tree.item(seleccionado[0], "values")[0]
        nombre = txtNombre.get()
        usuario = txtUsuario.get()
        contrasena = txtContraseña.get()
        if nombre and usuario and contrasena:
            try:
                # Cambiado "contraseña" por "contrasena"
                cursor.execute("UPDATE Empleados SET nombre = %s, usuario = %s, contrasena = %s WHERE id_empleado = %s",
                             (nombre, usuario, contrasena, id_empleado))
                conn.commit()
                messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
                limpiar_campos()
                mostrar_empleados()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar empleado: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un empleado para actualizar.")


def mostrar_empleados():
    try:
        # Cambiado para usar "contrasena" en lugar de "*"
        cursor.execute("SELECT id_empleado, nombre, usuario, contrasena FROM Empleados")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar empleados: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtNombre.delete(0, tk.END)
    txtUsuario.delete(0, tk.END)
    txtContraseña.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="EMPLEADOS")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_EMPLEADO")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblNombre = tk.Label(ventana, text="NOMBRE")
lblNombre.place(x=20, y=90, width=100, height=20)
txtNombre = tk.Entry(ventana, bg="#f4a261")
txtNombre.place(x=150, y=90, width=200, height=20)

lblUsuario = tk.Label(ventana, text="USUARIO")
lblUsuario.place(x=20, y=130, width=100, height=20)
txtUsuario = tk.Entry(ventana, bg="#2a9d8f")
txtUsuario.place(x=150, y=130, width=200, height=20)

lblContraseña = tk.Label(ventana, text="CONTRASEÑA")
lblContraseña.place(x=20, y=170, width=100, height=20)
txtContraseña = tk.Entry(ventana, bg="#e76f51", show="*")
txtContraseña.place(x=150, y=170, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_empleado)
btnGuardar.place(x=20, y=210, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_empleado)
btnEliminar.place(x=150, y=210, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_empleado)
btnActualizar.place(x=280, y=210, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=210, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_empleados)
btnMostrar.place(x=540, y=210, width=100, height=30)

# Configuración del Treeview (puedes mantener los nombres de columnas visuales con ñ)
tree = ttk.Treeview(ventana, columns=("id_empleado", "nombre", "usuario", "contrasena"), show="headings")
tree.heading("id_empleado", text="ID_EMPLEADO")
tree.heading("nombre", text="NOMBRE")
tree.heading("usuario", text="USUARIO")
tree.heading("contrasena", text="CONTRASEÑA")  # Visualización con ñ está bien
tree.column("id_empleado", width=100)
tree.column("nombre", width=150)
tree.column("usuario", width=150)
tree.column("contrasena", width=150)
tree.place(x=20, y=260, width=600, height=200)

# Cerrar conexión al salir
def on_closing():
    if 'conn' in globals() and conn.is_connected():
        cursor.close()
        conn.close()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.mainloop()