CREATE DATABASE IF NOT EXISTS extra;
USE extra;

CREATE TABLE IF NOT EXISTS Cajas (
    id_caja VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Categorias (
    id_categoria VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS Clientes (
    id_cliente VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Empleados (
    id_empleado VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Inventario (
    id_inventario VARCHAR(50) PRIMARY KEY,
    stock_actual INT NOT NULL,
    ubicacion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proveedor (
    id_proveedor VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS detalle_compras (
    id_detalle VARCHAR(50) PRIMARY KEY,
    id_compra VARCHAR(50) NOT NULL,
    id_articulo VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

INSERT INTO Cajas (id_caja, nombre) VALUES 
('CJ001', 'Caja Principal'),
('CJ002', 'Caja Secundaria'),
('CJ003', 'Caja de Emergencia');

INSERT INTO Categorias (id_categoria, nombre, descripcion) VALUES 
('CAT001', 'Electrónicos', 'Productos electrónicos y dispositivos'),
('CAT002', 'Alimentos', 'Comestibles y bebidas'),
('CAT003', 'Limpieza', 'Productos de limpieza para el hogar');

INSERT INTO Clientes (id_cliente, nombre, telefono) VALUES 
('CL001', 'Juan Pérez', '555-1234'),
('CL002', 'María García', '555-5678'),
('CL003', 'Carlos López', '555-9012');

INSERT INTO Empleados (id_empleado, nombre, usuario, contrasena) VALUES 
('EMP001', 'Ana Martínez', 'ana.martinez', 'ana123'),
('EMP002', 'Luis Rodríguez', 'luis.rod', 'luis456'),
('EMP003', 'Sofía Hernández', 'sofia.h', 'sofia789');

INSERT INTO Inventario (id_inventario, stock_actual, ubicacion) VALUES 
('INV001', 150, 'Almacén A'),
('INV002', 75, 'Almacén B'),
('INV003', 200, 'Almacén Principal');

INSERT INTO proveedor (id_proveedor, nombre, telefono) VALUES 
('PROV001', 'Suministros S.A.', '555-1111'),
('PROV002', 'Tecnología Global', '555-2222'),
('PROV003', 'Alimentos Frescos', '555-3333');

INSERT INTO detalle_compras (id_detalle, id_compra, id_articulo, cantidad, precio) VALUES 
('DET001', 'COMP001', 'ART001', 10, 25.50),
('DET002', 'COMP001', 'ART002', 5, 12.75),
('DET003', 'COMP002', 'ART003', 8, 18.25);