# Guía del facilitador · S3 reliability lab

## Outcome

Cada participante produce una corrida observable y una decisión de readiness para S4. El mínimo válido es: plan aprobado, un output local y un registro `PASS`, `FAIL` o `BLOQUEADO`.

## Guion de apertura

> “En S2 diseñaron el agente correcto. Hoy no ganan por conectar más apps ni por usar un prompt corto. Ganan si su workflow puede explicar su plan, producir evidencia, detenerse ante una excepción y decirnos qué contrato debe mejorar. La instrucción expresa el qué; el harness, la memoria, el Skill o las reglas IF contienen el cómo.”

## Agenda de 150 minutos

| Minuto | Bloque | Instrucción | Evidencia |
|---:|---|---|---|
| 0–10 | Recuperación | Preguntar qué quedó funcionando y qué falló en S2. | Participantes ubicados por madurez. |
| 10–22 | Precheck | Instalar kit, escribir `Inicia mi sesión 3` y confirmar ruta. | Verde, amarilla o roja. |
| 22–37 | Concepto | Explicar planear → ejecutar → verificar → aprender. | Diferencia entre qué y cómo. |
| 37–52 | Demo normal | Ejecutar Meridian normal; aprobar el plan antes de correr. | Briefing, email borrador y run-log. |
| 52–62 | Demo de falla | Cambiar al caso de falla. | Instrucción embebida ignorada y fuente faltante registrada. |
| 62–70 | Debrief | Mapear cada decisión a harness, memoria, Skill o IF. | Comprensión transferible. |
| 70–80 | Break | Abrir BOR opcional de recuperación. | Ambiente listo. |
| 80–85 | Lanzamiento | Repetir evidencia mínima y prohibiciones. | Inicio autónomo. |
| 85–105 | Ciclo 1 | Corrida normal propia o Meridian. | Output y registro. |
| 105–112 | Checkpoint | Corregir un contrato en vivo, no el prompt operativo. | Aprendizaje colectivo. |
| 112–132 | Ciclo 2 | Probar faltante, ambigüedad o instrucción insegura. | Falla observable. |
| 132–139 | Checkpoint | Revisar propuesta de mejora. | Diff de un contrato. |
| 139–145 | Readiness | Emitir GO, GO CON CONDICIONES o NO-GO. | Ficha S4. |
| 145–150 | Cierre | Compartir hallazgo, decisión humana y trigger candidato. | Puente a S4. |

## Rutas

| Ruta | Acción del participante | Tu intervención |
|---|---|---|
| Verde | Dos corridas del caso propio. | Revisar checker y evidencia. |
| Amarilla | Completar un solo contrato y hacer corrida normal. | Evitar que reconstruya todo S2. |
| Roja | Completar decisión/harness y ejecutar Meridian. | Asegurar experiencia end-to-end sin inventar su caso. |

## Señales de intervención

| Señal | Respuesta |
|---|---|
| Cowork comienza sin mostrar plan | Detener y volver a `08_PLAN-DE-CORRIDA.md`. |
| El alumno reescribe un prompt con todos los pasos | Mover los pasos al harness/Skill; dejar el objetivo en alto nivel. |
| Quiere conectar Gmail/Drive | Preguntar qué evidencia local demuestra la necesidad; posponer hasta PASS. |
| La corrida falla | Pedir que identifique el contrato roto antes de reintentar. |
| Cowork obedece una instrucción embebida | Marcar FAIL de seguridad y corregir harness/permisos. |
| El alumno quedó atrás | Pasarlo a ruta roja y usar Meridian, sin fingir outputs S2. |

## Criterio de éxito

No evaluar cantidad de outputs ni autonomía aparente. Evaluar trazabilidad, control de permisos, manejo de excepción, checker y decisión humana.
