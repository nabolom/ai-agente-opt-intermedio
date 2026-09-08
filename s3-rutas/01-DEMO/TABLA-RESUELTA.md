# Acordeón del facilitador

**No proyectes este archivo.**

---

## La tabla resuelta

| # | Paso | Tipo | Por qué |
|---|---|---|---|
| 1 | Detectar el correo con factura | **IF** | Etiqueta o remitente. Es una condición, no un criterio. |
| 2 | Extraer datos del PDF | **IA** | Cada proveedor factura distinto. Documento no estructurado. |
| 3 | Normalizar el nombre del proveedor | **IF** | Tabla de alias. «DEA» = «Distribuidora El Águila». Está en `datos/alias_proveedores.csv`. |
| 4 | Clasificar la categoría de gasto | **IA** | Requiere criterio sobre el concepto. |
| 5 | Validar contra presupuesto | **IF** | Un umbral sobre un número. Está en `datos/presupuesto.csv`. |
| 6 | Escribir el renglón y marcar dudosos | **Herramienta** | Escritura en la hoja. No decide nada. |

**Pasos de IA: 2.** `0.95² = 0.90` contra `0.95⁶ = 0.74`. Es un modelo didáctico que supone 95% por paso e independencia; la medición real viene de los casos de prueba.

---

## Las cuatro objeciones que vas a recibir

**«El paso 5 es IA porque decide si aprobar.»**
Es la objeción que buscas. Respuesta: *decidir si aprobar no es IA si la regla es aprobar por debajo de X. Lo que es IA es producir el número, no compararlo.* Si nadie la dice, provócala: pregunta explícitamente si el paso 5 es IA.

**«El paso 3 es IA porque tiene que reconocer que DEA es El Águila.»**
Buena objeción, y la respuesta es que depende de si la tabla de alias existe. Con la tabla, es un IF. Sin ella, es IA. Muestra `alias_proveedores.csv` y di: *esta tabla convirtió un paso de IA en un if. Eso es trabajo de diseño, no de modelo.*

**«El paso 4 podría ser un IF si cada proveedor tiene su categoría fija.»**
Correcta, y vale la pena reconocerla en voz alta. Respuesta: *sí, y ahí tendrían un solo paso de IA en todo el proceso — 0.95. Pero se rompe el día que ACME les venda algo que no es mantenimiento.* Ejemplo perfecto de la tensión entre confiabilidad y cobertura.

**«¿Y el paso 1 no debería ser IA para detectar si es factura o no?»**
Respuesta: *si el proveedor manda todo a la misma dirección con la misma etiqueta, es un filtro. Si manda facturas, cotizaciones y quejas al mismo buzón sin distinguir, entonces sí es IA — y les acaba de crecer el proceso a tres pasos de IA.* Buen momento para mostrar cómo el diseño del input cambia la aritmética.

---

## Qué pasa con cada factura

| Archivo | Qué esperar |
|---|---|
| `factura_acme_2026-03-04.pdf` | Sale limpio. Total `$12,450.00`, fecha `04/03/2026`, proveedor completo en el encabezado. |
| `factura_dea_2026-03-18.pdf` | **La que activa revisión humana.** Encabezado dice «DEA», nombre real solo en el pie. Dos montos posibles: `A pagar 5,184.91` y `Saldo pendiente 3,184.91`. |
| `factura_tecnoglobal_2026-03-11.pdf` | Caso intermedio. Formato distinto, fecha en texto, pero sin ambigüedad. Úsala si te sobra tiempo. |

---

## La frase de cierre

> «Ese número imperfecto es el punto de partida. Escalar correctamente no es fracasar: es saber dónde termina la autonomía segura.»
