---
title: "Enunciados anotados: resolver un problema paso a paso"
subtitle: "CI-0202 Principios de Informática"
---

# Enunciados anotados: resolver un problema paso a paso

Aquí se aplican los pasos A–E de `1_guia_de_resolucion.md` a dos problemas completos. Se muestra el **proceso mental completo antes de programar**; no se incluye el código de la solución en Python.

> **Cómo usarlo:** lea el enunciado, tape el resto, haga usted el análisis A2 y la traza A3 con la hoja de trabajo y, después, **compare** con lo que sigue.

Mientras lee, note que cada problema es **un patrón conocido con un contexto nuevo** (rampas de accesibilidad, consumo de agua). Los mismos patrones aparecen en laboratorios, tareas y evaluaciones con otros contextos.

---

# Problema 1: rampas de accesibilidad

## Enunciado

Una municipalidad revisa las **rampas de accesibilidad** de los edificios públicos. La **pendiente** $p$ (%) de una rampa se calcula con su **altura** $h$ (cm) y su **longitud horizontal** $L$ (cm):

$$p = \frac{h}{L} \cdot 100$$

Una rampa **cumple** la norma si su pendiente **no supera** la **pendiente máxima permitida** por el reglamento.

Escriba un programa en Python con las siguientes funciones:

A. `solicitar_numero_positivo(mensaje: str) -> float` **(25 %)**

   1. Muestra `mensaje` y lee un número por teclado. Si el dato no es un número (use `try except`) o es menor o igual a cero, muestra un mensaje de error y lo vuelve a solicitar. **Retorna** el número válido.

B. `calcular_pendiente(altura_cm: float, longitud_cm: float) -> float` **(15 %)**

   1. Calcula y **retorna** (no imprime) la pendiente de la rampa en porcentaje.

C. `main() -> None` **(60 %)**

   1. Solicita la pendiente máxima permitida usando `solicitar_numero_positivo`. **(5 %)**
   2. Mediante un ciclo `while`, revisa rampas mientras la persona usuaria responda `s` (mayúscula o minúscula) a la pregunta *¿Desea revisar otra rampa? (s/n):*. Se revisa al menos una rampa y cualquier respuesta distinta de `s` termina el ciclo. **(20 %)**
   3. Por cada rampa, imprime el encabezado `--- Nueva rampa ---`, solicita la altura y la longitud reutilizando `solicitar_numero_positivo`, **invoca** `calcular_pendiente` e imprime la pendiente (2 decimales) indicando si `Cumple` o `No cumple`. **(20 %)**
   4. Lleva la cuenta de la **cantidad de rampas** revisadas y de la **cantidad de rampas que cumplen**. **(10 %)**
   5. Al final, imprime un reporte con la **cantidad de rampas que cumplen** del total. **(5 %)**

### Ejemplo de ejecución

*Lo que aparece en **negrita** corresponde a lo que digita la persona usuaria*.

<pre>
Pendiente máxima permitida (%): <b>10</b>

--- Nueva rampa ---
Altura (cm): <b>50</b>
Longitud (cm): <b>600</b>
Pendiente: 8.33 % -> Cumple
¿Desea revisar otra rampa? (s/n): <b>s</b>

--- Nueva rampa ---
Altura (cm): <b>6O</b>
Error: debe ingresar un número válido mayor que cero.
Altura (cm): <b>0</b>
Error: debe ingresar un número válido mayor que cero.
Altura (cm): <b>60</b>
Longitud (cm): <b>600</b>
Pendiente: 10.00 % -> Cumple
¿Desea revisar otra rampa? (s/n): <b>S</b>

--- Nueva rampa ---
Altura (cm): <b>45</b>
Longitud (cm): <b>300</b>
Pendiente: 15.00 % -> No cumple
¿Desea revisar otra rampa? (s/n): <b>n</b>

--- Reporte ---
Rampas que cumplen: 2 de 3
</pre>

## A. Comprensión

### A2. Entradas, salidas, qué debo hacer y cómo hacerlo

| Función | Entradas | Salidas | Qué debo hacer |
|---|---|---|---|
| `solicitar_numero_positivo` | `mensaje: str`; lo que digita la persona | **retorna** `float`; **imprime** el mensaje de error | Pedir un número; si no es número o es $\le 0$, mostrar error y volver a pedir; retornar el válido |
| `calcular_pendiente` | `altura_cm`, `longitud_cm` | **retorna** `float` (%); **no** imprime | Dividir la altura entre la longitud y multiplicar por 100 |
| `main` | lo que digita la persona (pendiente máxima, altura, longitud, respuesta `s`/otra) | **imprime** encabezados, pendiente con `Cumple`/`No cumple`, reporte final | Pedir la pendiente máxima; repetir por cada rampa (pedir datos, calcular, comparar, contar); al final, reportar |

**Cómo lo hago**

| Función | Cómo uso las entradas | Cómo creo lo que retorno |
|---|---|---|
| `solicitar_numero_positivo` | `mensaje` se muestra **cada vez** que se pide el dato, también después de un error | el número nace **dentro de un ciclo**: se convierte lo digitado y se retorna cuando es válido (> 0) |
| `calcular_pendiente` | la altura va **arriba** de la división y la longitud **abajo**; el resultado se multiplica por 100 | `pendiente` nace de **una asignación** con la fórmula; no hace falta ciclo ni valor inicial |
| `main` | la pendiente máxima se guarda **antes** del ciclo y se compara con la pendiente de **cada** rampa; altura y longitud se pasan a `calcular_pendiente`; la respuesta controla el ciclo | **no aplica**: no retorna. Lo que construye son **dos contadores** (empiezan en 0 y suman 1) que usa en el reporte |

**Una frase por función**

- `solicitar_numero_positivo`: *recibe un texto, pide un número hasta que sea válido (> 0) y lo retorna.*
- `calcular_pendiente`: *recibe altura y longitud, calcula con la fórmula y retorna la pendiente.*
- `main`: *pide la pendiente máxima y, por cada rampa, pide los datos, calcula, compara y cuenta; al final imprime cuántas cumplen del total.*

**Detalle del contexto que cambia el "qué hacer":** "una rampa **cumple** si su pendiente **no supera** la máxima". Esa comparación aparece en el contexto, no en la lista de funciones, y está escrita en negativo: "no supera" significa **menor o igual** (`<=`). Si hay duda, el ejemplo la resuelve (A3).

### A3. Traza del ejemplo, línea por línea

Cada fila ejecuta una línea del ejemplo contra las funciones.

| # | Línea del ejemplo | Tipo | Responsable | Qué entra y qué sale | ¿Coincide con A2? |
|---|---|---|---|---|---|
| 1 | `Pendiente máxima permitida (%): 10` | [D] | `main` llama a `solicitar_numero_positivo` | recibe el mensaje; retorna `10.0` → `maxima = 10.0` | sí |
| 2 | *(línea en blanco)* y `--- Nueva rampa ---` | [P] | `main` | imprime la línea en blanco y el encabezado | el texto decía el encabezado; **la línea en blanco solo se ve en el ejemplo** |
| 3 | `Altura (cm): 50` | [D] | `main` → `solicitar_numero_positivo` | retorna `50.0` | sí; se reutiliza la misma función |
| 4 | `Longitud (cm): 600` | [D] | `main` → `solicitar_numero_positivo` | retorna `600.0` | sí |
| 5 | `Pendiente: 8.33 % -> Cumple` | [P] | `main` | `calcular_pendiente(50.0, 600.0)`: $50/600 \cdot 100 = 8.33$; $8.33 \le 10$ → `Cumple`; contadores: revisadas 1, cumplen 1 | **sí: la fórmula está bien entendida** |
| 6 | `¿Desea revisar otra rampa? (s/n): s` | [D] | `main` | `respuesta = "s"` → el ciclo continúa | sí |
| 7 | *(bloque 2)* `Altura (cm): 6O` | [D] | `solicitar_numero_positivo` | `"6O"` (con la letra O) no es número → **la función imprime** `Error: debe ingresar un número válido mayor que cero.` | **el error sale de la función auxiliar, no de `main`** |
| 8 | `Altura (cm): 0` | [D] | `solicitar_numero_positivo` | `0` es número pero $\le 0$ → imprime el error otra vez | sí; **se vuelve a pedir con el mismo mensaje** |
| 9 | `Altura (cm): 60` | [D] | `solicitar_numero_positivo` | válido; retorna `60.0` | sí |
| 10 | `Longitud (cm): 600` y `Pendiente: 10.00 % -> Cumple` | [D], [P] | `main` | $60/600 \cdot 100 = 10.00$; **exactamente igual** a la máxima → `Cumple`; revisadas 2, cumplen 2 | **sí: confirma que "no supera" es `<=`** |
| 11 | `¿Desea revisar otra rampa? (s/n): S` | [D] | `main` | `"S"` mayúscula → el ciclo continúa | sí: **hay que pasar la respuesta a minúscula** |
| 12 | *(bloque 3)* `45` y `300` → `Pendiente: 15.00 % -> No cumple` | [D], [P] | `main` | $45/300 \cdot 100 = 15.00 > 10$ → `No cumple`; revisadas 3, cumplen 2 | sí |
| 13 | `¿Desea ...?: n` | [D] | `main` | `respuesta = "n"` → el ciclo termina | sí |
| 14 | *(línea en blanco)*, `--- Reporte ---`, `Rampas que cumplen: 2 de 3` | [P] | `main` | usa los dos contadores | sí: **hacen falta dos contadores** |

**Lo que la traza reveló y el texto no decía**

1. Hay una **línea en blanco** antes de cada encabezado y antes del reporte.
2. Los mensajes de error **salen de `solicitar_numero_positivo`**, no de `main`.
3. `solicitar_numero_positivo` se usa **tres veces** (pendiente máxima, altura, longitud).
4. Una pendiente **igual** a la máxima cumple: la comparación es `<=`.
5. Hacen falta **dos contadores** (revisadas y cumplen).

## B. Descomposición

| Función | Subtareas | Patrón |
|---|---|---|
| `solicitar_numero_positivo` | (1) pedir el dato; (2) decidir si es número; (3) decidir si es > 0; (4) repetir si falla; (5) retornar | Validación con ciclo |
| `calcular_pendiente` | (1) aplicar la fórmula; (2) retornar | Cálculo directo |
| `main` | (1) pedir la máxima; (2) preparar contadores; (3) ciclo por rampa: encabezado, datos, cálculo, decisión, conteo, pregunta; (4) reporte | Ciclo controlado por respuesta, **dos contadores** |

## C. Algoritmo en pseudocódigo

Cada línea describe **lo que debe hacer una línea del programa**. Se obtiene leyendo el ejemplo de arriba abajo (técnica de `1b_como_escribir_pseudocodigo.md`, sección 3).

```text
main:
    Pedir la pendiente máxima con solicitar_numero_positivo y guardarla
    Poner en cero el contador de rampas revisadas
    Poner en cero el contador de rampas que cumplen
    Dejar la respuesta en "s" para que el ciclo se ejecute al menos una vez
    Mientras la respuesta sea "s":
        Mostrar una línea en blanco
        Mostrar el encabezado "--- Nueva rampa ---"
        Pedir la altura con solicitar_numero_positivo
        Pedir la longitud con solicitar_numero_positivo
        Calcular la pendiente llamando a calcular_pendiente con la altura y la longitud
        Sumar 1 al contador de rampas revisadas
        Si la pendiente es menor o igual a la máxima:
            Mostrar la pendiente con 2 decimales y "Cumple"
            Sumar 1 al contador de rampas que cumplen
        Si no:
            Mostrar la pendiente con 2 decimales y "No cumple"
        Preguntar si desea revisar otra rampa y guardar la respuesta en minúscula
    Mostrar una línea en blanco
    Mostrar el encabezado "--- Reporte ---"
    Mostrar cuántas rampas cumplen de cuántas se revisaron
```

```text
solicitar_numero_positivo(mensaje):
    Marcar que todavía no hay un número válido
    Mientras no haya un número válido:
        Intentar convertir a número lo que la persona digita al ver el mensaje
            Si el número es mayor que cero, marcar que ya es válido
            Si no, mostrar "Error: debe ingresar un número válido mayor que cero."
        Si lo digitado no se pudo convertir:
            Mostrar el mismo mensaje de error
    Retornar el número válido

calcular_pendiente(altura, longitud):
    Calcular la pendiente: dividir la altura entre la longitud y multiplicar por 100
    Retornar la pendiente
```

## E. Validación

1. **Reproduzca el ejemplo** (el ejemplo de este documento es el número 1):

```sh
python reproducir_ejemplo.py 2_enunciados_anotados.md mi_solucion.py --ejemplo 1
```

2. **Casos propios**

| Caso | Qué debe pasar | Qué pone a prueba |
|---|---|---|
| Una pendiente **exactamente igual** a la máxima | `Cumple` | "no supera" = `<=` |
| Una sola vuelta (`n` de inmediato) | `Rampas que cumplen: X de 1` | "al menos una rampa" |
| `S` mayúscula | continúa | "mayúscula o minúscula" |
| Cualquier otra respuesta (`x`, vacío) | termina | "cualquier respuesta distinta de `s`" |

3. **Lista de chequeo**

- [ ] `calcular_pendiente` retorna y **no** imprime.
- [ ] `solicitar_numero_positivo` se usa para **los tres** datos.
- [ ] La comparación es `<=`.
- [ ] El ciclo se ejecuta al menos una vez y termina con cualquier respuesta distinta de `s`.
- [ ] Hay **dos** contadores y el reporte dice "X de Y".

---

# Problema 2: consumo de agua de un condominio

## Enunciado

La administración de un condominio registra el **consumo diario de agua** (m³) para detectar fugas. Un día es de **consumo alto** si su consumo supera el promedio de todos los días registrados en más del **margen** indicado (en porcentaje).

Escriba un programa en Python con las siguientes funciones:

A. `solicitar_numero_no_negativo(mensaje: str) -> float` **(25 %)**

   1. Muestra `mensaje` y lee un número por teclado. Si el dato no es un número (use `try except`) o es negativo, muestra un mensaje de error y lo vuelve a solicitar. **Retorna** el número válido.

B. `buscar_dias_de_alto_consumo(consumos: list, margen: float) -> list` **(35 %)**

   1. **Retorna** (no imprime) una lista de tuplas `(dia, consumo)` con los días de consumo alto, en el orden en que se registraron.

C. `main() -> None` **(40 %)**

   1. Solicita el margen usando `solicitar_numero_no_negativo`. **(5 %)**
   2. Mediante un ciclo `while`, registra el consumo de cada día en una lista mientras la persona usuaria responda `s` (mayúscula o minúscula) a la pregunta *¿Desea registrar otro día? (s/n):*. Se registra al menos un día. **(15 %)**
   3. **Invoca** `buscar_dias_de_alto_consumo` e imprime cada día de consumo alto (consumo con 2 decimales) y la cantidad total. **(20 %)**

### Ejemplo de ejecución

*Lo que aparece en **negrita** corresponde a lo que digita la persona usuaria*.

<pre>
Margen (%): <b>-5</b>
Error: debe ingresar un número mayor o igual a cero.
Margen (%): <b>20</b>
Consumo del día (m³): <b>12.5</b>
¿Desea registrar otro día? (s/n): <b>s</b>
Consumo del día (m³): <b>doce</b>
Error: debe ingresar un número mayor o igual a cero.
Consumo del día (m³): <b>0</b>
¿Desea registrar otro día? (s/n): <b>s</b>
Consumo del día (m³): <b>14</b>
¿Desea registrar otro día? (s/n): <b>s</b>
Consumo del día (m³): <b>18.5</b>
¿Desea registrar otro día? (s/n): <b>s</b>
Consumo del día (m³): <b>15</b>
¿Desea registrar otro día? (s/n): <b>n</b>

Días de consumo alto:
Día 4: 18.50 m³
Día 5: 15.00 m³
Total: 2 día(s)
</pre>

## A. Comprensión

### A2. Entradas, salidas, qué debo hacer y cómo hacerlo

| Función | Entradas | Salidas | Qué debo hacer |
|---|---|---|---|
| `solicitar_numero_no_negativo` | `mensaje: str`; lo que digita la persona | **retorna** `float` (puede ser 0); **imprime** el error | Pedir un número; si no es número o es negativo, mostrar error y volver a pedir |
| `buscar_dias_de_alto_consumo` | `consumos: list`, `margen: float` | **retorna** `list` de tuplas `(dia, consumo)`; **no** imprime | Calcular el promedio de **todos** los consumos; recorrer y quedarse con los días de consumo alto |
| `main` | margen, consumos, respuesta `s`/otra | **imprime** una línea por día de consumo alto y el total | Pedir el margen; construir la lista de consumos con un ciclo; llamar a `buscar_dias_de_alto_consumo`; imprimir |

**Cómo lo hago**

| Función | Cómo uso las entradas | Cómo creo lo que retorno |
|---|---|---|
| `solicitar_numero_no_negativo` | `mensaje` se muestra cada vez que se pide el dato | el número nace **dentro de un ciclo** y se retorna cuando es válido ($\ge 0$) |
| `buscar_dias_de_alto_consumo` | `consumos` se recorre **dos veces**: una para sumar y sacar el promedio, otra para comparar cada día; `margen` dice **cuánto más** que el promedio debe ser un consumo para ser alto (la forma exacta se decide en A3) | la lista de días empieza **vacía** antes del segundo recorrido y se le **agrega** una tupla `(dia, consumo)` cada vez que un día es alto (qué número es `dia` también se decide en A3) |
| `main` | el margen se pide antes del ciclo y **no se usa** en `main`: solo se le pasa a la función; cada consumo se **agrega** a la lista | **no aplica**: no retorna. Construye la lista de consumos (empieza **vacía** y se llena en el ciclo) y recorre la lista que retorna la función |

**Frases**

- `solicitar_numero_no_negativo`: *recibe un texto, pide un número (cero o positivo) hasta que sea válido y lo retorna.*
- `buscar_dias_de_alto_consumo`: *recibe la lista y el margen, y retorna las tuplas (día, consumo) de los días de consumo alto.*
- `main`: *pide el margen y los consumos, llama a `buscar_dias_de_alto_consumo` e imprime los días y su cantidad.*

**Atención al "qué hacer":** "supera el promedio en más del margen (en porcentaje)" admite **varias lecturas**. ¿Porcentaje **de qué**?

- **Lectura A:** porcentaje **del promedio**: el consumo es alto si es mayor que $\text{promedio} \cdot (1 + \text{margen}/100)$.
- **Lectura B:** porcentaje **del consumo del día**: la diferencia $\text{consumo} - \text{promedio}$ es mayor que el margen % del consumo.
- **Lectura C:** el margen se **suma** tal cual: consumo $> \text{promedio} + \text{margen}$.

Además, ¿qué es `dia`: la **posición** en la lista (empieza en 0) o el número de día (empieza en 1)? Las dos dudas se resuelven en A3.

### A3. Traza del ejemplo, línea por línea

**Parte 1: construir la lista (`main` y `solicitar_numero_no_negativo`)**

| # | Línea del ejemplo | Tipo | Responsable | Qué entra y qué sale |
|---|---|---|---|---|
| 1 | `Margen (%): -5` | [D] | `main` → `solicitar_numero_no_negativo` | `-5` es negativo → la función imprime el error |
| 2 | `Margen (%): 20` | [D] | `solicitar_numero_no_negativo` | retorna `20.0` → `margen = 20.0` |
| 3 | `Consumo del día (m³): 12.5` y `s` | [D] | `main` → `solicitar_numero_no_negativo` | `consumos = [12.5]`; continúa |
| 4 | `Consumo del día (m³): doce` | [D] | `solicitar_numero_no_negativo` | `"doce"` no es número → imprime el error y vuelve a pedir |
| 5 | `Consumo del día (m³): 0` | [D] | `solicitar_numero_no_negativo` | retorna `0.0` → **el cero se acepta** (a diferencia del problema 1); `consumos = [12.5, 0.0]` |
| 6 | `14`, `18.5`, `15` y al final `n` | [D] | `main` | `consumos = [12.5, 0.0, 14.0, 18.5, 15.0]`; el ciclo termina |

**Parte 2: ejecutar `buscar_dias_de_alto_consumo([12.5, 0.0, 14.0, 18.5, 15.0], 20.0)` con cada lectura**

Primero, el promedio de **todos**: $(12.5 + 0 + 14 + 18.5 + 15)/5 = 60/5 = 12$.

| Posición | Consumo | Lectura **A**: ¿$c > 12 \cdot 1.2 = 14.4$? | Lectura **B**: ¿$(c - 12)/c > 20\%$? | Lectura **C**: ¿$c > 12 + 20 = 32$? |
|---|---|---|---|---|
| 0 | `12.5` | no | $0.5/12.5 = 4\%$ → no | no |
| 1 | `0` | no | no | no |
| 2 | `14` | no | $2/14 = 14.3\%$ → no | no |
| 3 | `18.5` | sí | $6.5/18.5 = 35.1\%$ → sí | no |
| 4 | `15` | sí | $3/15 = 20\%$, **no** es mayor → no | no |
| **Resultado** | | **2 días** | **1 día** | **0 días** |

**Parte 3: comparar con la salida del ejemplo**

| # | Línea del ejemplo | Responsable | ¿Qué lectura la produce? |
|---|---|---|---|
| 7 | *(línea en blanco)* y `Días de consumo alto:` | `main` (después de llamar a la función) | indiferente |
| 8 | `Día 4: 18.50 m³` | `main` recorre la lista retornada | A y B |
| 9 | `Día 5: 15.00 m³` | `main` | **solo A** |
| 10 | `Total: 2 día(s)` | `main` | **solo A** |

> **Conclusión:** solo la lectura **A** (porcentaje del promedio) reproduce el ejemplo. **El ejemplo manda.** Y el consumo `18.5`, que está en la **posición 3**, se imprime como `Día 4`: el número de día es **posición + 1**. (Ambas cosas se pueden comprobar con `reproducir_ejemplo.py`: una solución con la lectura B, o que use la posición como día, falla este ejemplo.)

**Lo que la traza reveló**

1. `solicitar_numero_no_negativo` **acepta el cero**: no se copia la validación `> 0` del problema 1.
2. El promedio es de **todos** los días: se necesita **antes** de decidir sobre cada uno.
3. El margen es un porcentaje **del promedio**.
4. El día se cuenta **desde 1**; la posición en la lista, desde 0.
5. `main` llama a la función **después** del ciclo, y hay una línea en blanco antes del encabezado de resultados.

## B. Descomposición

| Función | Subtareas | Patrón |
|---|---|---|
| `solicitar_numero_no_negativo` | pedir el dato; decidir si es número y no negativo; repetir; retornar | Validación con ciclo |
| `buscar_dias_de_alto_consumo` | (1) calcular el promedio de todos; (2) calcular el umbral; (3) recorrer con posición; (4) decidir si es alto; (5) agregar `(posición + 1, consumo)`; (6) retornar | **Acumulador** (suma), **recorrido con índice**, **filtro** |
| `main` | (1) pedir margen; (2) ciclo que agrega consumos; (3) llamar a la función; (4) imprimir una línea por día y el total | Ciclo controlado por respuesta, recorrido |

> `buscar_dias_de_alto_consumo` hace **dos tareas con dos recorridos**: el promedio no puede calcularse "sobre la marcha", porque hasta el último día no se conoce.

## C. Algoritmo en pseudocódigo

El de `buscar_dias_de_alto_consumo`, escrito en tres pasadas, está en `1b_como_escribir_pseudocodigo.md`, sección 4. Aquí, el de `main`, derivado de la traza (partes 1 y 3):

```text
main:
    Pedir el margen con solicitar_numero_no_negativo y guardarlo
    Crear una lista vacía para los consumos
    Dejar la respuesta en "s" para que el ciclo se ejecute al menos una vez
    Mientras la respuesta sea "s":
        Pedir el consumo del día con solicitar_numero_no_negativo y agregarlo a la lista
        Preguntar si desea registrar otro día y guardar la respuesta en minúscula
    Llamar a buscar_dias_de_alto_consumo con la lista y el margen, y guardar los días que retorna
    Mostrar una línea en blanco
    Mostrar el encabezado "Días de consumo alto:"
    Para cada día y consumo de la lista de días:
        Mostrar "Día", el número de día y el consumo con 2 decimales
    Mostrar el total, que es la cantidad de elementos de la lista de días
```

## E. Validación

1. **Reproduzca el ejemplo** (el ejemplo de este problema es el número 2):

```sh
python reproducir_ejemplo.py 2_enunciados_anotados.md mi_solucion.py --ejemplo 2
```

2. **Casos propios**

| `consumos`, `margen` | Promedio y umbral | Resultado esperado de `buscar_dias_de_alto_consumo` | Qué pone a prueba |
|---|---|---|---|
| `[10]`, `0` | `10`, `10` | `[]` | $10 > 10$ es falso: la comparación es **estricta** |
| `[0, 0]`, `20` | `0`, `0` | `[]` | retorna lista vacía, **no** `None`; no hay división entre cero |
| `[10, 20]`, `0` | `15`, `15` | `[(2, 20)]` | el día se numera desde 1 |
| `[10, 10, 13]`, `18` | `11`, `12.98` | `[(3, 13)]` | el umbral usa el porcentaje **del promedio** (con el porcentaje del día, 13 no sería alto) |

3. **Lista de chequeo**

- [ ] `solicitar_numero_no_negativo` **acepta** el cero y rechaza negativos.
- [ ] El promedio es de **todos** los días y se calcula **antes** de filtrar.
- [ ] Comparé con `>` (estricto) contra promedio × (1 + margen / 100).
- [ ] La tupla guarda el **número de día** (posición + 1) y el consumo.
- [ ] `buscar_dias_de_alto_consumo` retorna y no imprime; `main` guarda lo que retorna y lo **recorre** para imprimir.

---

# Lo que se repite en casi todos los problemas

| Lo que casi siempre pasa | Cómo se detecta |
|---|---|
| Una función **retorna** y otra **imprime** | Columna **Salidas** del paso A2 |
| Una regla escondida en el **contexto** | La traza (A3) no cuadra con el ejemplo |
| Un texto con **dos lecturas posibles** | Ejecute el ejemplo con cada lectura (como en el problema 2) |
| Una función auxiliar se **reutiliza** varias veces | La traza muestra la misma función en varias filas |
| El ejemplo muestra algo que el texto no dice | La lista "lo que la traza reveló" |
| Un ciclo que se ejecuta "al menos una vez" | Dejar la respuesta en `"s"` antes del ciclo |
| Contar desde 1 para la persona y desde 0 en la lista | El ejemplo imprime un número que no coincide con la posición |
| Dos tareas mezcladas en una función | Paso B: la lista de subtareas tiene más de una tarea con su propio recorrido |
