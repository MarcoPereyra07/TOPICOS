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
ventana.title("Detalle Compras")
ventana.geometry("640x480")

def guardar_detalle_compra():
    id_detalle = txtId.get()
    id_compra = txtCompra.get()
    id_articulo = txtArticulo.get()
    cantidad = txtCantidad.get()
    precio = txtPrecio.get()
    
    if id_detalle and id_compra and id_articulo and cantidad and precio:
        try:
            cursor.execute("""
                INSERT INTO detalle_compras 
                (id_detalle, id_compra, id_articulo, cantidad, precio) 
                VALUES (%s, %s, %s, %s, %s)
            """, (id_detalle, id_compra, id_articulo, cantidad, precio))
            conn.commit()
            messagebox.showinfo("Éxito", "Detalle guardado correctamente")
            limpiar_campos()
            mostrar_detalle_compras()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar: {err}")
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

def eliminar_detalle_compra():
    seleccionado = tree.selection()
    if seleccionado:
        id_detalle = tree.item(seleccionado[0], "values")[0]
        try:
            # Cambiado el nombre de la tabla
            cursor.execute("DELETE FROM detalle_compras WHERE id_detalle = %s", (id_detalle,))
            conn.commit()
            messagebox.showinfo("Éxito", "Detalle compra eliminado correctamente.")
            mostrar_detalle_compras()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar detalle compra: {err}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un detalle compra para eliminar.")

def actualizar_detalle_compra():
    seleccionado = tree.selection()
    if seleccionado:
        id_detalle = tree.item(seleccionado[0], "values")[0]
        id_compra = txtCompra.get()
        id_articulo = txtArticulo.get()
        cantidad = txtCantidad.get()
        precio = txtPrecio.get()
        if id_compra and id_articulo and cantidad and precio:
            try:
                # Cambiado el nombre de la tabla
                cursor.execute("UPDATE detalle_compras SET id_compra = %s, id_articulo = %s, cantidad = %s, precio = %s WHERE id_detalle = %s",
                             (id_compra, id_articulo, cantidad, precio, id_detalle))
                conn.commit()
                messagebox.showinfo("Éxito", "Detalle compra actualizado correctamente.")
                limpiar_campos()
                mostrar_detalle_compras()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al actualizar detalle compra: {err}")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un detalle compra para actualizar.")

def mostrar_detalle_compras():
    try:
        # Cambiado el nombre de la tabla
        cursor.execute("SELECT * FROM detalle_compras")
        rows = cursor.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al cargar detalle compras: {err}")

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtCompra.delete(0, tk.END)
    txtArticulo.delete(0, tk.END)
    txtCantidad.delete(0, tk.END)
    txtPrecio.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="DETALLE COMPRAS")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_DETALLE")
lblId.place(x=20, y=50, width=100, height=20)
txtId = tk.Entry(ventana, bg="yellow")
txtId.place(x=150, y=50, width=200, height=20)

lblCompra = tk.Label(ventana, text="ID_COMPRA")
lblCompra.place(x=20, y=90, width=100, height=20)
txtCompra = tk.Entry(ventana, bg="#f4a261")
txtCompra.place(x=150, y=90, width=200, height=20)

lblArticulo = tk.Label(ventana, text="ID_ARTÍCULO")
lblArticulo.place(x=20, y=130, width=100, height=20)
txtArticulo = tk.Entry(ventana, bg="#2a9d8f")
txtArticulo.place(x=150, y=130, width=200, height=20)

lblCantidad = tk.Label(ventana, text="CANTIDAD")
lblCantidad.place(x=20, y=170, width=100, height=20)
txtCantidad = tk.Entry(ventana, bg="#e76f51")
txtCantidad.place(x=150, y=170, width=200, height=20)

lblPrecio = tk.Label(ventana, text="PRECIO")
lblPrecio.place(x=20, y=210, width=100, height=20)
txtPrecio = tk.Entry(ventana, bg="#e9c46a")
txtPrecio.place(x=150, y=210, width=200, height=20)

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_detalle_compra)
btnGuardar.place(x=20, y=250, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_detalle_compra)
btnEliminar.place(x=150, y=250, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_detalle_compra)
btnActualizar.place(x=280, y=250, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=250, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_detalle_compras)
btnMostrar.place(x=540, y=250, width=100, height=30)

# Configuración del Treeview
tree = ttk.Treeview(ventana, columns=("id_detalle", "id_compra", "id_articulo", "cantidad", "precio"), show="headings")
tree.heading("id_detalle", text="ID_DETALLE")
tree.heading("id_compra", text="ID_COMPRA")
tree.heading("id_articulo", text="ID_ARTÍCULO")
tree.heading("cantidad", text="CANTIDAD")
tree.heading("precio", text="PRECIO")
tree.column("id_detalle", width=100)
tree.column("id_compra", width=100)
tree.column("id_articulo", width=100)
tree.column("cantidad", width=100)
tree.column("precio", width=100)
tree.place(x=20, y=300, width=600, height=160)

ventana.mainloop()