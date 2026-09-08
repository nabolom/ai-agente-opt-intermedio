# Ruta Híbrido

La ruta de la mayoría. Primero cortas, después mides.

## Paso 1 · Etiqueta cada paso

Llena [`PLANTILLA-tabla-de-pasos.md`](PLANTILLA-tabla-de-pasos.md) completa antes de construir nada.

## Paso 2 · Mueve a IF todo lo que se pueda

Recorre tu tabla y en cada paso marcado como IA pregúntate: **¿puedo escribir la regla completa en una línea?**

Si la respuesta es sí, ese paso era un if disfrazado. Cámbialo.

Los sospechosos de siempre:

- **Umbrales.** «Aprueba si es menor a X» es un if. Lo que es IA es producir el número.
- **Normalizaciones.** «ACME SA» = «ACME S.A. de C.V.» es una tabla de alias, no criterio.
- **Filtros de entrada.** «Los correos con esta etiqueta» es una condición.
- **Enrutamiento por categoría ya definida.** Si la categoría ya viene decidida, mandarla a su destino es un if.

**Cada paso que sale de IA sube la confiabilidad de todo el sistema.** No es estética: es aritmética.

## Paso 3 · Cuenta lo que sobrevivió

Pasos de IA después del corte: `___`

Antes del corte: `0.95` a la `___` = `___`
Después del corte: `0.95` a la `___` = `___`

Esa diferencia es tu trabajo de hoy, y es defendible frente a cualquiera.

## Paso 4 · Mide el núcleo

Sobre los pasos de IA que sobrevivieron, haz los cinco casos de la [`RUTA-IA.md`](RUTA-IA.md).

Si te quedaron dos o más pasos de IA, **mide solo uno hoy**: el que más te preocupa. Los demás se miden igual, después.

## La pregunta que ordena todo

La pregunta no es «¿qué más puede hacer mi agente?».

Es **«¿qué puedo quitarle?»**.
