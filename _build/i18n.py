"""Piezas comunes de idioma (ES por defecto, EN con botón) para las tres páginas."""

HEAD = """<script>(function(){var q=null;try{q=new URLSearchParams(location.search).get('lang');}catch(e){}
var l=(q==='en'||q==='es')?q:null;try{if(l)localStorage.setItem('nc_lang',l);else l=localStorage.getItem('nc_lang');}catch(e){}
if(l!=='en')l='es';window.NC_LANG=l;document.documentElement.lang=l;
window.NCT=function(es,en){return l==='en'?en:es;};})();</script>"""

CSS = """
/* selector de idioma */
.lang{display:flex;align-items:center;gap:2px;padding:3px;border:1px solid rgba(201,162,75,.18);border-radius:40px;background:rgba(19,39,59,.5)}
.lang button{font-family:var(--ui,Inter,system-ui,sans-serif);font-size:11px;font-weight:600;letter-spacing:.14em;color:var(--muted);background:none;border:0;padding:6px 10px;border-radius:40px;cursor:pointer;transition:color .2s,background .2s}
.lang button:hover{color:var(--bone)}
.lang button[aria-pressed="true"]{background:var(--metal);color:var(--night)}
.lang button:focus-visible{outline:2px solid var(--gold-bright);outline-offset:2px}
"""

def toggle(extra_class=""):
    return ('<div class="lang %s" role="group" aria-label="Idioma" data-i18n-attr="aria-label:a_lang">'
            '<button type="button" data-lang="es" aria-pressed="true">ES</button>'
            '<button type="button" data-lang="en" aria-pressed="false">EN</button></div>') % extra_class

APPLY = """<script>(function(){
var D=window.NC_EN||{};
if(window.NC_LANG==='en'){
  document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');if(D[k]!=null)el.innerHTML=D[k];});
  document.querySelectorAll('[data-i18n-attr]').forEach(function(el){el.getAttribute('data-i18n-attr').split(';').forEach(function(p){var kv=p.split(':');if(D[kv[1]]!=null)el.setAttribute(kv[0],D[kv[1]]);});});
  if(D._title)document.title=D._title;
  var m=document.querySelector('meta[name="description"]');if(m&&D._desc)m.setAttribute('content',D._desc);
}
/* fase 4: el portfolio en inglés vive en /en */
if(window.NC_LANG==='en')document.querySelectorAll('a[href="/"],a[href^="/#"]').forEach(function(a){a.setAttribute('href','/en'+a.getAttribute('href').slice(1));});
document.querySelectorAll('.lang [data-lang]').forEach(function(b){
  b.setAttribute('aria-pressed',String(b.getAttribute('data-lang')===window.NC_LANG));
  b.addEventListener('click',function(){
    var t=b.getAttribute('data-lang');if(t===window.NC_LANG)return;
    try{localStorage.setItem('nc_lang',t);}catch(e){}
    /* fase 2: conservar la sección que se está leyendo */
    var cur=[].slice.call(document.querySelectorAll('main section[id],section[id],footer[id]')).filter(function(x){return x.getBoundingClientRect().top<innerHeight*.4;}).pop();
    var url=location.pathname+'?lang='+t+(cur&&scrollY>40?'#'+cur.id:'');
    var ps=document.querySelectorAll('.curtain i');
    var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(window.gsap&&ps.length&&!rm){gsap.set(ps,{yPercent:100});gsap.to(ps,{yPercent:0,duration:.42,ease:'expo.in',stagger:.02,onComplete:function(){location.href=url;}});}
    else location.href=url;
  });
});
})();</script>"""


def rep(s, old, new, count=1):
    n = s.count(old)
    if n != count:
        raise SystemExit("esperaba %d y hay %d: %r" % (count, n, old[:90]))
    return s.replace(old, new)


# ---- fase 4: portfolio con dos páginas estáticas (/ en español y /en en inglés) ----
# El idioma ya no se decide en el cliente: cada página trae sus textos en el HTML.
# ?lang=en en / redirige a /en (y ?lang=es en /en a /), conservando el #ancla; vercel.json hace lo mismo en el servidor.
# Se guarda nc_lang para que /newsletter y /wattprint (que siguen traduciéndose en el cliente) sigan el idioma elegido.
def index_head(lang):
    other = '/' if lang == 'en' else '/en'
    return ("<script>(function(){var l='%s';window.NC_LANG=l;window.NCT=function(es,en){return l==='en'?en:es;};"
            "var q=null;try{q=new URLSearchParams(location.search).get('lang');}catch(e){}"
            "if(q&&q!==l&&(q==='en'||q==='es')){location.replace('%s'+location.hash);return;}"
            "try{localStorage.setItem('nc_lang',l);}catch(e){}})();</script>") % (lang, other)


def index_toggle(lang):
    def a(code, href, label):
        cur = ' aria-current="page"' if code == lang else ''
        return f'<a href="{href}" hreflang="{code}" lang="{code}"{cur}>{label}</a>'
    return ('<div class="lang" role="group" aria-label="%s">' % ('Language' if lang == 'en' else 'Idioma')
            + a('es', '/', 'ES') + a('en', '/en', 'EN') + '</div>')


# Al cambiar de idioma se conserva la sección que se está leyendo (#id) y se usa la cortina corta.
INDEX_SWITCH = """<script>(function(){
document.querySelectorAll('.lang a[hreflang]').forEach(function(a){
  a.addEventListener('click',function(e){
    if(a.getAttribute('aria-current')==='page'){e.preventDefault();return;}
    if(e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button!==0)return;
    e.preventDefault();
    var cur=[].slice.call(document.querySelectorAll('main section[id],section[id],footer[id]')).filter(function(x){return x.getBoundingClientRect().top<innerHeight*.4;}).pop();
    var url=a.getAttribute('href')+(cur&&scrollY>40?'#'+cur.id:'');
    var ps=document.querySelectorAll('.curtain i');
    var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(window.gsap&&ps.length&&!rm){gsap.set(ps,{yPercent:100});gsap.to(ps,{yPercent:0,duration:.42,ease:'expo.in',stagger:.02,onComplete:function(){location.href=url;}});}
    else location.href=url;
  });
});
})();</script>"""

INDEX_CSS = """
/* fase 4: el selector de idioma del portfolio son enlaces (/ y /en) */
.lang a{font-family:var(--ui,Inter,system-ui,sans-serif);font-size:11px;font-weight:600;letter-spacing:.14em;color:var(--muted);text-decoration:none;padding:6px 10px;border-radius:40px;transition:color .2s,background .2s;display:inline-flex;align-items:center;justify-content:center}
.lang a:hover{color:var(--bone)}
.lang a[aria-current="page"]{background:var(--metal);color:var(--night);cursor:default}
.lang a:focus-visible{outline:2px solid var(--gold-bright);outline-offset:2px;border-radius:999px}
@media(max-width:560px){.lang a{min-width:44px;min-height:44px;padding:0 8px}}
"""
