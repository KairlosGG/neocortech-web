import re
OUT='/home/claude/neocortech/out/'

# fase 4: en el portfolio (/ y /en) las @font-face van en línea (sin la petición bloqueante a fonts.css),
# solo con las caras que usa, con fuentes de reserva ajustadas (menos salto al llegar la fuente) y precarga de las tres del hero.
# Métricas de las reservas: /home/claude/audit/fase4-scripts/fallback_metrics.py (frente a Liberation = Arial/Times New Roman).
FACES = [('Cinzel', 400, 'cinzel-latin-400'), ('Cinzel', 500, 'cinzel-latin-500'), ('Inter', 400, 'inter-latin-400'),
         ('Inter', 500, 'inter-latin-500'), ('Inter', 600, 'inter-latin-600'), ('Inter', 700, 'inter-latin-700'),
         ('Cinzel Decorative', 700, 'cinzel-decorative-latin-700'), ('Marcellus', 400, 'marcellus-latin-400')]
# Solo las dos de Cinzel del titular (LCP): con tres, el JS (del que depende quitar la cortina) llegaba más tarde en Slow 4G.
PRELOAD = ['cinzel-latin-400', 'cinzel-latin-500']
SERIF = 'local("Times New Roman"),local("TimesNewRomanPSMT"),local("Liberation Serif"),local("Tinos"),local("Times")'
SANS = 'local("Arial"),local("ArialMT"),local("Liberation Sans"),local("Arimo"),local("Helvetica")'
FALLBACKS = [('Cinzel Fallback', SERIF, '131.5%', '74.2%', '28.3%'),
             ('Marcellus Fallback', SERIF, '110.7%', '88%', '25.3%'),
             ('Inter Fallback', SANS, '105.5%', '91.8%', '22.9%')]
INLINE = ('<style>' + ''.join(
    f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(/assets/fonts/{f}-normal.woff2) format('woff2')}}"
    for fam, w, f in FACES) + ''.join(
    f'@font-face{{font-family:"{n}";src:{src};size-adjust:{sa};ascent-override:{a};descent-override:{d};line-gap-override:0%}}'
    for n, src, sa, a, d in FALLBACKS) + '</style>\n')
PRE = ''.join(f'<link rel="preload" href="/assets/fonts/{f}-normal.woff2" as="font" type="font/woff2" crossorigin/>\n' for f in PRELOAD)

for f in ['index.html','en.html','newsletter.html','wattprint.html']:
    s=open(OUT+f,encoding='utf-8').read()
    s=re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?','',s)
    links=re.findall(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet"/?>\n?',s)
    for i,l in enumerate(links):
        if f in ('index.html','en.html'):
            js=''.join(re.findall(r'<script defer fetchpriority="high" src="[^"]+"></script>\n',s))
            if i==0:
                s=s.replace(js,'',1)
                s=s.replace(l,js+PRE+INLINE,1)  # JS primero (lo descubre antes el escáner), luego precargas y @font-face
            else:
                s=s.replace(l,'',1)
        else:
            s=s.replace(l,'<link rel="stylesheet" href="/assets/fonts/fonts.css"/>\n' if i==0 else '',1)
    # fase 4: una sola versión de GSAP en todo el sitio (la 3.15.0 del portfolio, cacheable entre páginas)
    s=s.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>','<script src="/assets/js/gsap-3.15.0.min.js"></script>')
    assert 'fonts.googleapis' not in s and 'cdnjs' not in s, f
    open(OUT+f,'w',encoding='utf-8').write(s)
print('selfhost ok')
