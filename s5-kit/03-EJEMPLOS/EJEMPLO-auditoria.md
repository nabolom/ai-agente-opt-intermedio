# Auditoría · Consolidación de facturas semanales
Fecha: 2026-09-14

## Dónde está hoy
Corre solo los lunes, consolida las facturas de la semana y deja un paquete listo para capturar. Lo que no corre es la captura en el ERP y la notificación al proveedor cuando falta una orden de compra.

## Gate
| Punto | Estado | Evidencia |
|---|---|---|
| v1 recortada | Cumplido | La v1 son 4 de los 9 pasos del proceso original |
| Frontera marcada y nombrada | Cumplido | Permiso — no hay acceso de escritura al ERP |
| Pasos encadenados en un Skill | Cumplido | `consolidacion-facturas/SKILL.md` |
| Tarea programada creada | Cumplido | Lunes 08:00 |
| Disparo manual verificado | Parcial | Se verificó una vez el 4 de septiembre, no se ha repetido |

## Pasos fuera de la v1
| Paso | Bloqueo | Qué lo desbloquea |
|---|---|---|
| Capturar en el ERP | Permiso | Pedirle al responsable de sistemas un usuario de escritura acotado a facturas |
| Notificar al proveedor sin OC | Nada | Está en el alcance del conector de correo actual, solo no se ha construido |
| Decidir si una factura ambigua se acepta | Juicio | Escribir el criterio de aceptación para volverlo verificable, o dejarlo humano |

## El siguiente paso
Construir la notificación al proveedor sin orden de compra en **modo borrador para revisión humana**. Es el único pendiente con bloqueo “Nada”, y es el paso que hoy consume las llamadas de seguimiento del miércoles.

## Las próximas dos semanas
1. Agregar el borrador de notificación al Skill y probarlo sin enviar, con un proveedor de baja criticidad.
2. Repetir el disparo manual una vez más para cerrar el punto parcial del gate.
3. Mandar la solicitud de usuario acotado a sistemas: sin eso, la captura en el ERP no avanza en ningún escenario.

## Huecos
No se encontró la tabla de pasos etiquetados. El conteo de 9 pasos se tomó de la descripción del proceso, no de la tabla original.
