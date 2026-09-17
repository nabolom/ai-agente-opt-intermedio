# Medir y mejorar · después de la sesión

La verificación te dice si una corrida pasó. Esto es distinto: te dice si tu sistema está mejorando o empeorando con el tiempo.

Necesita cuatro cosas. Si te falta una, no funciona.

## 1 · Una métrica con número

“Que salga bien” no se puede graficar. Estas sí:

- Porcentaje de outputs que pasaron sin que nadie los tocara.
- Número de hallazgos por corrida.
- Minutos entre que el sistema termina y alguien usa el resultado.
- Porcentaje de casos que llegaron a la frontera y requirieron decisión humana.

Elige una. Una sola.

## 2 · Una medición por corrida

Cada semana, después de que tu revisor entregue su reporte, anotas el número. Si mides una vez al mes tienes una anécdota, no una serie.

## 3 · Memoria

Un archivo donde viven las corridas anteriores. Sin eso, cada semana empieza de cero. Usa [`PLANTILLA-bitacora.md`](PLANTILLA-bitacora.md) de esta carpeta.

## 4 · Un cambio por iteración

Si cambias dos cosas y el número sube, no sabes cuál lo movió. Un cambio, una semana, un resultado.

## Prompt listo para pegar

Úsalo en Cowork cada semana, después de leer tu reporte de supervisión:

> Lee mi bitácora en [ruta a la bitácora] y el reporte de supervisión más reciente en [ruta a la carpeta de reportes]. Agrega un renglón nuevo a la bitácora con la semana, el valor de mi métrica esta semana, el cambio que apliqué la semana pasada y si el número subió, bajó o se quedó igual. Después dime una sola cosa: cuál es el único cambio que aplicaría la próxima semana y qué número espero que mueva. Si el cambio de la semana pasada empeoró la métrica, la recomendación es revertirlo. No modifiques ningún otro archivo.

## El límite

En Cowork, esto es asistido: el sistema mide y propone, tú apruebas el cambio. Que se modifique solo requiere infraestructura que no vive en tu escritorio.
