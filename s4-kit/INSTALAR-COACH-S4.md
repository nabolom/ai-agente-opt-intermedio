# Instala el coach S4

El coach te acompaña durante la actividad. **No es el Skill de tu automatización.** Primero instalas el coach; durante la sesión, el coach te ayudará a construir el Skill de tu propio proceso.

## Antes de empezar · descarga el paquete completo

El ZIP del coach **no contiene la actividad completa**. Primero debes incorporar `s4-kit/` a la misma carpeta que Cowork ya usó en S2 y S3. El ZIP exterior `s4-kit.zip` **no se instala como Skill**; solo se descomprime y se copia.

| Paso | Acción |
|---:|---|
| 0.1 | **[Descarga `s4-kit.zip`](https://github.com/nabolom/ai-agente-opt-intermedio/raw/refs/heads/main/dist/s4-kit.zip)**. |
| 0.2 | Abre Descargas y descomprime el archivo. |
| 0.3 | Copia la carpeta resultante `s4-kit/`. |
| 0.4 | Pégala en la raíz de tu Project existente, al mismo nivel que `00-INPUT/`, `04-SALIDAS/` y `s3-rutas/`. |
| 0.5 | Regresa al **mismo Project de Cowork**. No abras otro. |

No copies `s4-kit/` dentro de `00-INPUT/`, `04-SALIDAS/`, `skills/` o `s3-rutas/`. Tampoco instales `s4-kit.zip` como Skill: es el paquete exterior de la actividad.

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

## Instalación del coach

Solo después de ver `s4-kit/` dentro de tu Project, instala el ZIP interior del coach.

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
