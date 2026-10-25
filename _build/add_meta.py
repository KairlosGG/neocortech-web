import re, sys, json, os
OUT = '/home/claude/neocortech/out/'
SITE = os.environ.get('SITE', 'https://neocortech.vercel.app')

PAGES = {
    'index.html': ('/', 'og-carlos.jpg'),
    'newsletter.html': ('/newsletter', 'og-newsletter.jpg'),
    'wattprint.html': ('/wattprint', 'og-wattprint.jpg'),
}
for f, (path, img) in PAGES.items():
    s = open(OUT + f, encoding='utf-8').read()
    s = re.sub(r'\n<!-- meta:begin -->.*?<!-- meta:end -->', '', s, flags=re.S)
    tags = f'''
<!-- meta:begin -->
<link rel="canonical" href="{SITE}{path}"/>
<link rel="alternate" hreflang="es" href="{SITE}{path}"/>
<link rel="alternate" hreflang="en" href="{SITE}{path}?lang=en"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{SITE}{path}"/>
<meta property="og:image" content="{SITE}/assets/{img}"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:locale" content="es_ES"/>
<meta property="og:locale:alternate" content="en_GB"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="{SITE}/assets/{img}"/>
<!-- meta:end -->'''
    m = re.search(r'<meta property="og:description"[^>]*/>', s)
    s = s[:m.end()] + tags + s[m.end():]
    open(OUT + f, 'w', encoding='utf-8').write(s)

open(OUT + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
urls = ''.join(f'  <url><loc>{SITE}{p}</loc></url>\n' for p in ['/', '/newsletter', '/wattprint'])
open(OUT + 'sitemap.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
json.dump({
    "cleanUrls": True,
    "trailingSlash": False,
    "redirects": [
        {"source": "/tool/wattprint", "destination": "https://wattprint-kappa.vercel.app/", "permanent": True},
        {"source": "/tool/wattprint/(.*)", "destination": "https://wattprint-kappa.vercel.app/", "permanent": True}],
    "headers": [{"source": "/(.*)", "headers": [
        {"key": "X-Content-Type-Options", "value": "nosniff"},
        {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
        {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
        {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}]},
        {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}]
}, open(OUT + 'vercel.json', 'w'), indent=2)
print('meta ok', SITE)
