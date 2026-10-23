import re, sys, json
sys.path.insert(0, '/home/claude/neocortech/build')
from i18n import HEAD, CSS, APPLY, toggle, rep

SRC = '/home/claude/neocortech/src/'
OUT = '/home/claude/neocortech/out/'

# URL de acción del formulario de Kit (Kit → formulario → Embed → HTML → atributo action).
# Vacía = se abre un email de alta como alternativa.
KIT_ACTION = 'https://app.kit.com/forms/10085804/subscriptions'

COMMON_EN = {
    'a_nav': 'Ecosystem pages', 'a_lang': 'Language', 'brand_sub': 'AI governance',
    'ltag': 'The layer that governs AI', 'foot_meta': 'The layer that governs AI · Córdoba, Spain<br>© <span id="yr"></span> Neocortech — by Carlos Gallego Galán',
}


def common(s):
    s = rep(s, "<script>document.documentElement.className='js';</script>", "<script>document.documentElement.className='js';</script>\n" + HEAD)
    s = rep(s, '<div class="sub">Gobernanza de IA</div>', '<div class="sub" data-i18n="brand_sub">Gobernanza de IA</div>')
    s = rep(s, '<nav class="switch" aria-label="Páginas del ecosistema">', '<nav class="switch" aria-label="Páginas del ecosistema" data-i18n-attr="aria-label:a_nav">')
    # selector de idioma: justo después del switch, dentro de la cabecera
    i = s.index('<nav class="switch"')
    j = s.index('</nav>', i) + len('</nav>')
    s = s[:j] + '\n    ' + toggle() + s[j:]
    s = rep(s, '<div class="ltag">La capa que gobierna la IA</div>', '<div class="ltag" data-i18n="ltag">La capa que gobierna la IA</div>')
    s = rep(s, '<div class="meta">La capa que gobierna la IA · Córdoba, ES<br>© <span id="yr"></span> Neocortech — por Carlos Gallego Galán</div>',
            '<div class="meta" data-i18n="foot_meta">La capa que gobierna la IA · Córdoba, ES<br>© <span id="yr"></span> Neocortech — por Carlos Gallego Galán</div>')
    s = s.replace('</style>', CSS + '\n.nav-in{gap:16px}\n@media(max-width:640px){.nav-in .lang{order:2}}\n</style>', 1)
    return s


def finish(s, en, name):
    gs = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>'
    s = rep(s, gs, gs + '\n<script>window.NC_EN=' + json.dumps(en, ensure_ascii=False) + ';</script>\n' + APPLY)
    keys = set(re.findall(r'data-i18n="([^"]+)"', s)) | set(k.split(':')[1] for v in re.findall(r'data-i18n-attr="([^"]+)"', s) for k in v.split(';'))
    print(name, 'claves sin EN:', sorted(keys - set(en)))
    open(OUT + name, 'w', encoding='utf-8').write(s)


# ---------------- NEWSLETTER ----------------
s = common(open(SRC + 'newsletter.html', encoding='utf-8').read())
T = [
    ('<div class="eyebrow" style="justify-content:center">Newsletter · Gobernanza de IA</div>', 'nl_eb', 'Newsletter · AI governance'),
    ('<div class="tagline">La capa que gobierna la IA</div>', 'nl_tag', 'The layer that governs AI'),
    ('<p class="lead">Cómo gobernar el poder de la IA —agentes, IA generativa, ética, riesgos y sostenibilidad— <strong>antes de que se te vaya de las manos</strong>. Criterio auditable, pensado en voz alta por alguien que lo está implementando de verdad. No resúmenes de novedades.</p>',
     'nl_lead', 'How to govern the power of AI — agents, generative AI, ethics, risk and sustainability — <strong>before it gets out of hand</strong>. Auditable judgement, thought out loud by someone actually implementing it. Not news round-ups.'),
    ('<button class="btn primary" data-scroll="news-neo" data-c>Suscríbete <span class="ar">↗</span></button>', 'nl_cta', 'Subscribe <span class="ar">↗</span>'),
    ('<div class="scrollcue"><span>Baja</span>', None, None),
    ('<div class="eyebrow rvx" style="justify-content:center">Esencia</div>', 'nl_ess', 'Essence'),
    ('<p class="big rvx">La gobernanza no llega tarde por falta de normas. Llega tarde porque <em>nadie la construye mientras se construye la IA</em>.</p>',
     'nl_big', 'Governance isn\'t late for lack of rules. It\'s late because <em>nobody builds it while the AI is being built</em>.'),
    ('<h3>El guardián-constructor</h3>', 'nl_arch_h', 'The guardian-builder'),
    ('<p>Neocortech no vende miedo regulatorio. Da la capa de criterio que convierte un sistema de IA en algo que se puede desplegar, defender y auditar. Orden y energía: el oro que estructura, el zafiro que corre por dentro.</p>',
     'nl_arch_p', 'Neocortech doesn\'t sell regulatory fear. It provides the layer of judgement that turns an AI system into something you can deploy, defend and audit. Order and energy: the gold that gives structure, the sapphire that runs inside.'),
    ('<div class="eyebrow rvx">Detrás de Neocortech</div>', 'nl_behind', 'Behind Neocortech'),
    ('<p class="lead rvx">Implementador, no auditor. Dirijo producto y adopción de IA, y ahora escribo en voz alta el criterio que aplico cuando toca hacer que un sistema de IA sea gobernable de verdad.</p>',
     'nl_me', 'Implementer, not auditor. I lead AI products and adoption, and now I write out loud the judgement I apply when an AI system has to become truly governable.'),
    ('<li class="rvx"><span><b>ISO/IEC 42001 Lead Implementer</b> — en formación (examen 2026).</span></li>', 'nl_c1', '<b>ISO/IEC 42001 Lead Implementer</b> — PECB, exam passed (Aug 2026).'),
    ('<li class="rvx"><span><b>Máster oficial en Metaverso/VR/AR</b> (Complutense, Matrícula de Honor) + MBA + Ing. Civil.</span></li>', 'nl_c2', '<b>MSc in Metaverse, VR and AR</b> (Complutense, Highest Distinction), 360º Business Master and Civil Engineering.'),
    ('<li class="rvx"><span><b>Experto en Inteligencia Artificial</b> (150h · 6 ECTS) y Google Generative AI Leader.</span></li>', 'nl_c3', '<b>AI Expert Programme</b> (150 h · 6 ECTS) and Google Generative AI Leader.'),
    ('<li class="rvx"><span>Sin humo: cada credencial, tal cual es. Ni una inflada.</span></li>', 'nl_c4', 'No smoke: every credential exactly as it is. Not one inflated.'),
    ('<p class="q">"No audito la IA. <span class="g">La construyo para que se pueda auditar.</span>"</p>', 'nl_q', '“I don\'t audit AI. <span class="g">I build it so it can be audited.</span>”'),
    ('<div class="attr">— El principio de la marca</div>', 'nl_attr', '— The brand\'s principle'),
    ('<div class="eyebrow rvx" style="justify-content:center">La edición inaugural</div>', 'nl_first', 'The first issue'),
    ('<h2 class="rvx" style="margin-top:14px">Entra antes de la Edición 0</h2>', 'nl_join_h', 'Get in before Issue 0'),
    ('<p class="lead rvx" style="margin:14px auto 0;text-align:center">El post fundacional usa una historia que media generación tech ya conoce para explicar qué es la gobernanza de IA y por qué llega tarde casi siempre.</p>',
     'nl_join_p', 'The founding post uses a story half a tech generation already knows to explain what AI governance is and why it almost always arrives late. <em>Written in Spanish.</em>'),
    ('<h3 style="color:var(--gold-bright)">Únete a la lista</h3>', 'nl_list', 'Join the list'),
    ('<div class="microcopy">Tuteo, sin humo, voz de practitioner. Sin spam. Te aviso cuando abra el cupo.</div>', 'nl_micro', 'Plain talk, no smoke, a practitioner\'s voice. No spam. Unsubscribe in one click.'),
]
for old, key, en in T:
    if key is None:
        continue
    m = re.match(r'(<(\w+)[^>]*?)(>)(.*)(</\2>)$', old, re.S)
    assert m, old
    new = m.group(1) + ' data-i18n="%s"' % key + '>' + m.group(4) + m.group(5)
    s = rep(s, old, new)
# viñetas: el texto va dentro de <span>; traducimos el <span>
for k in ['nl_c1', 'nl_c2', 'nl_c3', 'nl_c4']:
    s = re.sub(r'<li class="rvx" data-i18n="%s"><span>(.*?)</span></li>' % k, r'<li class="rvx"><span data-i18n="%s">\1</span></li>' % k, s)
s = rep(s, '<div class="scrollcue"><span>Baja</span>', '<div class="scrollcue"><span data-i18n="nl_down">Baja</span>')
# credenciales alineadas con el CV
s = rep(s, '<b>ISO/IEC 42001 Lead Implementer</b> — en formación (examen 2026).', '<b>ISO/IEC 42001 Lead Implementer</b> — PECB, examen superado (ago. 2026).')
s = rep(s, '<b>Máster oficial en Metaverso/VR/AR</b> (Complutense, Matrícula de Honor) + MBA + Ing. Civil.', '<b>Máster en Metaverso, VR y AR</b> (Complutense, Matrícula de Honor), Máster de Negocios 360º e Ingeniería Civil.')
s = rep(s, '<b>Experto en Inteligencia Artificial</b> (150h · 6 ECTS) y Google Generative AI Leader.', '<b>Experto en Inteligencia Artificial</b> (150 h · 6 ECTS) y Google Generative AI Leader.')
s = rep(s, 'Tuteo, sin humo, voz de practitioner. Sin spam. Te aviso cuando abra el cupo.', 'Tuteo, sin humo, voz de practitioner. Sin spam. Te das de baja con un clic.')

# formulario real (Kit) con honeypot y confirmación inline
old_form = '''      <div class="field-row">
        <input id="email-neo" type="email" placeholder="tu@correo.com" autocomplete="email"/>
        <button class="btn primary" id="sub-neo" data-c>Quiero entrar</button>
      </div>'''
new_form = '''      <form class="field-row" id="form-neo" method="post" target="kit-sink" novalidate>
        <label class="sr" for="email-neo" data-i18n="nl_lbl">Tu correo</label>
        <input id="email-neo" name="email_address" type="email" placeholder="tu@correo.com" autocomplete="email" required data-i18n-attr="placeholder:nl_ph"/>
        <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"/>
        <button class="btn primary" id="sub-neo" type="submit" data-c data-i18n="nl_btn">Quiero entrar</button>
      </form>
      <iframe name="kit-sink" title="kit" hidden></iframe>'''
s = rep(s, old_form, new_form)
s = rep(s, '<div class="ok" id="ok-neo" role="status">Anotado. Te escribiré desde Neocortech antes de publicar. ✦</div>',
        '<div class="ok" id="ok-neo" role="status" data-i18n="nl_ok">Anotado. Revisa tu correo y confirma la suscripción. ✦</div>')
old_js = '''  var inp=document.getElementById('email-neo'),btn=document.getElementById('sub-neo'),ok=document.getElementById('ok-neo');
  if(!btn)return;
  function submit(){var v=(inp.value||'').trim();if(!/.+@.+\\..+/.test(v)){inp.style.borderColor='#F87171';inp.focus();return;}
    inp.style.borderColor='';inp.disabled=true;btn.disabled=true;btn.textContent='✓';ok.classList.add('show');}
  btn.addEventListener('click',submit);
  inp.addEventListener('keydown',function(e){if(e.key==='Enter')submit();});'''
new_js = '''  var KIT_ACTION=%s;
  var form=document.getElementById('form-neo'),inp=document.getElementById('email-neo'),btn=document.getElementById('sub-neo'),ok=document.getElementById('ok-neo');
  if(!form)return;
  form.addEventListener('submit',function(e){
    var v=(inp.value||'').trim();
    if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v)){e.preventDefault();inp.style.borderColor='#F87171';inp.focus();return;}
    inp.style.borderColor='';
    var bot=form.querySelector('.hp').value;
    if(bot||!KIT_ACTION){e.preventDefault();
      if(!bot){ok.textContent=NCT('Se ha abierto tu correo con el alta preparada: envíalo y te apunto. ✦','Your email app opened with the sign-up ready: send it and I will add you. ✦');location.href='mailto:carlosgallegogalan@gmail.com?subject='+encodeURIComponent(NCT('Alta en la newsletter de Neocortech','Neocortech newsletter sign-up'))+'&body='+encodeURIComponent(NCT('Quiero apuntarme con este correo: ','Please add this email: ')+v);}
    }else{form.action=KIT_ACTION;}
    setTimeout(function(){inp.disabled=true;btn.disabled=true;btn.textContent='✓';ok.classList.add('show');},50);
  });''' % json.dumps(KIT_ACTION)
s = rep(s, old_js, new_js)
s = s.replace('</style>', '.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}.hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}\n</style>', 1)

en = dict(COMMON_EN)
en.update({k: v for _, k, v in T if k})
en.update({
    '_title': 'Neocortech — Newsletter · The layer that governs AI',
    '_desc': 'An AI governance newsletter: agents, generative AI, ethics, risk and sustainability, with auditable judgement. Written in Spanish by someone implementing it.',
    'nl_down': 'Scroll', 'nl_lbl': 'Your email', 'nl_ph': 'you@email.com', 'nl_btn': 'Count me in',
    'nl_ok': 'Done. Check your inbox and confirm your subscription. ✦',
})
finish(s, en, 'newsletter.html')

# ---------------- WATTPRINT ----------------
s = common(open(SRC + 'wattprint.html', encoding='utf-8').read())
W = [
    ('<div class="eyebrow rvx" style="justify-content:center">Herramienta · Sostenibilidad</div>', 'wp_eb', 'Tool · Sustainability'),
    ('<h2 class="rvx gold" style="margin:14px 0 8px">Un mundo aparte, con su propia piel</h2>', 'wp_h', 'A world apart, with its own skin'),
    ('<p class="lead rvx" style="margin:0 auto;text-align:center">Wattprint tiene identidad propia y vive fuera de la marca. Pero se abre desde aquí, con un botón.</p>', 'wp_lead', 'Wattprint has its own identity and lives outside the brand. But it opens from here, with one button.'),
    ('<div class="top"><span class="b"></span>/tool/wattprint · sin registro · datos Ember + Uptime Institute</div>', 'wp_top', '<span class="b"></span>/tool/wattprint · no sign-up · Ember + Uptime Institute data'),
    ('<h2>¿Cuánto carbono, energía y agua consume tu IA?</h2>', 'wp_card_h', 'How much carbon, energy and water does your AI use?'),
    ('<p>Calcula la huella de tus entrenamientos e inferencias en 60 segundos. Metodología SCI (ISO 21031). Gratis y sin registro.</p>', 'wp_card_p', 'Calculate the footprint of your training runs and inference in 60 seconds. SCI methodology (ISO/IEC 21031). Free, no sign-up. The tool is in Spanish.'),
    ('<div class="wpm c">CO₂e · kg</div>', None, None),
    ('<div class="wpm e">Energía · kWh</div>', 'wp_m_e', 'Energy · kWh'),
    ('<div class="wpm w">Agua · litros</div>', 'wp_m_w', 'Water · litres'),
    ('<a class="wpbtn" href="/tool/wattprint/" data-c>Abrir Wattprint <span>→</span></a>', 'wp_btn', 'Open Wattprint <span>→</span>'),
    ('<p class="wpnote"><span class="dot">◆</span> Identidad verde propia · convive con Neocortech sin fundirse con ella</p>', 'wp_note', '<span class="dot">◆</span> Its own green identity · lives alongside Neocortech without merging into it'),
    ('<div class="eyebrow rvx">Qué mide</div>', 'wp_what', 'What it measures'),
    ('<h2 class="rvx" style="margin-bottom:10px">Tres huellas, un cálculo</h2>', 'wp_three', 'Three footprints, one calculation'),
    ('<p class="lead rvx">Entrenar y servir modelos no consume "nube": consume electricidad, emite carbono y evapora agua en centros de datos concretos. Wattprint pone número a las tres cosas.</p>', 'wp_three_p', 'Training and serving models doesn\'t consume “cloud”: it consumes electricity, emits carbon and evaporates water in specific data centres. Wattprint puts a number on all three.'),
    ('<div class="feat rvx"><span class="n">01</span><span class="wpk c">CO₂e · kg</span><h4>Carbono</h4><p>Emisiones de entrenamiento e inferencia según la intensidad de carbono de la red eléctrica que alimenta el centro de datos. No es igual entrenar en Francia que en Polonia.</p></div>', 'wp_f1',
     '<span class="n">01</span><span class="wpk c">CO₂e · kg</span><h4>Carbon</h4><p>Training and inference emissions based on the carbon intensity of the grid that powers the data centre. Training in France is not the same as training in Poland.</p>'),
    ('<div class="feat rvx"><span class="n">02</span><span class="wpk e">Energía · kWh</span><h4>Electricidad</h4><p>Consumo del hardware (GPU/TPU) durante el trabajo, corregido por el PUE del centro de datos: la energía que gasta el edificio, no solo el chip.</p></div>', 'wp_f2',
     '<span class="n">02</span><span class="wpk e">Energy · kWh</span><h4>Electricity</h4><p>Hardware consumption (GPU/TPU) during the job, adjusted by the data centre\'s PUE: the energy the building uses, not just the chip.</p>'),
    ('<div class="feat rvx"><span class="n">03</span><span class="wpk w">Agua · litros</span><h4>Agua</h4><p>El coste hídrico de la refrigeración, estimado con el WUE. La huella de la que casi nadie habla y que ya condiciona dónde se pueden construir centros de datos.</p></div>', 'wp_f3',
     '<span class="n">03</span><span class="wpk w">Water · litres</span><h4>Water</h4><p>The water cost of cooling, estimated with WUE. The footprint almost nobody talks about, and one that already limits where data centres can be built.</p>'),
    ('<div class="eyebrow rvx" style="justify-content:center">Metodología</div>', 'wp_meth', 'Methodology'),
    ('<p class="lead rvx" style="margin:14px auto 0;text-align:center">Wattprint no estima a ojo: aplica la especificación <strong>SCI (ISO/IEC 21031)</strong> de la Green Software Foundation, el estándar internacional para medir el carbono del software.</p>', 'wp_meth_p',
     'Wattprint doesn\'t guess: it applies the Green Software Foundation\'s <strong>SCI (ISO/IEC 21031)</strong> specification, the international standard for measuring software carbon.'),
    ('''<div class="legend">
        <b>E</b> — energía consumida por el software (kWh) · <b>I</b> — intensidad de carbono de la red (gCO₂e/kWh)<br>
        <b>M</b> — carbono embebido del hardware amortizado · <b>R</b> — unidad funcional (p. ej., por inferencia)
      </div>''', 'wp_legend', '<b>E</b> — energy consumed by the software (kWh) · <b>I</b> — grid carbon intensity (gCO₂e/kWh)<br><b>M</b> — amortised embodied carbon of the hardware · <b>R</b> — functional unit (e.g. per inference)'),
    ('<div class="eyebrow rvx">Fuentes de datos</div>', 'wp_src', 'Data sources'),
    ('<div class="feat rvx"><span class="n">A</span><h4>Ember</h4><p>Intensidad de carbono de la electricidad por país y por red, con datos abiertos y actualizados. Es lo que convierte tus kWh en kg de CO₂e según dónde corre tu IA.</p></div>', 'wp_a',
     '<span class="n">A</span><h4>Ember</h4><p>Carbon intensity of electricity by country and grid, with open, up-to-date data. It turns your kWh into kg of CO₂e depending on where your AI runs.</p>'),
    ('<div class="feat rvx"><span class="n">B</span><h4>Uptime Institute</h4><p>Medias de eficiencia de la industria de centros de datos: PUE (energía) y WUE (agua). Es lo que convierte el consumo del chip en el consumo real del edificio.</p></div>', 'wp_b',
     '<span class="n">B</span><h4>Uptime Institute</h4><p>Industry averages for data centre efficiency: PUE (energy) and WUE (water). It turns chip consumption into the building\'s real consumption.</p>'),
    ('<p class="wpnote rvx"><span class="dot">◆</span> Sin humo también aquí: cada número sale de una fuente citable, no de un multiplicador inventado</p>', 'wp_note2', '<span class="dot">◆</span> No smoke here either: every number comes from a citable source, not a made-up multiplier'),
]
for old, key, en_ in W:
    if key is None:
        continue
    m = re.match(r'(<(\w+)[^>]*?)(>)(.*)(</\2>)$', old, re.S)
    assert m, old
    s = rep(s, old, m.group(1) + ' data-i18n="%s"' % key + '>' + m.group(4) + m.group(5))
s = rep(s, 'Metodología SCI (ISO 21031).', 'Metodología SCI (ISO/IEC 21031).', 2)
en = dict(COMMON_EN)
en.update({k: v for _, k, v in W if k})
en.update({
    '_title': 'Wattprint — Your AI\'s footprint in 60 seconds · Neocortech',
    '_desc': 'Calculate how much carbon, energy and water your AI uses: training and inference with the SCI methodology (ISO/IEC 21031) and data from Ember and Uptime Institute.',
})
finish(s, en, 'wattprint.html')
