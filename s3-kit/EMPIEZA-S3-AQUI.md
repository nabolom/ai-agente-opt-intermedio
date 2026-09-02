# Empieza S3 aquí · Del agente diseñado al workflow confiable

## Resultado de la sesión

Hoy no volverás a diseñar tu automatización. Cowork revisará lo que construiste en S2, te asignará una ruta de recuperación o ejecución y conducirá dos ciclos: **corrida normal** y **corrida de falla**. Terminarás con evidencia para decidir si tu workflow está listo para recibir un trigger en S4.

## Instala el kit sin perder S2

| Paso | Acción |
|---:|---|
| 1 | Descarga `s3-kit.zip` y descomprímelo. |
| 2 | Copia la carpeta completa `s3-kit/` dentro de la misma carpeta que usaste en S2. No reemplaces `04-SALIDAS/`, `PROGRESO.md` ni tu PDF. |
| 3 | Abre el mismo Project de Cowork. Si ya estaba abierto, inicia una tarea nueva. |
| 4 | Instala `s3-kit/dist/ai-agent-opt-runner.zip` desde **Customize → Skills** y actívalo. |
| 5 | Mantén el modo de aprobación en **Manual**. |
| 6 | Escribe: **`Inicia mi sesión 3.`** |

Si no puedes instalar Skills, abre [`INICIAR-S3-SIN-SKILL.md`](INICIAR-S3-SIN-SKILL.md) y pega el bloque en Cowork.

## Qué hará el runner

| Etapa | Acción | Evidencia |
|---:|---|---|
| 1 | Precheck de S2 | Ruta verde, amarilla o roja y faltantes exactos. |
| 2 | Plan antes de actuar | `08_PLAN-DE-CORRIDA.md`. |
| 3 | Corrida normal | Un borrador dentro de `04-SALIDAS/s3/`. |
| 4 | Verificación | `09_REGISTRO-DE-CORRIDA.md` con PASS, FAIL o BLOQUEADO. |
| 5 | Corrida de falla | Fuente faltante, ambigüedad o instrucción insegura. |
| 6 | Aprendizaje | `10_PROPUESTA-DE-MEJORA.md`; ningún cambio silencioso. |
| 7 | Decisión S4 | `11_READINESS-S4.md` con GO, GO CON CONDICIONES o NO-GO. |

## Regla de la sesión

> Una instrucción de alto nivel expresa el **qué**. El **cómo** debe existir en el harness, la memoria, el Skill o las reglas IF. Si Cowork no puede explicar de dónde obtuvo un paso, no es autonomía: es un hueco del diseño.

La primera evidencia se guarda localmente. No se envía, publica, compra, borra ni modifica información externa. Un conector solo puede proponerse después de una corrida local PASS.
