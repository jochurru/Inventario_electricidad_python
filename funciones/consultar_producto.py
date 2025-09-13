from conexion import conectar_db, obtener_cursor, cerrar_conexion

def consultar_productos():
    print("\n🔍 CONSULTA DE PRODUCTOS")
    print("1. Ver todos los productos")
    print("2. Ver solo nombres y marcas")
    print("3. Ver precios")
    print("4. Ver stock disponible")
    print("5. Buscar por categoría")
    print("6. Buscar producto por nombre")
    print("7. Volver al menú principal")

    opcion = input("Seleccione una opción: ").strip()

    conn, cursor = obtener_cursor()
    if not cursor:
        print("❌ No se pudo obtener el cursor.")
        return
    
    try:
        if opcion == "1":
            cursor.execute("SELECT * FROM productos")
            productos= cursor.fetchall()
            print("\n📋 Lista completa de productos:")
            print("-" * 80)
            for p in productos:
                print(f"🆔 ID: {p[0]}")
                print(f"📦 Nombre: {p[1]}")
                print(f"🏷️ Marca: {p[2]}")
                print(f"📂 Categoría: {p[3]}")
                print(f"💰 Precio: ${p[4]:.2f}")
                print(f"📦 Stock: {p[5]} unidades")
                print(f"📝 Descripción: {p[6]}")
                print("-" * 80)                
        
        elif opcion == "2":
            cursor.execute("SELECT nombre, marca FROM productos")
            print("\n🏷️ Nombres y marcas de productos:")
            print("-" * 50)
            for nombre, marca in cursor.fetchall():
                print(f"📦 Nombre: {nombre}")
                print(f"🏷️ Marca: {marca}")
            print("-" * 50)
        
        elif opcion == "3":
            cursor.execute("SELECT nombre, precio FROM productos")
            print("\n💰 Precios de productos:")
            print("-" * 50)
            for nombre, precio in cursor.fetchall():
                print(f"📦 Nombre: {nombre}")
                print(f"💰 Precio: ${precio:.2f}")
            print("-" * 50)   
        
        elif opcion == "4":
            cursor.execute("SELECT nombre, stock FROM productos")
            print("\n📦 Stock disponible:")
            print("-" * 50)
            for nombre, stock in cursor.fetchall():
                print(f"📦 Nombre: {nombre}")
                print(f"📊 Stock: {stock} unidades")
            print("-" * 50)

        elif opcion == "5":
            categoria = input("Ingrese la categoría a buscar: ").strip().capitalize()
            cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
            productos = cursor.fetchall()
            if productos:
                print(f"\n📋 Productos en la categoría '{categoria}':")
                print("-" * 80)
                for p in productos:
                    print(f"🆔 ID: {p[0]}")
                    print(f"📦 Nombre: {p[1]}")
                    print(f"🏷️ Marca: {p[2]}")
                    print(f"💰 Precio: ${p[4]:.2f}")
                    print(f"📦 Stock: {p[5]} unidades")
                    print(f"📝 Descripción: {p[6]}")
                    print("-" * 80)
            else:
                print(f"❌ No se encontraron productos en la categoría '{categoria}'.")
        
        elif opcion == "6":
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{nombre}%",))
            productos = cursor.fetchall()
            if productos:
                print(f"\n📋 Productos que coinciden con '{nombre}':")
                print("-" * 80)
                for p in productos:
                    print(f"🆔 ID: {p[0]}")
                    print(f"📦 Nombre: {p[1]}")
                    print(f"🏷️ Marca: {p[2]}")
                    print(f"📂 Categoría: {p[3]}")
                    print(f"💰 Precio: ${p[4]:.2f}")
                    print(f"📦 Stock: {p[5]} unidades")
                    print(f"📝 Descripción: {p[6]}")
                    print("-" * 80) 
            else:
                print(f"❌ No se encontraron productos que coincidan con '{nombre}'.")
        
        elif opcion == "7":
            print("🔙 Volviendo al menú principal.")
            return
        
        else:
            print("❌ Opción inválida. Intente nuevamente.")
            return
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        cerrar_conexion(conn)
    