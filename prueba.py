from conexion import conectar_db

#Conexion a la base de datos
conn = conectar_db()
if conn:
    print("Conexión establecida exitosamente.")
    conn.close()
else:
    print("No se pudo establecer la conexión.")
