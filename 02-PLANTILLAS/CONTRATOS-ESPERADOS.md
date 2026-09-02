# Contratos esperados

Cowork generará estos archivos dentro de `04-SALIDAS/` después de cada aprobación.

| Archivo | Debe contener | No pasa si… |
|---|---|---|
| `00_RESUMEN-VISION.md` | Persona, trigger, proceso, frecuencia, output, hechos/inferencias/faltantes. | Solo repite el nombre del proyecto. |
| `01_DIAGNOSTICO.md` | Bloqueos de datos, reglas, permisos, proceso y expectativa; causa raíz. | Confunde síntoma con causa. |
| `02_DECISION-IA-IF.md` | Veredicto IF, IA, híbrido o no automatizar; evidencia, confianza y condición de cambio. | Recomienda IA sin justificar ambigüedad. |
| `03_ALCANCE-Y-RIESGOS.md` | MVP, no-alcance, riesgo, gate humano y fallback. | Pretende ejecutar todo el proceso. |
| `04_HARNESS.md` | Objetivo, trigger, input, proceso, herramientas, restricciones, output, checker y límite. | Usa instrucciones vagas o permisos amplios. |
| `05_MEMORIA.md` | Fuente de verdad, hechos estables, decisiones, datos prohibidos, owner y change gate. | Guarda secretos o permite actualización silenciosa. |
| `06_PRUEBAS.md` | Normal, faltante, ambigua e insegura con PASS/FAIL. | Solo prueba el camino feliz. |
| `07_FICHA-FINAL.md` | Arquitectura, evidencia, decisión humana, limitaciones y siguiente mejora. | Afirma estar listo sin evidencia. |

## Cierre obligatorio de outputs

```text
ESTADO: BORRADOR PARA REVISIÓN
ACCIONES EXTERNAS EJECUTADAS: ninguna
EXCEPCIONES: [lista o “ninguna”]
DECISIÓN HUMANA NECESARIA: [decisión concreta]
```
