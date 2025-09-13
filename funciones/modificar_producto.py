from conexion import conectar_db, obtener_cursor, cerrar_conexion

def modificar_producto():
    print("\n✏️ MODIFICAR PRODUCTO")
    try:
        id_producto = int(input("Ingrese el ID del producto a modificar: "))
    except ValueError:
        print("❌ Error: El ID debe ser un número entero.")
        return
    
    print("\n📋 ¿Qué desea modificar?")
    print("1. Nombre")
    print("2. Marca")
    print("3. Categoría")
    print("4. Precio")
    print("5. Stock")
    print("6. Descripción")
    print("7. Volver al menú principal")

    opcion = input("Seleccione una opción: ").strip()
    campos= {
        "1": "nombre",
        "2": "marca",
        "3": "categoria",
        "4": "precio",
        "5": "stock",
        "6": "descripcion"
    }
    if opcion not in campos and opcion != "7":
        print("❌ Opción inválida. Intente nuevamente.")
        return
    elif opcion == "7":
        print("🔙 Volviendo al menú principal.")
        return
    nuevo_valor = input(f"📝 Ingrese el nuevo valor para {campos[opcion]}: ")

    #Validar tipos de datos
    if campos[opcion]=="precio":
        try:
            nuevo_valor = float(nuevo_valor)
        except ValueError:
            print("❌ Error: El precio debe ser un número válido.")
            return
    elif campos[opcion]=="stock":
        try:
            nuevo_valor = int(nuevo_valor)
        except ValueError:
            print("❌ Error: El stock debe ser un número entero.")
            return
    conn, cursor = obtener_cursor()
    if not cursor:
        print("❌ No se pudo obtener el cursor.")
        return
    try:
        cursor.execute(f"""UPDATE productos SET {campos[opcion]} =? WHERE id = ?""",
                    (nuevo_valor, id_producto))
        conn.commit()
        print(f"\n✅ Producto con ID {id_producto} modificado correctamente.")
    except Exception as e:
        print(f"❌ Error al modificar el producto: {e}")
    finally:
        cerrar_conexion(conn)


