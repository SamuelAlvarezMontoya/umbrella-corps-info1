import mysql.connector

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="informatica1",
            password="info2026_2",
            database="ProF_Info120262"
        )
        return conexion
    except Exception as error:
        print("Error al conectar a MySQL:", error)
        return None