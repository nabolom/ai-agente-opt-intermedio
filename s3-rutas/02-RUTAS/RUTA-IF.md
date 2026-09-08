# Ruta IF

Tu proceso no necesita un agente. Necesita sus reglas escritas.

**Un IF ejecuta la misma regla de forma determinística.** Su confiabilidad depende de que la regla sea correcta y cubra los casos reales. Si documentas excepciones y conflictos, tu sistema puede ser el más confiable del salón.

## Qué construyes hoy

Tu tabla de reglas completa: una fila por regla.

| Input | Condición | Acción | Excepción |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

- **Input** — qué entra y de dónde viene.
- **Condición** — la regla, escrita completa. Sin «según el caso» ni «normalmente».
- **Acción** — qué pasa exactamente cuando la condición se cumple.
- **Excepción** — qué pasa cuando no se cumple ninguna regla.

## La parte que importa

**La regla que no puedas escribir es un hueco real en tu proceso.** No la fuerces. Anótala aparte:

> Reglas que no pude escribir:
> - [ ]
> - [ ]

Esa lista es el entregable más valioso de tu sesión. Cada renglón es una decisión que hoy alguien toma de memoria y nadie documentó. Si esa persona se va, el proceso se va con ella.

## Cómo lo pruebas hoy

Toma cinco casos reales de la última semana. Pásalos por tu tabla a mano, uno por uno.

- ¿Los cinco encontraron una regla que aplicara?
- ¿Alguno cayó en la excepción?
- ¿Alguno encontró **dos** reglas que aplicaban a la vez? Eso es un conflicto: resuélvelo con un orden de prioridad.

## Si te sobra tiempo

Escribe la regla que hoy dejaste en la lista de «no pude escribir». Pregúntale a la persona que sí sabe. Esa conversación es el trabajo real.

## Dónde va a correr esto

Hoy no. Una tabla de reglas necesita un motor determinístico con un disparador de evento, y eso es tema de S4. Hoy lo que importa es que las reglas existan escritas y probadas contra casos reales.
