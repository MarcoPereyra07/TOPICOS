import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Clientes")
ventana.geometry("640x480")

# Datos temporales
datos_clientes = []

# Funciones CRUD
def guardar_cliente():
    id_cliente = txtId.get()
    nombre = txtNombre.get()
    telefono = txtTelefono.get()
    if id_cliente and nombre and telefono:
        cliente = (id_cliente, nombre, telefono)
        datos_clientes.append(cliente)
        messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
        limpiar_campos()
        mostrar_clientes()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

def eliminar_cliente():
    seleccionado = lista_clientes.curselection()
    if seleccionado:
        indice = seleccionado[0]
        datos_clientes.pop(indice)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
        mostrar_clientes()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar.")

def actualizar_cliente():
    seleccionado = lista_clientes.curselection()
    if seleccionado:
        indice = seleccionado[0]
        id_cliente = txtId.get()
        nombre = txtNombre.get()
        telefono = txtTelefono.get()
        if id_cliente and nombre and telefono:
            datos_clientes[indice] = (id_cliente, nombre, telefono)
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            limpiar_campos()
            mostrar_clientes()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
    else:
        messagebox.showwarning("Advertencia", "Seleccione un cliente para actualizar.")

def mostrar_clientes():
    lista_clientes.delete(0, tk.END)
    for cliente in datos_clientes:
        lista_clientes.insert(tk.END, cliente)

def limpiar_campos():
    txtId.delete(0, tk.END)
    txtNombre.delete(0, tk.END)
    txtTelefono.delete(0, tk.END)

# Interfaz gráfica
lblTitulo = tk.Label(ventana, text="CLIENTES")
lblTitulo.place(x=250, y=10, width=150, height=30)

lblId = tk.Label(ventana, text="ID_CLIENTE")
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

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_cliente)
btnGuardar.place(x=20, y=170, width=100, height=30)

btnEliminar = tk.Button(ventana, text="Eliminar", command=eliminar_cliente)
btnEliminar.place(x=150, y=170, width=100, height=30)

btnActualizar = tk.Button(ventana, text="Actualizar", command=actualizar_cliente)
btnActualizar.place(x=280, y=170, width=100, height=30)

btnLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
btnLimpiar.place(x=410, y=170, width=100, height=30)

btnMostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_clientes)
btnMostrar.place(x=540, y=170, width=100, height=30)

lista_clientes = tk.Listbox(ventana)
lista_clientes.place(x=20, y=220, width=600, height=240)

ventana.mainloop()