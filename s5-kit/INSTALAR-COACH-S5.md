# Instala el coach S5

El coach ya viene listo. **No necesitas abrir, editar ni volver a comprimir su Skill.**

## Primero incorpora la actividad completa

| Paso | Acción |
|---:|---|
| 1 | **[Descarga `s5-kit.zip`](https://github.com/nabolom/ai-agente-opt-intermedio/raw/refs/heads/main/dist/s5-kit.zip)**. |
| 2 | Abre Descargas y descomprime el archivo. |
| 3 | Copia la carpeta resultante `s5-kit/`. |
| 4 | Pégala en la raíz del mismo Project usado en S2, S3 y S4, al mismo nivel que `00-INPUT/`, `04-SALIDAS/`, `s3-rutas/` y `s4-kit/`. Si ya tenías una versión anterior de `s5-kit/`, reemplázala completa; no dejes `s5-kit 2/` ni mezcles ambas. |
| 5 | Regresa a ese mismo Project de Cowork. No abras otro. |

El ZIP exterior `s5-kit.zip` contiene la actividad completa y **no se instala como Skill**.

Al terminar, la estructura debe verse así:

```text
tu-project/
├── s4-kit/                 ← si conservas sesiones anteriores
└── s5-kit/
    ├── 04-SIN-SISTEMA/
    ├── 07-SALIDAS/
    └── dist/
        └── s5-cerrar-loop-coach.zip
```

Si no conservas el Project anterior, crea una carpeta `mi-s5-demo`, coloca `s5-kit/` dentro y selecciona `mi-s5-demo` con **Use an existing folder**.

## Después instala solo el coach

| Paso | Acción |
|---:|---|
| 1 | Abre Claude Desktop. |
| 2 | Entra a **Customize → Skills**. |
| 3 | Pulsa **Add → Upload a skill**. |
| 4 | Selecciona `s5-kit/dist/s5-cerrar-loop-coach.zip`. |
| 5 | Activa `s5-cerrar-loop-coach`. |
| 6 | Regresa al mismo Project y abre una tarea nueva. |
| 7 | Escribe **`Inicia mi S5.`** |

## Cómo saber que quedó bien

La primera respuesta debe:

1. decirte que hará un precheck;
2. buscar evidencias de S4 y un output;
3. asignarte ruta verde, recuperación o demo;
4. hacerte máximo cuatro preguntas, no pedirte que edites el Skill.

## Si no puedes instalar Skills

Abre [`INICIAR-S5-SIN-SKILL.md`](INICIAR-S5-SIN-SKILL.md), copia las instrucciones del coach en una tarea nueva y después escribe `Inicia mi S5.`. Conserva el mismo precheck, las mismas rutas y los mismos outputs.
