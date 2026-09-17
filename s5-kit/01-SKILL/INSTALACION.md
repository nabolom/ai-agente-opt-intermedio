# Instalación · 5 minutos

Cowork instala Skills desde un archivo ZIP. El ZIP de esta carpeta ya tiene la estructura correcta, pero primero debes completar tu configuración.

## Instala tu versión configurada

1. Descarga [`revision-de-sistema.zip`](revision-de-sistema.zip) y descomprímelo.
2. Abre la carpeta resultante `revision-de-sistema/` y edita `SKILL.md`.
3. Completa los nueve campos del bloque **CONFIGURACIÓN** con tus rutas y criterios reales. Usa [`../02-CONFIGURACION/PLANTILLA-config.md`](../02-CONFIGURACION/PLANTILLA-config.md) como guía.
4. Vuelve a comprimir la carpeta completa `revision-de-sistema/`:
   - **Mac:** clic secundario sobre la carpeta → **Comprimir “revision-de-sistema”**.
   - **Windows:** clic secundario → **Comprimir en archivo ZIP** o **Enviar a → Carpeta comprimida**.
5. En Cowork, entra a **Customize → Skills → Add → Upload a skill** y selecciona el ZIP que acabas de crear.
6. Activa `revision-de-sistema`.
7. Abre una sesión nueva en el mismo Project y escribe `supervisa mi sistema`.

> El ZIP debe contener una carpeta raíz `revision-de-sistema/` y, dentro, `SKILL.md`. No subas `SKILL.md` suelto ni el ZIP completo del repositorio.

## Cómo saber que quedó bien

Si el Skill responde pidiéndote completar un campo, está bien instalado: está leyendo tu configuración y encontró un corchete sin llenar. Completa ese campo, vuelve a comprimir la carpeta y reemplaza el Skill.

Si responde como si fuera una conversación normal, no se activó. Revisa que el archivo se llame exactamente `SKILL.md`, que esté dentro de la carpeta `revision-de-sistema/` y que el Skill esté activo.

## Si no puedes subir Skills

Abre una sesión nueva en Cowork, pega el contenido completo de [`SKILL.md`](SKILL.md) como primer mensaje y agrega al final: “Estas son tus instrucciones para esta conversación.” Funciona igual, pero solo dentro de esa conversación.
