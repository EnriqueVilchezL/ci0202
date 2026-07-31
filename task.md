# Tarea: Convertir la sección "Ejercicios de práctica" en ejercicios ejecutables

## Contexto

Cada notebook de `material_teorico/book/<N>_tema/*.ipynb` termina con una sección
titulada (con variantes) `## 📝 Ejercicios de práctica`. Hoy en día, en casi todos
los notebooks, esa sección es **una sola celda Markdown gigante** que contiene,
para cada ejercicio, un encabezado (`**Ejercicio N.M — Título**`) seguido de un
bloque ```` ```python ```` con el enunciado escrito como comentarios (o código de
ejemplo). No son celdas de código reales: el estudiante no tiene dónde escribir su
solución, no hay retroalimentación automática, y no hay solución de referencia.

**Objetivo:** Reestructurar la sección de ejercicios de cada notebook para que
cada ejercicio individual quede compuesto por **cuatro celdas reales del
notebook**, en este orden:

1. **Celda de enunciado** (Markdown): el encabezado del ejercicio (`**Ejercicio
   N.M — Título**`) y su descripción, tal como está hoy pero sin el bloque
   ```` ```python ```` incrustado.
2. **Celda de código inicial** (code cell):
   - Si el ejercicio no depende de datos/variables provistas: una celda vacía
     con únicamente el comentario `# Su código acá`.
   - Si el ejercicio necesita código de arranque (variables ya declaradas,
     datos de entrada, un bloque "NO MODIFICAR", etc. — como en los ejercicios
     3.1, 3.2, 4.2, 4.3, 5.2 y 6.2 de `2_variables_y_valores`, o el 2.1 de
     `6_control_de_flujo_de_ejecucion`), esa celda debe contener el código de
     arranque necesario, seguido de `# Su código acá` para lo que falta por
     completar.
3. **Celda de pruebas automáticas** (code cell), colapsada para Colab:
   - La primera línea del código debe ser el comentario
     `#@title Pruebas automáticas (solo ejecutar, no modificar)`.
   - Debe usar el framework `notebook_cell_tester`
     (`from notebook_cell_tester.tester import ColabTestFramework, TestCase,
     TestSection`), siguiendo la skill **`doing-tests`** de este repo
     (`.claude/skills/doing-tests/SKILL.md`) para diseñar las secciones de
     prueba (Correctness / Edge Cases / Error Handling / Code Style /
     Variables / Functions, incluyendo solo las secciones pertinentes al
     ejercicio).
   - Metadata de la celda:
     ```json
     "metadata": {
       "cellView": "form",
       "collapsed": true
     }
     ```
   - Ver `material_practico/labs/2_variables_y_valores/laboratorio_variables_y_valores.ipynb`
     (celdas de prueba, p. ej. índice 5) como referencia exacta de formato.
4. **Celda de posible solución** (code cell), también colapsada para Colab:
   - Contiene una solución de referencia completa y correcta del ejercicio.
   - Debe iniciar con el comentario `#@title Posible solución (ejecutar para
     ver una solución de referencia)` (o similar) para que se comporte como
     celda de formulario colapsada en Colab.
   - Misma metadata que la celda de pruebas:
     ```json
     "metadata": {
       "cellView": "form",
       "collapsed": true
     }
     ```
   - La solución debe seguir el enfoque de diseño descendente
     (`material_practico/otros/top_down_approach.md`) y las convenciones de
     estilo del curso (snake_case, nombres descriptivos).

Los encabezados de subsección (`### 1️⃣ Ejercicios: ...`) y los separadores
(`---`) que agrupan ejercicios por tema deben conservarse como celdas Markdown
independientes, igual que hoy.

Al inicio de la sección de ejercicios de cada notebook (antes del primer
ejercicio) se deben agregar dos celdas, igual que en
`material_teorico/book/2_variables_y_valores/variables_y_valores.ipynb`
(celdas 63 y 64):

1. **Celda Markdown** con el texto:
   ```
   ### Pruebas automáticas

   **EJECUTE LA CELDA DE ABAJO ANTES DE EMPEZAR A EJECUTAR SU CÓDIGO**
   Esto sirve para que pueda ejecutar casos de prueba sobre su código.

   ---
   ```
2. **Celda de código** (sin metadata especial) con únicamente:
   ```python
   !pip install --upgrade --force-reinstall notebook-cell-tester --q
   ```

## Alcance: notebooks a modificar

Inspeccionado el 2026-07-30. Todos los notebooks bajo `material_teorico/book/`
que tienen sección de ejercicios de práctica y su estado actual:

| Notebook | Celda(s) de la sección hoy | Estado actual |
|---|---|---|
| `2_variables_y_valores/variables_y_valores.ipynb` | 62 | 1 celda Markdown gigante con bloques ` ```python ` como enunciados. 6 subtemas, ~14 ejercicios. |
| `3_operadores_y_expresiones/operadores_y_expresiones.ipynb` | 36 | Igual patrón. |
| `4_errores_y_pruebas/errores_y_pruebas.ipynb` | 33–34 | Igual patrón (celda 33 es contenido teórico "Solución de las Pruebas" con `assert`, no confundir con la sección de ejercicios en sí; revisar antes de tocar). |
| `5_entrada_y_salida_de_datos/entrada_y_salida_de_datos.ipynb` | 30 | Igual patrón. |
| `6_control_de_flujo_de_ejecucion/control_de_flujo_de_ejecucion.ipynb` | 103 | Igual patrón. |
| `7_subrutinas/subrutinas.ipynb` | 99 | Igual patrón — **revisar `material_practico/labs/7_subrutinas/TESTS.md`** por si hay restricciones (p. ej. prohibición de `break`/`while True`, requisito de `main`) aplicables también a estos ejercicios teóricos. |
| `8_estructuras_de_datos_fundamentales/estructuras_de_datos_fundamentales.ipynb` | 188 | Igual patrón. |
| `9_introduccion_al_uso_de_bibliotecas/introduccion_al_uso_de_bibliotecas.ipynb` | 54 | Igual patrón. |
| `10_computacion_numerica/computacion_numerica.ipynb` | 195 | Igual patrón. |
| `11_manipulacion_de_archivos/manipulacion_de_archivos.ipynb` | 111 | Igual patrón. |
| `12_visualizacion_de_datos/visualizacion_de_datos.ipynb` | celdas 76–109 | **Caso distinto**: ya tiene celdas separadas por ejercicio (enunciado, pistas colapsables, celda de código inicial, celda de pruebas con `assert`/`print` manuales) y una celda Markdown de solución dentro de un bloque `<details>` colapsable de Markdown — no una celda de código colapsada de Colab. Hay que: (a) convertir las celdas de prueba manuales a `notebook_cell_tester` con metadata `cellView/collapsed`, y (b) convertir cada bloque `<details>` de solución en una celda de código real con la metadata de colapso indicada, en vez de Markdown. |

Notebooks **sin** sección de ejercicios de práctica (no aplican a esta tarea):
`1_fundamentos_de_la_programacion/basicas_de_colab.ipynb`,
`1_fundamentos_de_la_programacion/desactivar_gemini.ipynb`.

## Notas y restricciones

- Todo el contenido nuevo debe escribirse en **español**, siguiendo las
  convenciones de `CLAUDE.md`.
- No inventar requisitos de estilo/algoritmo que el enunciado original no
  pedía: aceptar múltiples soluciones válidas en las pruebas (no fijar nombres
  de variables exactos salvo que el ejercicio los exija explícitamente).
- No testear conceptos que aún no se han enseñado en ese punto del temario
  (`material_practico/CI0202_Principios_I_2026.md` define el orden).
- Antes de escribir las pruebas de cada ejercicio, **buscar en internet la
  documentación de `notebook_cell_tester`** (no adivinar su API), tal como
  indica la skill `doing-tests`.
- Mantener el emoji/formato de encabezados existente (📝, 1️⃣, etc.) en las
  celdas de enunciado — solo se está separando el enunciado del código, no
  rediseñando el contenido pedagógico.
- Verificar, notebook por notebook, si existe un `TESTS.md` relevante en el
  lab práctico equivalente (mismo número de tema bajo
  `material_practico/labs/`) con restricciones que las pruebas deban respetar.
- Después de editar cada notebook, validar que el JSON siga siendo válido y
  que las celdas de prueba/solución realmente queden con
  `"collapsed": true` y `"cellView": "form"` en su metadata (se puede
  verificar con un script Python que cargue el `.ipynb` con `json.load` y
  revise `cell['metadata']`).

## Plan de ejecución sugerido

1. Procesar un notebook a la vez (empezar por `2_variables_y_valores`, que ya
   fue inspeccionado en detalle en esta tarea).
2. Para cada notebook, parsear la celda Markdown de ejercicios y, por cada
   ejercicio, generar las 4 celdas descritas arriba, preservando el orden y
   agrupamiento por subtema.
3. Usar la skill `doing-tests` para diseñar y escribir las pruebas de cada
   ejercicio.
4. Escribir una solución de referencia correcta y con buen estilo para cada
   ejercicio.
5. Guardar el notebook (usar `NotebookEdit` o edición directa del JSON,
   preservando `nbformat`/metadata del notebook).
6. Repetir para el resto de los notebooks listados en la tabla de alcance,
   dejando `12_visualizacion_de_datos` para el final por ser el caso con más
   diferencias estructurales respecto al resto.
