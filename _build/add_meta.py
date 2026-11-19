import base64, datetime, hashlib, html, re, sys, json, os
OUT = '/home/claude/neocortech/out/'
SITE = os.environ.get('SITE', 'https://neocortech.vercel.app')

# fase 4: el portfolio tiene dos páginas estáticas, / (es) y /en (en), con canonical propio y hreflang recíprocos.
# newsletter y wattprint siguen traduciéndose en el cliente con ?lang=en, que no es una página indexable aparte,
# así que ya no anuncian un hreflang inglés (Google lo descartaba al apuntar el canonical a la versión española).
PAGES = {
    'index.html': ('/', 'og-carlos-es.jpg', 'es'),
    'en.html': ('/en', 'og-carlos-en.jpg', 'en'),
    'newsletter.html': ('/newsletter', 'og-newsletter.jpg', None),
    'wattprint.html': ('/wattprint', 'og-wattprint.jpg', None),
}
ALT = f'''<link rel="alternate" hreflang="es" href="{SITE}/"/>
<link rel="alternate" hreflang="en" href="{SITE}/en"/>
<link rel="alternate" hreflang="x-default" href="{SITE}/"/>'''


def person(lang, desc):
    """Datos estructurados Person, solo con lo que ya está publicado en la web."""
    d = {"@context": "https://schema.org", "@type": "Person", "@id": SITE + "/#carlos",
         "name": "Carlos Gallego Galán", "jobTitle": "Product Designer · Technical PM",
         "description": desc, "url": SITE + ('/en' if lang == 'en' else '/'),
         "image": SITE + "/assets/cine-poster.webp",
         "address": {"@type": "PostalAddress", "addressLocality": "Córdoba", "addressCountry": "ES"},
         "sameAs": ["https://www.linkedin.com/in/carlosgallegogalan", "https://github.com/KairlosGG"]}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '</script>'


for f, (path, img, lang) in PAGES.items():
    s = open(OUT + f, encoding='utf-8').read()
    s = re.sub(r'\n<!-- meta:begin -->.*?<!-- meta:end -->', '', s, flags=re.S)
    if lang:
        loc, alt_loc = ('en_GB', 'es_ES') if lang == 'en' else ('es_ES', 'en_GB')
        desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
        extra = ALT + f'\n<meta property="og:locale" content="{loc}"/>\n<meta property="og:locale:alternate" content="{alt_loc}"/>\n' + person(lang, desc)
    else:
        extra = '<meta property="og:locale" content="es_ES"/>'
    tags = f'''
<!-- meta:begin -->
<link rel="canonical" href="{SITE}{path}"/>
{extra}
<meta property="og:type" content="website"/>
<meta property="og:url" content="{SITE}{path}"/>
<meta property="og:image" content="{SITE}/assets/{img}"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="{SITE}/assets/{img}"/>
<!-- meta:end -->'''
    m = re.search(r'<meta property="og:description"[^>]*/>', s)
    s = s[:m.end()] + tags + s[m.end():]
    open(OUT + f, 'w', encoding='utf-8').write(s)

open(OUT + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
today = datetime.date.today().isoformat()
links = ''.join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{SITE}{p}"/>' for h, p in [('es', '/'), ('en', '/en'), ('x-default', '/')])
urls = ''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>{today}</lastmod>{links if p in ("/", "/en") else ""}</url>\n'
               for p in ['/', '/en', '/newsletter', '/wattprint'])
open(OUT + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                     f'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')

# fase 4: Content-Security-Policy. Los scripts en línea que quedan (pocos en el portfolio; más en newsletter y wattprint)
# se autorizan por su hash, calculado aquí sobre las páginas ya terminadas (add_meta.py es el último paso que toca el HTML).
hashes = set()
for f in PAGES:
    s = open(OUT + f, encoding='utf-8').read()
    for m in re.finditer(r'<script(\s[^>]*)?>(.*?)</script>', s, re.S):
        attrs = m.group(1) or ''
        if 'src=' in attrs or 'application/ld+json' in attrs:
            continue
        hashes.add("'sha256-" + base64.b64encode(hashlib.sha256(m.group(2).encode('utf-8')).digest()).decode() + "'")
KIT = 'https://app.kit.com https://*.kit.com https://*.convertkit.com'
CSP = ("default-src 'self'; script-src 'self' " + ' '.join(sorted(hashes)) + "; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data:; font-src 'self'; media-src 'self'; connect-src 'self'; manifest-src 'self'; "
       f"frame-src 'self' {KIT}; form-action 'self' {KIT}; frame-ancestors 'self'; base-uri 'self'; object-src 'none'; upgrade-insecure-requests")

# fase 4: caché. Fuentes y JS llevan versión en el nombre (librerías con su versión, app.<hash>.js) -> un año e immutable.
# Las imágenes no llevan versión -> 7 días y stale-while-revalidate de 30. HTML y PDF -> caché corta.
IMMUTABLE = "public, max-age=31536000, immutable"
json.dump({
    "cleanUrls": True,
    "trailingSlash": False,
    "redirects": [
        {"source": "/", "has": [{"type": "query", "key": "lang", "value": "en"}], "destination": "/en", "permanent": True},
        {"source": "/en", "has": [{"type": "query", "key": "lang", "value": "es"}], "destination": "/", "permanent": True},
        {"source": "/tool/wattprint", "destination": "https://wattprint-kappa.vercel.app/", "permanent": True},
        {"source": "/tool/wattprint/(.*)", "destination": "https://wattprint-kappa.vercel.app/", "permanent": True}],
    "headers": [
        {"source": "/(.*)", "headers": [
            {"key": "X-Content-Type-Options", "value": "nosniff"},
            {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
            {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
            {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"},
            {"key": "Content-Security-Policy", "value": CSP}]},
        {"source": "/((?!assets/).*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"}]},
        {"source": "/assets/js/(.*)", "headers": [{"key": "Cache-Control", "value": IMMUTABLE}]},
        {"source": "/assets/fonts/(.*)\\.woff2", "headers": [{"key": "Cache-Control", "value": IMMUTABLE}]},
        {"source": "/assets/fonts/fonts.css", "headers": [{"key": "Cache-Control", "value": "public, max-age=86400, stale-while-revalidate=604800"}]},
        {"source": "/assets/cv/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]},
        {"source": "/assets/((?!fonts/|js/|cv/).*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800, stale-while-revalidate=2592000"}]}]
}, open(OUT + 'vercel.json', 'w'), indent=2, ensure_ascii=False)
print('meta ok', SITE, 'csp hashes', len(hashes))
