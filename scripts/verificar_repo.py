#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
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
        fail('el ZIP no tiene la carpeta raíz correcta')

pattern = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    for raw in pattern.findall(text):
        target = raw.split('#', 1)[0].strip()
        if not target or target.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not (path.parent / target).resolve().exists():
            fail(f'link roto en {path.relative_to(ROOT)}: {raw}')

contract = (ROOT / 'INSTRUCCIONES-PROJECT.md').read_text(encoding='utf-8')
for phrase in ('IF / DETERMINÍSTICO', 'IA CON REVISIÓN HUMANA', 'HÍBRIDO: IF + IA', 'NO AUTOMATIZAR TODAVÍA'):
    if phrase not in skill and phrase not in contract:
        fail(f'falta veredicto {phrase}')

if (ROOT / '.claude').exists() or (ROOT / 'CLAUDE.md').exists():
    fail('el repo intermedio no debe contener runtime de Claude Code')

print('OK — onboarding, links, coach, ZIP, árbol IA/IF y seguridad validados.')
