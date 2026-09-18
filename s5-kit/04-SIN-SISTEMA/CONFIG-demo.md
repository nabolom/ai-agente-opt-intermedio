# Configuración base · demo

El coach usa este bloque automáticamente. No tienes que copiar rutas ni editar archivos.

PROCESO: Consolidación semanal de embarques
ENTRADA: s5-kit/04-SIN-SISTEMA/entrada-demo/
SALIDA: s5-kit/04-SIN-SISTEMA/salida-demo/
REPORTES: s5-kit/07-SALIDAS/
CADENCIA: todos los lunes a las 8:00, con ventana aceptable de 15 minutos
FRONTERA: permiso — el sistema no escribe en el sistema de transporte; deja un paquete revisable
CRITERIO 1: Toda cifra del resumen aparece y coincide con el detalle de la fuente
CRITERIO 2: Cada cliente, ruta y pendiente de la fuente aparece con detalle en el output
CRITERIO 3: El registro de ejecución confirma que no hubo escritura ni envío externo
CRITERIO CRÍTICO: CRITERIO 2 — si falta un cliente, ruta o pendiente, el consolidado no es utilizable
