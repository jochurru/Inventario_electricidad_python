from conexion import conectar_db, obtener_cursor, cerrar_conexion

def eliminar_producto():
    print("\n🗑️ ELIMINAR PRODUCTO")
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("❌ Error: El ID debe ser un número entero.")
        return

    conn, cursor = obtener_cursor()
    if not cursor:
        print("❌ No se pudo obtener el cursor.")
        return
    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print("⚠️ No se encontró ningún producto con ese ID.")
            return

        print(f"\n🧾 Producto encontrado:")
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Marca: {producto[2]} | Categoría: {producto[3]} | Precio: ${producto[4]} | Stock: {producto[5]}")

        confirmacion = input("❗ ¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()
        if confirmacion == "s":
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conn.commit()
            print(f"✅ Producto ID {id_producto} eliminado correctamente.")
        else:
            print("↩ Eliminación cancelada.")
    except Exception as e:
        print(f"❌ Error al eliminar el producto: {e}")
    finally:
        cerrar_conexion(conn)
