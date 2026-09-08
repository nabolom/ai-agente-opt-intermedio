# Caso de la demo · Facturas de proveedor

Caso neutral, no es el proceso de nadie del grupo. Sirve como plantilla visual del ejercicio.

## El proceso hoy

Llegan correos con facturas en PDF de unos 15 proveedores. Alguien abre cada correo, lee el PDF, y teclea el renglón en la hoja de gastos: proveedor, monto, fecha, categoría.

Toma entre 40 y 60 minutos diarios.

## Por qué funciona como demo

- Es reconocible para cualquier área.
- Tiene exactamente dos pasos donde el sistema decide, y cuatro que parecen decisiones y no lo son.
- El veredicto del coach fue «híbrido», que es lo que le va a tocar a la mayoría del grupo.

## Los archivos

Están en [`datos/`](datos/):

| Archivo | Para qué |
|---|---|
| `facturas/factura_acme_2026-03-04.pdf` | El caso limpio |
| `facturas/factura_tecnoglobal_2026-03-11.pdf` | Formato distinto, sin ambigüedad |
| `facturas/factura_dea_2026-03-18.pdf` | **El que activa revisión humana** |
| `alias_proveedores.csv` | La tabla que convierte el paso 3 en un IF |
| `presupuesto.csv` | El umbral del paso 5 |
| `hoja_gastos.csv` | El destino del paso 6 |

## Si alguien llega sin su proceso

Siéntalo con este caso. Sale con el método aprendido y lo aplica a lo suyo esta semana. No lo dejes sin ejercicio.
