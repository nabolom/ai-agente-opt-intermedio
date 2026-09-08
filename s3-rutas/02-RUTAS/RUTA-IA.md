# Ruta IA

Tu proceso tiene un paso donde el sistema decide de verdad. Hoy le pones número.

## Qué construyes hoy

Cinco casos de prueba y tu primera tasa de acierto.

## Qué es un caso

**Un input y la salida que tú esperas.** Nada más.

```
Input:            [lo que entra, tal como llega en la realidad]
Salida esperada:  [lo que debería salir]
```

## La regla que lo vuelve real

**La salida esperada la fijas tú, antes de correr nada.**

Un «correcto» que solo Claude puede confirmar no es una prueba. Si para saber si acertó tienes que volver a preguntarle al modelo, no mediste nada.

## El reparto

| Cantidad | Tipo | Para qué |
|---|---|---|
| 3 | Típicos | Confirman lo obvio |
| 1 | De límite | Donde vive la ambigüedad real |
| 1 | Adversarial | Intenta romperlo a propósito |

**Cinco casos del camino feliz sacan 5/5 y el número te miente hacia arriba.** El de límite y el adversarial son los que enseñan.

Si no se te ocurre el caso de límite, piensa en el que a ti mismo te costaría decidir.

## Tu suite

| # | Tipo | Input | Salida esperada | ¿Acertó? |
|---|---|---|---|---|
| 1 | típico |  |  |  |
| 2 | típico |  |  |  |
| 3 | típico |  |  |  |
| 4 | límite |  |  |  |
| 5 | adversarial |  |  |  |

**Mi número: `___ / 5`**

## Cuando el número está feo

En este orden. No te saltes escalones.

1. **¿La regla está escrita ambigua?** El caso más común, con muchísima diferencia.
2. **¿Faltan ejemplos, sobre todo del caso límite?**
3. **¿Le estás pidiendo IA a algo que era un if?** Vuelve a tu tabla de pasos.
4. **¿El modelo es el adecuado?** Casi nunca es la respuesta.

El que ve un número feo y dice «mejor le pongo un modelo más grande» no diagnosticó: adivinó.

## Al terminar

Escribe una línea: qué cambiaste y si el número subió. Si subió sin que sepas por qué, fue suerte.
