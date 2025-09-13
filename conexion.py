import sqlite3

# Eliminar ejecución automática
# conn = sqlite3.connect('inventario.db')
# conn.close()
# print("Conexión exitosa a la base de datos SQLite.")

def conectar_db(nombre_bd="inventario.db"):
    try:
        conn = sqlite3.connect(nombre_bd)
        print("Conexión exitosa a la base de datos SQLite.")
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def obtener_cursor(nombre_bd="inventario.db"):
    try:
        conn = sqlite3.connect(nombre_bd)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error al obtener el cursor: {e}")
        return None, None

def cerrar_conexion(conn):
    if conn:
        conn.close()
        print("Conexión cerrada.")