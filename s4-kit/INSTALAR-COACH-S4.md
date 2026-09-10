# Instala el coach S4

El coach te acompaña durante la actividad. **No es el Skill de tu automatización.** Primero instalas el coach; durante la sesión, el coach te ayudará a construir el Skill de tu propio proceso.

## Antes de empezar

Usa el **mismo Project de Cowork** de S2 y S3. No abras otro Project: el coach necesita leer tu tabla de pasos, el paso probado y el número de acierto de S3.

Confirma que dentro de la carpeta del Project ves:

```text
ai-agente-opt-intermedio/
├── s3-rutas/
├── s4-kit/
│   ├── dist/
│   │   └── s4-encadenar-coach.zip
│   └── 04-SALIDAS/
│       └── PROGRESO-S4.md
└── ...
```

## Instalación

| Paso | Acción |
|---:|---|
| 1 | Abre Claude Desktop. |
| 2 | Entra a **Customize → Skills**. |
| 3 | Pulsa **Add → Upload a skill**. |
| 4 | Selecciona `s4-kit/dist/s4-encadenar-coach.zip`. |
| 5 | Activa `s4-encadenar-coach`. |
| 6 | Regresa al mismo Project y abre una tarea nueva. |
| 7 | Escribe: **`Inicia mi S4.`** |

## Qué hará primero

El coach buscará tres evidencias de S3: la tabla de pasos, un paso construido y probado, y el número de acierto. Con eso te asignará una ruta:

| Ruta | Qué significa |
|---|---|
| **Verde** | Puedes trabajar con tu proceso. |
| **Amarilla** | Falta una evidencia; la reconstruirás antes de avanzar. |
| **Demo** | Usarás el caso de facturas para aprender la mecánica sin inventar datos propios. |

## Cómo trabajará contigo

En cada fase el coach hará cinco cosas: explicará el concepto, formulará preguntas, propondrá un borrador, esperará tu confirmación y solo entonces guardará el archivo. No decidirá tu V1, tu frontera ni tus números por ti.

La ruta termina cuando tienes:

1. `recorte-v1-v2.md`.
2. `frontera.md`.
3. `skill_[proceso].md`.
4. Una corrida manual revisada.
5. Una tarea programada visible y disparable manualmente.
6. `gate-s5.md` completo.

## Si no puedes instalar el Skill

Abre [`INICIAR-S4-SIN-SKILL.md`](INICIAR-S4-SIN-SKILL.md) y sigue la ruta de respaldo. La actividad conserva el mismo precheck, las mismas fases y los mismos gates.

## Si el coach no se activa

Comprueba que el Skill está activo y escribe exactamente:

> Inicia mi S4.

Si todavía no responde como coach, abre `s4-kit/skills/s4-encadenar-coach/SKILL.md`, copia su contenido en una tarea nueva y vuelve a escribir la frase. No avances directamente a `/schedule`: primero debe completarse la corrida supervisada.
