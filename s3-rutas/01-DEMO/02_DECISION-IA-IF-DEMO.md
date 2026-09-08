# 02 · Decisión IA / IF

> Artefacto de referencia. Reproduce el formato que el coach entrega en S2.

## Veredicto

**HÍBRIDO**

## Evidencia

**Por qué no es IF puro.** Las facturas llegan en PDF con formatos distintos por proveedor. No hay una posición fija de la que se pueda leer el monto con una regla. Extraer requiere interpretar un documento no estructurado.

**Por qué no es IA pura.** Cuatro de los seis pasos tienen reglas completas y salida exacta: el filtro de correo, la normalización del proveedor, la validación de presupuesto y la escritura en la hoja. Pasarlos por un modelo agrega error sin agregar criterio.

**Dónde vive la ambigüedad real.** En dos lugares: leer el PDF y decidir la categoría de gasto cuando el concepto no es obvio.

## Alcance del MVP

Los seis pasos, con los dudosos marcados para revisión humana en vez de resueltos por el sistema.

## Decisión humana

Ningún renglón marcado como dudoso se da por bueno sin que una persona lo confirme.

## Lo que este documento NO dice

Este veredicto es del proceso completo. No dice qué paso construir primero ni cuáles pasos son deterministas.

**Eso es exactamente el trabajo de hoy.**
