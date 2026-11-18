"""Índice interactivo de proyectos y filas del taller.

Genera el HTML de las secciones «Proyectos» y «Taller» (español) y las claves en inglés.
Los textos de cada ficha (pj*, tk*) siguen en sections_new.html / en_maker.py la primera vez
y se copian aquí para tener una sola fuente.
"""
import html

IMG = '/assets/projects/'

# Filtros: clave, etiqueta ES, etiqueta EN
FILTERS = [
    ('all', 'Todos', 'All'),
    ('vr', 'Realidad virtual', 'Virtual reality'),
    ('w3d', 'Web360 y 3D', 'Web360 and 3D'),
    ('game', 'Juegos', 'Games'),
    ('mob', 'Móvil y AR', 'Mobile and AR'),
]

# Orden del índice. ctx = contexto que se lee en la lista.
P = [
 dict(k='pj6', name='LiVRe', cats='vr', imgs=['livre'], ctx=('Fundación Magtel', 'Fundación Magtel')),
 dict(k='pj16', name='Cerco Industrial · Fase III', cats='vr w3d', imgs=['cerco-render', 'cerco-tour', 'cerco-modelo'], ctx=('Con un socio', 'With a partner'), name_en='Cerco Industrial · Phase III'),
 dict(k='pj1', name='SOL 672', cats='vr game', imgs=['sol672'], ctx=('Juego educativo VR', 'Educational VR game')),
 dict(k='pj7', name='In-Habit · CongreSkills', cats='w3d', imgs=['inhabit'], ctx=('Formación inclusiva', 'Inclusive training')),
 dict(k='pj3', name='Cronos Adventure', cats='vr game', imgs=['cronos'], ctx=('VR multijugador', 'Multiplayer VR')),
 dict(k='pj9', name='Metropolitan', cats='vr w3d', imgs=['metropolitan'], ctx=('Metrovacesa', 'Metrovacesa')),
 dict(k='pj10', name='Tour virtual COEC', cats='w3d', imgs=['coec'], ctx=('Colegio de Enfermería de Córdoba', 'Córdoba College of Nursing')),
 dict(k='pj2', name='BioVoyager VR', cats='vr game', imgs=['biovoyager'], ctx=('Juego educativo VR', 'Educational VR game')),
 dict(k='pj4', name='Superinspector', cats='game', imgs=['superinspector'], ctx=('Serious game', 'Serious game')),
 dict(k='pj5', name='Olympia XR', cats='vr w3d mob', imgs=['olympia'], ctx=('Con la Universidad Complutense', 'With Complutense University')),
 dict(k='pj8', name='José Cuervo 360º', cats='w3d', imgs=['josecuervo'], ctx=('Próximo Spain', 'Próximo Spain')),
 dict(k='pj11', name='Navidad 360º', cats='', imgs=['juegaterapia'], ctx=('Juegaterapia', 'Juegaterapia')),
 dict(k='pj12', name='Invitación en realidad aumentada', cats='mob', imgs=['invitacion-ar'], ctx=('Congreso', 'Conference'), name_en='Augmented reality invitation'),
 dict(k='pj13', name='Maqueta 3D de la base logística', cats='w3d', imgs=['ejercito'], ctx=('Ejército de Tierra', 'Spanish Army'), name_en='3D model of the logistics base'),
 dict(k='pj14', name='Calidad del aire en Carboneras', cats='', imgs=['carboneras'], ctx=('SGS · 2021', 'SGS · 2021'), name_en='Air quality in Carboneras'),
 dict(k='pj15', name='Empollo App', cats='mob', imgs=['empollo'], ctx=('Proyecto propio · 2015', 'Own project · 2015')),
]
for p in P:
    p.setdefault('name_en', {'Navidad 360º': 'Christmas in 360º', 'Tour virtual COEC': 'COEC virtual tour'}.get(p['name'], p['name']))

# Textos nuevos o cambiados de las fichas
BODY_ES = {
 'pj13': '<div class="ptags">3D · Eventos · Cliente: Ejército de Tierra</div><h3>Maqueta 3D de la base logística</h3><p>Maqueta 3D de la base logística de Córdoba para que el Ejército de Tierra la presentara en sus eventos. Fue el primer cliente de EONESIA.</p>',
 'pj16': '<div class="ptags">Web360 · Realidad virtual · Patrimonio industrial</div><h3>Cerco Industrial · Fase III</h3><p>Tour virtual del Cerco Industrial de Peñarroya-Pueblonuevo. Modelos 3D de los edificios históricos a partir de unas 13.900 fotografías aéreas y terrestres, panorámicas 360º con fichas de cada edificio y locuciones en español e inglés, y un puesto de realidad virtual en el mirador con seis visores. Proyecto fuera de EONESIA, financiado con ayudas LEADER.</p><div class="prole"><b>Mi papel:</b> diseño y dirección de parte del proyecto, junto a otro socio.</div><div class="plinks2"><a class="plink" href="https://www.cercoindustrialtourvirtual.com/fase3/index.htm" target="_blank" rel="noopener" data-c>Entrar en el tour ↗</a><a class="plink" href="https://www.cercoindustrialvirtual.com/faseiii" target="_blank" rel="noopener" data-c>Ver el proyecto ↗</a></div>',
}
BODY_EN = {
 'pj16': '<div class="ptags">Web360 · Virtual reality · Industrial heritage</div><h3>Cerco Industrial · Phase III</h3><p>Virtual tour of the Cerco Industrial in Peñarroya-Pueblonuevo, Spain. 3D models of the historic buildings built from around 13,900 aerial and ground photographs, 360º panoramas with a card for each building and narration in Spanish and English, and a virtual reality station at the viewpoint with six headsets. Outside EONESIA, funded through the EU LEADER programme.</p><div class="prole"><b>My role:</b> designed and directed part of the project, together with a partner.</div><div class="plinks2"><a class="plink" href="https://www.cercoindustrialtourvirtual.com/fase3/index.htm" target="_blank" rel="noopener" data-c>Enter the tour ↗</a><a class="plink" href="https://www.cercoindustrialvirtual.com/faseiii" target="_blank" rel="noopener" data-c>See the project ↗</a></div>',
}

TALLER = [
 ('tk1', 'rumbo', 'Rumbo: ficha de un lead con el email del agente, la probabilidad de cierre y el encaje explicado'),
 ('tk2', 'colibri', 'Colibrí: el valle con las cuatro etapas de la entrevista'),
 ('tk3', 'wattprint', 'Wattprint: huella de una tarea de IA y mapa de dónde conviene ejecutarla'),
 ('tk4', 'forja', 'Forja 42001: plataforma de estudio para la ISO/IEC 42001'),
]
TALLER_ALT_EN = {
 'tk1': 'Rumbo: a lead record with the agent’s email, close probability and explained fit score',
 'tk2': 'Colibrí: the valley with the four interview stages',
 'tk3': 'Wattprint: the footprint of an AI task and a map of where to run it',
 'tk4': 'Forja 42001: study platform for ISO/IEC 42001',
}


def esc(s):
    return html.escape(s, quote=True)


def proyectos_html(bodies):
    counts = {f: sum(1 for p in P if f in p['cats'].split()) for f, _, _ in FILTERS}
    counts['all'] = len(P)
    chips = ''.join(
        f'<button type="button" class="ixf" data-f="{f}" aria-pressed="{"true" if f == "all" else "false"}"><span data-i18n="ixf_{f}">{es}</span> <span class="ixf-n">{counts[f]}</span></button>'
        for f, es, _ in FILTERS)
    items = []
    for i, p in enumerate(P):
        pid = 'ix-' + p['k']
        figs = ''.join(
            f'<img src="{IMG}{im}.webp" alt="" loading="lazy" decoding="async" width="1600" height="900"{" class=\"on\"" if j == 0 else ""}/>'
            for j, im in enumerate(p['imgs']))
        dots = ''
        if len(p['imgs']) > 1:
            dots = '<div class="ix-dots" role="group" aria-label="Imágenes" data-i18n-attr="aria-label:a_ixdots">' + ''.join(
                f'<button type="button" aria-label="{j+1}"{" aria-current=true" if j == 0 else ""}></button>' for j in range(len(p['imgs']))) + '</div>'
        items.append(
            f'<li class="ix-it" data-cats="{p["cats"]}">'
            f'<button type="button" class="ix-row" id="{pid}-b" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="{pid}">'
            f'<span class="ix-name" data-i18n="ixn_{p["k"]}">{esc(p["name"])}</span>'
            f'<span class="ix-ctx" data-i18n="ixc_{p["k"]}">{esc(p["ctx"][0])}</span></button>'
            f'<div class="ix-panel{" on" if i == 0 else ""}" id="{pid}" role="region" aria-labelledby="{pid}-b">'
            f'<div class="ix-media">{figs}{dots}</div>'
            f'<div class="pbody ix-body" data-i18n="{p["k"]}">{bodies[p["k"]]}</div></div></li>')
    return (
        '<!-- PROYECTOS (índice interactivo) -->\n<section id="proyectos">\n  <div class="wrap">\n'
        '    <span class="eyebrow rvx" data-i18n="e02p"><span class="n">02</span> Proyectos</span>\n'
        '    <h2 class="sec rvx" data-i18n="h_proy">Cosas que existen <em>porque las hice realidad.</em></h2>\n'
        '    <p class="plead rvx" data-i18n="proy_lead">Lo que he creado, dirigido o diseñado desde 2015, en EONESIA y fuera de ella. Elige uno para ver qué era y qué hice yo.</p>\n'
        f'    <div class="ixf-bar rvx" role="group" aria-label="Filtrar proyectos" data-i18n-attr="aria-label:a_ixf">{chips}</div>\n'
        f'    <ul class="ix rvx" id="ix">{"".join(items)}</ul>\n'
        '  </div>\n</section>\n')


def taller_html(bodies):
    rows = ''.join(
        f'<article class="tr rvx"><div class="tr-img"><img src="{IMG}{im}.webp" alt="{esc(alt)}" data-i18n-attr="alt:a_{k}" loading="lazy" decoding="async" width="1600" height="900"/></div>'
        f'<div class="tc tr-body" data-i18n="{k}">{bodies[k]}</div></article>'
        for k, im, alt in TALLER)
    return (
        '<!-- TALLER (lo que construyo por mi cuenta) -->\n<section id="taller">\n  <div class="wrap">\n'
        '    <span class="eyebrow rvx" data-i18n="e03t"><span class="n">03</span> Taller</span>\n'
        '    <h2 class="sec rvx" data-i18n="h_taller">Lo que construyo <em>por mi cuenta.</em></h2>\n'
        '    <p class="plead rvx" data-i18n="taller_lead">Productos propios que diseño y construyo dirigiendo agentes de IA. Cada uno resuelve un problema concreto y se puede probar.</p>\n'
        f'    <div class="trs">{rows}</div>\n'
        '  </div>\n</section>\n')


def en_keys():
    d = {
        'e02p': '<span class="n">02</span> Projects',
        'proy_lead': 'What I have created, directed or designed since 2015, at EONESIA and beyond. Pick one to see what it was and what I did.',
        'a_ixf': 'Filter projects', 'a_ixdots': 'Images',
    }
    for f, _, en in FILTERS:
        d['ixf_' + f] = en
    for p in P:
        d['ixn_' + p['k']] = esc(p['name_en'])
        d['ixc_' + p['k']] = esc(p['ctx'][1])
    d.update(BODY_EN)
    for k, v in TALLER_ALT_EN.items():
        d['a_' + k] = v
    return d
