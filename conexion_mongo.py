from pymongo import MongoClient


def conectar_mongo():
    """Establece y retorna la conexión con la base de datos ProF_Info120262 en MongoDB Atlas"""
    try:
        enlace = "mongodb+srv://informatica1:info2026_2@cluster0.jasgyru.mongodb.net/"
        cliente = MongoClient(enlace)
        base_datos = cliente["ProF_Info120262"]
        return base_datos
    except Exception as error:
        print("Error al conectar a MongoDB:", error)
        return None


def generar_id_mongo(coleccion, nombre_id):
    """Calcula un número entero consecutivo para usar como ID sencillo en MongoDB"""
    mayor = 0
    for documento in coleccion.find():
        if nombre_id in documento and documento[nombre_id] > mayor:
            mayor = documento[nombre_id]
    return mayor + 1


# CRUD 1: COLECCIÓN notas_microbiologia

def crear_nota(id_muestra, observaciones, color, hemolisis, borde, olor, incubacion, alerta):
    """Guarda una nueva nota morfológica de microbiología en MongoDB"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["notas_microbiologia"]
        nuevo_id = generar_id_mongo(coleccion, "id_nota")
        documento = {
            "id_nota": nuevo_id,
            "id_muestra": id_muestra,
            "observaciones": observaciones,
            "color": color,
            "hemolisis": hemolisis,
            "borde": borde,
            "olor": olor,
            "condiciones_incubacion": incubacion,
            "alerta_epidemiologica": alerta
        }
        coleccion.insert_one(documento)
        return True
    except Exception as error:
        print("Error al crear nota en MongoDB:", error)
        return False


def ver_notas():
    """Consulta y retorna todas las notas de la colección notas_microbiologia"""
    db = conectar_mongo()
    if db is None:
        return []
    try:
        coleccion = db["notas_microbiologia"]
        lista = []
        for doc in coleccion.find():
            lista.append(doc)
        return lista
    except Exception as error:
        print("Error al consultar notas en MongoDB:", error)
        return []


def modificar_nota(id_nota, nuevas_observaciones, nueva_alerta):
    """Modifica las observaciones y la alerta epidemiológica de una nota según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["notas_microbiologia"]
        cambios = {
            "$set": {
                "observaciones": nuevas_observaciones,
                "alerta_epidemiologica": nueva_alerta
            }
        }
        coleccion.update_one({"id_nota": id_nota}, cambios)
        return True
    except Exception as error:
        print("Error al modificar nota en MongoDB:", error)
        return False


def eliminar_nota(id_nota):
    """Elimina una nota microbiológica de MongoDB según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["notas_microbiologia"]
        coleccion.delete_one({"id_nota": id_nota})
        return True
    except Exception as error:
        print("Error al eliminar nota en MongoDB:", error)
        return False


# CRUD 2: COLECCIÓN archivos_adjuntos


def crear_archivo(id_muestra, tipo_archivo, ruta_local, metadatos):
    """Registra un archivo adjunto (tinción de Gram, placa o MALDI-TOF) en MongoDB"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["archivos_adjuntos"]
        nuevo_id = generar_id_mongo(coleccion, "id_archivo")
        documento = {
            "id_archivo": nuevo_id,
            "id_muestra": id_muestra,
            "tipo_archivo": tipo_archivo,
            "ruta_local": ruta_local,
            "metadatos": metadatos
        }
        coleccion.insert_one(documento)
        return True
    except Exception as error:
        print("Error al crear archivo adjunto en MongoDB:", error)
        return False


def ver_archivos():
    """Consulta y retorna todos los documentos de la colección archivos_adjuntos"""
    db = conectar_mongo()
    if db is None:
        return []
    try:
        coleccion = db["archivos_adjuntos"]
        lista = []
        for doc in coleccion.find():
            lista.append(doc)
        return lista
    except Exception as error:
        print("Error al consultar archivos adjuntos:", error)
        return []


def modificar_archivo(id_archivo, nueva_ruta, nuevos_metadatos):
    """Actualiza la ruta local y los metadatos de un archivo adjunto según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["archivos_adjuntos"]
        cambios = {
            "$set": {
                "ruta_local": nueva_ruta,
                "metadatos": nuevos_metadatos
            }
        }
        coleccion.update_one({"id_archivo": id_archivo}, cambios)
        return True
    except Exception as error:
        print("Error al modificar archivo adjunto:", error)
        return False


def eliminar_archivo(id_archivo):
    """Elimina un registro de archivo adjunto según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["archivos_adjuntos"]
        coleccion.delete_one({"id_archivo": id_archivo})
        return True
    except Exception as error:
        print("Error al eliminar archivo adjunto:", error)
        return False



# CRUD 3: COLECCIÓN telemetria_incubadora

def crear_telemetria(id_muestra, temperatura, co2, humedad, horas_incubacion):
    """Registra una lectura de telemetría de incubadora en MongoDB"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["telemetria_incubadora"]
        nuevo_id = generar_id_mongo(coleccion, "id_telemetria")
        documento = {
            "id_telemetria": nuevo_id,
            "id_muestra": id_muestra,
            "temperatura": temperatura,
            "co2": co2,
            "humedad": humedad,
            "horas_incubacion": horas_incubacion
        }
        coleccion.insert_one(documento)
        return True
    except Exception as error:
        print("Error al registrar telemetría:", error)
        return False


def ver_telemetrias():
    """Consulta y retorna todas las lecturas de telemetría de incubadoras"""
    db = conectar_mongo()
    if db is None:
        return []
    try:
        coleccion = db["telemetria_incubadora"]
        lista = []
        for doc in coleccion.find():
            lista.append(doc)
        return lista
    except Exception as error:
        print("Error al consultar telemetría:", error)
        return []


def modificar_telemetria(id_telemetria, nueva_temperatura, nuevo_co2, nueva_humedad, nuevas_horas):
    """Modifica una lectura de telemetría existente según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["telemetria_incubadora"]
        cambios = {
            "$set": {
                "temperatura": nueva_temperatura,
                "co2": nuevo_co2,
                "humedad": nueva_humedad,
                "horas_incubacion": nuevas_horas
            }
        }
        coleccion.update_one({"id_telemetria": id_telemetria}, cambios)
        return True
    except Exception as error:
        print("Error al modificar telemetría:", error)
        return False


def eliminar_telemetria(id_telemetria):
    """Elimina un registro de telemetría según su ID"""
    db = conectar_mongo()
    if db is None:
        return False
    try:
        coleccion = db["telemetria_incubadora"]
        coleccion.delete_one({"id_telemetria": id_telemetria})
        return True
    except Exception as error:
        print("Error al eliminar telemetría:", error)
        return False
