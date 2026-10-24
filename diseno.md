# 2. Diseño del Algoritmo

El diseño del sistema se estructura mediante un diagrama de flujo y un pseudocódigo modular que permite gestionar el registro, validación, búsqueda, ordenamiento y almacenamiento persistente de las matrículas.

## 2.1. Diagrama de Flujo

El algoritmo principal inicia cargando las matrículas existentes desde el archivo de texto `sistema_matriculas_olaya.txt`. A continuación, despliega un bucle iterativo que muestra el menú principal y procesa la opción seleccionada por el usuario (desde registrar un nuevo alumno hasta salir del sistema):

* **Inicio** $\rightarrow$ Cargar matrículas $\rightarrow$ Mostrar Menú Principal.
* **Opción 1:** Registrar matrícula (valida datos, autogenera el código correlativo tipo `MAT-0001`, asigna fecha actual y guarda en el archivo).
* **Opción 2 y 3:** Buscar por código o por DNI (búsqueda lineal).
* **Opción 4 y 5:** Listar ordenado por código o por nombre (algoritmo de ordenamiento por inserción).
* **Opción 0:** Salir del programa.

## 2.2. Pseudocódigo

```text
INICIO
  matriculas = cargar_matriculas("sistema_matriculas_olaya.txt")
  
  REPETIR
    MOSTRAR "\n--- MATRÍCULAS I.E. JOSÉ OLAYA ---"
    MOSTRAR "1. Registrar matrícula"
    MOSTRAR "2. Buscar por código"
    MOSTRAR "3. Buscar por DNI"
    MOSTRAR "4. Listar (ordenado por código)"
    MOSTRAR "5. Listar (ordenado por nombre)"
    MOSTRAR "0. Salir"
    
    LEER opcion
    
    SEGUN opcion:
      "1": 
        datos = pedir_datos()
        SI validar_datos(datos, matriculas) ENTONCES
          datos["codigo"] = generar_codigo(matriculas)
          datos["fecha"] = fecha_actual()
          matriculas.agregar(datos)
          guardar_matriculas(matriculas)
          MOSTRAR "Matrícula registrada con éxito"
        SINO
          MOSTRAR mensaje de error
          
      "2": 
        LEER codigo
        res = buscar_por_codigo(matriculas, codigo)
        MOSTRAR res (o "No encontrado")
        
      "3": 
        LEER dni
        res = buscar_por_dni(matriculas, dni)
        MOSTRAR res (o "No encontrado")
        
      "4": 
        listar_ordenado(matriculas, "codigo")
        
      "5": 
        listar_ordenado(matriculas, "nombres")
        
      "0":
        MOSTRAR "Hasta luego."
        
      DE LO CONTRARIO:
        MOSTRAR "Opción inválida."
        
  HASTA opcion == "0"
FIN
