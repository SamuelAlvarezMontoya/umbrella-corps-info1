from pymongo import MongoClient

def conectar_mongo():
    try:
        enlace = "mongodb+srv://informatica1:info2026_2@cluster0.jasgyru.mongodb.net/"
        cliente = MongoClient(enlace)
        base_datos = cliente["ProF_Info120262"]
        #Esto es para verificar que la contraseña y la red funcionan
        base_datos.list_collection_names()
        return base_datos
    except Exception as error:
        print("Error al conectar a MongoDB:", error)
        return None