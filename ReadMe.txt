# 🧰 Inventario Eléctrico – Proyecto Python + SQLite

Este sistema permite gestionar un inventario de productos eléctricos con carga, consulta, modificación y eliminación, todo desde terminal y con lógica simbólica.

## 📦 Funcionalidades

- Cargar nuevos productos con validación
- Consultar productos por nombre, categoría, stock o precio
- Modificar campos específicos de un producto
- Eliminar productos con confirmación previa
- Menú principal interactivo y submenús por función

## 🧱 Estructura del proyecto
Inventario_Electricidad/ ├── main.py ├── conexion.py ├── funciones/ │   ├── init.py │   ├── insertar_producto.py │   ├── consultar_producto.py │   ├── modificar_producto.py │   └── eliminar_producto.py

## 🗃️ Base de datos

- SQLite local
- Tabla `productos` con campos:
  - `id`, `nombre`, `marca`, `categoria`, `precio`, `stock`, `descripcion`

## 🧠 Requisitos

- Python 3.x
- No requiere librerías externas

## 🚀 Ejecución

```bash
python main.py



Proyecto desarrollado por Jonatan Churruarin, técnico autodidacta con experiencia en modularización de sistemas, documentación simbólica y gestión de inventario con Python + SQLite.  
Especializado en estructuración pedagógica de procesos técnicos, validación de datos y diseño de interfaces terminales funcionales.  
Este proyecto forma parte de su laboratorio de aprendizaje aplicado, con enfoque en resiliencia, claridad estructural y automatización de tareas administrativas.