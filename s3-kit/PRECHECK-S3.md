# Precheck S3

Cowork debe revisar primero `PROGRESO.md` y los archivos existentes en `04-SALIDAS/`. No crear ni corregir nada durante el precheck.

## Evidencias mínimas

| Contrato S2 | Evidencia esperada | Si falta |
|---|---|---|
| Visión | `00_RESUMEN-VISION.md` o PDF con usuario, trigger y resultado. | Extraer un resumen provisional y marcarlo pendiente. |
| Diagnóstico | `01_DIAGNOSTICO.md`. | No impide demo; sí impide caso propio. |
| Decisión | `02_DECISION-IA-IF.md`. | Asignar ruta roja. |
| Alcance | `03_ALCANCE-Y-RIESGOS.md`. | Asignar ruta amarilla. |
| Harness | `04_HARNESS.md`. | Asignar ruta amarilla. |
| Memoria | `05_MEMORIA.md`. | Permitir corrida sin memoria y registrar la limitación. |
| Skill o reglas IF | `skills/*/SKILL.md` o decisión explícita IF. | No asumir que siempre se necesita Skill. |
| Pruebas | `06_PRUEBAS.md`. | Crear pruebas en S3 antes de declarar readiness. |

## Asignación de ruta

| Ruta | Condición | Objetivo |
|---|---|---|
| **Verde · Ejecutar** | Existen decisión, alcance y harness; memoria o Skill son coherentes con la arquitectura. | Dos corridas y readiness S4. |
| **Amarilla · Completar** | Existe decisión, pero falta alcance, harness o definición de output/checker. | Completar solo el contrato faltante y ejecutar una corrida. |
| **Roja · Recuperar** | Falta decisión IA/IF/híbrido o no hay input verificable. | Completar decisión y harness; después usar la demo Meridian. |

## Formato de respuesta

```text
RUTA ASIGNADA: VERDE / AMARILLA / ROJA
EVIDENCIA ENCONTRADA: [archivos]
FALTANTES QUE BLOQUEAN: [lista o “ninguno”]
LIMITACIONES NO BLOQUEANTES: [lista o “ninguna”]
PRIMER PASO: [una sola acción]
```

El alumno debe confirmar la ruta antes de que Cowork escriba o ejecute.
