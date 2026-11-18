"""Sustituye las secciones Proyectos y Taller de sections_new.html por el índice interactivo."""
import json, re, sys
sys.path.insert(0, '/home/claude/neocortech/build')
from projects import proyectos_html, taller_html, BODY_ES

B = '/home/claude/neocortech/build/'
s = open(B + 'sections_new.html', encoding='utf-8').read()
bodies = json.load(open(B + 'bodies_es.json', encoding='utf-8'))
bodies.update(BODY_ES)

a = s.index('<!-- PROYECTOS')
b = s.index('</section>', a) + len('</section>\n')
s = s[:a] + proyectos_html(bodies) + s[b:]
a = s.index('<!-- TALLER')
b = s.index('</section>', a) + len('</section>\n')
s = s[:a] + taller_html(bodies) + s[b:]
open(B + 'sections_new.html', 'w', encoding='utf-8').write(s)
print('secciones ok')
