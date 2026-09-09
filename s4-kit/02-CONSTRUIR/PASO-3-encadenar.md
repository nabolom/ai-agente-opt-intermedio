# Paso 3 · Encadena · 25 min

Un solo skill que corre de punta a punta, de la entrada a tu frontera.

## La estructura

```markdown
---
name: [nombre-de-tu-proceso]
description: >
  Usar cuando el usuario escriba: "[FRASE DE INVOCACIÓN]"
---

## Rol
[Quién es el agente para este proceso.]

## Input
[Cada fuente con su ruta exacta.]
Si falta [la crítica], detente y dilo. No continúes con supuestos.

## Proceso
1. [Paso 1 de tu v1]
2. [Paso 2]
3. [...]
N. Arma el paquete de ejecución con el formato de Output.

## Output
[El paquete: qué lleva, en qué orden, con qué formato.]

## Restricciones
NUNCA [escribas / envíes / registres] en [tu frontera].
NUNCA inventes un dato que no esté en la fuente.
[Tus restricciones propias.]
```

## Las tres cosas que lo hacen funcionar

**Un solo skill, no varios encadenados a mano.** Si tienes que invocar tres veces, no es una cadena.

**La frontera va escrita como restricción.** No como comentario. `NUNCA escribas en X` es lo que hace que el trigger sea seguro.

**Cada paso dice qué hacer si falla.** Un paso que se detiene y avisa es mejor que uno que sigue con un dato inventado.

## Pruébalo

Corre la cadena a mano con tu frase de invocación. Sin instrucciones extra.

- ¿Corrió los pasos en orden?
- ¿Se detuvo en tu frontera, o se pasó?
- ¿El output es un paquete ejecutable, o todavía es un análisis?

**Revisa el archivo que produjo, no el resumen que te dio.** No son lo mismo.

## Antes de seguir

- [ ] Un solo skill, una sola frase de invocación.
- [ ] La frontera está escrita como `NUNCA`.
- [ ] Corrió completa al menos una vez.
- [ ] Revisé el output real, no el resumen.
