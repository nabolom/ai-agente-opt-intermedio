# Acordeón del facilitador · S4

**No proyectes este archivo.**

## El recorte del caso de facturas

| # | Paso | Tipo | ¿V1? | Por qué |
|---:|---|---|---|---|
| 1 | Detectar el archivo nuevo | IF | Sí | Comparar contra lo ya registrado |
| 2 | Extraer datos del PDF | IA | Sí | Ya construido en S3 |
| 3 | Normalizar el proveedor | IF | Sí | Tabla de alias |
| 4 | Clasificar la categoría | IA | Sí | Con el default de la tabla |
| 5 | Validar contra presupuesto | IF | Sí | Umbral |
| 6 | Registrar en el ERP | Herramienta | **No** | **Frontera de permiso** |

## Nivel del caso

**B+C.** Alguien deja los PDF en la carpeta (entrada alimentada) y el agente se detiene antes de registrar (frontera de salida). Es el nivel de la mayoría del grupo.

## Las tres objeciones

**«¿Por qué no puede escribir en la hoja? Es un CSV.»**

Puede, técnicamente. La frontera aquí es de permiso, no de conector: escribir en el sistema contable es irreversible y nadie audita lo que un proceso desatendido escribió bien. Respuesta: *si la escritura es reversible y auditable, muévela dentro de la v1. Si no, se queda afuera.* Es una decisión de diseño, no una regla fija.

**«Entonces la automatización no ahorra tanto.»**

Cuenta en voz alta: 50 minutos de teclear contra 2 de pegar. El ahorro está casi completo. Lo que quedó afuera es el paso que menos tiempo tomaba y más riesgo tenía.

**«Mi proceso está todo dentro de un sistema sin conector.»**

Es el caso duro. Respuesta: *recorta a otra rebanada — casi siempre la capa de análisis o de preparación sí vive fuera del sistema cerrado.* Trabájalo con esa persona en el bloque individual, no frente al grupo.

## Las frases

> «La frontera no le quitó valor al proceso. Le puso un borde honesto.»

> «¿Qué necesita tener en la mano la persona para ejecutar en dos minutos?»

> «El martes no pueden esperar a que sean las 8:00 para demostrar.»
