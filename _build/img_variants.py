"""Fase 4 · variantes de 800 y 1200 px de las capturas de proyectos (para srcset).
Lee static/projects/*.webp (1600 px) y escribe out/assets/projects/<nombre>-800.webp y -1200.webp.
Solo regenera una variante si el original es más nuevo, así que el build sigue siendo rápido."""
import os, glob
from PIL import Image
SRC = '/home/claude/neocortech/static/projects/'
OUT = '/home/claude/neocortech/out/assets/projects/'
WIDTHS = (800, 1200)
os.makedirs(OUT, exist_ok=True)
n = 0
for f in sorted(glob.glob(SRC + '*.webp')):
    name = os.path.splitext(os.path.basename(f))[0]
    if name.endswith(tuple('-%d' % w for w in WIDTHS)):
        continue
    im = None
    for w in WIDTHS:
        dst = f'{OUT}{name}-{w}.webp'
        if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(f):
            continue
        im = im or Image.open(f).convert('RGB')
        if im.width <= w:
            continue
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(dst, 'WEBP', quality=80, method=6)
        n += 1
print('variantes de imagen:', n, 'nuevas')
