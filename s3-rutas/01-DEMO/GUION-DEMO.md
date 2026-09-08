# Guion de la demo · 20 minutos

Los pasos operativos están en [`LEEME-DEMO.md`](LEEME-DEMO.md). Este archivo es el porqué de cada bloque.

## La demo tiene dos mitades

**Primera mitad — cortar.** No se hace en Cowork. Es un ejercicio de pensamiento y el valor está en que el grupo discuta si cada paso decide o sigue una regla. Abrir la herramienta ahí no agrega nada.

**Segunda mitad — construir.** Sí es Cowork. Si el grupo no te ve construir un paso, a los 35 minutos del bloque individual vas a tener seis personas atoradas sin saber qué hacer.

**La regla:** la demo es el ejercicio individual hecho una vez, en chiquito. Mismas dos mitades, mismo orden.

## La tabla resuelta

| # | Paso | Tipo | Por qué |
|---|---|---|---|
| 1 | Detectar el correo con factura | IF | Etiqueta o remitente. Es una condición, no un criterio. |
| 2 | Extraer datos del PDF | **IA** | Cada proveedor factura distinto. Documento no estructurado. |
| 3 | Normalizar el nombre del proveedor | IF | Tabla de alias. «DEA» = «Distribuidora El Águila». |
| 4 | Clasificar la categoría de gasto | **IA** | Requiere criterio sobre el concepto. |
| 5 | Validar contra presupuesto | IF | Un umbral sobre un número. |
| 6 | Escribir el renglón y marcar dudosos | Herramienta | Escritura en la hoja. No decide nada. |

## El paso que enseña

El **5**. Casi siempre alguien lo llama IA. No lo adelantes: deja que se equivoquen y ahí corriges. El error tiene que ocurrir primero para que la corrección se quede.

## Por qué la cobertura autónoma termina en 1 de 2

ACME puede resolverse sin ayuda; DEA debe escalar a revisión. El sistema no cubrió ambos casos de forma autónoma, pero sí manejó ambos de forma segura. Esa diferencia entre **cobertura** y **seguridad** es el aprendizaje.

La factura de DEA está diseñada para eso: nombre del proveedor solo en el pie y dos montos posibles. Si el skill reporta ambos y marca revisión, el guard rail funcionó; si elige uno sin avisar, falló.
