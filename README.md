# AI Agente Opt · Intermedio

> **Abre tu PDF, entiende tu automatización y construye el agente correcto desde Cowork.**

Este repositorio funciona como un coach guiado. No necesitas Terminal ni Claude Code. Trabajarás con el PDF de visión que ya revisaste, identificarás bloqueos y expectativas, decidirás si tu solución necesita **IA, reglas IF, un sistema híbrido o todavía no debe automatizarse**, y después construirás harness, memoria, Skill y pruebas.

## Arranque en seis pasos

| Paso | Acción |
|---:|---|
| 1 | En GitHub, pulsa **Code → Download ZIP** y descomprime la carpeta. |
| 2 | Copia tu PDF revisado dentro de [`00-INPUT/`](00-INPUT/README.md). No uses información que no puedas compartir. |
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

Abre [`GUIA-FACILITADOR.md`](GUIA-FACILITADOR.md) para el encuadre, tiempos y señales de intervención. La ruta rápida para los participantes está en [`RUTA-EN-VIVO.md`](RUTA-EN-VIVO.md).

## Referencias

[1]: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills "How to create custom Skills"
[2]: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely "Use Claude Cowork safely"
