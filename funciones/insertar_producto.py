from conexion import conectar_db, obtener_cursor, cerrar_conexion

def cargar_productos_desde_usuario():
    print("\n 📝CARGA DE NUEVOS PRODUCTOS")
    try:
        nombre = str(input("📝 Ingrese el nombre del producto: ")).strip().capitalize()
        marca = str(input("🏷️Ingrese la marca del producto: ")).strip().capitalize()
        categoria = str(input("📂Ingrese la categoría del producto: ")).strip().capitalize()
        precio = float(input("💰Ingrese el precio del producto: "))
        stock = int(input("📦Ingrese la cantidad en stock del producto: "))
        descripcion = str(input("📝Ingrese una descripción del producto: ")).strip().capitalize()
        conn, cursor = obtener_cursor()
        if cursor:
            cursor.execute("""
                INSERT INTO productos (nombre, marca, categoria, precio, stock, descripcion)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nombre, marca, categoria, precio, stock, descripcion))
            conn.commit()
            print(f"\n✅ Producto '{nombre}' insertado correctamente.")
            cerrar_conexion(conn)
        else:
            print("❌ No se pudo obtener el cursor.")
    except ValueError:
        print("⚠️ Error: precio y cantidad deben ser números válidos.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    except ValueError:
        print("❌ Error: Tipo de dato inválido. Por favor, intente nuevamente.")
        return

