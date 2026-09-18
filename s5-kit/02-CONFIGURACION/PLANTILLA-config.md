# Configuración de revisión · referencia

No tienes que llenar esto antes de instalar el coach. Durante la conversación, el coach localizará lo que pueda, te preguntará solo lo que falte, propondrá un borrador y lo guardará después de tu confirmación en `s5-kit/07-SALIDAS/config-revision.md`.

| Campo | Qué significa | De dónde puede salir |
|---|---|---|
| PROCESO | Nombre entendible del trabajo | Gate de S4 o tu explicación |
| ENTRADA | Carpeta o archivos que consume | Project y output de S3/S4 |
| SALIDA | Carpeta donde quedó el resultado | Última corrida visible |
| REPORTES | Lugar separado para la revisión | Siempre `s5-kit/07-SALIDAS/` |
| CADENCIA | Cuándo debía correr y qué retraso es aceptable | Panel Scheduled o tu confirmación |
| FRONTERA | Dónde debe detenerse | `frontera.md` o gate de S4 |
| CRITERIO 1 | Condición verificable de calidad | Output esperado |
| CRITERIO 2 | Condición verificable de completitud o seguridad | Fuentes y frontera |
| CRITERIO 3 | Condición adicional | Opcional |

## Cómo se verá el archivo

```text
PROCESO: ...
ENTRADA: ...
SALIDA: ...
REPORTES: s5-kit/07-SALIDAS/
CADENCIA: ...
FRONTERA: ...
CRITERIO 1: ...
CRITERIO 2: ...
CRITERIO 3: ... o NO APLICA
CRITERIO CRÍTICO: ... o NINGUNO
```

## Regla

El coach puede proponer nombres y criterios a partir de evidencia, pero tú debes confirmarlos. No debe inventar una ruta, una cadencia ni una frontera.
