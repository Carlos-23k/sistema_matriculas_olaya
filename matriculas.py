import re

GRADOS = ["1", "2", "3", "4", "5"]
SECCIONES = ["A", "B", "C", "D", "E"]

def validar_datos(datos, lista=None):
    """Devuelve (True, "") si todo está Ok, o (False, "mensaje de error")."""
    if not datos.get("nombres", "").strip():
        return False, "El nombre no puede estar vacío"
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", datos["nombres"].strip()):
        return False, "El nombre solo puede tener letras y espacios"
    if not re.fullmatch(r"\d{8}", datos.get("dni", "")):
        return False, "El DNI debe tener exactamente 8 dígitos"
    if datos.get("grado", "") not in GRADOS:
        return False, "El grado debe ser 1, 2, 3, 4 o 5"
    if datos.get("seccion", "").upper() not in SECCIONES:
        return False, "La sección debe ser A, B, C, D o E"
    if not datos.get("apoderado", "").strip():
        return False, "Debe indicar el nombre del apoderado"
    if lista is not None:
        for m in lista:
            if m["dni"] == datos["dni"]:
                return False, "Ya existe una matrícula con ese DNI"
    return True, ""

def generar_codigo(lista):
    """Correlativo tipo MAT-0001, MAT-0002..."""
    numeros = []
    for n in lista:
        num_str = n["codigo"].split("-")[-1]
        if num_str.isdigit():
            numeros.append(int(num_str))
    numero = max(numeros) + 1 if numeros else 1
    return f"MAT-{numero:04d}"

import os
import re
from datetime import datetime

RUTA = "sistema_matriculas_olaya.txt"
CAMPOS = ["codigo", "nombres", "dni", "grado", "seccion", "apoderado", "fecha"]
GRADOS = ["1", "2", "3", "4", "5"]
SECCIONES = ["A", "B", "C", "D", "E"]

# Funciones anteriores (Validación y Código - hechas por Freddy)
def validar_datos(datos, lista=None):
    if not datos.get("nombres", "").strip():
        return False, "El nombre no puede estar vacío"
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", datos["nombres"].strip()):
        return False, "El nombre solo puede tener letras y espacios"
    if not re.fullmatch(r"\d{8}", datos.get("dni", "")):
        return False, "El DNI debe tener exactamente 8 dígitos"
    if datos.get("grado", "") not in GRADOS:
        return False, "El grado debe ser 1, 2, 3, 4 o 5"
    if datos.get("seccion", "").upper() not in SECCIONES:
        return False, "La sección debe ser A, B, C, D o E"
    if not datos.get("apoderado", "").strip():
        return False, "Debe indicar el nombre del apoderado"
    if lista is not None:
        for m in lista:
            if m["dni"] == datos["dni"]:
                return False, "Ya existe una matrícula con ese DNI"
    return True, ""

def generar_codigo(lista):
    numeros = []
    for n in lista:
        num_str = n["codigo"].split("-")[-1]
        if num_str.isdigit():
            numeros.append(int(num_str))
    numero = max(numeros) + 1 if numeros else 1
    return f"MAT-{numero:04d}"

# --- NUEVAS FUNCIONES DEL TERCER INTEGRANTE ---

# 1. Persistencia
def cargar_matriculas(ruta=None):
    """Lee el archivo y devuelve una lista de diccionarios."""
    ruta = ruta or RUTA
    matriculas = []
    if not os.path.exists(ruta):
        return matriculas
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split("|")
            if len(partes) == len(CAMPOS):
                matriculas.append(dict(zip(CAMPOS, partes)))
    return matriculas

def guardar_matriculas(lista, ruta=None):
    """Reescribe el archivo con toda la lista."""
    ruta = ruta or RUTA
    with open(ruta, "w", encoding="utf-8") as f:
        for m in lista:
            f.write("|".join(m[c] for c in CAMPOS) + "\n")

# 2. Registro y Búsquedas
def pedir_datos():
    return {
        "nombres": input("Nombres y apellidos: ").strip(),
        "dni": input("DNI (8 dígitos): ").strip(),
        "grado": input("Grado (1-5): ").strip(),
        "seccion": input("Sección (A-E): ").strip().upper(),
        "apoderado": input("Apoderado: ").strip(),
    }

def registrar_matricula(lista, datos=None):
    """Junta pedir_datos + validar + guardar."""
    if datos is None:
        datos = pedir_datos()
    datos["seccion"] = datos.get("seccion", "").upper()
    ok, error = validar_datos(datos, lista)
    if not ok:
        return False, error
    datos["codigo"] = generar_codigo(lista)
    datos["fecha"] = datetime.now().strftime("%Y-%m-%d")
    lista.append(datos)
    guardar_matriculas(lista)
    return True, f"Matrícula registrada con código {datos['codigo']}"

def buscar_por_codigo(lista, codigo):
    """Búsqueda lineal por código."""
    for m in lista:
        if m["codigo"].upper() == codigo.strip().upper():
            return m
    return None

def buscar_por_dni(lista, dni):
    """Búsqueda lineal por DNI."""
    for m in lista:
        if m["dni"] == dni.strip():
            return m
    return None
