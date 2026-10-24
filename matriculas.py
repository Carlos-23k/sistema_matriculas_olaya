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
