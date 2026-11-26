import mysql.connector

def conectar_mysql():
    """Establece la conexión con MySQL"""
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


def crear_tablas_mysql():
    """Crea las 5 tablas relacionales del laboratorio en MySQL si no existen"""
    conexion = conectar_mysql()
    if conexion is None:
        return

    try:
        cursor = conexion.cursor()

        #Tabla administradores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS administradores (
                id_admin INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                usuario VARCHAR(50) NOT NULL
            )
        """)

        #Tabla usuarios (Bacteriólogos)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                usuario VARCHAR(50) NOT NULL,
                rol VARCHAR(50) NOT NULL
            )
        """)

        #Tabla pacientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id_paciente INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                edad INT NOT NULL,
                servicio VARCHAR(50) NOT NULL
            )
        """)

        #Tabla muestras_cultivos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS muestras_cultivos (
                id_muestra INT AUTO_INCREMENT PRIMARY KEY,
                id_paciente INT NOT NULL,
                tipo_muestra VARCHAR(60) NOT NULL,
                microorganismo VARCHAR(100) NOT NULL,
                tincion_gram VARCHAR(20) NOT NULL,
                fecha_aislamiento VARCHAR(20) NOT NULL
            )
        """)

        #Tabla antibiogramas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS antibiogramas (
                id_antibiograma INT AUTO_INCREMENT PRIMARY KEY,
                id_muestra INT NOT NULL,
                antibiotico VARCHAR(100) NOT NULL,
                familia VARCHAR(100) NOT NULL,
                cmi FLOAT NOT NULL,
                interpretacion VARCHAR(30) NOT NULL
            )
        """)

        conexion.commit()
        cursor.close()
        conexion.close()
        print("Las 5 tablas de MySQL fueron creadas y verificadas correctamente.")
    except Exception as error:
        print("Error al crear las tablas en MySQL:", error)


# CRUD 1: TABLA ADMINISTRADORES

def crear_administrador(nombre, usuario):
    """Inserta un nuevo administrador en MySQL"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO administradores (nombre, usuario) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, usuario))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al crear administrador:", error)
        return False


def ver_administradores():
    """Consulta y retorna todos los registros de la tabla administradores"""
    conexion = conectar_mysql()
    if conexion is None:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM administradores")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as error:
        print("Error al consultar administradores:", error)
        return []


def modificar_administrador(id_admin, nuevo_nombre, nuevo_usuario):
    """Actualiza el nombre y usuario de un administrador según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "UPDATE administradores SET nombre = %s, usuario = %s WHERE id_admin = %s"
        cursor.execute(sql, (nuevo_nombre, nuevo_usuario, id_admin))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al modificar administrador:", error)
        return False


def eliminar_administrador(id_admin):
    """Elimina un administrador de MySQL según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM administradores WHERE id_admin = %s"
        cursor.execute(sql, (id_admin,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al eliminar administrador:", error)
        return False


# CRUD 2: TABLA USUARIOS (BACTERIÓLOGOS)


def crear_usuario(nombre, usuario, rol):
    """Inserta un nuevo usuario (Bacteriólogo) en MySQL"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, usuario, rol) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, usuario, rol))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al crear usuario:", error)
        return False


def ver_usuarios():
    """Consulta y retorna todos los usuarios registrados en MySQL"""
    conexion = conectar_mysql()
    if conexion is None:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as error:
        print("Error al consultar usuarios:", error)
        return []


def modificar_usuario(id_usuario, nuevo_nombre, nuevo_usuario, nuevo_rol):
    """Actualiza los datos de un usuario según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET nombre = %s, usuario = %s, rol = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_nombre, nuevo_usuario, nuevo_rol, id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al modificar usuario:", error)
        return False


def eliminar_usuario(id_usuario):
    """Elimina un usuario de MySQL según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id_usuario = %s"
        cursor.execute(sql, (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al eliminar usuario:", error)
        return False


# CRUD 3: TABLA PACIENTES


def crear_paciente(nombre, edad, servicio):
    """Registra un nuevo paciente en MySQL"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO pacientes (nombre, edad, servicio) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, edad, servicio))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al crear paciente:", error)
        return False


def ver_pacientes():
    """Consulta y retorna todos los pacientes registrados"""
    conexion = conectar_mysql()
    if conexion is None:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as error:
        print("Error al consultar pacientes:", error)
        return []


def modificar_paciente(id_paciente, nuevo_nombre, nueva_edad, nuevo_servicio):
    """Modifica los datos de un paciente según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "UPDATE pacientes SET nombre = %s, edad = %s, servicio = %s WHERE id_paciente = %s"
        cursor.execute(sql, (nuevo_nombre, nueva_edad, nuevo_servicio, id_paciente))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al modificar paciente:", error)
        return False


def eliminar_paciente(id_paciente):
    """Elimina un paciente según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM pacientes WHERE id_paciente = %s"
        cursor.execute(sql, (id_paciente,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al eliminar paciente:", error)
        return False


# CRUD 4: TABLA MUESTRAS Y CULTIVOS


def crear_muestra(id_paciente, tipo_muestra, microorganismo, tincion_gram, fecha_aislamiento):
    """Registra una nueva muestra microbiológica en MySQL"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = """
            INSERT INTO muestras_cultivos (id_paciente, tipo_muestra, microorganismo, tincion_gram, fecha_aislamiento)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_paciente, tipo_muestra, microorganismo, tincion_gram, fecha_aislamiento))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al crear muestra:", error)
        return False


def ver_muestras():
    """Consulta y retorna todas las muestras y cultivos registrados"""
    conexion = conectar_mysql()
    if conexion is None:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM muestras_cultivos")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as error:
        print("Error al consultar muestras:", error)
        return []


def modificar_muestra(id_muestra, nuevo_tipo, nuevo_microorganismo, nueva_tincion, nueva_fecha):
    """Modifica los datos de una muestra registrada según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = """
            UPDATE muestras_cultivos
            SET tipo_muestra = %s, microorganismo = %s, tincion_gram = %s, fecha_aislamiento = %s
            WHERE id_muestra = %s
        """
        cursor.execute(sql, (nuevo_tipo, nuevo_microorganismo, nueva_tincion, nueva_fecha, id_muestra))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al modificar muestra:", error)
        return False


def eliminar_muestra(id_muestra):
    """Elimina una muestra de cultivo según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM muestras_cultivos WHERE id_muestra = %s"
        cursor.execute(sql, (id_muestra,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al eliminar muestra:", error)
        return False


# CRUD 5: TABLA ANTIBIOGRAMAS

def interpretar_cmi(cmi):
    """Calcula automáticamente la interpretación clínica según el valor de CMI (ug/mL)"""
    if cmi <= 1.0:
        return "Sensible"
    elif cmi <= 4.0:
        return "Intermedio"
    else:
        return "Resistente"


def crear_antibiograma(id_muestra, antibiotico, familia, cmi):
    """Registra un resultado de antibiograma calculando su interpretación automáticamente"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        interpretacion = interpretar_cmi(cmi)
        cursor = conexion.cursor()
        sql = """
            INSERT INTO antibiogramas (id_muestra, antibiotico, familia, cmi, interpretacion)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (id_muestra, antibiotico, familia, cmi, interpretacion))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al crear antibiograma:", error)
        return False


def ver_antibiogramas():
    """Consulta y retorna todos los antibiogramas registrados"""
    conexion = conectar_mysql()
    if conexion is None:
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM antibiogramas")
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as error:
        print("Error al consultar antibiogramas:", error)
        return []


def modificar_antibiograma(id_antibiograma, nuevo_antibiotico, nueva_familia, nuevo_cmi):
    """Modifica un antibiograma y recalcula su interpretación automática"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        nueva_interpretacion = interpretar_cmi(nuevo_cmi)
        cursor = conexion.cursor()
        sql = """
            UPDATE antibiogramas
            SET antibiotico = %s, familia = %s, cmi = %s, interpretacion = %s
            WHERE id_antibiograma = %s
        """
        cursor.execute(sql, (nuevo_antibiotico, nueva_familia, nuevo_cmi, nueva_interpretacion, id_antibiograma))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al modificar antibiograma:", error)
        return False


def eliminar_antibiograma(id_antibiograma):
    """Elimina un antibiograma según su ID"""
    conexion = conectar_mysql()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM antibiogramas WHERE id_antibiograma = %s"
        cursor.execute(sql, (id_antibiograma,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as error:
        print("Error al eliminar antibiograma:", error)
        return False