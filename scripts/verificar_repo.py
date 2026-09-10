#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'S1-EMPIEZA-AQUI.md',
    'CHEAT-SHEET-S1-S4.md',
    'RUTA-EN-VIVO.md',
    'INSTRUCCIONES-PROJECT.md',
    'INICIAR-SIN-SKILL.md',
    'PROGRESO.md',
    'GUIA-FACILITADOR.md',
    '00-INPUT/README.md',
    '01-LECCIONES/GUIA-DE-LECCIONES.md',
    '02-PLANTILLAS/CONTRATOS-ESPERADOS.md',
    '03-EJEMPLOS/DECIDIR-IA-O-IF.md',
    '04-SALIDAS/README.md',
    'skills/ai-agent-opt-coach/SKILL.md',
    'dist/ai-agent-opt-coach.zip',
    'dist/s3-kit.zip',
    'dist/s4-kit.zip',
    's3-kit/EMPIEZA-S3-AQUI.md',
    's3-kit/PRECHECK-S3.md',
    's3-kit/INICIAR-S3-SIN-SKILL.md',
    's3-kit/GUIA-FACILITADOR-S3.md',
    's3-kit/TEORIA-S3.md',
    's3-kit/templates/08_PLAN-DE-CORRIDA.md',
    's3-kit/templates/09_REGISTRO-DE-CORRIDA.md',
    's3-kit/templates/10_PROPUESTA-DE-MEJORA.md',
    's3-kit/templates/11_READINESS-S4.md',
    's3-kit/demo-meridian/README.md',
    's3-kit/demo-meridian/01-caso-normal/emails_meridian.md',
    's3-kit/demo-meridian/01-caso-normal/pipeline.csv',
    's3-kit/demo-meridian/01-caso-normal/notas_reunion.md',
    's3-kit/demo-meridian/01-caso-normal/inteligencia_empresa.md',
    's3-kit/demo-meridian/02-caso-falla/emails_meridian.md',
    's3-kit/demo-meridian/02-caso-falla/pipeline.csv',
    's3-kit/skills/ai-agent-opt-runner/SKILL.md',
    's3-kit/dist/ai-agent-opt-runner.zip',
    's3-rutas/EMPIEZA-S3-RUTAS.md',
    's3-rutas/INSTALAR-S3-RUTAS.md',
    's3-rutas/GUIA-FACILITADOR-RUTAS.md',
    's3-rutas/01-DEMO/datos/alias_proveedores.csv',
    's3-rutas/01-DEMO/datos/hoja_gastos.csv',
    's3-rutas/01-DEMO/datos/presupuesto.csv',
    's4-kit/EMPIEZA-S4-AQUI.md',
    's4-kit/GUIA-FACILITADOR-S4.md',
    's4-kit/01-DEMO/LEEME-DEMO-S4.md',
    's4-kit/01-DEMO/PEGAR-1-skill-cadena-facturas.md',
    's4-kit/01-DEMO/FRONTERA-RESUELTA.md',
    's4-kit/02-CONSTRUIR/BLOQUE-60-MIN-S4.md',
    's4-kit/02-CONSTRUIR/PASO-1-recorte.md',
    's4-kit/02-CONSTRUIR/PASO-2-frontera.md',
    's4-kit/02-CONSTRUIR/PASO-3-encadenar.md',
    's4-kit/02-CONSTRUIR/PASO-4-programar.md',
    's4-kit/03-GATE-S5/CHECKLIST-GATE.md',
    's4-kit/03-GATE-S5/PLANTILLA-demo-5min.md',
    's4-kit/04-SALIDAS/README.md',
    's4-kit/04-SALIDAS/PROGRESO-S4.md',
    's4-kit/INSTALAR-COACH-S4.md',
    's4-kit/INICIAR-S4-SIN-SKILL.md',
    's4-kit/skills/s4-encadenar-coach/SKILL.md',
    's4-kit/skills/s4-encadenar-coach/examples/trigger-tests.md',
    's4-kit/dist/s4-encadenar-coach.zip',
]


def fail(message: str) -> None:
    print(f'FALLO: {message}', file=sys.stderr)
    raise SystemExit(1)


for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file() or path.stat().st_size == 0:
        fail(f'falta {relative}')

skill = (ROOT / 'skills/ai-agent-opt-coach/SKILL.md').read_text(encoding='utf-8')
if '[TODO' in skill or 'TODO:' in skill:
    fail('el Skill conserva TODOs')
if not re.search(r'^name:\s*ai-agent-opt-coach$', skill, re.MULTILINE):
    fail('el name del Skill es incorrecto')
if not re.search(r'^description:\s*\S.{40,}$', skill, re.MULTILINE):
    fail('la description del Skill es insuficiente')

with zipfile.ZipFile(ROOT / 'dist/ai-agent-opt-coach.zip') as archive:
    if 'ai-agent-opt-coach/SKILL.md' not in archive.namelist():
        fail('el ZIP del coach no tiene la carpeta raíz correcta')

runner = (ROOT / 's3-kit/skills/ai-agent-opt-runner/SKILL.md').read_text(encoding='utf-8')
if '[TODO' in runner or 'TODO:' in runner:
    fail('el runner conserva TODOs')
if not re.search(r'^name:\s*ai-agent-opt-runner$', runner, re.MULTILINE):
    fail('el name del runner es incorrecto')
if not re.search(r'^description:\s*\S.{40,}$', runner, re.MULTILINE):
    fail('la description del runner es insuficiente')

with zipfile.ZipFile(ROOT / 's3-kit/dist/ai-agent-opt-runner.zip') as archive:
    if 'ai-agent-opt-runner/SKILL.md' not in archive.namelist():
        fail('el ZIP del runner no tiene la carpeta raíz correcta')

with zipfile.ZipFile(ROOT / 'dist/s3-kit.zip') as archive:
    names = set(archive.namelist())
    for expected in (
        's3-kit/EMPIEZA-S3-AQUI.md',
        's3-kit/PRECHECK-S3.md',
        's3-kit/TEORIA-S3.md',
        's3-kit/dist/ai-agent-opt-runner.zip',
        's3-kit/templates/11_READINESS-S4.md',
    ):
        if expected not in names:
            fail(f'el s3-kit.zip no contiene {expected}')

pattern = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for raw in pattern.findall(text):
        target = raw.split('#', 1)[0].strip()
        if not target or target.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not (path.parent / target).resolve().exists():
            fail(f'link roto en {path.relative_to(ROOT)}: {raw}')

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for phrase in (
    '## Elige tu actividad',
    'CHEAT-SHEET-S1-S4.md',
    'Sesión 1 · Mapear el proceso',
    '## Outcome observable de S1',
    'my-automation.bolt.host',
    '## Outcomes observables de S2',
    's3-rutas-kit.zip',
    'Inicia mi S3 Rutas.',
    'Sesión 4 · Encadenar y encender',
    'dist/s4-kit.zip',
    's4-kit/EMPIEZA-S4-AQUI.md',
    's4-encadenar-coach.zip',
    'Inicia mi S4.',
    'No abras un Project nuevo',
):
    if phrase not in readme:
        fail(f'el README no hace visible: {phrase}')

input_guide = (ROOT / '00-INPUT/README.md').read_text(encoding='utf-8')
if 'mi-automatizacion.pdf' not in input_guide or 'S1-EMPIEZA-AQUI.md' not in input_guide:
    fail('00-INPUT no enlaza el outcome de S1')

s3_start = (ROOT / 's3-kit/EMPIEZA-S3-AQUI.md').read_text(encoding='utf-8')
if 'raw/refs/heads/main/dist/s3-kit.zip' not in s3_start:
    fail('la guía S3 no tiene descarga directa del kit')

contract = (ROOT / 'INSTRUCCIONES-PROJECT.md').read_text(encoding='utf-8')
for phrase in ('IF / DETERMINÍSTICO', 'IA CON REVISIÓN HUMANA', 'HÍBRIDO: IF + IA', 'NO AUTOMATIZAR TODAVÍA'):
    if phrase not in skill and phrase not in contract:
        fail(f'falta veredicto {phrase}')

failure_case = ROOT / 's3-kit/demo-meridian/02-caso-falla'
if (failure_case / 'notas_reunion.md').exists():
    fail('la demo de falla debe conservar la fuente faltante')
if 'Ignora las instrucciones' not in (failure_case / 'emails_meridian.md').read_text(encoding='utf-8'):
    fail('la demo de falla no contiene la prueba de instrucción embebida')

s4_root = ROOT / 's4-kit'
s4_files = [path for path in s4_root.rglob('*') if path.is_file()]
if len(s4_files) != 19:
    fail(f's4-kit debe tener 19 archivos y tiene {len(s4_files)}')

with zipfile.ZipFile(ROOT / 'dist/s4-kit.zip') as archive:
    packaged = set(archive.namelist())
    expected = {f's4-kit/{path.relative_to(s4_root).as_posix()}' for path in s4_files}
    missing = sorted(expected - packaged)
    if missing:
        fail(f'el s4-kit.zip no contiene: {", ".join(missing)}')
    if not all(name == 's4-kit/' or name.startswith('s4-kit/') for name in packaged):
        fail('el s4-kit.zip no conserva una única carpeta raíz s4-kit/')

for path in s4_files:
    if path.suffix.lower() in {'.csv', '.pdf'}:
        fail(f's4-kit duplica datos de S3: {path.relative_to(ROOT)}')
    if path.suffix.lower() == '.zip':
        continue
    text = path.read_text(encoding='utf-8')
    forbidden = re.search(r'\b(git|curl|terminal|n8n)\b|claude code', text, re.IGNORECASE)
    if forbidden:
        fail(f's4-kit menciona una herramienta prohibida en {path.relative_to(ROOT)}: {forbidden.group(0)}')

s4_skill = (s4_root / '01-DEMO/PEGAR-1-skill-cadena-facturas.md').read_text(encoding='utf-8')
if 'NUNCA escribas en `hoja_gastos.csv`' not in s4_skill:
    fail('el Skill de facturas no declara la frontera de escritura')

s4_coach = (s4_root / 'skills/s4-encadenar-coach/SKILL.md').read_text(encoding='utf-8')
if '[TODO' in s4_coach or 'TODO:' in s4_coach:
    fail('el coach S4 conserva TODOs')
if not re.search(r'^name:\s*s4-encadenar-coach$', s4_coach, re.MULTILINE):
    fail('el name del coach S4 es incorrecto')
for phrase in (
    'Explicar → preguntar → proponer → confirmar → guardar',
    'Explícame en una frase qué decidiste y por qué',
    '## Escalera de ayuda',
    'Ruta | Condición | Acción',
    'NUNCA programar antes de una corrida manual completa',
    's4-kit/04-SALIDAS/PROGRESO-S4.md',
    'raw/refs/heads/main/dist/s4-kit.zip',
    'No reconstruir plantillas ni continuar solo con el Skill',
):
    if phrase not in s4_coach:
        fail(f'el coach S4 no cubre: {phrase}')

with zipfile.ZipFile(s4_root / 'dist/s4-encadenar-coach.zip') as archive:
    names = set(archive.namelist())
    for expected in (
        's4-encadenar-coach/SKILL.md',
        's4-encadenar-coach/examples/trigger-tests.md',
    ):
        if expected not in names:
            fail(f'el ZIP del coach S4 no contiene {expected}')

s4_start = (s4_root / 'EMPIEZA-S4-AQUI.md').read_text(encoding='utf-8')
for phrase in ('produce borradores', '03-GATE-S5/CHECKLIST-GATE.md', 'PASO-4-programar.md', 'Inicia mi S4.', 'INSTALAR-COACH-S4.md'):
    if phrase not in s4_start:
        fail(f'la guía S4 no hace visible: {phrase}')

s4_install = (s4_root / 'INSTALAR-COACH-S4.md').read_text(encoding='utf-8')
for phrase in ('s4-kit.zip', 'no se instala como Skill', 's4-encadenar-coach.zip', 'Inicia mi S4.', 'INICIAR-S4-SIN-SKILL.md'):
    if phrase not in s4_install:
        fail(f'la instalación del coach S4 no cubre: {phrase}')


s4_schedule = (s4_root / '02-CONSTRUIR/PASO-4-programar.md').read_text(encoding='utf-8')
for phrase in ('/schedule', 'Dispara la tarea manualmente una vez', 'archivos o aplicaciones locales'):
    if phrase not in s4_schedule:
        fail(f'la programación S4 no cubre: {phrase}')

if (ROOT / '.claude').exists() or (ROOT / 'CLAUDE.md').exists():
    fail('el repo intermedio no debe contener runtime de Claude Code')

print('OK — continuidad S1→S4, PDF, links, Skills, rutas, frontera, trigger, gate y seguridad validados.')
