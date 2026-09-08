# Demo S3 · Cómo correrla

Todo lo que necesitas está en `datos/`. Nada que preparar más allá de los pasos 1 y 2.

---

## ANTES DE LA SESIÓN · 5 minutos

1. Copia la carpeta `datos/` a tu computadora, en una ruta fácil de leer en pantalla. Sugerencia: `~/demo-s3/`
2. Abre Cowork → **Add Folder** → selecciona esa carpeta. Verifica que ve las tres facturas y los tres CSV.
3. Ten abierto en otra ventana `PEGAR-1-tabla-en-blanco.md`, en modo edición, listo para proyectar.
4. Ten `PEGAR-2-skill-extraer-factura.md` abierto para explicar qué contiene. El instalable está en `dist/extraer-factura.zip`.
5. **No abras** `TABLA-RESUELTA.md` en pantalla. Es tu acordeón, no material del grupo.

---

## MINUTO 0–3 · El punto de partida

6. Proyecta la lámina del veredicto: **HÍBRIDO**.
7. Pregunta al grupo: *«Con esto, ¿qué construyo primero?»*
8. Deja el silencio tres segundos. No respondas tú. La respuesta es que no se puede saber — ese es el punto de la sesión.

---

## MINUTO 3–12 · La tabla · **NO abras Cowork todavía**

9. Proyecta `PEGAR-1-tabla-en-blanco.md`. Tiene los seis pasos y la columna de tipo vacía.
10. Ve paso por paso preguntando al grupo: *«¿este paso decide algo, o sigue una regla?»*
11. Escribe la respuesta del grupo en la columna, en vivo. Aunque se equivoquen.
12. **Espera el paso 5.** Casi siempre alguien lo llama IA. Cuando pase, para y di:

    > «Decidir si aprobar no es IA si la regla es aprobar por debajo de X. Lo que es IA es producir el número, no compararlo.»

13. No expliques esto antes de que alguien se equivoque. El error tiene que ocurrir primero.

---

## MINUTO 12–14 · La aritmética

14. Cuenta los pasos de IA en voz alta. Son **dos**.
15. Escribe en pantalla:
    - Sin el corte: `0.95⁶ = 0.74`
    - Con el corte: `0.95² = 0.90`
16. Aclara que `0.95ⁿ` es un modelo didáctico —supone 95% por paso e independencia— y di: *«Mismo proceso, misma herramienta, mismo modelo. Cambió qué le pediste al modelo.»*

---

## MINUTO 14–20 · Construyes el paso 2 · **ahora sí, Cowork**

17. Cambia a Cowork, compartiendo pantalla.
18. Abre **Customize → Skills → + Create skill → Upload a skill**, instala `dist/extraer-factura.zip` y actívalo. Que vean el flujo completo — no lo tengas ya puesto.
19. Escribe en el chat, exactamente:

    ```
    extrae los datos de la factura de ACME
    ```

20. Sale bien. Señala que no subiste nada, que encontró el archivo solo.
21. Ahora escribe:

    ```
    extrae los datos de la factura de DEA
    ```

22. **Aquí debe activar revisión humana.** Hay dos ambigüedades reales:
    - El proveedor viene como «DEA» en el encabezado; el nombre real solo está en el pie.
    - Hay dos montos posibles: `A pagar 5,184.91` y `Saldo pendiente 3,184.91`.
23. Di los dos números en voz alta: **cobertura autónoma: 1 de 2; cobertura segura: 2 de 2**. ACME salió sin ayuda. DEA no se resolvió sola, pero el guard rail evitó que el sistema inventara.
24. Cierra con:

    > «Ese número imperfecto es el punto de partida. Escalar correctamente no es fracasar: es saber dónde termina la autonomía segura.»

---

## MINUTO 20 · El puente

25. Abre `../02-RUTAS/BLOQUE-60-MIN.md` en pantalla.
26. Di:

    > «Su tabla va a tener entre cuatro y ocho pasos, y entre uno y tres van a ser de IA. Los primeros quince minutos hacen la tabla. Después construyen el primero de esos pasos.»

27. Suéltalos.

---

## Si algo sale mal

**Cowork no encuentra las facturas.** Verifica que agregaste la carpeta `datos/` completa, no solo `facturas/`. Como respaldo, arrastra el PDF al chat — se pierde el efecto de «lo encontró solo» pero la demo continúa.

**La factura de DEA reporta las dos cifras y marca `revisar: sí`.** Es el resultado correcto: el skill detectó el límite y escaló. Pregunta *«¿qué habría pasado si hubiera elegido una cifra sin avisar?»*.

**La factura de DEA elige una cifra y marca `revisar: no`.** Ahí sí falló. Pregunta *«¿de dónde sacó el nombre del proveedor?»* y *«¿por qué eligió ese monto y no el otro?»*. La respuesta expone que adivinó.

**Te sobra tiempo.** Corre la tercera factura, la de TecnoGlobal. Es el caso intermedio: formato distinto pero sin ambigüedad.
