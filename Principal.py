import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# === CONEXIÓN GLOBAL A LA BASE DE DATOS ===
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

# === FUNCIONES PARA LAS VENTANAS CRUD ===
def abrir_cajas():
    import Cajas
    Cajas.mostrar_ventana(conn, cursor)

def abrir_categorias():
    import Categorias
    Categorias.mostrar_ventana(conn, cursor)

def abrir_clientes():
    import Clientes
    Clientes.mostrar_ventana(conn, cursor)

def abrir_detalle_compras():
    import Detalle_Compras
    Detalle_Compras.mostrar_ventana(conn, cursor)

def abrir_empleados():
    import Empleados
    Empleados.mostrar_ventana(conn, cursor)

def abrir_inventario():
    import Inventario
    Inventario.mostrar_ventana(conn, cursor)

def abrir_proveedores():
    import Proveedores
    Proveedores.mostrar_ventana(conn, cursor)

# === MENÚ PRINCIPAL ===
def mostrar_menu():
    root = tk.Tk()
    root.title("Menú Principal - Sistema Extra")
    root.geometry("400x500")
    root.configure(bg="#f8f9fa")

    titulo = tk.Label(root, text="Sistema Extra", font=("Arial", 20, "bold"), bg="#f8f9fa")
    titulo.pack(pady=20)

    # Botones del menú
    botones = [
        ("Cajas", abrir_cajas),
        ("Categorías", abrir_categorias),
        ("Clientes", abrir_clientes),
        ("Detalle Compras", abrir_detalle_compras),
        ("Empleados", abrir_empleados),
        ("Inventario", abrir_inventario),
        ("Proveedores", abrir_proveedores)
    ]

    for texto, comando in botones:
        btn = tk.Button(root, text=texto, width=30, height=2,
                        command=comando, bg="#457b9d", fg="white", font=("Arial", 10))
        btn.pack(pady=10)

    salir_btn = tk.Button(root, text="Salir", width=30, height=2, command=root.quit,
                          bg="#e63946", fg="white", font=("Arial", 10))
    salir_btn.pack(pady=20)

    root.mainloop()

# === MÓDULOS CRUD EXTERNOS (estructurados como módulos reutilizables) ===

# --- Ejemplo: crud_cajas.py ---
# Guarda este contenido en archivos separados como 'crud_cajas.py', 'crud_categorias.py', etc.

if __name__ == "__main__":
    mostrar_menu()