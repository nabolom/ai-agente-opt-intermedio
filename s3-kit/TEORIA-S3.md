# Teoría S3 · Del agente diseñado al workflow confiable

## Promesa de la sesión

> **Hoy no diseñamos otra automatización. Hoy demostramos si la que diseñamos puede ejecutar, explicar, detenerse y mejorar.**

## El arco completo

| Sesión | Pregunta central | Trabajo del participante | Outcome |
|---|---|---|---|
| **S1 · Mapear** | ¿Cómo funciona hoy el proceso? | Completa siete preguntas en [my-automation.bolt.host](https://my-automation.bolt.host/). | PDF de mapa de proceso con entradas, herramientas, output, intervención humana, juicio y MVP propuesto. |
| **S2 · Diseñar** | ¿Qué arquitectura y contratos necesita? | Cowork cuestiona el PDF y construye decisión IA/IF/híbrido, alcance, harness, memoria, Skill/reglas y pruebas. | Agente diseñado y primera evidencia local. |
| **S3 · Confiar** | ¿El workflow hace lo correcto y falla correctamente? | Ejecuta caso normal y caso de falla; registra evidencia y propone una mejora. | Readiness `GO`, `GO CON CONDICIONES` o `NO-GO` para S4. |
| **S4 · Operar** | ¿Qué trigger y conexiones puede recibir con seguridad? | Programa o integra solo lo que superó S3. | Workflow operable con owner, SLA, gate y monitoreo. |

El PDF de S1 es una **hipótesis documentada del proceso**, no una especificación técnica ni prueba de automatización. S2 la convierte en contratos. S3 somete esos contratos a evidencia.

## Los seis conceptos que sí debes enseñar

### 1. Un agente no es un prompt

Una instrucción de alto nivel expresa el **qué**. El **cómo** vive en contratos reutilizables.

| Capa | Pregunta que responde |
|---|---|
| Harness | ¿Cuál es el objetivo, proceso, límite, output, checker y fallback? |
| Memoria | ¿Qué contexto estable puede conservarse y quién aprueba cambios? |
| Skill | ¿Qué capacidad reusable se activa ante un trigger semántico? |
| Regla IF | ¿Qué decisión determinística no necesita interpretación? |
| Gate humano | ¿Qué decisión o acción no puede delegarse? |

### 2. Autonomía no significa ausencia de control

La autonomía útil es ejecutar dentro de un contrato, mostrar evidencia y detenerse al salir del límite. Un workflow que “hace muchas cosas” pero no explica sus fuentes ni permisos no es más avanzado: es menos gobernable.

### 3. El ciclo de confiabilidad

| Momento | Pregunta | Artefacto |
|---|---|---|
| **Planear** | ¿Qué fuentes, pasos, outputs y condiciones de parada usará? | `08_PLAN-DE-CORRIDA.md` |
| **Ejecutar** | ¿Siguió el contrato sin ampliar permisos? | Output local |
| **Verificar** | ¿Qué pasó realmente y qué criterio cumplió? | `09_REGISTRO-DE-CORRIDA.md` |
| **Aprender** | ¿Qué contrato debe cambiar según la evidencia? | `10_PROPUESTA-DE-MEJORA.md` |
| **Decidir** | ¿Está listo para recibir un trigger? | `11_READINESS-S4.md` |

### 4. Observabilidad antes de automatización

Si solo ves el resultado final, no sabes por qué salió bien ni podrás reparar una falla. S3 exige un plan visible, fuente por paso, excepciones, checker y estado `PASS`, `FAIL` o `BLOQUEADO`.

### 5. Fallar correctamente es parte del producto

Una corrida de falla no busca “romper a Claude”; comprueba que el sistema responda con seguridad cuando falta una fuente, hay ambigüedad o un archivo contiene una instrucción no confiable. Detenerse y pedir una decisión puede ser el resultado correcto.

### 6. Un trigger es un privilegio ganado

Gmail, Drive, calendarios y tareas programadas amplían alcance y consecuencias. Primero se demuestra una corrida local; después se diseña el trigger, permiso mínimo, owner, SLA, gate y fallback. `GO` no significa “automatiza todo”: significa que existe evidencia suficiente para el siguiente experimento controlado.

## Secuencia sugerida de teoría · 37 minutos

| Minuto | Concepto | Mensaje que debes dejar |
|---:|---|---|
| 0–5 | Arco S1→S4 | “El PDF era el mapa; S2 diseñó; S3 prueba; S4 opera.” |
| 5–11 | Agente ≠ prompt | “El qué cabe en una frase; el cómo debe vivir en contratos.” |
| 11–18 | Harness, memoria, Skill e IF | Explicar función y diferencia con un ejemplo, sin volver a construirlos. |
| 18–25 | Ciclo de confiabilidad | Planear, ejecutar, verificar, aprender y decidir. |
| 25–31 | Observabilidad | Output sin run-log no es evidencia suficiente. |
| 31–35 | Falla segura | `BLOQUEADO` puede ser éxito operativo. |
| 35–37 | Readiness S4 | Solo un workflow probado recibe trigger o conector. |

Después realiza la demo Meridian normal y de falla. Haz el break cuando el grupo ya haya visto ambos comportamientos y pueda explicar la diferencia.

## Estructura sugerida de slides

| Slide | Título | Visual o contenido |
|---:|---|---|
| 1 | Del agente diseñado al workflow confiable | Promesa y outcome S3. |
| 2 | El arco: mapa → diseño → evidencia → operación | S1, S2, S3 y S4 en una línea. |
| 3 | Un agente no es un prompt | “Qué” frente a stack del “cómo”. |
| 4 | Cuatro contratos, cuatro funciones | Harness, memoria, Skill e IF. |
| 5 | Autonomía dentro de límites | Contrato, permisos y gate humano. |
| 6 | Ciclo de confiabilidad | Planear → ejecutar → verificar → aprender → decidir. |
| 7 | Lo que no observas no lo puedes reparar | Plan, output, run-log y checker. |
| 8 | Fallar correctamente | Faltante, ambigüedad e instrucción embebida. |
| 9 | Meridian: misma instrucción, dos escenarios | Caso normal frente a caso de falla. |
| 10 | Readiness para S4 | GO, GO CON CONDICIONES y NO-GO. |

## Qué no volver a enseñar

No repitas la construcción completa de harness, memoria o Skill; usa un recap de siete minutos. No presentes conectores como meta de S3, no midas éxito por cantidad de destinos y no prometas ejecución sin intervención humana. La novedad de S3 es **evidencia, manejo de fallas y readiness**, no una herramienta adicional.

## Preguntas para el debrief

| Pregunta | Aprendizaje buscado |
|---|---|
| ¿Qué parte vino del PDF y qué parte tuvo que ser diseñada? | Distinguir proceso documentado de contrato técnico. |
| ¿Qué decisión vino del harness, memoria, Skill o IF? | Hacer visible el “cómo”. |
| ¿Qué observaste además del output? | Valorar run-log y checker. |
| ¿Por qué detenerse fue correcto? | Normalizar la falla segura. |
| ¿Qué evidencia falta para conectar un trigger? | Preparar S4 sin precipitar integraciones. |
