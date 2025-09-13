from conexion import conectar_db, obtener_cursor, cerrar_conexion
from funciones.insertar_producto import cargar_productos_desde_usuario
from funciones.consultar_producto import consultar_productos
from funciones.modificar_producto import modificar_producto
from funciones.eliminar_producto import eliminar_producto

def mostrar_menu():
    print("\n=== MENÚ DE GESTIÓN DE INVENTARIO ===")
    print("1. Cargar nuevos productos")
    print("2. Consultar productos")
    print("3. Modificar productos")
    print("4. Eliminar productos")
    print("5. Salir")

def main():
    conn, cursor = obtener_cursor()
    if conn is None or cursor is None:
        print("❌ No se pudo establecer la conexión o el cursor.")
        exit(1)
    else:
        print("✅ Conexión y cursor obtenidos exitosamente.")
        conn.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        marca TEXT,
                        categoria TEXT,
                        precio REAL NOT NULL,
                        stock INTEGER NOT NULL,
                        descripcion TEXT
                    )''')
        conn.commit()
        print("📦 Tabla 'productos' creada o ya existente.")
        cerrar_conexion(conn)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cargar_productos_desde_usuario()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("👋 Cerrando el sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
