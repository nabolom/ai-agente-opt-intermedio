# Demo S4 · Cómo correrla

Reutiliza los datos de `s3-rutas/01-DEMO/datos/`. No hay archivos nuevos que preparar.

---

## ANTES DE LA SESIÓN

1. Verifica que `s3-rutas/01-DEMO/datos/` sigue conectada en Cowork.
2. Confirma que el skill `extraer-factura` de S3 sigue en Settings → Skills.
3. **Prueba una tarea programada tuya**, cualquiera, y confirma que corrió.
4. No abras `FRONTERA-RESUELTA.md` en pantalla.

---

## PARTE 1 · ENCADENAR · 7 minutos

5. Proyecta la tabla de pasos de S3, la del caso de facturas.
6. Pregunta: *«¿cuáles de estos seis pasos podemos encender hoy?»*
7. Van a decir que los cinco primeros. El sexto —escribir en el ERP— es el que se atora.
8. Marca el recorte en pantalla: **v1 son cinco pasos. El sexto es la frontera.**
9. Pega el contenido de `PEGAR-1-skill-cadena-facturas.md` en Settings → Skills. Que te vean pegarlo.
10. Escribe en el chat:

    ```text
    procesa las facturas de la semana
    ```

11. Corre los cinco pasos seguidos. Señala en voz alta cada uno mientras pasa.

---

## PARTE 2 · LA FRONTERA · 6 minutos

12. Cuando termine, muestra el output y haz las tres preguntas:
    - *¿Dónde se detuvo?* En el paso 6.
    - *¿Por qué?* Frontera de permiso: escribir en el sistema contable es irreversible.
    - *¿Qué entregó en su lugar?* Los renglones listos para pegar, los dudosos marcados y las alertas de presupuesto.
13. Pregunta al grupo: *«¿cuánto tarda una persona en ejecutar esto?»* Dos minutos de copiar y pegar, contra 50 de teclear.
14. Di la frase:

    > «La frontera no le quitó valor al proceso. Le puso un borde honesto.»

15. Cierra con la pregunta que van a contestar ellos:

    > «¿Qué necesita tener en la mano la persona para ejecutar en dos minutos? La respuesta a eso es el output real de su proceso.»

---

## PARTE 3 · PROGRAMAR · 7 minutos

16. Di: *«ya corrió a mano y revisé el output. Ahora sí se puede encender.»*
17. Escribe en el chat:

    ```text
    /schedule
    ```

18. Contesta lo que te pregunte. Cadencia: diaria, 8:00.
19. Verifica que la tarea quedó creada y muéstrala en pantalla.
20. **Dispárala manualmente una vez.** Di:

    > «Esto no es opcional. El martes no pueden esperar a que sean las 8:00 para demostrar.»

21. Cierra:

    > «Cinco pasos encadenados, una frontera marcada y un trigger encendido. Eso es lo que van a hacer en la siguiente hora, con su proceso.»

> Si la demo depende de la carpeta local de S3, mantenla disponible mediante Claude Desktop. La ejecución remota solo aplica cuando las fuentes necesarias están disponibles mediante conectores o archivos guardados en la cuenta.

---

## Si algo sale mal

**La cadena se rompe a la mitad.** Perfecto para enseñar: muestra en qué paso se detuvo y pregunta al grupo si es un problema de la regla o del dato. Es el diagnóstico de S3 aplicado.

**`/schedule` no aparece.** Actualiza la app. Si no da tiempo, explica el flujo con la lámina y sigue — el grupo lo hace en el bloque individual.

**La tarea programada no corre.** Muestra la ejecución manual y sé explícito: *«así lo van a demostrar el martes de todos modos.»*
