# 🧰 Inventario Eléctrico – Proyecto Python + SQLite

Este sistema permite gestionar un inventario de productos eléctricos con carga, consulta, modificación y eliminación, todo desde terminal y con lógica simbólica.

---

## 📦 Funcionalidades

- Cargar nuevos productos con validación
- Consultar productos por nombre, categoría, stock o precio
- Modificar campos específicos de un producto
- Eliminar productos con confirmación previa
- Menú principal interactivo y submenús por función

---

## 🧱 Estructura del proyecto
Inventario_Electricidad/ ├── main.py ├── conexion.py ├── funciones/ │   
├── init.py │   ├── insertar_producto.py │   ├── consultar_producto.py │   
├── modificar_producto.py │   └── eliminar_producto.py


---

## 🗃️ Base de datos

- SQLite local
- Tabla `productos` con los siguientes campos:
  - `id`, `nombre`, `marca`, `categoria`, `precio`, `stock`, `descripcion`

---

## 🧠 Requisitos

- Python 3.x
- No requiere librerías externas

---

## 🚀 Ejecución

```bash
python main.py


👨‍💻 Autor
Proyecto desarrollado por Jonatan Churruarin, técnico autodidacta con experiencia en:
- Modularización de sistemas
- Documentación simbólica aplicada a procesos técnicos
- Gestión de inventario con Python + SQLite
- Diseño de interfaces terminales funcionales
Este proyecto forma parte de su laboratorio de aprendizaje aplicado, con enfoque en resiliencia, claridad estructural y automatización de tareas administrativas.


🧭 Estado del proyecto
✅ Funcional
🛠️ Listo para futuras mejoras (interfaz visual, exportación)
📁 Documentado y estructurado para uso pedagógico y técnico
