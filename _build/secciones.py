"""Orden de las secciones del portfolio, numeración y menú (ES y EN). Una sola fuente.

Lo usan restructure.py (HTML en español) y en_maker.py (claves en inglés).
Cada entrada: id de la sección, etiqueta de la cabecera (ES, EN), etiqueta del menú (ES, EN).
"""

ORDEN = [
    ('proyectos', ('Proyectos', 'Projects'), ('Proyectos', 'Projects')),
    ('taller', ('Proyectos propios', 'Side projects'), ('Proyectos propios', 'Side projects')),
    ('perfil', ('Quién soy', 'Who I am'), ('Perfil', 'Profile')),
    ('aporto', ('Qué aporto', 'What I bring'), ('Qué aporto', 'What I bring')),
    ('trayectoria', ('Trayectoria', 'Career'), ('Trayectoria', 'Career')),
    ('formacion', ('Formación', 'Education'), ('Formación', 'Education')),
    ('manifiesto', ('La capa nueva · gobernanza de IA', 'The new layer · AI governance'), ('Gobernanza de IA', 'AI governance')),
    ('doctorado', ('Investigación · en exploración', 'Research · exploratory'), ('Investigación', 'Research')),
    ('contacto', ('Contacto', 'Contact'), ('Contacto', 'Contact')),
]


def num(i):
    return '%02d' % (i + 1)


def eyebrow_inner(i, label):
    return '<span class="n">%s</span> %s' % (num(i), label)


def menu_html():
    rows = ''.join(
        '\n    <a href="#%s" data-c><span class="on">%s</span><span data-i18n="ovm_%s">%s</span></a>' % (sid, num(i), sid, m[0])
        for i, (sid, _, m) in enumerate(ORDEN))
    return '<nav class="ov-nav" id="ovNav">' + rows + '\n  </nav>'


def en_keys():
    d = {}
    for i, (sid, eb, m) in enumerate(ORDEN):
        d['eb_' + sid] = eyebrow_inner(i, eb[1])
        d['ovm_' + sid] = m[1]
    return d
