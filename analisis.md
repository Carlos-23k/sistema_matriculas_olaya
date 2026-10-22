# 1. Análisis del Problema

## 1.2. Situación Problemática
* Dificultad para localizar rápidamente la matrícula de un estudiante.
* Posibilidad de errores al escribir datos (DNI incompleto, grado o sección equivocados).
* Riesgo de registrar dos veces al mismo estudiante.
* Demora para consultar o listar a los estudiantes matriculados por grado, sección o nombre.
* Riesgo de deterioro o pérdida de los formatos físicos.

## 1.3. Problema Central
La I.E. José Olaya requiere una forma organizada de registrar, validar, buscar, ordenar y almacenar los datos de las matrículas, con el fin de reducir errores y facilitar la gestión y consulta de cada estudiante matriculado[span_6](start_span)[span_6](end_span).

## 1.4. Matriz de Entradas, Procesos y Salidas
| Entradas | Procesos | Salidas |
| :--- | :--- | :--- |
| Nombres y apellidos del estudiante | Recibir los datos del estudiante y su apoderado | Código de matrícula (`MAT-0001`, `MAT-0002`...) |
| DNI (8 dígitos) | Validar nombre, DNI, grado, sección y apoderado; evitar DNI repetido | Mensaje de confirmación o de error |
| Grado (1 a 5) y sección (A a E) | Generar el código correlativo y la fecha de matrícula | Registro almacenado en el archivo `sistema_matriculas_olaya.tx |
| Nombre del apoderado | Guardar el registro en el archivo de texto | Resultado de la búsqueda (por código o por DNI) |
| Opción elegida en el menú; código o DNI a buscar | Buscar un registro y ordenar la lista (por código o por nombre) | Listado ordenado de matrículas |
