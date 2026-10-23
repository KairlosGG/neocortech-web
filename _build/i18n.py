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
document.querySelectorAll('.lang [data-lang]').forEach(function(b){
  b.setAttribute('aria-pressed',String(b.getAttribute('data-lang')===window.NC_LANG));
  b.addEventListener('click',function(){
    var t=b.getAttribute('data-lang');if(t===window.NC_LANG)return;
    try{localStorage.setItem('nc_lang',t);}catch(e){}
    var url=location.pathname+'?lang='+t;
    var ps=document.querySelectorAll('.curtain i');
    var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(window.gsap&&ps.length&&!rm){gsap.set(ps,{yPercent:100});gsap.to(ps,{yPercent:0,duration:.9,ease:'power4.inOut',stagger:.07,onComplete:function(){location.href=url;}});}
    else location.href=url;
  });
});
})();</script>"""


def rep(s, old, new, count=1):
    n = s.count(old)
    if n != count:
        raise SystemExit("esperaba %d y hay %d: %r" % (count, n, old[:90]))
    return s.replace(old, new)
