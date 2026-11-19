# Fase 4 · rendimiento. Se ejecuta desde build_index.py (exec) sobre la cadena `s` ya montada, con `rep` de i18n.py.
import hashlib, os, re

# ---------- 1. bucles que no paran ----------
# partículas: DPR 1 (son manchas difusas) y en pausa también con la pestaña oculta
s = rep(s, "function size(){DPR=Math.min(devicePixelRatio||1,1.5);W=c.width=innerWidth*DPR;", "function size(){DPR=1;W=c.width=innerWidth*DPR;")
# (las partículas vuelven a toda la página y ya se pausan con la pestaña oculta en src/index.html)

# caja negra: solo pide fotogramas si está a la vista, la pestaña es visible y algo cambia
# (se para cuando la apertura converge; con el cursor encima sigue, porque los puntos recorren las aristas)
s = rep(s, "H=cv.height=r.height*DPR;}\nsize();addEventListener('resize',size);",
        "H=cv.height=r.height*DPR;}\nsize();addEventListener('resize',function(){size();draw();});")
s = rep(s, "var kb=false;if(!RM){box.setAttribute('tabindex','0');",
        "var bbRun=false,bbVis=false,bbSt='',bbHo=-1;\nfunction bbOn(){return bbVis&&!document.hidden;}\n"
        "function kick(){if(!bbRun&&bbOn()){bbRun=true;requestAnimationFrame(loop);}}\n"
        "var kb=false;if(!RM){box.setAttribute('tabindex','0');")
s = rep(s, "if(stateEl)stateEl.textContent=reveal>.85?'AUDITABLE':reveal>.4?NCT('ABRIENDO…','OPENING…'):NCT('OPACO','OPAQUE');\n"
           "if(hintEl)hintEl.style.opacity=reveal>.3?0:1;draw();requestAnimationFrame(loop);}",
        "if(Math.abs(target-reveal)<.002)reveal=target;\n"
        "var st=reveal>.85?'AUDITABLE':reveal>.4?NCT('ABRIENDO…','OPENING…'):NCT('OPACO','OPAQUE');if(stateEl&&st!==bbSt){stateEl.textContent=st;bbSt=st;}\n"
        "var ho=reveal>.3?0:1;if(hintEl&&ho!==bbHo){hintEl.style.opacity=ho;bbHo=ho;}draw();\n"
        "if(bbOn()&&(reveal!==target||reveal>.6))requestAnimationFrame(loop);else bbRun=false;}")
s = rep(s, "if(RM){reveal=1;draw();}else loop();})();",
        "if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){if(!bbRun)draw();});\n"
        "if(RM){reveal=1;draw();}else{draw();if(stateEl){bbSt=NCT('OPACO','OPAQUE');stateEl.textContent=bbSt;}\n"
        "['pointerenter','pointermove','pointerdown','pointerleave','click','keydown','focus','blur'].forEach(function(n){box.addEventListener(n,kick);});\n"
        "addEventListener('pointerup',kick);document.addEventListener('visibilitychange',kick);\n"
        "if('IntersectionObserver' in window)new IntersectionObserver(function(e){bbVis=e[0].isIntersecting;kick();}).observe(box);else{bbVis=true;kick();}}})();")

# Lenis: su bucle solo corre mientras hay desplazamiento suave (rueda o scrollTo animado); en reposo u oculta, ningún fotograma.
# El ticker de GSAP ya se duerme solo cuando no hay animaciones (autoSleep).
s = rep(s, "(function raf(t){lenis.raf(t);requestAnimationFrame(raf);})();",
        "(function(){var id=0,idle=0;\n"
        "function tick(t){id=0;lenis.raf(t);var busy=lenis.isScrolling==='smooth'||(lenis.animate&&lenis.animate.isRunning);idle=busy?0:idle+1;if(idle<20&&!document.hidden)id=requestAnimationFrame(tick);}\n"
        "function wake(){if(!id&&!document.hidden){lenis.time=0;idle=0;id=requestAnimationFrame(tick);}}\n"
        "var st0=lenis.scrollTo;lenis.scrollTo=function(){var r=st0.apply(lenis,arguments);wake();return r;};\n"
        "addEventListener('wheel',wake,{passive:true,capture:true});document.addEventListener('visibilitychange',wake);wake();})();")

# ---------- 3. librerías y JS propio fuera del HTML, con nombre versionado y defer ----------
JS = '/home/claude/neocortech/out/assets/js/'
os.makedirs(JS, exist_ok=True)
foot = s.index('</footer>')
blocks = [m for m in re.finditer(r'<script>(.*?)</script>\n?', s[foot:], re.S)]
libs, app, keep = [], [], []
for m in blocks:
    code = m.group(1)
    head = code[:200]
    if 'GSAP 3.15.0' in head: libs.append(('gsap-3.15.0.min.js', code))
    elif 'ScrollTrigger 3.15.0' in head: libs.append(('ScrollTrigger-3.15.0.min.js', code))
    elif 'var e=`1.3.23`' in head: libs.append(('lenis-1.3.23.min.js', code))
    elif "lang a[hreflang]" in code: keep.append(m)
    else: app.append(code.strip())
assert [n for n, _ in libs] == ['gsap-3.15.0.min.js', 'ScrollTrigger-3.15.0.min.js', 'lenis-1.3.23.min.js'], [n for n, _ in libs]
assert len(app) == 3, len(app)  # app principal, fase 2, projects.js
for n, code in libs:
    open(JS + n, 'w', encoding='utf-8').write(code.strip() + '\n')
app_code = ';\n'.join(app) + '\n'
APP_NAME = 'app.' + hashlib.sha256(app_code.encode()).hexdigest()[:10] + '.js'
for old in os.listdir(JS):
    if re.fullmatch(r'app\.[0-9a-f]{10}\.js', old) and old != APP_NAME: os.remove(JS + old)
open(JS + APP_NAME, 'w', encoding='utf-8').write(app_code)
tail = s[foot:]
for m in blocks:
    if m not in keep: tail = tail.replace(m.group(0), '', 1)
s = s[:foot] + tail
# fetchpriority alta: con defer Chrome las pide con prioridad baja y las fuentes les quitaban ancho de banda (medido en Slow 4G)
tags = ''.join(f'<script defer fetchpriority="high" src="/assets/js/{n}"></script>\n' for n, _ in libs) + f'<script defer fetchpriority="high" src="/assets/js/{APP_NAME}"></script>\n'
s = rep(s, '</head>', tags + '</head>')
print('fase 4: js externo', [n for n, _ in libs], APP_NAME, len(app_code))
