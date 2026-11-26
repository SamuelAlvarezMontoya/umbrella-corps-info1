from validaciones import *
from conexion_mysql import *
from conexion_mongo import *


def gestionar_administradores():
    """Submenú CRUD para gestionar los administradores en MySQL"""
    while True:
        print("\nGESTIÓN DE ADMINISTRADORES\n")
        print("1. Crear administrador")
        print("2. Ver administradores")
        print("3. Modificar administrador")
        print("4. Eliminar administrador")
        print("5. Volver al menú anterior")

        opcion = pedir_entero("Elige una opción (1-5): ")

        if opcion == 1:
            nombre = pedir_letras("Nombre completo del administrador: ")
            usuario = pedir_texto("Usuario de acceso: ")
            if crear_administrador(nombre, usuario):
                print("Administrador creado correctamente.")

        elif opcion == 2:
            lista = ver_administradores()
            if len(lista) == 0:
                print("No hay administradores registrados.")
            else:
                print("\nLista de Administradores:")
                for admin in lista:
                    print(f"ID: {admin[0]} | Nombre: {admin[1]} | Usuario: {admin[2]}")

        elif opcion == 3:
            id_admin = pedir_entero("ID del administrador a modificar: ")
            nuevo_nombre = pedir_letras("Nuevo nombre completo: ")
            nuevo_usuario = pedir_texto("Nuevo usuario de acceso: ")
            if modificar_administrador(id_admin, nuevo_nombre, nuevo_usuario):
                print("Administrador modificado correctamente.")

        elif opcion == 4:
            id_admin = pedir_entero("ID del administrador a eliminar: ")
            if eliminar_administrador(id_admin):
                print("Administrador eliminado correctamente.")

        elif opcion == 5:
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


def gestionar_usuarios():
    """Submenú CRUD para gestionar los bacteriólogos/usuarios en MySQL"""
    while True:
        print("\nGESTIÓN DE USUARIOS / BACTERIÓLOGOS\n")
        print("1. Crear bacteriólogo")
        print("2. Ver bacteriólogos")
        print("3. Modificar bacteriólogo")
        print("4. Eliminar bacteriólogo")
        print("5. Volver al menú anterior")

        opcion = pedir_entero("Elige una opción (1-5): ")

        if opcion == 1:
            nombre = pedir_letras("Nombre completo del bacteriólogo: ")
            usuario = pedir_texto("Usuario de acceso: ")
            if crear_usuario(nombre, usuario, "Bacteriologo"):
                print("Bacteriólogo registrado correctamente.")

        elif opcion == 2:
            lista = ver_usuarios()
            if len(lista) == 0:
                print("No hay bacteriólogos registrados.")
            else:
                print("\nLista de Bacteriólogos:")
                for u in lista:
                    print(f"ID: {u[0]} | Nombre: {u[1]} | Usuario: {u[2]} | Rol: {u[3]}")

        elif opcion == 3:
            id_usuario = pedir_entero("ID del bacteriólogo a modificar: ")
            nuevo_nombre = pedir_letras("Nuevo nombre completo: ")
            nuevo_usuario = pedir_texto("Nuevo usuario de acceso: ")
            if modificar_usuario(id_usuario, nuevo_nombre, nuevo_usuario, "Bacteriologo"):
                print("Bacteriólogo modificado correctamente.")

        elif opcion == 4:
            id_usuario = pedir_entero("ID del bacteriólogo a eliminar: ")
            if eliminar_usuario(id_usuario):
                print("Bacteriólogo eliminado correctamente.")

        elif opcion == 5:
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


def gestionar_cultivos():
    """Submenú CRUD para gestionar los registros de muestras y cultivos en MySQL"""
    while True:
        print("\nGESTIÓN DE REGISTROS DE CULTIVOS\n")
        print("1. Registrar cultivo")
        print("2. Ver cultivos")
        print("3. Modificar cultivo")
        print("4. Eliminar cultivo")
        print("5. Volver al menú anterior")

        opcion = pedir_entero("Elige una opción (1-5): ")

        if opcion == 1:
            id_paciente = pedir_entero("ID del paciente: ")
            tipo_muestra = pedir_letras("Tipo de muestra (sangre, orina, esputo, etc.): ")
            microorganismo = pedir_letras("Microorganismo aislado: ")
            gram_opcion = pedir_entero("Tinción de Gram (1 = Positivo, 2 = Negativo): ")
            if gram_opcion == 1:
                tincion_gram = "Positivo"
            else:
                tincion_gram = "Negativo"
            fecha = pedir_fecha("Fecha de aislamiento (AAAA-MM-DD): ")

            if crear_muestra(id_paciente, tipo_muestra, microorganismo, tincion_gram, fecha):
                print("Cultivo registrado correctamente.")

        elif opcion == 2:
            lista = ver_muestras()
            if len(lista) == 0:
                print("No hay cultivos registrados.")
            else:
                print("\nLista de Cultivos:")
                for m in lista:
                    print(f"ID Muestra: {m[0]} | ID Paciente: {m[1]} | Tipo: {m[2]} | Bacteria: {m[3]} | Gram: {m[4]} | Fecha: {m[5]}")

        elif opcion == 3:
            id_muestra = pedir_entero("ID de la muestra a modificar: ")
            nuevo_tipo = pedir_letras("Nuevo tipo de muestra: ")
            nuevo_micro = pedir_letras("Nuevo microorganismo aislado: ")
            gram_opcion = pedir_entero("Nueva tinción de Gram (1 = Positivo, 2 = Negativo): ")
            if gram_opcion == 1:
                nueva_tincion = "Positivo"
            else:
                nueva_tincion = "Negativo"
            nueva_fecha = pedir_fecha("Nueva fecha de aislamiento (AAAA-MM-DD): ")

            if modificar_muestra(id_muestra, nuevo_tipo, nuevo_micro, nueva_tincion, nueva_fecha):
                print("Cultivo modificado correctamente.")

        elif opcion == 4:
            id_muestra = pedir_entero("ID de la muestra a eliminar: ")
            if eliminar_muestra(id_muestra):
                print("Cultivo eliminado correctamente.")

        elif opcion == 5:
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


def gestionar_archivos_criticos():
    """Submenú CRUD para gestionar archivos de análisis críticos en MongoDB (archivos_adjuntos)"""
    while True:
        print("\nGESTIÓN DE ARCHIVOS DE ANÁLISIS CRÍTICOS\n")
        print("1. Registrar archivo crítico")
        print("2. Ver archivos críticos")
        print("3. Modificar archivo crítico")
        print("4. Eliminar archivo crítico")
        print("5. Volver al menú anterior")

        opcion = pedir_entero("Elige una opción (1-5): ")

        if opcion == 1:
            id_muestra = pedir_entero("ID de la muestra asociada: ")
            tipo_archivo = pedir_texto("Tipo de archivo (Tincion Gram, Placa, MALDI-TOF): ")
            ruta_local = pedir_texto("Ruta local del archivo (ej: evidencias/gram1.png): ")
            metadatos = pedir_texto("Metadatos o nivel de criticidad: ")
            if crear_archivo(id_muestra, tipo_archivo, ruta_local, metadatos):
                print("Archivo crítico registrado en MongoDB.")

        elif opcion == 2:
            lista = ver_archivos()
            if len(lista) == 0:
                print("No hay archivos críticos registrados.")
            else:
                print("\nLista de Archivos Críticos (ya formateados):")
                for doc in lista:
                    print(f"ID: {doc['id_archivo']} | Muestra: {doc['id_muestra']} | Tipo: {doc['tipo_archivo']} | Ruta: {doc['ruta_local']} | Info: {doc['metadatos']}")

        elif opcion == 3:
            id_archivo = pedir_entero("ID del archivo a modificar: ")
            nueva_ruta = pedir_texto("Nueva ruta local: ")
            nuevos_metadatos = pedir_texto("Nuevos metadatos o criticidad: ")
            if modificar_archivo(id_archivo, nueva_ruta, nuevos_metadatos):
                print("Archivo crítico modificado correctamente.")

        elif opcion == 4:
            id_archivo = pedir_entero("ID del archivo a eliminar: ")
            if eliminar_archivo(id_archivo):
                print("Archivo crítico eliminado correctamente.")

        elif opcion == 5:
            break
        else:
            print("Opción no válida. Elige un número entre 1 y 5.")


def mostrar_menu_admin():
    """Menú principal del Administrador (Jefe de Laboratorio) de Umbrella Corps"""
    while True:
        print("\nMENÚ ADMINISTRADOR - UMBRELLA CORPS\n")
        print("1. Gestionar Administradores")
        print("2. Gestionar Usuarios / Bacteriólogos")
        print("3. Gestionar Registros de Cultivos")
        print("4. Gestionar Archivos de Análisis Críticos")
        print("5. Cerrar sesión")

        opcion = pedir_entero("Selecciona una opción (1-5): ")

        if opcion == 1:
            gestionar_administradores()
        elif opcion == 2:
            gestionar_usuarios()
        elif opcion == 3:
            gestionar_cultivos()
        elif opcion == 4:
            gestionar_archivos_criticos()
        elif opcion == 5:
            print("Cerrando sesión del Administrador...")
            break
        else:
            print("Opción incorrecta. Intenta de nuevo.")