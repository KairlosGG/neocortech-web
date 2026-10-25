"""Wattprint v2: copia la herramienta desde el repositorio aparte y actualiza los textos de /wattprint."""
import re, json
OUT = '/home/claude/neocortech/out/'
REPO = '/home/claude/wattprint/index.html'

URL = 'https://wattprint-kappa.vercel.app/'  # la herramienta vive en su propio proyecto de Vercel

p = OUT + 'wattprint.html'
s = open(p, encoding='utf-8').read()
R = [
 ('/tool/wattprint · sin registro · datos Ember + Uptime Institute', 'wattprint-kappa.vercel.app · sin registro · ES/EN · datos Ember, Uptime Institute y WRI'),
 ('/tool/wattprint · no sign-up · Ember + Uptime Institute data', 'wattprint-kappa.vercel.app · no sign-up · ES/EN · Ember, Uptime Institute and WRI data'),
 ('Calcula la huella de tus entrenamientos e inferencias en 60 segundos. Metodología SCI (ISO/IEC 21031). Gratis y sin registro.',
  'Calcula la huella de tus entrenamientos e inferencias, también por petición, y descarga el informe en PDF o CSV. Metodología SCI (ISO/IEC 21031). Gratis y sin registro.'),
 ('Calculate the footprint of your training runs and inference in 60 seconds. SCI methodology (ISO/IEC 21031). Free, no sign-up. The tool is in Spanish.',
  'Calculate the footprint of your training and inference runs, per request too, and download the report as PDF or CSV. SCI methodology (ISO/IEC 21031). Free, no sign-up.'),
 ('El coste hídrico de la refrigeración, estimado con el WUE. La huella',
  'El agua de refrigeración (WUE) y la que se gasta al generar la electricidad (factores del WRI). La huella'),
 ('The water cost of cooling, estimated with WUE. The footprint',
  'Cooling water (WUE) and the water used to generate the electricity (WRI factors). The footprint'),
 ('PUE (energía) y WUE (agua). Es lo que', 'el PUE. Es lo que'),
 ('PUE (energy) and WUE (water). It turns', 'PUE. It turns'),
 ('en 60 segundos', 'en un minuto'),
 ('href="/tool/wattprint/"', 'href="' + URL + '"'), ('in 60 seconds', 'in a minute'),
]
for a, b in R:
    n = s.count(a)
    assert n or b in s, a[:60]
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print('wattprint v2 ok')
