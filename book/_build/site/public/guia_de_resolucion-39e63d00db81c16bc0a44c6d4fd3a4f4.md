---
title: "Cómo resolver un problema de programación"
subtitle: "Guía de pensamiento computacional — CI-0202 Principios de Informática"
---

> **Idea central:** programar es el **cuarto** paso, no el primero. Quien empieza a teclear sin haber entendido el problema suele terminar borrando y reescribiendo funciones. Los tres pasos que preceden al código se hacen **en papel** y son los que ahorran tiempo.

Esta guía usa la misma metodología de pensamiento computacional del curso. Sirve igual para un laboratorio, una tarea o una evaluación en papel:

| Paso | Nombre | Se hace en | Pregunta que responde |
|---|---|---|---|
| **A** | **Comprensión** | papel | ¿Qué recibo, qué debo entregar y qué debo hacer? ¿Entiendo el ejemplo? |
| **B** | **Descomposición** | papel | ¿En qué partes pequeñas se divide? |
| **C** | **Algoritmo (pseudocódigo)** | papel | ¿Qué debe hacer cada línea? |
| **D** | **Codificación** | computador / hoja | ¿Cómo se escribe cada paso en Python? |
| **E** | **Validación** | computador / hoja | ¿Hace lo que el ejemplo muestra? |

## Reparto de tiempo sugerido (con tiempo limitado)

| Paso | A | B | C | D | E |
|---|---|---|---|---|---|
| **Porcentaje del tiempo** | 15 % | 10 % | 15 % | 45 % | 15 % |

Los pasos A, B y C suman cerca del **40 %** del tiempo. Parece mucho, pero es el tiempo que se recupera al no reescribir. Si dispone de 40 minutos, son unos 16 minutos antes de escribir la primera línea de Python.

Los ejemplos de esta guía vienen de dos problemas que se resuelven completos en la sección *Enunciados anotados*: **rampas de accesibilidad** y **consumo de agua de un condominio**.

---

# A. Comprensión

## A1. Lea todo, una vez, sin escribir código

Lea el contexto, la lista de funciones, el **ejemplo de ejecución** y las notas finales. No decida nada todavía.

## A2. Identifique entradas, salidas, qué debo hacer y cómo hacerlo

Para **cada función** (y para el programa completo), complete esta tabla. Es el corazón de la comprensión.

| | Pregunta | Cómo se encuentra |
|---|---|---|
| **Entradas** | ¿Qué recibe? ¿De qué tipo? | Los **parámetros** de la función; o lo que **digita** la persona usuaria |
| **Salidas** | ¿Qué entrega? ¿Lo **retorna** o lo **imprime**? | La palabra "retorna" o "imprime"/"muestra"; el tipo de retorno |
| **Qué debo hacer** | ¿Qué proceso transforma las entradas en las salidas? | Los **verbos** del enunciado: calcular, validar, repetir, contar, buscar, comparar... |
| **Cómo uso las entradas** | ¿Qué papel cumple **cada** entrada en lo que debo hacer? ¿Dónde aparece: en una fórmula, en una comparación, se recorre? | La fórmula o la regla del contexto; el ejemplo de ejecución |
| **Cómo creo lo que retorno** *(si retorna algo)* | ¿Cómo nace la variable que retorno: con una fórmula, empieza en 0 y se acumula, empieza como lista vacía y se llena...? | El tipo de retorno y la palabra que describe el resultado ("cantidad", "total", "lista de...", "si es...") |

Las dos últimas preguntas son el puente entre **entender** y **programar**: si las puede responder, ya tiene la mitad del pseudocódigo. Si la función solo imprime (como suele pasar con `main`), la última pregunta **no aplica**.

### Cómo se suele crear lo que se retorna

| Si se retorna... | La variable se crea así |
|---|---|
| Un valor calculado con una fórmula | **Una asignación** con la fórmula, usando las entradas |
| Una cantidad ("cuántos...") | Empieza en **0** antes del ciclo y **suma 1** cada vez que se cumple la condición |
| Un total o un promedio | Empieza en **0** y **acumula** en cada vuelta; el promedio se calcula al final |
| Una lista ("los que cumplen...") | Empieza como **lista vacía** y se **agrega** cada elemento que cumple |
| Un sí o un no (`bool`) | Una **comparación** con las entradas (o una variable que empieza en un valor y cambia si ocurre algo) |
| Un dato válido digitado por la persona | Se pide **dentro de un ciclo** y se retorna cuando cumple la validación |
| El mayor o el menor | Empieza con el **primer** elemento y se **reemplaza** si aparece uno mejor |

Termine con **una frase** por función:

> *"Esta función **recibe** ______ (tipo), **hace** ______ y **retorna / imprime** ______ (tipo)."*

Si no puede completar la frase, todavía no la entendió. Relea ese ítem.

**Ejemplo 1** (problema de las rampas, función `calcular_pendiente`):

| Pregunta | Respuesta |
|---|---|
| Entradas | `altura_cm` (float), `longitud_cm` (float) |
| Salidas | **retorna** la pendiente en % (float); no imprime |
| Qué debo hacer | calcular la pendiente con la fórmula del enunciado |
| Cómo uso las entradas | la altura va **arriba** de la división y la longitud **abajo**; el resultado se multiplica por 100 |
| Cómo creo lo que retorno | `pendiente` nace de **una asignación** con la fórmula; no hace falta ciclo ni valor inicial |

> **Frase:** "Recibe la altura y la longitud de la rampa, calcula la pendiente con la fórmula del enunciado y **retorna** el porcentaje."

**Ejemplo 2** (problema del consumo de agua, función `buscar_dias_de_alto_consumo`):

| Pregunta | Respuesta |
|---|---|
| Entradas | `consumos` (lista de float), `margen` (float, en %) |
| Salidas | **retorna** una lista de tuplas `(dia, consumo)`; no imprime |
| Qué debo hacer | encontrar los días cuyo consumo supera el promedio en más del margen |
| Cómo uso las entradas | `consumos` se recorre **dos veces**: una para sumar y sacar el promedio, otra para comparar cada día; `margen` se usa para calcular el umbral (promedio más el margen por ciento del promedio) |
| Cómo creo lo que retorno | la lista de días empieza **vacía** antes del segundo recorrido y se le **agrega** `(posición + 1, consumo)` cada vez que un día supera el umbral |

> **Frase:** "Recibe los consumos y el margen, compara cada día contra el promedio aumentado en el margen y **retorna** la lista de días de consumo alto."

### Detalles que conviene verificar siempre

Las palabras exactas del enunciado deciden detalles del "qué debo hacer". Si alguna le genera duda, **el ejemplo de ejecución la resuelve** (paso A3).

| Duda frecuente | Cómo se resuelve |
|---|---|
| **Retornar** o **imprimir** | "Retorna" = devuelve un valor a quien llamó. "Imprime" = lo muestra en pantalla. Una función con "retorna (no imprime)" **no** debe tener `print`. |
| **Mayor** o **mayor o igual** (y menor/menor o igual) | "supera", "mayor que" = `>`. "al menos", "mayor o igual" = `>=`. "no supera", "como máximo" = `<=`. |
| ¿Cuántas veces se repite algo? | "al menos una vez" = el ciclo se ejecuta antes de preguntar si continúa. |
| ¿Se pide **reutilizar** una función? | "reutilizando", "invoca", "usando" = llamar a la función, no copiar su lógica. |
| ¿Desde dónde se cuenta? | "día 1", "el primer elemento" = para la persona se empieza en 1; en una lista de Python, en 0. |

## A3. Analice y "ejecute" el ejemplo de ejecución

Este paso es lo que más ayuda y lo que casi nadie hace. **El ejemplo de ejecución es el mejor documento del enunciado**: muestra, línea por línea, qué ocurre. Se va a "ejecutar" **a mano** contra las funciones que el enunciado pide, **sin haber escrito nada de código**.

### Paso a paso

**1. Etiquete cada línea del ejemplo.**

- `[D]` = lo que **digita** la persona usuaria (aparece en **negrita**).
- `[P]` = lo que el programa **imprime**.

**2. Asigne un "responsable" a cada línea.** Pregúntese *"¿qué función produce esta línea?"* y anote **qué recibe y qué retorna**:

- ¿La imprime `main`? ¿O una función auxiliar?
- ¿Qué función se **llama** en este punto? ¿Con qué argumentos? ¿Qué retorna?

**3. Haga los cálculos que el ejemplo muestra** (con las fórmulas o la lógica del enunciado) y **compárelos** con lo que el ejemplo imprime. Si coinciden, su comprensión del "qué debo hacer" es correcta. Si **no** coinciden, hay algo mal en su comprensión: vuelva a A2.

**4. Anote lo que el ejemplo revela y el texto no dice**: líneas en blanco, de dónde sale un mensaje de error, qué se vuelve a pedir y cuántas veces, en qué orden salen las cosas.

### Formato de la traza

| # | Línea del ejemplo | Tipo | Responsable | Qué entra y qué sale | ¿Coincide con A2? |
|--|------------------|---|----------------------|------------------------|-------|
| 1 | `Altura (cm): 50` | [D] | `solicitar_numero_positivo` (llamada desde `main`) | recibe el mensaje; retorna 50.0 | sí |
| 2 | `Pendiente: 8.33 % -> Cumple` | [P] | `main` | `calcular_pendiente(50.0, 600.0)` retorna 8.33; 8.33 no supera 10 | sí |

### Reglas de oro del ejemplo

> 1. **Si el texto es ambiguo, el ejemplo manda.** Ejecute el ejemplo con cada lectura posible y quédese con la que reproduce la salida.
> 2. **Todo lo que está en el ejemplo es un requisito**, aunque el texto no lo diga (por ejemplo, una línea en blanco antes de un encabezado).
> 3. **Un error de lectura se descubre aquí**, con lápiz, y no después de escribir 40 líneas de código.

En la sección *Enunciados anotados* hay dos trazas completas.

---

# B. Descomposición

Un problema grande se resuelve **dividiéndolo**. El enunciado ya lo divide en funciones, pero dentro de cada función casi siempre hay **más de una tarea**.

## B1. Divida cada función en subtareas

Escriba una **lista numerada** con lo que hay que lograr, sin pensar aún en cómo.

**Ejemplo** (`buscar_dias_de_alto_consumo`, problema del consumo de agua):

1. Calcular el promedio de **todos** los consumos.
2. Recorrer los consumos y decidir cuáles son altos.
3. Guardar los días de consumo alto con su número de día.
4. Retornar la lista de días.

> Cuando una función mezcla dos tareas (aquí, "promedio" y "filtrar"), hay que **separarlas** en la cabeza o en el papel. Mezclarlas es la causa más frecuente de enredarse.

## B2. En `main`, use los bloques del ejemplo

Los bloques que se **repiten** en el ejemplo son un ciclo; los bloques que ocurren **una vez** al inicio o al final son preparación o reporte.

| En el ejemplo se ve... | En el algoritmo es... |
|---|---|
| Un dato que se pide una sola vez al inicio | una llamada antes del ciclo |
| Un bloque que se repite (encabezado, datos, resultado, pregunta "¿otro?") | el **cuerpo** de un ciclo |
| Un resumen al final | instrucciones **después** del ciclo |

## B3. Reconozca patrones

Casi todos los problemas del curso son un **patrón conocido** con un contexto nuevo. Reconocerlo ahorra pensar desde cero.

| Si el enunciado dice... | El patrón probable es... |
|---|---|
| "si no es válido, vuelve a pedirlo" | **Validación con ciclo** (`while` + `try`/`except`) |
| "mientras responda `s`", "repite hasta..." | **Ciclo controlado por respuesta** (centinela) |
| "cuántos...", "la cantidad de..." | **Contador** (inicia en 0, suma 1 cuando se cumple) |
| "el total de...", "el promedio de..." | **Acumulador** (inicia en 0, suma en cada vuelta) |
| "para cada elemento de la lista..." | **Recorrido** (`for`) |
| "las posiciones donde...", "los que cumplen..." | **Filtro**: lista que se va llenando con los que cumplen |
| "el mayor", "el menor" | **Máximo / mínimo** (se compara contra el mejor hasta ahora) |

---

# C. Algoritmo en pseudocódigo

**Haga siempre pseudocódigo antes de programar.** No es un trámite: es el momento en que usted **decide** cómo resuelve el problema, sin distraerse con la sintaxis de Python. Si hay un error de lógica, es mucho más fácil corregirlo aquí (borrar una línea) que en el código.

El pseudocódigo del curso se escribe en **español común**: cada línea es una frase que **describe lo que debe hacer una línea del programa**. No hace falta aprender palabras clave especiales; la sangría muestra qué va dentro de un ciclo o de una decisión. Por ejemplo:

```text
calcular_pendiente(altura, longitud):
    Calcular la pendiente: dividir la altura entre la longitud y multiplicar por 100
    Retornar la pendiente
```

## Un ejemplo con ciclos

`buscar_dias_de_alto_consumo` (problema del consumo de agua) tiene dos recorridos, una decisión y una lista que se va llenando. Observe cómo las respuestas del paso A2 se convierten casi directamente en líneas:

```text
buscar_dias_de_alto_consumo(consumos, margen):
    Poner la suma en cero
    Para cada consumo de la lista:
        Sumarle el consumo a la suma
    Calcular el promedio: dividir la suma entre la cantidad de consumos
    Calcular el umbral: el promedio más el margen por ciento del promedio
    Crear una lista vacía para los días de consumo alto
    Para cada posición de la lista de consumos, desde la primera hasta la última:
        Si el consumo en esa posición es mayor que el umbral:
            Agregar a la lista la tupla (posición + 1, consumo)
    Retornar la lista de días de consumo alto
```

| Respuesta del paso A2 | Líneas del pseudocódigo que salen de ella |
|---|---|
| *Cómo uso las entradas:* `consumos` se recorre **dos veces**, primero para el promedio | `Poner la suma en cero` y el primer `Para cada...` (acumulador) |
| *Cómo uso las entradas:* `margen` define cuánto más que el promedio es "alto" | `Calcular el umbral...` |
| *Cómo creo lo que retorno:* la lista empieza **vacía** y se **agrega** cada día alto | `Crear una lista vacía...`, el segundo `Para cada...`, el `Si...` y `Agregar...` |
| *Salidas:* **retorna** una lista; no imprime | `Retornar la lista...`, **fuera** de los dos ciclos y sin ningún "Mostrar" |

Note tres detalles que el pseudocódigo deja resueltos antes de escribir Python:

1. La suma se pone en cero **antes** del primer ciclo y el promedio se calcula **después** de él, no adentro.
2. El segundo ciclo recorre **posiciones**, porque la tupla necesita el número de día (posición + 1), no solo el consumo.
3. El *Retornar* tiene la misma sangría que la primera línea: está **fuera** de los ciclos.

## C1. Pruebe su pseudocódigo con el ejemplo

Antes de programar, **ejecute su pseudocódigo** con los datos del ejemplo (otra vez el paso A3, pero ahora contra **sus** pasos). Si el pseudocódigo produce el mismo resultado que el ejemplo, la lógica es correcta.

**Ejemplo:** el pseudocódigo anterior con `consumos = [12.5, 0, 14, 18.5, 15]` y `margen = 20`.

Primer ciclo: la suma pasa por 12.5, 12.5, 26.5, 45 y 60. Promedio $= 60 / 5 = 12$. Umbral $= 12 + 20\% \text{ de } 12 = 14.4$.

| Posición | Consumo | ¿Mayor que 14.4? | Lista de días después de la vuelta |
|---|---|---|---|
| 0 | 12.5 | no | `[]` |
| 1 | 0 | no | `[]` |
| 2 | 14 | no | `[]` |
| 3 | 18.5 | sí | `[(4, 18.5)]` |
| 4 | 15 | sí | `[(4, 18.5), (5, 15)]` |

Retorna `[(4, 18.5), (5, 15)]`, que es justo lo que el ejemplo de ejecución imprime (`Día 4` y `Día 5`). La lógica es correcta y ya se puede programar.

---

# D. Codificación

1. **Primero la estructura.** Escriba las firmas de las funciones y `main` como una lista de llamadas (enfoque de arriba abajo).
2. **Convierta cada línea de pseudocódigo en una línea de Python.** Una técnica muy eficaz: pegue el pseudocódigo **como comentarios** dentro de la función y escriba el código **debajo de cada comentario**.
3. **Una función a la vez**, y compruebe que cada una hace lo que dice su frase del paso A2.

> Si el código no sale, **vuelva al pseudocódigo**, no al enunciado: el pseudocódigo ya contiene lo que usted entendió.

---

# E. Validación

1. **Reproduzca el ejemplo.** Ejecute su programa con los mismos datos del ejemplo y compare. En papel, ejecute su código **a mano** línea por línea, como en el paso A3.
2. **Pruebe casos propios** que el ejemplo no cubre. Para cada función, pregúntese:
   - ¿Qué pasa **justo en el límite** (un valor igual al límite)?
   - ¿Qué pasa con **un solo** dato o con una lista **vacía**?
   - ¿Qué pasa con un dato **inválido**?
3. **Relea el enunciado como lista de chequeo**: para cada requisito (con su porcentaje, si lo tiene), ¿dónde está cubierto en mi código?
   - ¿Cada función **retorna** o **imprime** lo que dice el enunciado?
   - ¿Usé las funciones que debía **reutilizar**?
   - ¿Cumplí las restricciones (`while`, `try`/`except`, etc.)?
   - ¿El formato de impresión coincide con el ejemplo?

---

# Si se atasca a mitad del problema

1. **No borre todo.** Identifique en cuál paso está atascado (A, B, C o D).
2. Si no sabe **qué retorna**, vuelva a A2. Si no sabe **qué hacer**, mire la traza del ejemplo (A3). Si sabe qué hacer pero no **cómo**, escriba el pseudocódigo (C).
3. Si una función no sale, deje la **firma y `pass`**, y siga con las demás: en una evaluación suele haber puntos parciales por cada ítem.

## De dónde sale esta guía

La metodología A–E es la del curso. El énfasis en entender el problema y trabajar con **casos concretos antes de programar**, descomponer en subtareas y diseñar antes de escribir sintaxis se apoya en la literatura de educación en computación (marco PCDIT, receta de diseño de *How to Design Programs*, estudios sobre descomposición).

# Hoja de trabajo (imprimible)

**Nombre:** ______________________________  **Problema:** ______________

## A. Comprensión

**A2. Entradas, salidas y qué debo hacer**

| Función | Entradas (tipo) | Salidas (retorna o imprime) | Qué debo hacer |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Función | Cómo uso las entradas | Cómo creo lo que retorno (si aplica) |
|---|---|---|
| | | |
| | | |
| | | |

**Una frase por función:** *"Recibe ___, hace ___ y retorna / imprime ___."*

**A3. Traza del ejemplo**

| # | Línea del ejemplo | [D] / [P] | Responsable | Entra / sale | ¿Coincide con A2? |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

**Lo que el ejemplo revela y el texto no dice:** ________________________________________

## B. Descomposición

| Función | Subtareas (lista numerada) | Patrón |
|---|---|---|
| | | |
| | | |

## C. Pseudocódigo

(use el reverso de la hoja: una frase por cada línea que tendrá el programa)

## E. Validación

| Caso propio | Resultado esperado | Resultado de mi código |
|---|---|---|
| límite | | |
| vacío / un solo dato | | |
| dato inválido | | |

**Lista de chequeo:** cada requisito del enunciado y dónde lo cumplí.

| Requisito | ¿Dónde lo cumplí? | OK |
|---|---|---|
| | | |
| | | |
| | | |
