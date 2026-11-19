"""Índice interactivo de proyectos y filas del taller.

Genera el HTML de las secciones «Proyectos» y «Taller» (español) y las claves en inglés.
Los textos de cada ficha (pj*, tk*) siguen en sections_new.html / en_maker.py la primera vez
y se copian aquí para tener una sola fuente.
"""
import html

IMG = '/assets/projects/'

# fase 4: srcset con variantes de 800 y 1200 px (las genera build/img_variants.py en el build)
SRC_DIR = '/home/claude/neocortech/static/projects/'
SIZES_IX = '(min-width: 901px) 44vw, 92vw'
SIZES_TW = {'lead': '(min-width: 901px) 50vw, 92vw', 'pair': '(min-width: 901px) 44vw, 92vw'}


def _width(im):
    try:
        from PIL import Image
        return Image.open(SRC_DIR + im + '.webp').width
    except Exception:
        return 1600


def img_attrs(im, sizes, lazy_data=False):
    """src (la de 1200 o el original), srcset y sizes. Con lazy_data, como data-* para no descargar hasta que se vaya a mostrar."""
    w = _width(im)
    cands = [(f'{IMG}{im}-{v}.webp', v) for v in (800, 1200) if w > v] + [(f'{IMG}{im}.webp', w)]
    src = next((u for u, v in cands if v == 1200), cands[-1][0])
    srcset = ', '.join(f'{u} {v}w' for u, v in cands)
    pre = 'data-' if lazy_data else ''
    return f'{pre}src="{src}" {pre}srcset="{srcset}" sizes="{sizes}"'

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
 dict(k='pj17', name='Pegasus Misión', cats='game', imgs=['pegasus'], ctx=('Fundación Sebastián Almagro', 'Fundación Sebastián Almagro'), name_en='Pegasus Mission'),
 dict(k='pj9', name='Metropolitan', cats='vr w3d', imgs=['metropolitan'], ctx=('Metrovacesa', 'Metrovacesa')),
 dict(k='pj10', name='Tour virtual COEC', cats='w3d', imgs=['coec'], ctx=('Colegio de Enfermería de Córdoba', 'Córdoba College of Nursing')),
 dict(k='pj2', name='BioVoyager VR', cats='vr game', imgs=['biovoyager'], ctx=('Juego educativo VR', 'Educational VR game')),
 dict(k='pj4', name='Superinspector', cats='game', imgs=['superinspector'], ctx=('Serious game', 'Serious game')),
 dict(k='pj5', name='Olympia XR', cats='vr w3d mob', imgs=['olympia'], ctx=('Con la Universidad Complutense', 'With Complutense University')),
 dict(k='pj8', name='José Cuervo 360º', cats='w3d', imgs=['josecuervo'], ctx=('Próximo Spain', 'Próximo Spain')),
 dict(k='pj11', name='Navidad 360º', cats='', imgs=['juegaterapia'], ctx=('Juegaterapia', 'Juegaterapia')),
 dict(k='pj12', name='Invitación en realidad aumentada', cats='mob', imgs=['invitacion-ar'], ctx=('Congreso', 'Conference'), name_en='Augmented reality invitation'),
 dict(k='pj13', name='Maqueta 3D de la BLET', cats='w3d', imgs=['ejercito'], ctx=('Ejército de Tierra', 'Spanish Army'), name_en='Spanish Army logistics base, 3D model'),
 dict(k='pj14', name='Calidad del aire en Carboneras', cats='', imgs=['carboneras'], ctx=('SGS · 2021', 'SGS · 2021'), name_en='Air quality in Carboneras'),
 dict(k='pj15', name='Empollo App', cats='mob', imgs=['empollo'], ctx=('Proyecto propio · 2015', 'Own project · 2015')),
]
for p in P:
    p.setdefault('name_en', {'Navidad 360º': 'Christmas in 360º', 'Tour virtual COEC': 'COEC virtual tour'}.get(p['name'], p['name']))

# Textos nuevos o cambiados de las fichas
BODY_ES = {
 'pj13': '<div class="ptags">3D · Eventos · Cliente: Ejército de Tierra</div><h3>Maqueta 3D de la BLET</h3><p>Maqueta 3D de la futura Base Logística del Ejército de Tierra (BLET) en Córdoba, para que el Ejército la presentara en sus eventos. Fue el primer cliente de EONESIA.</p><div class="prole"><b>Mi papel:</b> diseño UX/UI.</div>',
 'pj15': '<div class="ptags">App móvil · EdTech · Proyecto propio · 2015</div><h3>Empollo App</h3><p>App para universitarios que convierte el estudio en una partida de preguntas al estilo del Trivial. Nació en Córdoba con la idea de llevarla a otras universidades, y en las primeras 24 horas consiguió más de 500 usuarios activos.</p><div class="paward">★ Ganadora · Startup Weekend Córdoba 2015</div><div class="prole"><b>Mi papel:</b> cofundador y CEO.</div>',
 'pj3': "<div class=\"ptags\">VR · Multijugador · Educación y salud</div><h3>Cronos Adventure</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Reto</span>Que niños hospitalizados en unidades de oncología aprendan historia jugando juntos, sin moverse de su sitio y sin que la experiencia los canse.</p><dl class=\"pcase\"><div><dt>Qué es</dt><dd>Una barca mágica recorre distintas épocas de la historia. Varios niños viajan a la vez, exploran y colaboran entre ellos.</dd></div><div><dt>Cuidados de diseño</dt><dd>Se juega sentado y la barca avanza sola, así nadie tiene que caminar ni dirigir el movimiento y se evita el mareo. Interacciones sencillas y una narración que guía cada paso.</dd></div><div><dt>Por qué multijugador</dt><dd>En el hospital pasan mucho tiempo aislados; compartir la aventura con otros niños es parte de la experiencia.</dd></div><div><dt>Resultado</dt><dd>Producto propio de EONESIA, en su catálogo de realidad virtual para educación y salud.</dd></div></dl><div class=\"prole\"><b>Mi papel:</b> dirección del producto y todo el diseño UX/UI.</div><a class=\"plink\" href=\"https://www.eonesia.com/portfolios/experiencias-cronos-adventure-historia-vr/\" target=\"_blank\" rel=\"noopener\" data-c>Ver proyecto ↗</a>",
 'pj10': "<div class=\"ptags\">Web360 · Tour virtual · Salud</div><h3>Tour virtual COEC</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Reto</span>Que estudiantes, profesionales y ciudadanía conozcan por dentro el Colegio Oficial de Enfermería de Córdoba antes de ir, y que el Colegio se muestre con transparencia.</p><dl class=\"pcase\"><div><dt>Qué es</dt><dd>Un recorrido 360º por sus instalaciones que se abre en el navegador, en móvil, tablet u ordenador, sin gafas ni instalar nada.</dd></div><div><dt>Qué diseñé</dt><dd>La navegación entre espacios, los puntos interactivos con la información de cada área y la interfaz, pensada para alguien que entra por primera vez y no sabe dónde está cada cosa.</dd></div><div><dt>Resultado</dt><dd>Tour publicado para el Colegio y una de las referencias de salud de EONESIA.</dd></div></dl><div class=\"prole\"><b>Mi papel:</b> diseño de producto UX/UI.</div><a class=\"plink\" href=\"https://www.eonesia.com/portfolios/experiencias-tour-virtual-centro-coec/\" target=\"_blank\" rel=\"noopener\" data-c>Ver proyecto ↗</a>",
 'pj16': "<div class=\"ptags\">Web360 · Realidad virtual · Patrimonio industrial</div><h3>Cerco Industrial · Fase III</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Reto</span>Documentar y dar a conocer el patrimonio industrial del Cerco de Peñarroya-Pueblonuevo, tanto en el propio recinto como desde cualquier casa.</p><dl class=\"pcase\"><div><dt>Datos de partida</dt><dd>Unas 13.900 fotografías aéreas y terrestres para reconstruir en 3D más de veinte edificios, aligerados para que funcionen en tiempo real en web y en realidad virtual.</dd></div><div><dt>Decisiones de diseño</dt><dd>Interfaz mínima con pictogramas y una jerarquía clara; puntos numerados por edificio con su ficha; comparativas del estado actual y del pasado; locuciones en español e inglés.</dd></div><div><dt>En el mirador</dt><dd>Un puesto de realidad virtual con seis asientos giratorios, para mirar en 360º sin desplazarse, seis visores autónomos y tabletas para que el personal guíe a cada visitante.</dd></div><div><dt>Para que cargue en cualquier sitio</dt><dd>Cada edificio se carga por separado y hay una versión ligera para dispositivos modestos.</dd></div><div><dt>Resultado</dt><dd>Fase III publicada, financiada con ayudas LEADER del Grupo de Desarrollo Rural Valle del Alto Guadiato. Proyecto fuera de EONESIA.</dd></div></dl><div class=\"prole\"><b>Mi papel:</b> diseño y dirección de parte del proyecto, junto a otro socio.</div><div class=\"plinks2\"><a class=\"plink\" href=\"https://www.cercoindustrialtourvirtual.com/fase3/index.htm\" target=\"_blank\" rel=\"noopener\" data-c>Entrar en el tour ↗</a><a class=\"plink\" href=\"https://www.cercoindustrialvirtual.com/faseiii\" target=\"_blank\" rel=\"noopener\" data-c>Ver el proyecto ↗</a></div>",
 'pj17': "<div class=\"ptags\">Serious game · Simulador · Orientación profesional</div><h3>Pegasus Misión</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Reto</span>Que los jóvenes descubran cómo es trabajar como mecánico o piloto de helicópteros, y que Pegasus Aero Group llegue a ese público para captar talento.</p><dl class=\"pcase\"><div><dt>Qué es</dt><dd>Un videojuego simulador de operaciones en el que el jugador se pone en la piel de los mecánicos y los pilotos.</dd></div><div><dt>Cliente</dt><dd>Fundación Sebastián Almagro, de Pegasus Aero Group.</dd></div></dl><div class=\"prole\"><b>Mi papel:</b> dirección del proyecto, diseño de producto UX/UI y game design de todo el videojuego. Dirigí a los artistas 3D, al artista generalista y a los programadores en Unity.</div>",
}
BODY_EN = {
 'pj6': '<div class="ptags">VR · Inclusive training</div><h3>LiVRe</h3><p class="pcase-reto"><span class="pcase-k">Challenge</span>Help people with intellectual disabilities practise everyday tasks in virtual reality and gain independence, at their own pace and without fear of getting it wrong.</p><dl class="pcase"><div><dt>Where</dt><dd>9 care centres for people with disabilities across Córdoba, Seville and Málaga provinces. Client: Fundación Magtel (Futuro Singular programme).</dd></div><div><dt>How we tested it</dt><dd>Around 20 people with very different profiles tried both controllers and hand tracking, in alternating order.</dd></div><div><dt>What we changed</dt><dd>Hand tracking by default, with controllers as an alternative for people with less mobility; more colour and contrast so objects are easy to tell apart; visual and audio feedback on every action, so people always know when they have got it right.</dd></div><div><dt>Design safeguards</dt><dd>No artificial movement, so nobody feels dizzy; one instruction at a time; mistakes carry no penalty and can be retried.</dd></div><div><dt>Outcome</dt><dd>A project worth over €100,000; each person’s progress was tracked on a data platform.</dd></div></dl><div class="prole"><b>My role:</b> project direction and user testing in care centres.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-realidad-virtual-inclusiva-livre/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 'pj13': '<div class="ptags">3D · Events · Client: Spanish Army</div><h3>Spanish Army logistics base, 3D model</h3><p>A 3D model of the future Spanish Army Logistics Base (BLET) in Córdoba, for the Army to present at its events. It was EONESIA’s first client.</p><div class="prole"><b>My role:</b> UX/UI design.</div>',
 'pj15': '<div class="ptags">Mobile app · EdTech · Own project · 2015</div><h3>Empollo App</h3><p>An app for university students that turns studying into a Trivial Pursuit-style quiz game. It started in Córdoba with the aim of reaching other universities, and it got more than 500 active users in its first 24 hours.</p><div class="paward">★ Winner · Startup Weekend Córdoba 2015</div><div class="prole"><b>My role:</b> co-founder and CEO.</div>',
 'pj3': "<div class=\"ptags\">VR · Multiplayer · Education and health</div><h3>Cronos Adventure</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Challenge</span>Help children in hospital oncology units learn history by playing together, without leaving their seat and without the experience wearing them out.</p><dl class=\"pcase\"><div><dt>What it is</dt><dd>A magic boat travels through different periods of history. Several children ride at once, explore and work together.</dd></div><div><dt>Design care</dt><dd>Children play seated and the boat moves on its own, so nobody has to walk or steer and motion sickness is avoided. Simple interactions and narration that guides every step.</dd></div><div><dt>Why multiplayer</dt><dd>Children in hospital spend a lot of time isolated; sharing the adventure with others is part of the experience.</dd></div><div><dt>Outcome</dt><dd>An EONESIA product, part of its virtual reality catalogue for education and health.</dd></div></dl><div class=\"prole\"><b>My role:</b> product direction and all the UX/UI design.</div><a class=\"plink\" href=\"https://www.eonesia.com/portfolios/experiencias-cronos-adventure-historia-vr/\" target=\"_blank\" rel=\"noopener\" data-c>View project ↗</a>",
 'pj10': "<div class=\"ptags\">Web360 · Virtual tour · Health</div><h3>COEC virtual tour</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Challenge</span>Let students, professionals and the public see inside the Córdoba College of Nursing before they visit, and help the College present itself openly.</p><dl class=\"pcase\"><div><dt>What it is</dt><dd>A 360º walkthrough of its facilities that opens in the browser on phone, tablet or computer, with no headset and nothing to install.</dd></div><div><dt>What I designed</dt><dd>Navigation between spaces, the interactive points with information about each area, and the interface, built for someone visiting for the first time who does not know where anything is.</dd></div><div><dt>Outcome</dt><dd>A published tour for the College and one of EONESIA’s health references.</dd></div></dl><div class=\"prole\"><b>My role:</b> UX/UI product design.</div><a class=\"plink\" href=\"https://www.eonesia.com/portfolios/experiencias-tour-virtual-centro-coec/\" target=\"_blank\" rel=\"noopener\" data-c>View project ↗</a>",
 'pj16': "<div class=\"ptags\">Web360 · Virtual reality · Industrial heritage</div><h3>Cerco Industrial · Phase III</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Challenge</span>Document and share the industrial heritage of the Cerco in Peñarroya-Pueblonuevo, Spain, both on site and from anywhere.</p><dl class=\"pcase\"><div><dt>Starting data</dt><dd>Around 13,900 aerial and ground photographs to rebuild more than twenty buildings in 3D, optimised to run in real time on the web and in virtual reality.</dd></div><div><dt>Design decisions</dt><dd>A minimal interface with pictograms and a clear hierarchy; numbered points for each building with its own card; then-and-now comparisons; narration in Spanish and English.</dd></div><div><dt>At the viewpoint</dt><dd>A virtual reality station with six swivel seats, so people can look around in 360º without walking, six standalone headsets and tablets so staff can guide each visitor.</dd></div><div><dt>Loads anywhere</dt><dd>Each building loads separately and there is a light version for less powerful devices.</dd></div><div><dt>Outcome</dt><dd>Phase III published, funded by the EU LEADER programme through the Valle del Alto Guadiato rural development group. Outside EONESIA.</dd></div></dl><div class=\"prole\"><b>My role:</b> designed and directed part of the project, together with a partner.</div><div class=\"plinks2\"><a class=\"plink\" href=\"https://www.cercoindustrialtourvirtual.com/fase3/index.htm\" target=\"_blank\" rel=\"noopener\" data-c>Enter the tour ↗</a><a class=\"plink\" href=\"https://www.cercoindustrialvirtual.com/faseiii\" target=\"_blank\" rel=\"noopener\" data-c>See the project ↗</a></div>",
 'pj17': "<div class=\"ptags\">Serious game · Simulator · Career guidance</div><h3>Pegasus Mission</h3><p class=\"pcase-reto\"><span class=\"pcase-k\">Challenge</span>Show young people what it is like to work as a helicopter mechanic or pilot, and help Pegasus Aero Group reach that audience and attract talent.</p><dl class=\"pcase\"><div><dt>What it is</dt><dd>An operations simulator game where the player steps into the shoes of mechanics and pilots.</dd></div><div><dt>Client</dt><dd>Fundación Sebastián Almagro, part of Pegasus Aero Group.</dd></div></dl><div class=\"prole\"><b>My role:</b> project direction, UX/UI product design and game design for the whole game. I directed the 3D artists, the generalist artist and the Unity developers.</div>",
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

# fase 2: texto alternativo de cada imagen del índice (ES, EN), descrito a partir de la imagen
ALT = {
 'livre': ('Visor de realidad virtual con el logotipo de LiVRe', 'VR headset with the LiVRe logo'),
 'cerco-render': ('Recreación 3D de un castillete minero y una chimenea del Cerco Industrial', '3D recreation of a mine headframe and a chimney at the Cerco Industrial'),
 'cerco-tour': ('Tour virtual: vista aérea del Cerco Industrial con los edificios señalados en el mapa', 'Virtual tour: aerial view of the Cerco Industrial with the buildings marked on the map'),
 'cerco-modelo': ('Modelo 3D de la sala de turbinas de la central térmica, dentro del tour virtual', '3D model of the power station turbine hall, inside the virtual tour'),
 'sol672': ('Pantalla de título de SOL 672: un brote verde sobre la superficie de Marte', 'SOL 672 title screen: a green sprout on the surface of Mars'),
 'inhabit': ('Auditorio virtual de In-Habit con butacas de madera y pantalla', 'In-Habit virtual auditorium with wooden seats and a screen'),
 'pegasus': ('Pantalla de inicio de Pegasus Misión: un helicóptero amarillo en el helipuerto y el menú del simulador', 'Pegasus Mission start screen: a yellow helicopter on the helipad and the simulator menu'),
 'cronos': ('Pantalla de título de Cronos Adventure: un portal luminoso frente a un personaje', 'Cronos Adventure title screen: a glowing portal in front of a character'),
 'metropolitan': ('Recreación de los edificios de viviendas de Metropolitan', 'Rendering of the Metropolitan residential buildings'),
 'coec': ('Tour virtual: entrada a la sede del Colegio Oficial de Enfermería de Córdoba', 'Virtual tour: entrance to the Córdoba College of Nursing building'),
 'biovoyager': ('Logotipo de BioVoyager VR con la cápsula de exploración', 'BioVoyager VR logo with the exploration capsule'),
 'superinspector': ('Pantalla de título de Superinspector de alimentos con el inspector protagonista', 'Superinspector title screen with the inspector character'),
 'olympia': ('Dos aficionados con camisetas de fútbol frente a un estadio iluminado', 'Two fans in football shirts facing a floodlit stadium'),
 'josecuervo': ('Recreación 3D del tren José Cuervo Express junto a una estación con agaves', '3D rendering of the José Cuervo Express train beside a station with agave plants'),
 'juegaterapia': ('Fotograma del vídeo navideño: niños jugando en la nieve con muñecos de nieve', 'Frame from the Christmas video: children playing in the snow with snowmen'),
 'invitacion-ar': ('Móvil que muestra la invitación como una tarjeta 3D flotante en un congreso', 'Phone showing the invitation as a floating 3D card at a conference'),
 'ejercito': ('Vista aérea de la maqueta 3D de la base logística', 'Aerial view of the 3D model of the logistics base'),
 'carboneras': ('Vista aérea de Carboneras con los puntos de medición en colores', 'Aerial view of Carboneras with colour-coded measurement points'),
 'empollo': ('Logotipo de Empollo App: un polluelo con birrete y gafas', 'Empollo App logo: a chick with a graduation cap and glasses'),
}


def title_tag(body):
    """fase 2: el nombre del proyecto ya es el encabezado (h3 con el botón); el título del panel queda como texto visual."""
    return body.replace('<h3>', '<p class="ix-t" aria-hidden="true">', 1).replace('</h3>', '</p>', 1)


def esc(s):
    return html.escape(s, quote=True)


# fase 4: solo el primer proyecto (abierto por defecto en escritorio) lleva src; el resto, data-src/data-srcset
# y projects.js los hidrata al pasar, enfocar o abrir la fila (y a sus vecinas), para que los paneles ocultos no descarguen nada.
def proyectos_html(bodies):
    counts = {f: sum(1 for p in P if f in p['cats'].split()) for f, _, _ in FILTERS}
    counts['all'] = len(P)
    chips = ''.join(
        f'<button type="button" class="ixf" data-f="{f}" aria-pressed="{"true" if f == "all" else "false"}"><span data-i18n="ixf_{f}">{es}</span> <span class="ixf-n">{counts[f]}</span></button>'
        for f, es, _ in FILTERS)
    items = []
    for i, p in enumerate(P):
        pid = 'ix-' + p['k']
        n = len(p['imgs'])
        figs = ''.join(
            f'<img {img_attrs(im, SIZES_IX, lazy_data=(i > 0))} alt="{esc(ALT[im][0])}" data-i18n-attr="alt:a_ixi_{im}" loading="lazy" decoding="async" width="1600" height="900"{" class=\"on\"" if j == 0 else " aria-hidden=\"true\""}/>'
            for j, im in enumerate(p['imgs']))
        dots = ''
        if n > 1:
            dots = (f'<div class="ix-dots" role="group" aria-label="Imágenes de {esc(p["name"])}" data-i18n-attr="aria-label:a_ixdots_{p["k"]}">' + ''.join(
                f'<button type="button" aria-label="Imagen {j+1} de {n}" data-i18n-attr="aria-label:a_ixdot_{j+1}_{n}"{" aria-current=true" if j == 0 else ""}></button>' for j in range(n)) + '</div>')
        items.append(
            f'<li class="ix-it" data-cats="{p["cats"]}">'
            f'<h3 class="ix-h"><button type="button" class="ix-row" id="{pid}-b" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="{pid}">'
            f'<span class="ix-name" data-i18n="ixn_{p["k"]}">{esc(p["name"])}</span>'
            f'<span class="ix-ctx" data-i18n="ixc_{p["k"]}">{esc(p["ctx"][0])}</span></button></h3>'
            f'<div class="ix-panel{" on" if i == 0 else ""}" id="{pid}" role="region" aria-labelledby="{pid}-b">'
            f'<div class="ix-media">{figs}{dots}</div>'
            f'<div class="pbody ix-body" data-i18n="{p["k"]}">{title_tag(bodies[p["k"]])}</div></div></li>')
    return (
        '<!-- PROYECTOS (índice interactivo) -->\n<section id="proyectos">\n  <div class="wrap">\n'
        '    <span class="eyebrow rvx" data-i18n="e02p"><span class="n">02</span> Proyectos</span>\n'
        '    <h2 class="sec rvx" data-i18n="h_proy">Proyectos que he <em>diseñado o dirigido.</em></h2>\n'
        '    <p class="plead rvx" data-i18n="proy_lead">Lo que he creado, dirigido o diseñado desde 2015, en EONESIA y fuera de ella. Elige uno para ver qué era y qué hice yo.</p>\n'
        f'    <div class="ixf-bar rvx" role="group" aria-label="Filtrar proyectos" data-i18n-attr="aria-label:a_ixf">{chips}</div>\n'
        '    <p id="ixLive" class="sr-only" aria-live="polite" aria-atomic="true"></p>\n'
        f'    <ul class="ix rvx" id="ix">{"".join(items)}</ul>\n'
        '  </div>\n</section>\n')


def taller_html(bodies):
    # fase 1: clases propias del Taller (.tw*) para no chocar con .tr/.tc/.tl de otras piezas.
    # Rumbo en cabeza, Colibrí y Wattprint en pareja, Forja (sin publicar) en una línea.
    kind = ['lead', 'pair', 'pair', 'note']
    rows = ''.join(
        f'<article class="tw tw-{kind[i]} rvx">'
        + ('' if kind[i] == 'note' else f'<div class="tw-img"><img {img_attrs(im, SIZES_TW[kind[i]])} alt="{esc(alt)}" data-i18n-attr="alt:a_{k}" loading="lazy" decoding="async" width="1600" height="900"/></div>')
        + f'<div class="tw-body" data-i18n="{k}">{bodies[k]}</div></article>'
        for i, (k, im, alt) in enumerate(TALLER))
    return (
        '<!-- TALLER (lo que construyo por mi cuenta) -->\n<section id="taller">\n  <div class="wrap">\n'
        '    <span class="eyebrow rvx" data-i18n="e03t"><span class="n">03</span> Proyectos propios</span>\n'
        '    <h2 class="sec rvx" data-i18n="h_taller">Lo que construyo <em>por mi cuenta.</em></h2>\n'
        '    <p class="plead rvx" data-i18n="taller_lead">Productos propios que diseño y construyo dirigiendo agentes de IA. Cada uno resuelve un problema concreto y se puede probar.</p>\n'
        f'    <div class="tws">{rows}</div>\n'
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
    for im, (_, en) in ALT.items():
        d['a_ixi_' + im] = esc(en)
    for p in P:
        d['a_ixdots_' + p['k']] = 'Images of ' + esc(p['name_en'])
        for j in range(len(p['imgs'])):
            d['a_ixdot_%d_%d' % (j + 1, len(p['imgs']))] = 'Image %d of %d' % (j + 1, len(p['imgs']))
    for k, v in TALLER_ALT_EN.items():
        d['a_' + k] = v
    return d
