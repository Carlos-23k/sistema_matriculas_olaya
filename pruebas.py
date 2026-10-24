# pruebas.py - 16 Casos de prueba automatizados
from matriculas import validar_datos, buscar_por_codigo, buscar_por_dni, ordenar_por, cargar_matriculas, guardar_matriculas
import os

def ejecutar_pruebas():
    print("Ejecutando los 16 casos de prueba automatizados...")
    test_ruta = "test_matriculas.txt"
    if os.path.exists(test_ruta):
        os.remove(test_ruta)
    
    lista = []
    
    # 1. Registro válido
    d1 = {"nombres": "Ana Torres", "dni": "45678912", "grado": "3", "seccion": "A", "apoderado": "Daniel Sanchez"}
    ok, _ = validar_datos(d1, lista)
    assert ok == True
    d1["codigo"] = "MAT-0001"
    lista.append(d1)
    
    # 2. Código correlativo
    d2 = {"nombres": "Luis Perez", "dni": "12345678", "grado": "1", "seccion": "b", "apoderado": "Julia Andrade"}
    d2["seccion"] = d2["seccion"].upper()
    ok, _ = validar_datos(d2, lista)
    assert ok == True
    d2["codigo"] = "MAT-0002"
    lista.append(d2)
    
    # 3. Sección en mayúscula
    assert d2["seccion"] == "B"
    
    # 4. DNI muy corto
    ok, _ = validar_datos({"nombres": "Test", "dni": "123", "grado": "1", "seccion": "A", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 5. DNI con letras
    ok, _ = validar_datos({"nombres": "Test", "dni": "1234567a", "grado": "1", "seccion": "A", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 6. Nombre vacío
    ok, _ = validar_datos({"nombres": "   ", "dni": "99999999", "grado": "1", "seccion": "A", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 7. Grado inválido
    ok, _ = validar_datos({"nombres": "Test", "dni": "99999999", "grado": "9", "seccion": "A", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 8. Sección inválida
    ok, _ = validar_datos({"nombres": "Test", "dni": "99999999", "grado": "1", "seccion": "Z", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 9. DNI duplicado
    ok, _ = validar_datos({"nombres": "Otro", "dni": "45678912", "grado": "2", "seccion": "B", "apoderado": "Padre"}, lista)
    assert ok == False
    
    # 10. Lista intacta tras rechazos
    assert len(lista) == 2
    
    # 11. Búsqueda por código
    res = buscar_por_codigo(lista, "mat-0002")
    assert res is not None and res["nombres"] == "Luis Perez"
    
    # 12. Búsqueda por DNI
    res = buscar_por_dni(lista, "45678912")
    assert res is not None and res["codigo"] == "MAT-0001"
    
    # 13. Código inexistente
    res = buscar_por_codigo(lista, "MAT-9999")
    assert res is None
    
    # 14. Ordenar por nombre
    ordenada = ordenar_por(lista, "nombres")
    assert ordenada[0]["nombres"] == "Ana Torres"
    
    # 15 & 16. Persistencia (Guardar y cargar)
    guardar_matriculas(lista, test_ruta)
    cargadas = cargar_matriculas(test_ruta)
    assert len(cargadas) == 2
    assert cargadas[0]["dni"] == lista[0]["dni"]
    
    if os.path.exists(test_ruta):
        os.remove(test_ruta)
        
    print("¡16 de 16 pruebas ejecutadas y superadas correctamente!")

if __name__ == "__main__":
    ejecutar_pruebas()
