import re
OUT='/home/claude/neocortech/out/'
for f in ['index.html','newsletter.html','wattprint.html']:
    s=open(OUT+f,encoding='utf-8').read()
    s=re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?','',s)
    links=re.findall(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet"/?>\n?',s)
    for i,l in enumerate(links):
        s=s.replace(l,'<link rel="stylesheet" href="/assets/fonts/fonts.css"/>\n' if i==0 else '',1)
    s=s.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>','<script src="/assets/js/gsap-3.12.5.min.js"></script>')
    assert 'fonts.googleapis' not in s and 'cdnjs' not in s, f
    open(OUT+f,'w',encoding='utf-8').write(s)
print('selfhost ok')

# herramienta Wattprint: solo cambia de dónde se cargan las tipografías
t=OUT+'tool/wattprint/index.html'
s=open(t,encoding='utf-8').read()
s=re.sub(r'<link rel="preconnect" href="https://fonts\.(googleapis|gstatic)\.com"[^>]*>\n?','',s)
s=re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet"/?>','<link rel="stylesheet" href="/assets/fonts/fonts.css"/>',s)
assert 'fonts.googleapis' not in s
open(t,'w',encoding='utf-8').write(s)
print('wattprint tool ok')
