"""Arregla Wattprint en src/ (idempotente) y genera el repositorio aparte en /home/claude/wattprint."""
import os, re, shutil

SRC = '/home/claude/neocortech/src/tool/wattprint/index.html'
REPO_URL = 'https://github.com/KairlosGG/wattprint'
LIVE = 'neocortech-kohl.vercel.app/tool/wattprint/'
KIT = 'https://app.kit.com/forms/10085804/subscriptions'

s = open(SRC, encoding='utf-8').read()

def sub(old, new):
    global s
    if new in s:
        return
    if old not in s:
        return
    s = s.replace(old, new, 1)

# 1 · Newsletter conectada a Kit (Neocortech). Kit no devuelve CORS: no-cors y respuesta opaca.
sub("endpoint: '',            // ← pega aquí tu URL",
    f"endpoint: '{KIT}', // Kit · Neocortech")
sub("fieldName: 'email',      // nombre del campo que espera tu proveedor",
    "fieldName: 'email_address', // campo que espera Kit")
sub("{method:'POST',body,mode:'cors'}", "{method:'POST',body,mode:'no-cors'}")
sub("✓ Apuntado. Bienvenido a IA Sostenible — revisa tu correo.",
    "✓ Casi está: confirma la suscripción en el correo que te acaba de llegar (mira también en spam).")
sub("Cada semana: cómo reducir la huella de carbono, energía y agua de la IA. Directo, técnico, sin humo.",
    "Suscríbete a Neocortech, mi newsletter sobre gobernanza de IA: agentes, IA generativa, ética, riesgos y sostenibilidad.")

sub("const body=new FormData();", "const body=new URLSearchParams(); // urlencoded, como un formulario normal")

# 2 · URL real en la tarjeta PNG y en los enlaces generados desde un sandbox
sub("shareUrl: 'wattprint.app', // URL impresa en la tarjeta PNG",
    f"shareUrl: '{LIVE}', // URL impresa en la tarjeta PNG")

# 3 · Autoría y código en el pie
sub("wattprint v1.0 · dark mode = menos energía en OLED ·",
    'wattprint v1.0 · hecho por <a href="https://neocortech-kohl.vercel.app/" style="text-decoration:underline;text-underline-offset:2px">Carlos Gallego Galán</a> · '
    f'<a href="{REPO_URL}" target="_blank" rel="noopener" style="text-decoration:underline;text-underline-offset:2px">código en GitHub</a> ·')

# 4 · Envío como formulario normal a un iframe oculto (el mismo método que ya funciona en /newsletter)
sub('<form id="nlForm" style="display:flex', '<form id="nlForm" method="post" target="kit-sink-wp" style="display:flex')
sub('<input id="nlEmail" name="email" type="email"', '<input id="nlEmail" name="email_address" type="email"')
sub('<button id="nlBtn" class="btn btn-primary" type="submit">Suscribirme</button>\n      </form>',
    '<button id="nlBtn" class="btn btn-primary" type="submit">Suscribirme</button>\n      </form>\n      <iframe name="kit-sink-wp" title="kit" hidden></iframe>')
_a = s.find("$('nlForm').addEventListener('submit', async e=>{")
if _a != -1:
    _b = s.find("\n});", _a) + 4
    s = s[:_a] + """$('nlForm').addEventListener('submit', e=>{
  const form=$('nlForm'), email=$('nlEmail').value.trim(), msg=$('nlMsg'), btn=$('nlBtn');
  if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)){ e.preventDefault(); $('nlEmail').focus(); return; }
  if(!CONFIG.newsletter.endpoint){ e.preventDefault(); msg.textContent='Formulario sin configurar.'; return; }
  form.action=CONFIG.newsletter.endpoint; // el navegador envía el formulario al iframe oculto
  setTimeout(()=>{
    btn.disabled=true; btn.textContent='✓';
    msg.textContent='✓ Casi está: confirma la suscripción en el correo que te acaba de llegar (mira también en spam).';
    msg.style.color='var(--carbon)';
  },50);
});""" + s[_b:]

s = s.replace('metodología SCI (ISO 21031)', 'metodología SCI (ISO/IEC 21031)')
open(SRC, 'w', encoding='utf-8').write(s)
print('src wattprint ok')

# ---------- repositorio aparte ----------
R = '/home/claude/wattprint/'
os.makedirs(R + 'fonts', exist_ok=True)
t = s
t = re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?', '', t)
t = re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet"/?>',
           '<link rel="stylesheet" href="fonts/fonts.css"/>', t)
assert 'fonts.googleapis' not in t
open(R + 'index.html', 'w', encoding='utf-8').write(t)

FD = '/home/claude/neocortech/out/assets/fonts/'
need = ['space-grotesk-latin-500-normal', 'space-grotesk-latin-700-normal',
        'inter-latin-400-normal', 'inter-latin-500-normal', 'inter-latin-600-normal',
        'jetbrains-mono-latin-400-normal', 'jetbrains-mono-latin-500-normal', 'jetbrains-mono-latin-700-normal']
css = ''
for n in need:
    shutil.copy(FD + n + '.woff2', R + 'fonts/')
    fam = {'space': 'Space Grotesk', 'inter': 'Inter', 'jetbr': 'JetBrains Mono'}[n[:5]]
    w = re.search(r'-(\d00)-', n).group(1)
    css += f"@font-face{{font-family:'{fam}';font-style:normal;font-display:swap;font-weight:{w};src:url({n}.woff2) format('woff2')}}\n"
open(R + 'fonts/fonts.css', 'w').write(css)
print('repo ok')
