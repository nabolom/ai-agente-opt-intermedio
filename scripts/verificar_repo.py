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
    'Sesión 1 · Mapear el proceso',
    '## Outcome observable de S1',
    'my-automation.bolt.host',
    '## Outcomes observables de S2',
    'Descargar `s3-kit.zip`',
    'Inicia mi sesión 3',
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

if (ROOT / '.claude').exists() or (ROOT / 'CLAUDE.md').exists():
    fail('el repo intermedio no debe contener runtime de Claude Code')

print('OK — continuidad S1→S3, PDF, links, Skills, ZIPs, teoría, demos y seguridad validados.')
