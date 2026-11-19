import re, sys
sys.path.insert(0, '/home/claude/neocortech/build')
from i18n import CSS, rep, index_head, index_toggle, INDEX_SWITCH, INDEX_CSS

src = open('/home/claude/neocortech/src/index.html', encoding='utf-8').read()
body = open('/home/claude/neocortech/build/index_body.html', encoding='utf-8').read()
en = open('/home/claude/neocortech/build/index_en_full.js', encoding='utf-8').read()

# 1. cuerpo: del menú overlay al pie, con el retrato de src (póster como archivo y vídeo con carga diferida)
a = src.index('<!-- full-screen overlay menu -->')
b = src.index('</footer>') + len('</footer>')
video = re.search(r'<img class="poster".*?<video id="cinevid".*?</video>', src, re.S).group(0)  # fase 1: póster como archivo + vídeo diferido
assert body.count('{{VIDEO}}') == 1
s = src[:a] + body.replace('{{VIDEO}}', video) + src[b:]

# 2. cabecera: subtítulo, aria, selector de idioma, texto del menú
s = rep(s, '<span class="wm"><span class="neo">NEO</span>CORTECH</span><span class="sub">Gobernanza de IA</span>', '<span class="wm wm-cg"><span class="cg-n">Carlos</span> <span class="cg-a">Gallego Galán</span></span><span class="sub">Product Designer · Technical PM</span>')
s = rep(s, '<nav class="switch" aria-label="Páginas del ecosistema">', '<nav class="switch" aria-label="Páginas del ecosistema" data-i18n-attr="aria-label:a_nav">')
s = rep(s, '<button class="menu-btn" id="menuBtn"', index_toggle('es') + '\n      <button class="menu-btn" id="menuBtn"')  # fase 4: enlaces / y /en
s = rep(s, '<span id="menuTxt">Índice</span>', '<span id="menuTxt">Índice</span>')
s = rep(s, '<button class="totop-float" id="toTopFloat" aria-label="Volver arriba">', '<button class="totop-float" id="toTopFloat" aria-label="Volver arriba" data-i18n-attr="aria-label:a_totop">')

# 3. metadatos alineados con el CV (fase 3: diseño y dirección de producto, ≤155 caracteres)
DESC_ES = 'Diseño y dirección de producto. Realidad virtual para salud e inclusión, herramientas web y agentes de IA con supervisión humana. Córdoba, remoto.'
s = re.sub(r'<meta name="description" content="[^"]*"/>',
           '<meta name="description" content="' + DESC_ES + '"/>', s, count=1)
s = re.sub(r'<meta property="og:description" content="[^"]*"/>',
           '<meta property="og:description" content="' + DESC_ES + '"/>', s, count=1)


s = re.sub(r'<title>[^<]*</title>', '<title>Carlos Gallego Galán — Hago productos que funcionan.</title>', s, count=1)
s = re.sub(r'<meta property="og:title" content="[^"]*"/>', '<meta property="og:title" content="Carlos Gallego Galán — Hago productos que funcionan."/>', s, count=1)

# 4. idioma (fase 4): la página española ya no lleva el diccionario inglés; /en se genera aparte (en_page.py) con los textos en el HTML
s = rep(s, "<script>document.documentElement.className='js';</script>", "<script>document.documentElement.className='js';</script>\n" + index_head('es'))
extra_css = CSS + """
/* proyectos (galería) y taller */
.psub{font-family:var(--display);font-weight:400;font-size:clamp(22px,2.4vw,30px);margin-top:72px;letter-spacing:.01em}
.psub em{color:var(--gold);font-style:normal;font-size:.7em;letter-spacing:.06em}
.psub+.pgrid{margin-top:28px}
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
.pj h3{font-family:var(--display);font-weight:400;font-size:clamp(21px,2vw,26px);letter-spacing:.01em;line-height:1.15}
.pj p{color:var(--muted);font-size:14.5px;line-height:1.6}
.paward{align-self:flex-start;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-bright);border:1px solid rgba(240,216,150,.32);border-radius:30px;padding:6px 12px}
.prole{font-size:13px;line-height:1.55;color:var(--muted)}
.prole b{color:var(--bone);font-weight:600}
.plink{margin-top:auto;padding-top:6px;align-self:flex-start;font-size:13px;color:var(--gold-bright);text-decoration:none;border-bottom:1px solid rgba(201,162,75,.35);transition:border-color .2s}
.plink:hover{border-color:var(--gold-bright)}
.tgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;margin-top:46px}
@media(max-width:760px){.tgrid{grid-template-columns:1fr}}
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
extra_css += open('/home/claude/neocortech/build/projects.css', encoding='utf-8').read()
extra_css += open('/home/claude/neocortech/build/fase1.css', encoding='utf-8').read()  # fase 1: diseño y estructura
extra_css += open('/home/claude/neocortech/build/fase2.css', encoding='utf-8').read()  # fase 2: accesibilidad y UX
extra_css += open('/home/claude/neocortech/build/fase3.css', encoding='utf-8').read()  # fase 3: contenido
extra_css += INDEX_CSS + open('/home/claude/neocortech/build/fase4.css', encoding='utf-8').read()  # fase 4: rendimiento (último)
s = rep(s, '</style>\n</head>', extra_css + '</style>\n</head>') if '</style>\n</head>' in s else s.replace('</head>', '<style>' + extra_css + '</style>\n</head>', 1)
first_script = s.index('<script>/*!', s.index('</footer>'))
s = s[:first_script] + INDEX_SWITCH + '\n' + s[first_script:]

# 5. textos que pone el JavaScript
# fase 3: los botones del hero entran con el resto del hero
s = rep(s, ".fromTo('.hero-foot .meta',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.6')", ".fromTo('.hero-foot .meta',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.6')\n.fromTo('.hero-cta',{y:24,autoAlpha:0},{y:0,autoAlpha:1,duration:.7,ease:'power3.out'},'-=.6')")
s = rep(s, "hintEl.textContent='toca y mantén pulsada la caja para abrirla'", "hintEl.textContent=NCT('toca y mantén pulsada la caja para abrirla','tap and hold the box to open it')")
s = rep(s, "stateEl.textContent=reveal>.85?'AUDITABLE':reveal>.4?'ABRIENDO…':'OPACO'", "stateEl.textContent=reveal>.85?'AUDITABLE':reveal>.4?NCT('ABRIENDO…','OPENING…'):NCT('OPACO','OPAQUE')")
s = rep(s, "txt.textContent=o?'Cerrar':'Índice'", "txt.textContent=o?NCT('Cerrar','Close'):NCT('Índice','Index')")
s = rep(s, "hh.textContent='✦ camino completado'", "hh.textContent=NCT('✦ recorrido completo','✦ path complete')")
s = rep(s, "{x:.10,y:.5,l:'PETICIÓN',t:'in'},{x:.32,y:.27,l:'PERCEPCIÓN',t:'p'},{x:.32,y:.73,l:'CONTEXTO·RAG',t:'p'},{x:.55,y:.5,l:'RAZONAMIENTO',t:'r'},{x:.74,y:.29,l:'POLÍTICA·ISO 42001',t:'pol'},{x:.74,y:.71,l:'VERIFICACIÓN',t:'pol'},{x:.90,y:.5,l:'ACCIÓN',t:'out'}",
        "{x:.10,y:.5,l:NCT('PETICIÓN','REQUEST'),t:'in'},{x:.32,y:.27,l:NCT('PERCEPCIÓN','PERCEPTION'),t:'p'},{x:.32,y:.73,l:NCT('CONTEXTO·RAG','CONTEXT·RAG'),t:'p'},{x:.55,y:.5,l:NCT('RAZONAMIENTO','REASONING'),t:'r'},{x:.74,y:.29,l:NCT('POLÍTICA·ISO 42001','POLICY·ISO 42001'),t:'pol'},{x:.74,y:.71,l:NCT('VERIFICACIÓN','VERIFICATION'),t:'pol'},{x:.90,y:.5,l:NCT('ACCIÓN','ACTION'),t:'out'}")
s = s.replace('<span id="menuTxt">Índice</span>', '<span id="menuTxt" data-i18n="menu">Índice</span>', 1)


# ---- correcciones de la auditoría ----
# 1. menú: el overlay tenía pointer-events:none porque nunca recibía la clase .open
s = rep(s, "function setOpen(o){open=o;document.body.classList.toggle('menu-open',o);", "function setOpen(o){open=o;ov.classList.toggle('open',o);document.body.classList.toggle('menu-open',o);")
# 2. investigación: los paneles estaban apilados en la misma celda de una rejilla; el JS espera un carrusel horizontal
s = rep(s, ".htrack{display:grid;padding:6px 2px}\n.htrack .hpanel{grid-area:1/1;width:min(100%,780px);margin:0 auto}",
        ".htrack{display:flex;gap:26px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:6px calc((100% - min(100%,780px))/2);cursor:grab}\n.htrack::-webkit-scrollbar{display:none}\n.htrack.dragging{cursor:grabbing;scroll-snap-type:none}\n.htrack{-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}\n.htrack .hpanel{flex:0 0 min(100%,780px);scroll-snap-align:center}\n.hpanel .out a{pointer-events:auto}")
s = rep(s, "  .htrack{flex-direction:column;gap:18px;overflow:visible;scroll-snap-type:none;cursor:default;transform:none!important;-webkit-mask-image:none;mask-image:none}",
        "  .htrack{flex-direction:column;gap:18px;overflow:visible;scroll-snap-type:none;cursor:default;padding:6px 0;transform:none!important;-webkit-mask-image:none;mask-image:none}\n  .htrack .hpanel{flex:none;width:100%;padding-right:clamp(26px,6vw,40px)}\n  .hpanel .pn{display:none}")
# 3. proyectos en móvil: la pila pegajosa tapaba el contenido de las tarjetas altas
# (fase 1: la pila de tarjetas .pcard ya no existe; se quitó su JS)
s = s.replace('</style>\n</head>', '@media(max-width:820px){.pcard{position:relative;top:auto!important;margin-bottom:18px}}\n</style>\n</head>', 1)

# ---- fase 2: accesibilidad y UX ----
# a. enlace para saltar al contenido, landmark <main> y botón «volver arriba» al final del orden de tabulación
s = rep(s, '<body>\n', '<body>\n<a class="skip" href="#main" data-i18n="skip">Saltar al contenido</a>\n')
s = rep(s, '<button class="totop-float" id="toTopFloat" aria-label="Volver arriba" data-i18n-attr="aria-label:a_totop">↑</button>\n', '')
s = rep(s, '<a id="top"></a>\n', '<a id="top"></a>\n<main id="main" tabindex="-1">\n')
s = rep(s, '<!-- CONTACTO -->\n<footer id="contacto">', '</main>\n\n<!-- CONTACTO -->\n<footer id="contacto">')
s = rep(s, '</footer>\n', '</footer>\n<button class="totop-float" id="toTopFloat" aria-label="Volver arriba" data-i18n-attr="aria-label:a_totop">↑</button>\n')
# b. menú: cerrado = inerte (fuera del orden de tabulación y del árbol de accesibilidad); sin aria-modal
#    (el botón Cerrar vive en la cabecera, fuera del diálogo; con el menú abierto el resto de la página queda inerte)
s = rep(s, '<div id="overlay" role="dialog" aria-modal="true" aria-label="Menú de navegación" data-i18n-attr="aria-label:a_menu">',
        '<div id="overlay" role="dialog" aria-label="Menú de navegación" data-i18n-attr="aria-label:a_menu" data-lenis-prevent inert>')
#    en móvil, las páginas del ecosistema (Carlos/Newsletter/Wattprint) pasan de la cabecera al menú
s = rep(s, '  <div class="ov-side">\n',
        '  <nav class="ov-pages" aria-label="Páginas del ecosistema" data-i18n-attr="aria-label:a_ovpages">\n'
        '    <a href="/" aria-current="page" data-c>Carlos</a><a href="/newsletter" data-c>Newsletter</a><a href="/wattprint" data-c>Wattprint</a>\n'
        '  </nav>\n  <div class="ov-side">\n')
a = s.index('/* overlay menu */')
b = s.index('window.__setMenu=setOpen;})();', a) + len('window.__setMenu=setOpen;})();')
s = s[:a] + open('/home/claude/neocortech/build/fase2_menu.js', encoding='utf-8').read().strip() + s[b:]
# c. anclas: mueven el foco al destino y actualizan la URL (compatibles con Lenis)
old_anchor = "document.querySelectorAll('a[href^=\"#\"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var el=document.querySelector(id);if(!el)return;e.preventDefault();if(window.__setMenu)window.__setMenu(false);if(lenis)lenis.scrollTo(el,{offset:-66});else el.scrollIntoView({behavior:'smooth'});});});"
s = rep(s, old_anchor, "document.querySelectorAll('a[href^=\"#\"]').forEach(function(a){a.addEventListener('click',function(e){var id=a.getAttribute('href');if(id.length<2)return;var el=document.getElementById(id.slice(1));if(!el)return;e.preventDefault();if(window.__setMenu)window.__setMenu(false,true);if(lenis)lenis.start();window.__goTo(el,id,true);});});")
# d. jerarquía de encabezados sin saltos: h4 de Perfil e Investigación -> h3; la capa nueva, la tesis y el pie con su h2
s = s.replace('<h4>', '<h3>').replace('</h4>', '</h3>').replace('.lyr h4', '.lyr h3').replace('.hpanel h4', '.hpanel h3')
s = rep(s, '<p class="big" id="maniBig" data-i18n="mani">', '<h2 class="big" id="maniBig" data-i18n="mani">')
i = s.index('id="maniBig"'); j = s.index('</p>', i); s = s[:j] + '</h2>' + s[j + 4:]
s = rep(s, '<div class="t-title rvx" data-i18n="th_title">', '<h2 class="t-title rvx" data-i18n="th_title">')
i = s.index('data-i18n="th_title"'); j = s.index('</div>', i); s = s[:j] + '</h2>' + s[j + 6:]
s = rep(s, '<h3 class="rvx" data-i18n="foot_h">', '<h2 class="rvx foot-h" data-i18n="foot_h">')
i = s.index('data-i18n="foot_h"'); j = s.index('</h3>', i); s = s[:j] + '</h2>' + s[j + 5:]
s = s.replace('footer h3', 'footer .foot-h')
assert '<h4' not in s and 'h4{' not in s, 'quedan h4'
# e. caja negra: operable con teclado (el foco la entreabre, Intro/Espacio la abre del todo); con movimiento reducido sigue siendo imagen
s = rep(s, "function loop(){target=held?1:(box.matches(':hover')?Math.max(target,.62):0);",
        "var kb=false;if(!RM){box.setAttribute('tabindex','0');box.setAttribute('role','button');box.setAttribute('aria-pressed','false');\n"
        "box.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();kb=!kb;box.setAttribute('aria-pressed',String(kb));}});\n"
        "box.addEventListener('blur',function(){kb=false;box.setAttribute('aria-pressed','false');});}\n"
        "function loop(){target=(held||kb)?1:((box.matches(':hover')||document.activeElement===box)?Math.max(target,.62):0);")
s = rep(s, "if(hintEl)hintEl.style.opacity=reveal>.3?0:.7;", "if(hintEl)hintEl.style.opacity=reveal>.3?0:1;")
s = s.replace('</body>', '<script>' + open('/home/claude/neocortech/build/fase2.js', encoding='utf-8').read() + '</script>\n</body>', 1)

s = s.replace('</body>', '<script>' + open('/home/claude/neocortech/build/projects.js', encoding='utf-8').read() + '</script>\n</body>', 1)

# ---- fase 4: rendimiento ----
exec(open('/home/claude/neocortech/build/fase4.py', encoding='utf-8').read())
open('/home/claude/neocortech/out/index.html', 'w', encoding='utf-8').write(s)

# comprobaciones
keys = set(re.findall(r'data-i18n="([^"]+)"', s)) | set(k.split(':')[1] for v in re.findall(r'data-i18n-attr="([^"]+)"', s) for k in v.split(';'))
enkeys = set(re.findall(r'(?:^|[,{\n])\s*([A-Za-z_][A-Za-z0-9_]*)\s*:', en)) | set(re.findall(r'NC_EN\["([^"]+)"\]', en)) | {'menu'}
for bad2 in ['h1c','h1d']: pass
print('claves sin EN:', sorted(keys - enkeys))
for bad in ['CINO', 'Head of AI', 'Doctorando', 'DaSCI', 'en curso)', '618', 'Propuesta doctoral', '+30 experiencias', 'IELTS']:
    if bad in s: print('SIGUE:', bad)
print('ok', len(s))
