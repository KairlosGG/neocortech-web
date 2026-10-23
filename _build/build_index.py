import re, sys
sys.path.insert(0, '/home/claude/neocortech/build')
from i18n import HEAD, CSS, APPLY, toggle, rep

src = open('/home/claude/neocortech/src/index.html', encoding='utf-8').read()
body = open('/home/claude/neocortech/build/index_body.html', encoding='utf-8').read()
en = open('/home/claude/neocortech/build/index_en_full.js', encoding='utf-8').read()

# 1. cuerpo: del menú overlay al pie, conservando el vídeo original (póster incrustado)
a = src.index('<!-- full-screen overlay menu -->')
b = src.index('</footer>') + len('</footer>')
video = re.search(r'<video id="cinevid".*?</video>', src, re.S).group(0)
assert body.count('{{VIDEO}}') == 1
s = src[:a] + body.replace('{{VIDEO}}', video) + src[b:]

# 2. cabecera: subtítulo, aria, selector de idioma, texto del menú
s = rep(s, '<span class="sub">Gobernanza de IA</span>', '<span class="sub" data-i18n="brand_sub">Gobernanza de IA</span>')
s = rep(s, '<nav class="switch" aria-label="Páginas del ecosistema">', '<nav class="switch" aria-label="Páginas del ecosistema" data-i18n-attr="aria-label:a_nav">')
s = rep(s, '<div class="navclock">', toggle() + '\n      <div class="navclock">')
s = rep(s, '<span id="menuTxt">Índice</span>', '<span id="menuTxt">Índice</span>')
s = rep(s, '<button class="totop-float" id="toTopFloat" aria-label="Volver arriba">', '<button class="totop-float" id="toTopFloat" aria-label="Volver arriba" data-i18n-attr="aria-label:a_totop">')

# 3. metadatos alineados con el CV
s = re.sub(r'<meta name="description" content="[^"]*"/>',
           '<meta name="description" content="Carlos Gallego Galán, Technical Product Manager. Hago productos que funcionan: realidad virtual, Web360, serious games y agentes de IA, de la idea a la entrega. ISO/IEC 42001 Lead Implementer (examen superado, ago. 2026)."/>', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*"/>',
           '<meta property="og:description" content="Technical Product Manager. Realidad virtual, Web360, serious games y agentes de IA, de la idea a la entrega."/>', s, count=1)


s = re.sub(r'<title>[^<]*</title>', '<title>Carlos Gallego Galán — Hago productos que funcionan.</title>', s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*"/>', '<meta property="og:title" content="Carlos Gallego Galán — Hago productos que funcionan."/>', s, count=1)

# 4. idioma: script en <head>, estilos, diccionario + aplicación antes de los scripts del cuerpo
s = rep(s, "<script>document.documentElement.className='js';</script>", "<script>document.documentElement.className='js';</script>\n" + HEAD)
extra_css = CSS + """
/* proyectos (galería) y taller */
.plead{max-width:62ch;color:var(--muted);font-size:17px;line-height:1.65;margin-top:20px}
.pgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:46px}
@media(max-width:1020px){.pgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){.pgrid{grid-template-columns:1fr}}
.pj{background:linear-gradient(160deg,#102030,#0A1522);border:1px solid var(--line2);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;transition:border-color .3s,box-shadow .35s}
.pj:hover{border-color:rgba(201,162,75,.5);box-shadow:0 22px 50px -28px rgba(201,162,75,.35)}
.pimg{aspect-ratio:1000/434;overflow:hidden;background:#0A1522}
.pimg img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.pj:hover .pimg img{transform:scale(1.045)}
.pbody{padding:22px 24px 24px;display:flex;flex-direction:column;gap:10px;flex:1}
.ptags,.tk{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);line-height:1.6}
.pj h3,.tc h3{font-family:var(--display);font-weight:400;font-size:clamp(21px,2vw,26px);letter-spacing:.01em;line-height:1.15}
.pj p,.tc p{color:var(--muted);font-size:14.5px;line-height:1.6}
.paward{align-self:flex-start;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-bright);border:1px solid rgba(240,216,150,.32);border-radius:30px;padding:6px 12px}
.prole{font-size:13px;line-height:1.55;color:var(--muted)}
.prole b{color:var(--bone);font-weight:600}
.plink{margin-top:auto;padding-top:6px;align-self:flex-start;font-size:13px;color:var(--gold-bright);text-decoration:none;border-bottom:1px solid rgba(201,162,75,.35);transition:border-color .2s}
.plink:hover{border-color:var(--gold-bright)}
.tgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;margin-top:46px}
@media(max-width:760px){.tgrid{grid-template-columns:1fr}}
.tc{background:var(--slate);border:1px solid var(--line2);border-radius:20px;padding:28px 28px 26px;display:flex;flex-direction:column;gap:12px;transition:border-color .3s}
.tc:hover{border-color:rgba(201,162,75,.5)}
.tlinks{margin-top:auto;padding-top:8px;display:flex;flex-wrap:wrap;gap:18px}
.tlinks a{font-size:13px;color:var(--gold-bright);text-decoration:none;border-bottom:1px solid rgba(201,162,75,.35)}
.tlinks a:hover{border-color:var(--gold-bright)}
.tsoon{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted2)}

.plinks{display:flex;flex-wrap:wrap;gap:18px;margin:14px 0 4px}
.plinks a{font-size:13px;color:var(--gold-bright);text-decoration:none;border-bottom:1px solid rgba(201,162,75,.35);padding-bottom:2px;transition:border-color .2s}
.plinks a:hover{border-color:var(--gold-bright)}
a.inl{color:var(--gold-bright);text-decoration:none;border-bottom:1px solid rgba(201,162,75,.35)}
.hpanel .out a{color:inherit;text-decoration:none;border-bottom:1px solid rgba(201,162,75,.45)}
.hpanel .out a:hover{color:var(--gold-bright)}
@media(max-width:560px){.lang button{padding:5px 8px}.nav-right{gap:12px}#menuTxt{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
"""
s = rep(s, '</style>\n</head>', extra_css + '</style>\n</head>') if '</style>\n</head>' in s else s.replace('</head>', '<style>' + extra_css + '</style>\n</head>', 1)
first_script = s.index('<script>/*!', s.index('</footer>'))
s = s[:first_script] + '<script>' + en + '</script>\n' + APPLY + '\n' + s[first_script:]

# 5. textos que pone el JavaScript
s = rep(s, "hintEl.textContent='toca y mantén pulsada la caja para abrirla'", "hintEl.textContent=NCT('toca y mantén pulsada la caja para abrirla','tap and hold the box to open it')")
s = rep(s, "stateEl.textContent=reveal>.85?'AUDITABLE':reveal>.4?'ABRIENDO…':'OPACO'", "stateEl.textContent=reveal>.85?'AUDITABLE':reveal>.4?NCT('ABRIENDO…','OPENING…'):NCT('OPACO','OPAQUE')")
s = rep(s, "txt.textContent=o?'Cerrar':'Índice'", "txt.textContent=o?NCT('Cerrar','Close'):NCT('Índice','Index')")
s = rep(s, "scrubhint.textContent='AR · en vivo'", "scrubhint.textContent=NCT('AR · en vivo','AR · live')")
s = rep(s, "hh.textContent='✦ camino completado'", "hh.textContent=NCT('✦ recorrido completo','✦ path complete')")
s = rep(s, "{x:.10,y:.5,l:'PETICIÓN',t:'in'},{x:.32,y:.27,l:'PERCEPCIÓN',t:'p'},{x:.32,y:.73,l:'CONTEXTO·RAG',t:'p'},{x:.55,y:.5,l:'RAZONAMIENTO',t:'r'},{x:.74,y:.29,l:'POLÍTICA·ISO 42001',t:'pol'},{x:.74,y:.71,l:'VERIFICACIÓN',t:'pol'},{x:.90,y:.5,l:'ACCIÓN',t:'out'}",
        "{x:.10,y:.5,l:NCT('PETICIÓN','REQUEST'),t:'in'},{x:.32,y:.27,l:NCT('PERCEPCIÓN','PERCEPTION'),t:'p'},{x:.32,y:.73,l:NCT('CONTEXTO·RAG','CONTEXT·RAG'),t:'p'},{x:.55,y:.5,l:NCT('RAZONAMIENTO','REASONING'),t:'r'},{x:.74,y:.29,l:NCT('POLÍTICA·ISO 42001','POLICY·ISO 42001'),t:'pol'},{x:.74,y:.71,l:NCT('VERIFICACIÓN','VERIFICATION'),t:'pol'},{x:.90,y:.5,l:NCT('ACCIÓN','ACTION'),t:'out'}")
s = s.replace('<span id="menuTxt">Índice</span>', '<span id="menuTxt" data-i18n="menu">Índice</span>', 1)
s = s.replace('window.NC_EN={', 'window.NC_EN={menu:"Index",', 1)


# ---- correcciones de la auditoría ----
# 1. menú: el overlay tenía pointer-events:none porque nunca recibía la clase .open
s = rep(s, "function setOpen(o){open=o;document.body.classList.toggle('menu-open',o);", "function setOpen(o){open=o;ov.classList.toggle('open',o);document.body.classList.toggle('menu-open',o);")
# 2. investigación: los paneles estaban apilados en la misma celda de una rejilla; el JS espera un carrusel horizontal
s = rep(s, ".htrack{display:grid;padding:6px 2px}\n.htrack .hpanel{grid-area:1/1;width:min(100%,780px);margin:0 auto}",
        ".htrack{display:flex;gap:26px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:6px calc((100% - min(100%,780px))/2);cursor:grab}\n.htrack::-webkit-scrollbar{display:none}\n.htrack.dragging{cursor:grabbing;scroll-snap-type:none}\n.htrack{-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}\n.htrack .hpanel{flex:0 0 min(100%,780px);scroll-snap-align:center}\n.hpanel .out a{pointer-events:auto}")
s = rep(s, "  .htrack{flex-direction:column;gap:18px;overflow:visible;scroll-snap-type:none;cursor:default;transform:none!important;-webkit-mask-image:none;mask-image:none}",
        "  .htrack{flex-direction:column;gap:18px;overflow:visible;scroll-snap-type:none;cursor:default;padding:6px 0;transform:none!important;-webkit-mask-image:none;mask-image:none}\n  .htrack .hpanel{flex:none;width:100%;padding-right:clamp(26px,6vw,40px)}\n  .hpanel .pn{display:none}")
# 3. proyectos en móvil: la pila pegajosa tapaba el contenido de las tarjetas altas
s = rep(s, "cards.forEach(function(card,i){card.style.top=(94+i*16)+'px';", "if(innerWidth>820)cards.forEach(function(card,i){card.style.top=(94+i*16)+'px';")
s = s.replace('</style>\n</head>', '@media(max-width:820px){.pcard{position:relative;top:auto!important;margin-bottom:18px}}\n</style>\n</head>', 1)

open('/home/claude/neocortech/out/index.html', 'w', encoding='utf-8').write(s)

# comprobaciones
keys = set(re.findall(r'data-i18n="([^"]+)"', s)) | set(k.split(':')[1] for v in re.findall(r'data-i18n-attr="([^"]+)"', s) for k in v.split(';'))
enkeys = set(re.findall(r'(?:^|[,{\n])\s*([A-Za-z_][A-Za-z0-9_]*)\s*:', en)) | set(re.findall(r'NC_EN\["([^"]+)"\]', en)) | {'menu'}
for bad2 in ['h1c','h1d']: pass
print('claves sin EN:', sorted(keys - enkeys))
for bad in ['CINO', 'Head of AI', 'Doctorando', 'DaSCI', 'en curso)', '618', 'Propuesta doctoral', '+30 experiencias', 'IELTS']:
    if bad in s: print('SIGUE:', bad)
print('ok', len(s))
