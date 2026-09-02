# Ruta en vivo · AI Agente Opt

## Resultado

Cowork leerá tu PDF revisado, enseñará una lección por vez y te ayudará a decidir si tu automatización necesita **IA, IF, híbrido o todavía no debe construirse**. Después configurará contigo harness, memoria, Skill y pruebas.

## Preparación

| Paso | Acción |
|---:|---|
| 1 | Descarga y descomprime el repo. |
| 2 | Copia tu PDF en `00-INPUT/`. |
| 3 | Abre la carpeta como Project de Cowork. |
| 4 | Pega `INSTRUCCIONES-PROJECT.md` en las instrucciones. |
| 5 | Instala y activa `dist/ai-agent-opt-coach.zip`. |
| 6 | Mantén el modo Manual. |

## Frase única de inicio

```text
Inicia mi ruta AI Agent Opt.
```

No pidas “construye todo”. El coach debe explicar una lección, hacer máximo cinco preguntas y esperar. Lee el borrador y responde **“apruebo esta lección”** o indica una corrección concreta.

## Checkpoints para 42 minutos

| Minuto | Meta |
|---:|---|
| 0–7 | Ambiente y PDF listos. |
| 7–17 | Visión resumida y confirmada. |
| 17–27 | Bloqueos y expectativas diagnosticados. |
| 27–35 | Decisión IA, IF, híbrido o no automatizar. |
| 35–42 | Alcance y primer borrador de harness/memoria. |

No es necesario terminar ocho lecciones. El mínimo valioso es una decisión tecnológica con evidencia. Si llegas a la prueba, el resultado válido es `PASS`, `FAIL` o `BLOQUEADO`.

## Evidencia para plenaria

> “Mi caso es **[IA / IF / híbrido / no automatizar]** porque ___; el principal bloqueo es ___; la decisión que conservo como humano es ___.”
