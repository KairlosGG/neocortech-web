"""Fase 4 · versión inglesa estática e indexable: out/en.html (con cleanUrls de Vercel queda en /en).
Parte de out/index.html (español) y aplica el diccionario de build/index_en_full.js en el HTML, igual que hacía el
cliente: primero el contenido de cada [data-i18n] (el más externo) y después los atributos de [data-i18n-attr].
Cambia también lang, title, description, og:title/og:description, la cabecera de idioma y los enlaces a «Carlos».
canonical, hreflang, og:url y og:locale los pone add_meta.py."""
import html, json, re, subprocess, sys
from html.parser import HTMLParser
sys.path.insert(0, '/home/claude/neocortech/build')
from i18n import index_head, index_toggle, rep

B = '/home/claude/neocortech/build/'
OUT = '/home/claude/neocortech/out/'
D = json.loads(subprocess.check_output(['node', '-e',
    "global.window={};require(process.argv[1]);process.stdout.write(JSON.stringify(window.NC_EN))", B + 'index_en_full.js']))
D.setdefault('menu', 'Index')
# como en la página española (build_index.py, fase 2), los h4 de los textos pasan a h3
D = {k: v.replace('<h4>', '<h3>').replace('</h4>', '</h3>') if isinstance(v, str) else v for k, v in D.items()}
s = open(OUT + 'index.html', encoding='utf-8').read()

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr', 'param'}


class Spans(HTMLParser):
    """Posiciones (inicio del contenido, fin del contenido) de cada elemento con un atributo dado."""
    def __init__(self, text, attr):
        super().__init__(convert_charrefs=False)
        self.text, self.attr, self.stack, self.found = text, attr, [], []
        self.lines = [0]
        for m in re.finditer('\n', text): self.lines.append(m.end())
    def off(self):
        l, c = self.getpos(); return self.lines[l - 1] + c
    def handle_starttag(self, tag, attrs):
        o = self.off(); end = o + len(self.get_starttag_text())
        if tag in VOID: return
        self.stack.append((tag, o, end, dict(attrs).get(self.attr)))
    def handle_endtag(self, tag):
        o = self.off()
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for t, so, se, v in self.stack[i:][::-1]:
                    if t == tag and v is not None: self.found.append((so, se, o, v))
                del self.stack[i:]; return


def apply_content(s):
    p = Spans(s, 'data-i18n'); p.feed(s); p.close()
    spans = sorted(p.found)
    outer, last_end = [], -1
    for so, se, eo, k in spans:  # solo los más externos (el cliente también sustituía primero el exterior)
        if so >= last_end: outer.append((so, se, eo, k)); last_end = eo
    miss = []
    for so, se, eo, k in reversed(outer):
        if k in D: s = s[:se] + D[k] + s[eo:]
        else: miss.append(k)
    return s, miss


def apply_attrs(s):
    def one(m):
        tag = m.group(0)
        spec = re.search(r'data-i18n-attr="([^"]+)"', tag).group(1)
        for pair in spec.split(';'):
            a, k = pair.split(':', 1)
            if k not in D: continue
            v = html.escape(D[k], quote=True)  # el cliente usaba setAttribute (texto literal)
            if re.search(r'\s%s="[^"]*"' % re.escape(a), tag): tag = re.sub(r'(\s%s=")[^"]*(")' % re.escape(a), lambda mm: mm.group(1) + v + mm.group(2), tag, count=1)
            else: tag = tag.replace(' data-i18n-attr=', f' {a}="{v}" data-i18n-attr=', 1)
        return tag
    return re.sub(r'<[a-zA-Z][^<>]*\sdata-i18n-attr="[^"]+"[^<>]*>', one, s)


body_a = s.index('<body'); 
head, body = s[:body_a], s[body_a:]
body, miss = apply_content(body)
body = apply_attrs(body)
s = head + body
# cabecera
s = rep(s, '<html lang="es"', '<html lang="en"')
s = rep(s, 'id="bbState">OPACO</span>', 'id="bbState">OPAQUE</span>')  # estado inicial de la caja negra (lo cambia el JS)
s = rep(s, index_head('es'), index_head('en'))
s = rep(s, index_toggle('es'), index_toggle('en'))
s = re.sub(r'<title>[^<]*</title>', '<title>' + D['_title'] + '</title>', s, count=1)
for sel, k in [(r'<meta name="description" content="[^"]*"/>', '_desc'), (r'<meta property="og:description" content="[^"]*"/>', '_desc'),
               (r'<meta property="og:title" content="[^"]*"/>', '_title')]:
    attr = sel.split('content=')[0].replace('<meta ', '').strip()
    s, n = re.subn(sel, lambda m: m.group(0).split('content=')[0] + 'content="' + D[k].replace('"', '&quot;') + '"/>', s, count=1)
    assert n == 1, sel
# enlaces internos a la portada en español -> /en
s, n = re.subn(r'href="/"', 'href="/en"', s)
s = s.replace('href="/en" hreflang="es"', 'href="/" hreflang="es"')  # el selector ES sigue apuntando a /
open(OUT + 'en.html', 'w', encoding='utf-8').write(s)
left = [k for k in re.findall(r'data-i18n="([^"]+)"', s) if k not in D]
print('en.html ok', len(s), 'sin traducir:', sorted(set(miss + left)), 'enlaces / -> /en:', n - 1)
