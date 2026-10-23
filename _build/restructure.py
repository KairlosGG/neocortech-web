"""Reorganiza el portfolio con enfoque maker a partir de index_body.v1.html."""
import re
B = '/home/claude/neocortech/build/'
s = open(B + 'index_body.v1.html', encoding='utf-8').read()
new = open(B + 'sections_new.html', encoding='utf-8').read()


def cut(src, start, end):
    a = src.index(start)
    b = src.index(end, a) + len(end)
    return src[a:b]


def rep(x, old, new_):
    assert x.count(old) == 1, old[:80]
    return x.replace(old, new_)


overlay = cut(s, '<!-- full-screen overlay menu -->', '</div>\n</div>\n')
hero = s[s.index('<a id="top"></a>'):s.index('<!-- MANIFESTO')]  # héroe + marquesina
mani = cut(s, '<!-- MANIFESTO + BLACK BOX -->', '</section>\n')
perfil = cut(s, '<!-- PERFIL + cinematic portrait -->', '</section>\n')
aporto = cut(s, '<!-- APORTO + Venn -->', '</section>\n')
tray = cut(s, '<!-- TRAYECTORIA -->', '</section>\n')
inv = cut(s, '<!-- INVESTIGACIÓN -->', '</section>\n')
form = cut(s, '<!-- FORMACIÓN -->', '</section>\n')
foot = cut(s, '<!-- CONTACTO -->', '</footer>\n')

# --- menú
nav_old = overlay[overlay.index('<nav class="ov-nav" id="ovNav">'):overlay.index('</nav>') + 6]
overlay = overlay.replace(nav_old, '''<nav class="ov-nav" id="ovNav">
    <a href="#perfil" data-c><span class="on">01</span><span data-i18n="ov1">Perfil</span></a>
    <a href="#proyectos" data-c><span class="on">02</span><span data-i18n="ov2"><em>Proyectos</em></span></a>
    <a href="#taller" data-c><span class="on">03</span><span data-i18n="ov3">Taller</span></a>
    <a href="#aporto" data-c><span class="on">04</span><span data-i18n="ov4">Qué <em>aporto</em></span></a>
    <a href="#manifiesto" data-c><span class="on">05</span><span data-i18n="ov5">La capa <em>nueva</em></span></a>
    <a href="#doctorado" data-c><span class="on">06</span><span data-i18n="ov6">Investigación</span></a>
    <a href="#contacto" data-c><span class="on">07</span><span data-i18n="ov7">Contacto</span></a>
  </nav>''')

# --- héroe: enfoque maker (opción A)
hero = rep(hero, '''      <span class="line-mask"><span class="l1" data-i18n="h1a">Construyo IA</span></span>
      <span class="line-mask"><span class="l2"><span class="it" data-i18n="h1b">agéntica.</span></span></span>
      <span class="line-mask"><span class="l1" data-i18n="h1c">Y la hago</span></span>
      <span class="line-mask"><span class="l2"><span class="it" data-i18n="h1d">gobernable.</span></span></span>''',
'''      <span class="line-mask"><span class="l1" data-i18n="h1a">Hago productos</span></span>
      <span class="line-mask"><span class="l2"><span class="it" data-i18n="h1b">que funcionan.</span></span></span>''')
hero = re.sub(r'<p class="intro rvx" data-i18n="intro">.*?</p>',
              '<p class="intro rvx" data-i18n="intro">Desde 2015 convierto ideas en cosas que se usan: una app con 500 usuarios en 24 horas, una obra de 16 km de alta tensión, experiencias de realidad virtual para clientes y, ahora, agentes de IA. La capa nueva: <strong>que esa IA se pueda explicar y auditar.</strong></p>', hero, flags=re.S)
hero = re.sub(r'<div class="mqt" id="mq" data-i18n="mq">.*?</div></div>',
              '<div class="mqt" id="mq" data-i18n="mq">\n  <span class="mqi"><i></i>Producto digital</span><span class="mqi"><i></i><b>De la idea a la entrega</b></span><span class="mqi"><i></i>Realidad virtual</span><span class="mqi"><i></i>Web360</span><span class="mqi"><i></i><b>Serious games</b></span><span class="mqi"><i></i>Diseño UX/UI</span><span class="mqi"><i></i>Agentes de IA</span><span class="mqi"><i></i><b>Gobernable por construcción</b></span><span class="mqi"><i></i>Discovery · PoC · MVP</span><span class="mqi"><i></i>ISO/IEC 42001</span>\n</div></div>', hero, flags=re.S)

# --- perfil pasa a ser 01
perfil = rep(perfil, '<span class="eyebrow rvx" data-i18n="e02"><span class="n">02</span> Quién soy</span>',
             '<span class="eyebrow rvx" data-i18n="e01p"><span class="n">01</span> Quién soy</span>')

# --- qué aporto pasa a 04, enfoque maker
aporto = rep(aporto, '<span class="eyebrow rvx" data-i18n="e03"><span class="n">03</span> Qué aporto</span>',
             '<span class="eyebrow rvx" data-i18n="e04a"><span class="n">04</span> Qué aporto</span>')
aporto = rep(aporto, '<h2 class="sec rvx" data-i18n="h_aporto">Construir IA es la parte fácil.<br/><em>Hacerla gobernable</em> es la mía.</h2>',
             '<h2 class="sec rvx" data-i18n="h_aporto">Del problema <em>al producto.</em><br/>Y que se pueda auditar.</h2>')
aporto = re.sub(r'\s*<p class="posit rvx" data-i18n="posit">.*?</p>', '', aporto, flags=re.S)
aporto = rep(aporto, 'aria-label="Intersección de construir con IA, implementar gobernanza e investigar"',
             'aria-label="Intersección de diseñar, construir y hacerlo auditable"')
aporto = re.sub(r'<div class="vlbl top">.*?</div></div>', '<div class="vlbl top"><div class="vn">01</div><div class="vt" data-i18n="v1t">Diseño</div><div class="vs" data-i18n="v1s">discovery · UX/UI · game design</div></div>', aporto, count=1, flags=re.S)
aporto = re.sub(r'<div class="vlbl bl">.*?</div></div>', '<div class="vlbl bl"><div class="vn">02</div><div class="vt" data-i18n="v2t">Construyo</div><div class="vs" data-i18n="v2s">XR · web · agentes de IA</div></div>', aporto, count=1, flags=re.S)
aporto = re.sub(r'<div class="vlbl br">.*?</div></div>', '<div class="vlbl br"><div class="vn">03</div><div class="vt" data-i18n="v3t">Lo hago auditable</div><div class="vs">ISO/IEC 42001 · AI Act</div></div>', aporto, count=1, flags=re.S)
aporto = re.sub(r'<div class="conv-copy">.*?</div>\n    </div>', '''<div class="conv-copy">
        <h3 class="rvx" data-i18n="conv_h">Tres oficios, una sola persona</h3>
        <p class="rvx" data-i18n="conv1"><span class="hl">Con el diseño:</span> hablo con el cliente y con los usuarios, defino qué hay que construir y lo diseño en Figma antes de escribir una línea. Así lo hice en realidad virtual, en Web360 y en los productos de SGS.</p>
        <p class="rvx" data-i18n="conv2"><span class="hl">Con las manos:</span> coordino equipos de desarrollo, 3D y diseño, y construyo mis propios productos dirigiendo agentes de IA. <a class="inl" href="#taller">Rumbo</a>, mi CRM agéntico, está publicado con su código.</p>
        <p class="rvx" data-i18n="conv3"><span class="hl">Con el estándar:</span> la capa nueva. Diseño la gobernanza dentro del sistema con la ISO/IEC 42001 y el Reglamento Europeo de IA: supervisión humana y trazabilidad desde el principio.</p>
      </div>
    </div>''', aporto, count=1, flags=re.S)

# --- gobernanza: la capa nueva (05)
mani = rep(mani, '<span class="eyebrow rvx" data-i18n="e01"><span class="n">01</span> La tesis, en una frase</span>',
           '<span class="eyebrow rvx" data-i18n="e05g"><span class="n">05</span> La capa nueva · gobernanza de IA</span>')
mani = rep(mani, '<div class="tags rvx" data-i18n="box_tags">',
           '<p class="rvx" data-i18n="posit">El 74 % de las empresas prevé desplegar IA agéntica en los próximos dos años, pero solo el 21 % tiene un modelo de gobernanza maduro para agentes autónomos (Deloitte, <i>State of AI in the Enterprise</i>, 2026).</p>\n        <div class="tags rvx" data-i18n="box_tags">')

# --- investigación pasa a 06 y contacto a 07
inv = rep(inv, '<span class="n">05</span> Investigación · en exploración', '<span class="n">06</span> Investigación · en exploración')
foot = rep(foot, '<span class="eyebrow rvx" data-i18n="e06">06 · Contacto</span>', '<span class="eyebrow rvx" data-i18n="e07">07 · Contacto</span>')

R = '\n<div class="rule"></div>\n\n'
out = overlay + '\n' + hero + '\n' + perfil + R + new + R + aporto + R + mani + R + tray + '\n' + inv + '\n' + form + '\n' + foot
open(B + 'index_body.html', 'w', encoding='utf-8').write(out)
print('ok', len(out))
