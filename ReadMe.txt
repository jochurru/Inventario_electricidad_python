# ⚡ Inventario Eléctrico — Python + SQLite

Sistema de gestión de inventario desarrollado en Python con persistencia en SQLite.

El proyecto permite administrar productos eléctricos desde una interfaz de terminal, aplicando operaciones CRUD, validaciones de datos y una estructura modular para separar responsabilidades.

---

## 🚀 Funcionalidades

- Alta de productos
- Consulta de inventario
- Búsqueda y filtros por distintos campos
- Modificación de productos
- Eliminación con confirmación
- Persistencia de datos con SQLite
- Menú interactivo por terminal
- Código organizado en módulos independientes

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

- Python
- SQLite
- SQL
- Programación modular
- Manejo de errores
- Validación de datos

---

## 🗃️ Modelo de datos

La aplicación utiliza una base SQLite con una tabla principal de productos.

Campos principales:

- `id`
- `nombre`
- `marca`
- `categoria`
- `precio`
- `stock`
- `descripcion`

---

## 📁 Estructura del proyecto

```text
Inventario_electricidad_python/
├── main.py
├── conexion.py
├── inventario.db
├── funciones/
│   ├── __init__.py
│   ├── insertar_producto.py
│   ├── consultar_producto.py
│   ├── modificar_producto.py
│   └── eliminar_producto.py
└── README.md
