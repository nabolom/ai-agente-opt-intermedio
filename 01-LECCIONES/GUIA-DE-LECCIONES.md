# Guía de lecciones

## Contrato general

Cada lección produce una decisión y un archivo. Enseñar primero, preguntar después, esperar respuesta, proponer borrador y escribir solo tras aprobación.

| Lección | Microconcepto | Preguntas obligatorias | Artefacto y criterio de avance |
|---:|---|---|---|
| **0 · Ambiente** | Un agente necesita fuentes y límites antes de actuar. | ¿Existe un PDF legible? ¿Contiene datos sensibles? ¿Qué otros archivos están autorizados? | Inventario visible; si falta PDF, detenerse. |
| **1 · Visión** | Automatizar no es “usar IA”; es mejorar un resultado observable. | ¿Quién vive el problema? ¿Qué dispara el proceso? ¿Qué output necesita? ¿Con qué frecuencia? | `00_RESUMEN-VISION.md` separa hechos del PDF, inferencias y faltantes. |
| **2 · Diagnóstico** | Un bloqueo puede ser de datos, reglas, permisos, proceso o expectativa. | ¿Dónde se pierde tiempo? ¿Qué error es frecuente? ¿Qué decisión requiere juicio? ¿Qué espera el alumno de Cowork? | `01_DIAGNOSTICO.md` contiene causas, no solo síntomas. |
| **3 · IA vs IF** | IF ejecuta reglas; IA interpreta ambigüedad acotada; el híbrido combina ambas. | ¿La entrada es estructurada? ¿Las reglas cubren todos los casos? ¿El output es exacto? ¿Hay texto no estructurado? ¿Cómo se verifica? | `02_DECISION-IA-IF.md` emite un veredicto con evidencia y confianza. |
| **4 · Alcance** | El MVP automatiza la parte repetible y deja la decisión irreversible al humano. | ¿Cuál es el output útil más pequeño? ¿Qué queda fuera? ¿Qué puede salir mal? ¿Quién confirma? | `03_ALCANCE-Y-RIESGOS.md` declara MVP, no-alcance y gate humano. |
| **5 · Harness** | Identidad + contexto + herramientas + restricciones + output + checker. | ¿Qué debe saber? ¿Qué puede leer/escribir? ¿Cuándo se detiene? ¿Qué formato produce? | `04_HARNESS.md` tiene seis componentes y mínimo privilegio. |
| **6 · Memoria** | Memoria útil guarda hechos estables y decisiones aprobadas, no una conversación completa. | ¿Cuál es la fuente de verdad? ¿Qué cambia? ¿Qué no debe guardarse? ¿Quién aprueba cambios? | `05_MEMORIA.md` define owner, retención, prohibidos y change gate. |
| **7 · Skill** | Un Skill enseña una capacidad repetible y cuándo activarla. No todo proceso necesita uno. | ¿Se repetirá? ¿Tiene trigger claro? ¿Entradas y output estables? ¿Cómo falla? | `skills/<nombre>/SKILL.md` válido o decisión explícita de no crear Skill. |
| **8 · Pruebas** | Un sistema confiable debe funcionar y fallar correctamente. | ¿Qué pasa normal, sin dato, con ambigüedad y con solicitud insegura? | `06_PRUEBAS.md` y `07_FICHA-FINAL.md` con PASS/FAIL/BLOQUEADO. |

## Matriz IA, IF, híbrido

| Señal | IF | IA | Híbrido |
|---|---:|---:|---:|
| Campos y formato estables | Fuerte | Débil | Fuerte |
| Reglas completas | Fuerte | No necesaria | Parcial |
| Texto o documentos no estructurados | Débil | Fuerte | Fuerte |
| Ambigüedad que requiere interpretación | Débil | Fuerte | Fuerte |
| Output exacto y validación determinística | Fuerte | Débil | Fuerte |
| Consecuencia alta del error | Solo con controles | Solo borrador | Preferido con gates |

## Veredicto

El archivo `02_DECISION-IA-IF.md` debe usar solo uno:

- `IF / DETERMINÍSTICO`
- `IA CON REVISIÓN HUMANA`
- `HÍBRIDO: IF + IA`
- `NO AUTOMATIZAR TODAVÍA`

Incluir confianza alta, media o baja y la evidencia que haría cambiar el veredicto.

## Cierre universal de cada lección

```text
LECCIÓN: [número]
ESTADO: LISTA / BLOQUEADA
ARTEFACTO PROPUESTO: [ruta]
DECISIÓN QUE NECESITO DE TI: [confirmación]
SIGUIENTE LECCIÓN: [número y nombre]
```
