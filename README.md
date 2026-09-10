# AI Agente Opt · Intermedio

> **Abre tu PDF, entiende tu automatización y construye el agente correcto desde Cowork.**

Este repositorio acompaña cuatro sesiones conectadas. En S1 documentas tu proceso y generas el PDF de entrada; en S2 Cowork cuestiona ese PDF y diseña el agente correcto; en S3 cortas y construyes el workflow; en S4 lo encadenas, marcas su frontera y lo enciendes. No necesitas Terminal ni Claude Code.

> **Mapa completo del curso:** consulta la [`CHEAT-SHEET-S1-S4.md`](CHEAT-SHEET-S1-S4.md) para repasar conceptos, outcomes, archivos, frases de arranque, errores comunes y criterios de avance.

## Elige tu actividad

| Si estás en… | Empieza aquí | Frase de arranque |
|---|---|---|
| **Sesión 1 · Mapear el proceso** | Abre [`S1-EMPIEZA-AQUI.md`](S1-EMPIEZA-AQUI.md) y completa [Cloud para Automatización](https://my-automation.bolt.host/). | Outcome: `mi-automatizacion.pdf` |
| **Sesión 2 · Diseñar el agente correcto** | Sigue los seis pasos de esta página. | `Inicia mi ruta AI Agent Opt.` |
| **Sesión 3 · Cortar el proceso paso por paso** | **[Descarga `s3-rutas-kit.zip`](https://github.com/nabolom/ai-agente-opt-intermedio/raw/refs/heads/main/s3-rutas/dist/s3-rutas-kit.zip)**, instala `s3-rutas-coach.zip` y sigue [`s3-rutas/INSTALAR-S3-RUTAS.md`](s3-rutas/INSTALAR-S3-RUTAS.md). | `Inicia mi S3 Rutas.` |
| **Sesión 4 · Encadenar y encender** | Instala [`s4-encadenar-coach.zip`](s4-kit/dist/s4-encadenar-coach.zip) y abre [`s4-kit/EMPIEZA-S4-AQUI.md`](s4-kit/EMPIEZA-S4-AQUI.md). | `Inicia mi S4.` |

> **Antes de iniciar en Cowork:** no cambies las reglas del Project. Instala el único Skill de la sesión, `s3-rutas/02-RUTAS/dist/s3-rutas-coach.zip`; este guía las fases y guarda el seguimiento en `s3-rutas/03-SALIDAS/PROGRESO-S3.md`, sin tocar S2.

> **No abras un Project nuevo para S3 o S4.** Usa la misma carpeta para conservar tu PDF, memoria y outputs aprobados. En S4 instala únicamente `s4-kit/dist/s4-encadenar-coach.zip`; el coach te ayudará a crear un Skill distinto para tu proceso.

### Material adicional · no usar durante esta S3

El laboratorio anterior [`s3-kit/`](s3-kit/EMPIEZA-S3-AQUI.md) se conserva intacto como práctica posterior de confiabilidad. No es la ruta de esta clase y no debe instalarse junto con `s3-rutas/` durante la sesión.

## Outcome observable de S1

| Entregable | Contenido | Uso en S2 |
|---|---|---|
| **PDF de mapa de proceso** | Nombre, entradas y fuentes, herramientas, output y destinatarios, intervención manual, juicio humano y MVP propuesto. | Cowork lo trata como una hipótesis: separa hechos e inferencias, identifica bloqueos y decide `IF`, `IA`, `híbrido` o `no automatizar todavía`. |

Para generarlo, completa los siete pasos en [my-automation.bolt.host](https://my-automation.bolt.host/), pulsa **Descargar PDF** y selecciona **Guardar como PDF** en el navegador. Consulta [`S1-EMPIEZA-AQUI.md`](S1-EMPIEZA-AQUI.md).

## Outcomes observables de S2

| Outcome | Evidencia que tendrás |
|---|---|
| **Comprender la automatización** | Resumen de visión que separa hechos, inferencias y faltantes. |
| **Diagnosticar bloqueos y expectativas** | Causas de datos, reglas, permisos, proceso o alcance. |
| **Elegir la arquitectura correcta** | Veredicto `IF`, `IA`, `híbrido` o `no automatizar todavía`, con evidencia. |
| **Reducir a un MVP seguro** | Alcance, no-alcance, riesgos y decisión humana. |
| **Construir el harness** | Objetivo, trigger, fuentes, pasos, herramientas, restricciones, output, checker y fallback. |
| **Diseñar memoria controlada** | Fuente de verdad, hechos estables, datos prohibidos y aprobación de cambios. |
| **Definir una capacidad reutilizable** | Skill válido cuando aporta valor, o decisión explícita de no crearlo cuando basta IF. |
| **Probar antes de confiar** | Casos normal, faltante, ambiguo e inseguro con `PASS`, `FAIL` o `BLOQUEADO`. |

Estos outcomes son la entrada de S3: ahí el agente debe demostrar que puede ejecutar el workflow, explicar qué hizo y fallar correctamente.

## S2 · Arranque en seis pasos

| Paso | Acción |
|---:|---|
| 1 | En GitHub, pulsa **Code → Download ZIP** y descomprime la carpeta. |
| 2 | Copia el PDF generado en S1 dentro de [`00-INPUT/`](00-INPUT/README.md). Si no lo tienes, genéralo primero desde [`S1-EMPIEZA-AQUI.md`](S1-EMPIEZA-AQUI.md). No uses información que no puedas compartir. |
| 3 | Abre Claude Desktop → **Cowork → Projects → `+` → Use an existing folder** y elige esta carpeta. |
| 4 | Pega [`INSTRUCCIONES-PROJECT.md`](INSTRUCCIONES-PROJECT.md) en las instrucciones del Project. |
| 5 | Instala `dist/ai-agent-opt-coach.zip` desde **Customize → Skills** y actívalo.[1] |
| 6 | En el Project escribe: **`Inicia mi ruta AI Agent Opt.`** |

Si tu cuenta no permite instalar Skills, usa [`INICIAR-SIN-SKILL.md`](INICIAR-SIN-SKILL.md). El recorrido sigue funcionando.

## Qué aprenderás y construirás

| Lección | Pregunta | Artefacto |
|---:|---|---|
| 0 | ¿Está listo el ambiente y el PDF? | Inventario de entrada |
| 1 | ¿Qué visión describe el PDF? | `00_RESUMEN-VISION.md` |
| 2 | ¿Cuáles son los bloqueos y expectativas? | `01_DIAGNOSTICO.md` |
| 3 | ¿Es IA, IF, híbrido o no automatizar? | `02_DECISION-IA-IF.md` |
| 4 | ¿Cuál es el MVP seguro? | `03_ALCANCE-Y-RIESGOS.md` |
| 5 | ¿Qué necesita el harness? | `04_HARNESS.md` |
| 6 | ¿Qué debe recordar y qué debe olvidar? | `05_MEMORIA.md` |
| 7 | ¿Necesita un Skill? | `skills/mi-proceso/SKILL.md` |
| 8 | ¿Funciona y falla correctamente? | `06_PRUEBAS.md` y `07_FICHA-FINAL.md` |

## Cómo trabaja el coach

El coach presenta **una lección breve**, hace máximo cinco preguntas, espera tus respuestas y propone un borrador. Solo después de tu confirmación escribe el artefacto y avanza [`PROGRESO.md`](PROGRESO.md). No salta etapas y no fuerza IA cuando una regla IF es mejor.

## La decisión más importante

| Veredicto | Úsalo cuando… |
|---|---|
| **IF / determinístico** | Las entradas son estructuradas, las reglas están completas y el output debe ser exacto. |
| **IA** | Hay texto/documentos no estructurados y se necesita extraer, clasificar, resumir o redactar con revisión. |
| **Híbrido** | Las reglas controlan validación y permisos; la IA resuelve interpretación acotada. |
| **No automatizar todavía** | Faltan fuentes, no existe output verificable o un error tendría consecuencias altas sin gate humano. |

## Regla de seguridad

La primera corrida termina en un **borrador revisable**. No envía, publica, compra, borra ni modifica sistemas. Empieza con la carpeta y el PDF; agrega conectores solo después de demostrar necesidad y factibilidad. Anthropic recomienda limitar accesos, comenzar con tareas de bajo riesgo y revisar cuidadosamente Skills y acciones externas.[2]

## Para el facilitador

Abre [`S1-EMPIEZA-AQUI.md`](S1-EMPIEZA-AQUI.md) para el outcome de S1, [`GUIA-FACILITADOR.md`](GUIA-FACILITADOR.md) para S2, [`s3-rutas/GUIA-FACILITADOR-RUTAS.md`](s3-rutas/GUIA-FACILITADOR-RUTAS.md) para S3 y [`s4-kit/GUIA-FACILITADOR-S4.md`](s4-kit/GUIA-FACILITADOR-S4.md) para S4. El laboratorio anterior [`s3-kit/`](s3-kit/EMPIEZA-S3-AQUI.md) se conserva como práctica posterior de confiabilidad.

## Referencias

[1]: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills "How to create custom Skills"
[2]: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely "Use Claude Cowork safely"
