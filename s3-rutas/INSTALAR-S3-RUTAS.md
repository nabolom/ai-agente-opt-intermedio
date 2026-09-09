# Instalar S3 Rutas sin perder tu trabajo anterior

S3 se agrega a la misma carpeta y al mismo Project que utilizaste en S2. **No reemplaza** tus outputs, memoria, instrucciones ni archivos aprobados.

## Los tres pasos

### 1. Agrega la carpeta

1. Descarga [`s3-rutas-kit.zip`](dist/s3-rutas-kit.zip).
2. Descomprime el ZIP.
3. Copia la carpeta resultante `s3-rutas/` dentro de la carpeta raíz que ya utilizaste en S2.

Debe quedar al mismo nivel que `00-INPUT/`, `04-SALIDAS/` y `PROGRESO.md`. Si ves `s3-rutas/s3-rutas/`, quedó duplicada: mueve la carpeta interior un nivel hacia arriba.

### 2. Instala un solo Skill

En Cowork, abre **Customize → Skills → + Create skill → Upload a skill**. Instala y activa:

[`02-RUTAS/dist/s3-rutas-coach.zip`](02-RUTAS/dist/s3-rutas-coach.zip)

**No cambies las instrucciones del Project.** El Skill agrega el comportamiento de S3 solo cuando utilizas su frase de inicio.

### 3. Inicia S3

Abre el mismo Project de Cowork, empieza una tarea nueva y escribe:

```text
Inicia mi S3 Rutas.
```

Cowork debe confirmar que ve `s3-rutas/`, localizar tu decisión de S2 y decirte cuál es la primera fase pendiente.

## Qué se conserva

| Trabajo anterior | Qué ocurre |
|---|---|
| Tu PDF de entrada | Se conserva sin cambios. |
| `02_DECISION-IA-IF.md` | Se usa como punto de partida; no se reemplaza. |
| `04-SALIDAS/` | Se conserva sin cambios. |
| `PROGRESO.md` | Se conserva sin cambios. |
| Instrucciones del Project | No se editan. |
| Skills y memoria anteriores | Permanecen disponibles. |

## Qué se agrega

La carpeta nueva contiene la demo de facturas, las cuatro rutas, el Skill único de acompañamiento y un progreso independiente en `s3-rutas/03-SALIDAS/PROGRESO-S3.md`.

> **Comprobación rápida:** si Cowork confirma la carpeta, recupera el veredicto de S2 y menciona la primera fase pendiente, estás listo.
