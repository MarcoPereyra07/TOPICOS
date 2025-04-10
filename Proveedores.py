import tkinter as tk
from tkinter import messagebox, ttk

# Crear ventana
ventana = tk.Tk()
ventana.title("Proveedores")
ventana.geometry("640x480")

# Datos temporales
datos_proveedores = []

# Funciones CRUD
def guardar_proveedor():
    id_proveedor = txtId.get()
    nombre = txtNombre.get()
    telefono = txtTelefono.get()
    if id_proveedor and nombre and telefono:
        proveedor = (id_proveedor, nombre, telefono)
        datos_proveedores.append(proveedor)
        messagebox.showinfo("Éxito", "Proveedor guardado correctamente.")
        limpiar_campos()
        mostrar_proveedores()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_proveedor():
    seleccionado = tree.selection()
    if seleccionado:
        indice = tree.index(seleccionado[0])
        datos_proveedores.pop(indice)
        messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
        mostrar_proveedores()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un proveedor para eliminar.")

def actualizar_proveedor():
    seleccionado = tree.selection()
    if seleccionado:
        indice = tree.index(seleccionado[0])
        id_proveedor = txtId.get()
        nombre = txtNombre.get()
        telefono = txtTelefono.get()
        if id_proveedor and nombre and telefono:
            datos_proveedores[indice] = (id_proveedor, nombre, telefono)
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
            limpiar_campos()
            mostrar_proveedores()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un proveedor para actualizar.")

def mostrar_proveedores():
    # Limpiar el Treeview antes de mostrar nuevos datos
    for item in tree.get_children():
        tree.delete(item)
    
    # Insertar datos en el Treeview
    for proveedor in datos_proveedores:
        tree.insert("", "end", values=proveedor)

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