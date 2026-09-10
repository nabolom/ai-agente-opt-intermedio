# Cheat sheet · Claude para Productividad Intermedio

## De una idea de automatización a un proceso que corre con límites

**Autor:** León Ruiz  
**Repositorio:** [AI Agente Opt · Intermedio](https://github.com/nabolom/ai-agente-opt-intermedio)

> **La historia completa en una línea:** S1 **mapea** el proceso; S2 **decide** qué arquitectura necesita; S3 **demuestra** un paso con evidencia; S4 **encadena y enciende** una versión mínima segura.

---

## 1. El mapa completo en 60 segundos

| Sesión | Pregunta central | Lo que cambia | Outcome observable | Frase o acción de inicio |
|---|---|---|---|---|
| **S1 · Mapear** | ¿Qué ocurre realmente hoy? | Una idea vaga se convierte en un mapa del proceso. | `mi-automatizacion.pdf` | Completar [Cloud para Automatización](https://my-automation.bolt.host/) |
| **S2 · Diseñar** | ¿Esto necesita IF, IA, híbrido o todavía no debe automatizarse? | El PDF deja de ser una propuesta y se convierte en una hipótesis cuestionada. | Decisión tecnológica, MVP, harness, memoria, Skill o reglas y pruebas. | `Inicia mi ruta AI Agent Opt.` |
| **S3 · Demostrar** | ¿Quién decide cada paso y qué tan bien funciona uno de ellos? | El proceso completo se abre paso por paso. | Tabla etiquetada, un paso construido, cinco pruebas y un número. | `Inicia mi S3 Rutas.` |
| **S4 · Operar** | ¿Qué versión puede correr hoy, cómo arranca y dónde debe detenerse? | Los pasos probados se convierten en una cadena con trigger y frontera. | V1 encadenada, corrida manual, tarea programada y gate de S5. | `Inicia mi S4.` |

La progresión evita un error frecuente: **intentar automatizar un proceso completo antes de entender sus decisiones, datos, límites y fallas**. Cada sesión reduce una incertidumbre diferente.[1]

```text
S1                S2                    S3                     S4
MAPA       →       ARQUITECTURA    →    EVIDENCIA        →     OPERACIÓN
¿Qué pasa?         ¿Qué lo resuelve?     ¿Funciona un paso?      ¿Puede correr solo?
```

---

## 2. Las piezas: qué es cada cosa y para qué sirve

| Pieza | Definición práctica | Pregunta que responde | Error común |
|---|---|---|---|
| **Prompt** | Una instrucción puntual dentro de una conversación. | ¿Qué necesito ahora? | Confundir una buena respuesta con un sistema repetible. |
| **Project de Cowork** | La carpeta, instrucciones y contexto persistente del trabajo. | ¿Dónde vive el proceso? | Crear un Project nuevo en cada sesión y perder continuidad. |
| **Coach de la sesión** | Skill pedagógico que explica, pregunta, propone, espera confirmación y registra avance. | ¿Cómo aprendo y construyo sin saltarme etapas? | Confundirlo con el Skill que ejecutará el proceso. |
| **Skill del proceso** | Capacidad reutilizable que se activa con una frase y produce un output definido. | ¿Cómo se ejecuta esta capacidad siempre de la misma manera? | Crear un Skill para algo que una regla IF resolvería mejor. |
| **IF** | Regla determinística: si ocurre X, hacer Y. | ¿La decisión puede escribirse completa? | Llamar “IA” a umbrales, filtros o tablas de equivalencia. |
| **IA** | Interpretación acotada de texto, documentos o ambigüedad. | ¿Dos personas razonables podrían responder distinto? | Darle IA a pasos que requieren exactitud absoluta sin checker. |
| **Híbrido** | IF controla validación, reglas y permisos; IA interpreta solo donde hace falta. | ¿Qué partes deben ser exactas y cuáles requieren contexto? | Poner IA en todos los pasos. |
| **Harness** | Contrato operativo del agente: objetivo, trigger, fuentes, pasos, herramientas, restricciones, output, checker y fallback. | ¿Dentro de qué límites puede actuar? | Escribir solo el rol y olvidar verificación o manejo de fallas. |
| **Memoria** | Hechos estables y decisiones aprobadas que pueden reutilizarse. | ¿Qué debe recordar y qué debe olvidar? | Guardar conversaciones completas, datos sensibles o supuestos no aprobados. |
| **Checker** | Criterio observable que determina si el resultado cumple. | ¿Cómo sabemos que está bien? | Pedir al mismo agente que se declare correcto sin una expectativa previa. |
| **Fallback** | Conducta segura cuando falta información o el paso no puede completarse. | ¿Qué hace cuando algo falla? | Inventar, continuar silenciosamente o ocultar el bloqueo. |
| **Frontera** | Punto donde el agente se detiene por conector, permiso o juicio humano. | ¿Hasta dónde llega la automatización? | Tratar la frontera como fracaso en vez de diseñarla. |
| **Trigger** | Evento o horario que inicia una cadena. | ¿Cuándo comienza el trabajo? | Creer que el trigger mejora un flujo defectuoso. |
| **Gate humano** | Confirmación necesaria antes de una acción sensible o irreversible. | ¿Qué decisión sigue siendo humana? | Automatizar envío, publicación, compra o modificación externa en la primera versión. |

### La distinción que más importa

| Coach pedagógico | Skill de tu proceso |
|---|---|
| Te ayuda a **entender y decidir**. | Ayuda a **ejecutar una capacidad**. |
| Se activa con `Inicia mi S2/S3/S4`. | Se activa con una frase como `procesa las facturas de esta semana`. |
| Hace preguntas y aplica gates. | Sigue el harness confirmado. |
| No elige por ti. | No cambia las reglas por sí solo. |

---

# 3. Sesión 1 · Mapear

## Idea clave

> **Antes de automatizar, haz visible el trabajo.**

S1 no decide todavía si necesitas IA. Documenta cómo crees que funciona hoy el proceso y genera el input que S2 cuestionará.[2]

## Las siete preguntas del PDF

| Sección | Lo que debes poder explicar |
|---|---|
| **Nombre del proceso** | Qué proceso quieres mejorar. |
| **Entradas y fuentes** | Qué necesita para empezar y de dónde viene. |
| **Herramientas** | Qué apps, archivos o carpetas toca hoy. |
| **Output y destinatario** | Qué produce y quién lo usa. |
| **Intervención manual** | Dónde participa una persona. |
| **Juicio humano** | Qué depende de contexto, criterio o información no escrita. |
| **Versión mínima** | Qué parte pequeña podría automatizarse primero. |

## Outcome

`mi-automatizacion.pdf`

**Está terminado cuando:** abre correctamente, contiene las siete respuestas y no incluye secretos ni datos personales innecesarios.[2]

## Qué todavía no sabes al terminar S1

El PDF es una **hipótesis**, no una especificación técnica. Todavía no sabes si el proceso necesita IA, si las reglas están completas, si tienes permisos, si el output es verificable o si el alcance es demasiado grande.

## Error común

**“Mi proceso podría automatizarse completo.”** En S1 se permite pensar en grande; S2 se encargará de cuestionar y reducir esa visión.

## Puente a S2

Copia el PDF en `00-INPUT/`. El coach de S2 lo leerá como evidencia inicial, separará hechos de inferencias y señalará lo que falta.

---

# 4. Sesión 2 · Diseñar

## Idea clave

> **Automatizar no significa usar IA. Significa elegir el mecanismo correcto para cada resultado.**

S2 transforma el mapa de S1 en contratos operativos. El coach enseña una lección, hace preguntas, propone un borrador y escribe únicamente después de tu aprobación.[1] [3]

## Las nueve lecciones y sus artefactos

| Lección | Decisión | Archivo esperado |
|---:|---|---|
| **0 · Ambiente** | ¿El PDF existe, es legible y seguro? | Inventario de entrada |
| **1 · Visión** | ¿Qué problema, trigger, frecuencia y output están realmente documentados? | `00_RESUMEN-VISION.md` |
| **2 · Diagnóstico** | ¿El bloqueo es de datos, reglas, permisos, proceso o expectativa? | `01_DIAGNOSTICO.md` |
| **3 · IA vs IF** | ¿Qué arquitectura corresponde y con qué evidencia? | `02_DECISION-IA-IF.md` |
| **4 · Alcance** | ¿Cuál es el output útil más pequeño y qué queda fuera? | `03_ALCANCE-Y-RIESGOS.md` |
| **5 · Harness** | ¿Cómo debe comportarse el agente? | `04_HARNESS.md` |
| **6 · Memoria** | ¿Qué recuerda, qué no guarda y quién aprueba cambios? | `05_MEMORIA.md` |
| **7 · Skill** | ¿La capacidad es repetible y merece convertirse en Skill? | `skills/<nombre>/SKILL.md` o decisión de no crearlo |
| **8 · Pruebas** | ¿Funciona normal y falla correctamente? | `06_PRUEBAS.md` y `07_FICHA-FINAL.md` |

## Árbol de decisión: IA, IF, híbrido o no automatizar

```text
¿Puedes escribir la regla completa como “si X, haz Y”?
├─ Sí → IF
└─ No
   └─ ¿Hay texto/documentos o ambigüedad que requiere interpretación?
      ├─ Sí → IA con revisión humana
      └─ No → revisa si faltan reglas o datos

¿El proceso combina validaciones exactas e interpretación?
└─ Sí → Híbrido

¿Faltan fuentes, permisos, output verificable o un gate para un error de alto impacto?
└─ Sí → No automatizar todavía
```

| Veredicto | Señal dominante | Ejemplo de mecanismo |
|---|---|---|
| **IF / determinístico** | Entrada estructurada, regla completa, output exacto | Umbral, filtro, tabla de equivalencias |
| **IA con revisión humana** | Texto no estructurado o interpretación acotada | Extraer, clasificar, resumir o redactar un borrador |
| **Híbrido** | Validación exacta + interpretación | IF valida; IA interpreta; humano confirma |
| **No automatizar todavía** | Faltan datos, reglas, permisos o control de riesgo | Resolver primero el bloqueo |

## Fórmula del harness

```text
HARNESS = objetivo + trigger + fuentes + pasos + herramientas
          + restricciones + output + checker + fallback
```

Un harness responde: qué hace el agente, con qué información, qué puede tocar, dónde debe detenerse, qué entrega, cómo se comprueba y qué ocurre cuando no puede continuar.

## Fórmula de memoria

```text
MEMORIA ÚTIL = hechos estables + decisiones aprobadas + fuente de verdad
               + owner + retención + datos prohibidos + gate de cambio
```

La memoria no es “recordar todo”. Es conservar únicamente lo que debe reutilizarse sin convertir una conversación o un supuesto en verdad.

## Pruebas mínimas

| Caso | Qué debe demostrar |
|---|---|
| **Normal** | Produce el output esperado. |
| **Faltante** | Detecta el dato ausente y se detiene o pide ayuda. |
| **Ambiguo** | Declara incertidumbre o solicita decisión. |
| **Inseguro** | Rechaza una acción fuera de permisos. |

Estados válidos: `PASS`, `FAIL` o `BLOQUEADO`. Un `BLOQUEADO` correcto puede ser más confiable que una respuesta aparentemente completa.

## Frase de arranque

> **Inicia mi ruta AI Agent Opt.**

## Criterio de terminado

Puedes explicar **por qué** tu proceso es IF, IA, híbrido o todavía no automatizable; tienes un MVP acotado; el harness y la memoria tienen límites; y existe evidencia de pruebas.

## Errores comunes

| Error | Corrección |
|---|---|
| “Quiero un agente que haga todo.” | Reduce al output útil más pequeño. |
| “Necesita IA porque es complejo.” | Busca primero reglas, umbrales y tablas. |
| “El agente recordará la conversación.” | Declara memoria estable y fuente de verdad. |
| “El agente se revisa a sí mismo.” | Define salida esperada y checker antes de correr. |

---

# 5. Sesión 3 · Demostrar

## Idea clave

> **El veredicto de S2 describe el proceso completo; S3 descubre quién decide cada paso.**

S3 abre el proceso en cuatro a ocho pasos. Cada paso se etiqueta como **IF, IA, herramienta o humano**, con una razón escrita por el participante.[4]

## Las preguntas que descubren un IF disfrazado

| Pregunta | Qué detecta |
|---|---|
| ¿Ese paso decide, o compara contra un número? | Umbral determinístico |
| ¿Puedes escribir la regla completa en una línea? | Regla IF |
| ¿Dos personas razonables podrían responder distinto? | Ambigüedad compatible con IA |
| ¿La categoría ya viene definida? | Enrutamiento, no interpretación |

## Modelo didáctico de confiabilidad

Si cada paso de IA tuviera 95% de acierto y los errores fueran independientes, una cadena de `n` pasos tendría una probabilidad ilustrativa de `0.95ⁿ` de atravesarlos todos correctamente. **No es una medición real**; sirve para mostrar por qué conviene reducir los pasos de IA. La evidencia real sale de las pruebas.[5]

| Pasos de IA | Resultado ilustrativo `0.95ⁿ` |
|---:|---:|
| 1 | 95.0% |
| 2 | 90.3% |
| 3 | 85.7% |
| 4 | 81.5% |

## Las cuatro rutas

| Ruta | Qué construyes | Cómo lo pruebas |
|---|---|---|
| **IF** | Tabla `input → condición → acción → excepción` | Cinco casos pasados a mano; detectar faltantes y conflictos |
| **IA** | Skill corto del único paso de IA prioritario | Tres casos típicos, uno límite y uno adversarial |
| **Híbrido** | Reglas para lo determinístico + un Skill para el núcleo interpretativo | Cinco casos con salida esperada definida antes de correr |
| **No automatizar todavía** | Tabla del faltante + el paso pequeño que sí puede ejecutarse | Ejecutar el paso y registrar el bloqueo con dueño |

## La regla de oro de las pruebas

> **La salida esperada se escribe antes de correr.**

Si defines lo esperado después de ver el resultado, estás justificando, no evaluando.

## Outcomes

1. `tabla-de-pasos.md`: cada paso, tipo, razón y efecto de falla.
2. Un paso construido: regla o Skill, según la ruta.
3. Evidencia de cinco casos o del faltante.
4. Tu número: `___ / 5` y la primera mejora.

## Frase de arranque

> **Inicia mi S3 Rutas.**

## Criterio de terminado

Puedes decir cuántos pasos tiene el proceso, cuántos son realmente de IA, por qué y qué ocurrió al probar uno. **Un paso probado vale más que un proceso completo supuesto.**[4] [5]

## Errores comunes

| Error | Corrección |
|---|---|
| Etiquetar todos los pasos como IA | Buscar reglas, umbrales, filtros y herramientas. |
| Construir todo el proceso | Construir solo el primer paso de la ruta. |
| Probar solo casos fáciles | Incluir límite y adversarial. |
| Dejar que el agente defina lo esperado | El humano fija el oracle antes de correr. |

---

# 6. Sesión 4 · Operar

## Idea clave

> **La versión mínima que corre sola le gana a la versión completa que no corre.**

S4 no agrega todos los pasos pendientes. Recorta una **V1 ejecutable hoy**, marca una frontera, encadena los pasos y añade un trigger.[6]

## Las dos preguntas de arquitectura

| | Llega al final | Se detiene en frontera |
|---|---|---|
| **Arranca solo** | A | B |
| **Alguien lo alimenta** | C | B+C |

1. **¿Cómo arranca?** Por hora o porque una persona coloca un archivo.
2. **¿Dónde se detiene?** Al terminar o ante una frontera de conector, permiso o juicio.

## V1 y V2

| V1 · Hoy | V2 · Después |
|---|---|
| Pasos ya construidos o con regla completa. | Pasos que requieren integración, permiso, mayor prueba o definición. |
| Debe producir un output útil. | Conserva la visión completa sin bloquear la demo. |
| Se puede ejecutar y verificar. | Tiene condición explícita para incorporarse. |

## Los tres tipos de frontera

| Frontera | Qué significa | Ejemplo de salida segura |
|---|---|---|
| **Conector** | Cowork no tiene acceso al sistema final. | Archivo listo para importar o instrucciones exactas. |
| **Permiso** | Existe acceso técnico, pero no autorización para escribir. | Borrador para aprobación. |
| **Juicio** | La decisión debe seguir siendo humana. | Recomendación con evidencia y opciones. |

### Fórmula de frontera

> El agente llega hasta **[paso]** y se detiene por **[conector / permiso / juicio]**. Entrega **[paquete]**, que una persona ejecuta en **[tiempo]**.

La frontera es buena cuando entrega un **paquete de ejecución**, no solo análisis. La persona no debería tener que volver a buscar datos ni reconstruir el razonamiento.

## Anatomía de la cadena

```text
Una invocación
    ↓
Paso 1 de V1
    ↓
Paso 2 de V1
    ↓
Checker / manejo de falla
    ↓
Output en borrador
    ↓
FRONTERA: NUNCA ejecutar la acción externa
```

El Skill encadenado debe incluir frase de invocación, rutas de fuentes, pasos en orden, comportamiento ante faltantes, output verificable y la frontera escrita como `NUNCA`.

## Orden correcto: nunca lo inviertas

```text
1. Construir la cadena
2. Ejecutarla manualmente
3. Abrir y revisar el output real
4. Confirmar que respetó la frontera
5. Crear el trigger
6. Disparar la tarea manualmente
7. Medir y preparar la demo
```

Programar un flujo no lo mejora; solo repite su comportamiento. En Cowork, las tareas programadas pueden ejecutarse con la cadencia elegida. Si dependen de archivos o aplicaciones locales, necesitan acceso a través de Claude Desktop.[7]

## Gate de salida a S5

| Evidencia | Debes poder mostrarla, no solo afirmarla |
|---|---|
| **1. La V1 corre hasta la frontera** | Una invocación, pasos en orden y output en destino. |
| **2. El trigger está creado** | Tarea visible con cadencia. |
| **3. Puedes dispararlo manualmente** | Comprobado durante S4. |
| **4. Conservas tu número de S3** | `___ / 5`. |
| **5. Estimaste tiempo recuperado** | Tiempo antes y después por semana. |

Estas cinco evidencias son el guion de la demo de S5.[8]

## Frase de arranque

> **Inicia mi S4.**

El coach aplica el ciclo **explicar → preguntar → proponer → confirmar → guardar**, exige que expliques cada decisión con tus propias palabras y bloquea la programación si no existe una corrida supervisada.

## Errores comunes

| Error | Corrección |
|---|---|
| Crear otro Project | Mantener el mismo Project para conservar S2 y S3. |
| Encadenar toda la visión | Recortar V1 y dejar V2 explícita. |
| Confundir frontera con fracaso | Diseñar el paquete que recibe el humano. |
| Ir directo a `/schedule` | Probar manualmente y revisar el archivo real. |
| Programar envío o escritura externa | Producir borrador; mantener gate humano. |
| Declarar “funcionó” sin evidencia | Mostrar output, trigger, número y tiempo. |

---

# 7. Ejemplo transversal · Caso didáctico de facturas

> Este ejemplo ilustra el método. No sustituye el proceso ni los datos del participante.

## S1 · El mapa

Una persona recibe facturas, extrae proveedor, monto y fecha, normaliza el proveedor, categoriza el gasto, compara contra presupuesto y registra la fila en una hoja. La decisión final de registrar permanece con una persona.

## S2 · La arquitectura

| Paso | Mecanismo sugerido | Razón |
|---|---|---|
| Extraer campos | IF o herramienta si el formato es estable; IA si los documentos varían | Depende de la estructura real |
| Normalizar proveedor | IF / tabla de alias | Equivalencia determinística |
| Categorizar gasto | IA acotada o IF si existe catálogo completo | Puede requerir interpretación |
| Comparar presupuesto | IF | Comparación numérica |
| Registrar en hoja | Humano / frontera de permiso | Primera versión solo entrega borrador |

Veredicto: **híbrido**. El harness limita las fuentes, prohíbe inventar y exige un borrador. La memoria conserva alias aprobados, no facturas completas.

## S3 · La evidencia

Se construye solo el paso de categorización —si realmente requiere IA— y se prueba con cinco casos: tres típicos, uno límite y uno adversarial. El participante define antes las categorías esperadas y obtiene un número como `4 / 5`.

## S4 · La operación

La V1 encadena extracción, normalización, categorización y comparación. Se detiene antes de escribir en la hoja. Produce una fila candidata, fuente, explicación de la excepción y estado `BORRADOR`. Después de una corrida manual revisada, se programa el trigger. Una persona conserva la decisión de registrar.

---

# 8. Diagnóstico rápido · Si te falta algo, vuelve aquí

| Lo que te pasa | Qué significa | Dónde regresar |
|---|---|---|
| No puedes explicar el proceso de inicio a fin | Falta mapa | **S1** |
| Tienes una idea, pero no sabes si es IA | Falta decisión tecnológica | **S2 · Lección 3** |
| El alcance sigue siendo “todo el proceso” | Falta MVP y no-alcance | **S2 · Lección 4** |
| El agente cambia de comportamiento | Falta harness o memoria aprobada | **S2 · Lecciones 5–6** |
| No sabes cuántos pasos son realmente de IA | Falta corte paso por paso | **S3 · Tabla** |
| Tienes un veredicto, pero nada construido | Falta un paso de la ruta | **S3 · Construye** |
| “Funcionó”, pero no tienes casos ni número | Falta evidencia | **S3 · Prueba** |
| Un paso funciona, pero necesitas varias instrucciones | Falta cadena | **S4 · Encadenar** |
| El ERP o la hoja no se pueden modificar | Encontraste una frontera | **S4 · Frontera** |
| Quieres programar, pero no has visto el output real | Falta corrida supervisada | **S4 · Fase 4** |
| La tarea existe, pero no sabes demostrarla | Falta prueba manual y gate | **S4 · Gate S5** |
| No puedes instalar un coach | Usa la ruta `SIN-SKILL` de la sesión | **Fallback** |

---

# 9. Checklist maestro de artefactos

## S1

- [ ] `00-INPUT/mi-automatizacion.pdf`

## S2

- [ ] `04-SALIDAS/00_RESUMEN-VISION.md`
- [ ] `04-SALIDAS/01_DIAGNOSTICO.md`
- [ ] `04-SALIDAS/02_DECISION-IA-IF.md`
- [ ] `04-SALIDAS/03_ALCANCE-Y-RIESGOS.md`
- [ ] `04-SALIDAS/04_HARNESS.md`
- [ ] `04-SALIDAS/05_MEMORIA.md`
- [ ] Skill del proceso o decisión explícita de usar IF
- [ ] `04-SALIDAS/06_PRUEBAS.md`
- [ ] `04-SALIDAS/07_FICHA-FINAL.md`

## S3

- [ ] `s3-rutas/03-SALIDAS/tabla-de-pasos.md`
- [ ] `reglas.md`, `evals-5.md` o `faltante.md`, según la ruta
- [ ] Un paso construido y probado
- [ ] Número `___ / 5` o estado de ejecución
- [ ] Primera mejora identificada

## S4

- [ ] `s4-kit/04-SALIDAS/recorte-v1-v2.md`
- [ ] `s4-kit/04-SALIDAS/frontera.md`
- [ ] `s4-kit/04-SALIDAS/skill_[proceso].md`
- [ ] Corrida supervisada revisada
- [ ] Tarea programada visible y disparable
- [ ] `s4-kit/04-SALIDAS/gate-s5.md`

> No subas al repositorio público PDFs, outputs personales, credenciales ni información real de la empresa.

---

# 10. Frases de arranque y ayuda

| Necesidad | Frase |
|---|---|
| Empezar S2 | `Inicia mi ruta AI Agent Opt.` |
| Empezar S3 | `Inicia mi S3 Rutas.` |
| Empezar S4 | `Inicia mi S4.` |
| Retomar S4 | `Continúa mi S4.` |
| Pedir explicación | `No entiendo esta fase. Explícala con el caso demo y vuelve a preguntarme con mi proceso.` |
| Evitar que decida por ti | `No elijas por mí. Hazme las preguntas y registra solo lo que confirme.` |
| Exigir evidencia | `No marques la fase como completa hasta que revisemos el archivo real.` |

---

# 11. Cómo explicar el curso en 60 segundos

> En S1 hicimos visible un proceso y lo convertimos en un PDF. En S2 cuestionamos ese PDF: identificamos bloqueos, decidimos si cada solución requería IF, IA, una combinación o si todavía no era automatizable, y diseñamos harness, memoria y pruebas. En S3 abrimos el proceso paso por paso, construimos solo uno y lo probamos con cinco casos para obtener evidencia. En S4 recortamos una versión que sí podía correr, marcamos dónde debía detenerse, encadenamos los pasos y añadimos un trigger. El resultado no es un agente que “hace todo”; es un proceso más pequeño, observable y seguro que sabemos explicar, probar y mejorar.

---

# 12. Las ocho reglas que debes recordar

1. **El PDF es una hipótesis, no la verdad.**
2. **IF antes que IA cuando la regla puede escribirse completa.**
3. **IA solo para interpretación acotada y verificable.**
4. **El humano define la salida esperada antes de correr.**
5. **Un paso probado vale más que un proceso completo supuesto.**
6. **Una frontera bien diseñada es parte de la solución.**
7. **Primero corrida manual; después trigger.**
8. **La primera versión produce borradores revisables, no acciones externas irreversibles.**

---

## Referencias

[1]: https://github.com/nabolom/ai-agente-opt-intermedio "AI Agente Opt · Intermedio"
[2]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/S1-EMPIEZA-AQUI.md "Sesión 1 · Documenta tu automatización"
[3]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/01-LECCIONES/GUIA-DE-LECCIONES.md "Guía de lecciones S2"
[4]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/s3-rutas/EMPIEZA-S3-RUTAS.md "Empieza S3 Rutas"
[5]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/s3-rutas/02-RUTAS/BLOQUE-60-MIN.md "Bloque individual S3"
[6]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/s4-kit/EMPIEZA-S4-AQUI.md "Empieza S4 aquí"
[7]: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork "Schedule recurring tasks in Claude Cowork"
[8]: https://github.com/nabolom/ai-agente-opt-intermedio/blob/main/s4-kit/03-GATE-S5/CHECKLIST-GATE.md "Gate de salida a S5"
