def pedir_texto(mensaje):
    """Pide cualquier texto (con letras, números o símbolos) y verifica que no esté vacío"""
    while True:
        try:
            texto = input(mensaje).strip()
            if texto == "":
                print("Error: No puedes dejar este campo vacío.")
            else:
                return texto
        except Exception:
            print("Error: Ocurrió un problema al leer el texto.")


def pedir_letras(mensaje):
    """Pide un texto que solo tenga letras y espacios (nombres de personas o bacterias)"""
    while True:
        try:
            texto = input(mensaje).strip()
            sin_espacios = texto.replace(" ", "")
            if texto == "" or sin_espacios.isalpha() == False:
                print("Error: Ingresa solo letras (sin números ni símbolos).")
            else:
                return texto
        except Exception:
            print("Error: Ocurrió un problema al leer el dato.")


def pedir_entero(mensaje):
    """Pide un número entero positivo (edad, ID, opciones de menú, horas)"""
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error: El número no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Error: Debes escribir un número entero válido.")


def pedir_decimal(mensaje):
    """Pide un número decimal positivo (CMI, temperatura, humedad)"""
    while True:
        try:
            numero = float(input(mensaje))
            if numero < 0:
                print("Error: El valor no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Error: Debes escribir un número decimal válido (ej: 0.5 o 37.5).")


def pedir_fecha(mensaje):
    """Pide una fecha en formato AAAA-MM-DD y verifica que sea válida"""
    while True:
        try:
            fecha = input(mensaje).strip()
            if len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
                print("Error: Escribe la fecha como AAAA-MM-DD (ejemplo: 2026-11-26).")
            else:
                partes = fecha.split("-")
                anio = int(partes[0])
                mes = int(partes[1])
                dia = int(partes[2])

                if anio < 1900 or anio > 2100 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
                    print("Error: Fecha fuera de rango. Revisa año, mes y día.")
                else:
                    return fecha
        except ValueError:
            print("Error: Año, mes y día deben ser números.")