# Claves nuevas o cambiadas para el enfoque maker (se añaden al final de index_en.js)
import json
EN = {
 "ov1": "Profile", "ov2": "<em>Projects</em>", "ov3": "Side projects", "ov4": "What I <em>bring</em>", "ov5": "AI governance", "ov6": "Research", "ov7": "Contact",
 "_title": "Carlos Gallego Galán — Product Designer · Technical PM",
 "_desc": "Product design and product management. Virtual reality for health and inclusion, web tools and AI agents with human oversight. Córdoba, Spain, remote.",
 "h1a": "“Creativity is", "h1m": "about solving", "h1b": "problems.”", "h1cite": "— Ed Catmull, co-founder of Pixar",
 "intro": "Since 2015 I have been turning ideas into things people use: an app with 500 users in 24 hours, virtual reality experiences for clients and, now, AI agents. The new layer: <strong>making that AI explainable and auditable.</strong>",
 "e01p": '<span class="n">01</span> Who I am',
 "e02p": '<span class="n">02</span> Projects · EONESIA 2022–2026',
 "h_proy": "Projects I have <em>designed or led.</em>",
 "proy_lead": "Immersive products I created, directed or designed as co-founder and Product and Innovation Lead at EONESIA, built for VR headsets, web and mobile.",
 "pj1": '<div class="ptags">VR · Educational game · STEM</div><h3>SOL 672</h3><p>The player is an astronaut stranded on Mars who has to restore power, produce oxygen and keep the station running using science and logic.</p><div class="paward">★ Finalist · Indie Games Málaga Awards 2024</div><div class="prole"><b>My role:</b> product creation and direction, UX/UI design, game design, narrative.</div><a class="plink" href="https://www.eonesia.com/portfolios/sol672-experiencia-ciencia-vr/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj2": '<div class="ptags">VR · Educational game · Biology</div><h3>BioVoyager VR</h3><p>A microscopic journey through the human body inside an exploration capsule, visiting organs, tissues and vital systems at cellular scale.</p><div class="prole"><b>My role:</b> product creation and direction, UX/UI design, game design, narrative.</div><a class="plink" href="https://www.eonesia.com/portfolios/bioyager-vr/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj3": '<div class="ptags">VR · Multiplayer · Education and health</div><h3>Cronos Adventure</h3><p>A multiplayer boat journey through historical periods, designed for children in hospital oncology units.</p><div class="prole"><b>My role:</b> product direction and UX/UI design.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-cronos-adventure-historia-vr/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj4": '<div class="ptags">PC · First-person serious game (demo)</div><h3>Superinspector</h3><p>The player is a food inspector who scans supermarket products, reads nutrition labels and faces ethical dilemmas whose outcomes change the game.</p><div class="prole"><b>My role:</b> product creation and direction, UX/UI design, game design, narrative.</div><a class="plink" href="https://www.eonesia.com/portfolios/superinspector/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj5": '<div class="ptags">VR · AR · Web3D · Social XR</div><h3>Olympia XR</h3><p>Cross-platform social XR experience for football communities, published on SideQuest, developed with the Complutense University of Madrid.</p><div class="prole"><b>My role:</b> product design, business model and game design; project execution.</div>',
 "pj6": '<div class="ptags">VR · Inclusive training · Client: Fundación Magtel</div><h3>LiVRe</h3><p>Everyday scenarios in VR where people with intellectual disabilities practise daily-living skills safely and at their own pace. €100k+ project.</p><div class="prole"><b>My role:</b> project direction and user testing in care centres.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-realidad-virtual-inclusiva-livre/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj7": '<div class="ptags">Web360 · Training platform</div><h3>In-Habit · CongreSkills</h3><p>Immersive platform that trains people with Down syndrome for five event-industry jobs through practical simulations.</p><div class="prole"><b>My role:</b> 3D avatar menu to choose the right outfit for each job, UI design, support on UX and logic.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-in-habit-formacion-inclusiva/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj8": '<div class="ptags">Web360 · Corporate training · Client: Próximo Spain</div><h3>José Cuervo 360º</h3><p>Browser-based 360º tour of the brand\'s headquarters for bartenders, with the brand\'s history and gamified cocktail training.</p><div class="prole"><b>My role:</b> client project lead.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-tour-virtual-corporativo-cuervo/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj9": '<div class="ptags">VR · 360º tour · Client: Metrovacesa</div><h3>Metropolitan</h3><p>Prospective buyers walk through homes and the community before they are built and give feedback on the services planned for the development.</p><div class="prole"><b>My role:</b> product creation and direction, UX/UI design, narrative.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-tour-virtual-inmobiliario-metropolitan/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj10": '<div class="ptags">Web360 · Virtual tour · Client: Córdoba College of Nursing</div><h3>COEC virtual tour</h3><p>A browser-based walkthrough of the College\'s facilities, so students, professionals and the public can see every space before they visit.</p><div class="prole"><b>My role:</b> UX/UI product design.</div><a class="plink" href="https://www.eonesia.com/portfolios/experiencias-tour-virtual-centro-coec/" target="_blank" rel="noopener" data-c>View project ↗</a>',
 "pj11": '<div class="ptags">360º video · Generative AI · Client: Juegaterapia</div><h3>Christmas in 360º</h3><p>A Christmas video for Juegaterapia\'s 360º immersive room in Madrid.</p><div class="prole"><b>My role:</b> created the video with ComfyUI, After Effects, Premiere and ElevenLabs.</div>',
 "pj12": '<div class="ptags">Augmented reality · Mobile · Events</div><h3>Augmented reality invitation</h3><p>A conference invitation that opens on the phone as a floating 3D card where guests answer questions.</p><div class="prole"><b>My role:</b> 3D modelling and animation in Blender, and building the experience in Onirix.</div>',
 "pj13": '<div class="ptags">3D · Events · Client: Spanish Army</div><h3>3D model of the logistics base</h3><p>A 3D model of the Córdoba logistics base for the Spanish Army to present at its events. It was EONESIA\'s first client.</p>',
 "psub": "Before EONESIA <em>· 2015–2021</em>",
 "pj14": '<div class="ptags">Geospatial data · Environment · SGS · 2021</div><h3>Air quality in Carboneras</h3><p>Hourly data from SGS sensors on a colour-coded map showing where levels approach or exceed EU and Spanish limits, so the client can act before breaching them. One of the two new business lines I launched at SGS.</p><div class="prole"><b>My role:</b> product design, data processing in Excel and R, and visualisation.</div>',
 "pj15": '<div class="ptags">Mobile app · EdTech · Own project · 2015</div><h3>Empollo App</h3><p>A gamified EdTech MVP. It reached more than 500 active users in its first 24 hours.</p><div class="paward">★ Winner · Startup Weekend Córdoba 2015</div><div class="prole"><b>My role:</b> co-founder and CEO.</div>',
 "e03t": '<span class="n">03</span> Side projects',
 "h_taller": "What I build <em>on my own.</em>",
 "taller_lead": "My own products, designed and built by directing AI agents. Each one solves a specific problem and you can try it.",
 "tk1": '<div class="tk">Agentic AI · CRM</div><h3>Rumbo</h3><p>Five agents prepare each sales opportunity: they research the account, score fit with rules that can be explained, recommend a product and draft the first email. No email goes out without human approval, and every action is logged.</p><div class="tlinks"><a href="https://rumbo-crm-omega.vercel.app" target="_blank" rel="noopener" data-c>Try the demo ↗</a><a href="https://github.com/KairlosGG/rumbo-crm" target="_blank" rel="noopener" data-c>See the code ↗</a></div>',
 "tk2": '<div class="tk">Conversational AI</div><h3>Colibrí</h3><p>A guided interview in stages, with a character who accompanies the user and a results dashboard. Demo version of a real pilot, with no client data. In Spanish.</p><div class="tlinks"><a href="https://colibri-entrevista.vercel.app" target="_blank" rel="noopener" data-c>Try the demo ↗</a><a href="https://github.com/KairlosGG/colibri-entrevista" target="_blank" rel="noopener" data-c>See the code ↗</a></div>',
 "tk3": '<div class="tk">Sustainability · Web tool</div><h3>Wattprint</h3><p>Calculates in a minute the carbon, energy and water used by AI training and inference, with the SCI methodology (ISO/IEC 21031) and data from Ember and Uptime Institute.</p><div class="tlinks"><a href="/wattprint" data-c>Try Wattprint →</a><a href="https://github.com/KairlosGG/wattprint" target="_blank" rel="noopener" data-c>See the code ↗</a></div>',
 "tk4": '<div class="tk">Learning · In progress</div><h3>Forja 42001</h3><p>A study platform and exam simulator I built to prepare for the ISO/IEC 42001 Lead Implementer. I want to turn it into a product with original content.</p><div class="tlinks"><span class="tsoon">Not published</span></div>',
 "e04a": '<span class="n">04</span> What I bring',
 "h_aporto": "From problem <em>to product.</em>",
 "a_venn": "Intersection of designing, building and making it auditable",
 "v1t": "I design", "v1s": "discovery · UX/UI · game design",
 "v2t": "I build", "v2s": "XR · web · AI agents",
 "v3t": "I make it auditable",
 "conv1": '<span class="hl">Design:</span> I talk to the client and the users, define what needs building and design it in Figma before a line of code is written. That is how I worked in virtual reality, in Web360 and on the SGS products.',
 "conv2": '<span class="hl">Build:</span> I coordinate development, 3D and design teams, and I build my own products by directing AI agents. <a class="inl" href="#taller">Rumbo</a>, my agentic CRM, is public with its source code.',
 "conv3": '<span class="hl">Standards:</span> the new layer. I design governance into the system with ISO/IEC 42001 and the EU AI Act: human oversight and traceability from the start.',
 "e05g": '<span class="n">05</span> The new layer · AI governance',
 "posit": "74% of companies plan to deploy agentic AI within the next two years, but only 21% have a mature governance model for autonomous agents (<a class=\"inl\" href=\"https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html\" target=\"_blank\" rel=\"noopener\">Deloitte, <i>State of AI in the Enterprise</i>, 2026 ↗</a>).",
 "e07": "07 · Contact",
}
import sys; sys.path.insert(0, '/home/claude/neocortech/build')
from projects import en_keys
EN.update(en_keys())
# fase 1: orden, numeración y menú
from secciones import en_keys as sec_keys
EN.update(sec_keys())
EN['cue'] = 'Scroll'
# fase 3: contenido (CV, botones del hero)
EN['cta_proy'] = 'See projects'
EN['cv'] = 'Download CV (PDF)'
EN['cv_href'] = '/assets/cv/CV_Carlos_Gallego_Galan_EN.pdf'
# fase 2: en el índice el nombre ya es el h3 (con el botón); el título del panel pasa a texto visual
import re as _re
from projects import title_tag
for _k in list(EN):
    if _re.fullmatch(r'pj\d+', _k):
        EN[_k] = title_tag(EN[_k])
EN['skip'] = 'Skip to content'
EN['a_ovpages'] = 'Ecosystem pages'
s = open('index_en.js', encoding='utf-8').read().rstrip().rstrip(';')
assert s.endswith('}')
add = ''.join(f'window.NC_EN[{json.dumps(k)}]={json.dumps(v, ensure_ascii=False)};\n' for k, v in EN.items())
open('index_en_full.js', 'w', encoding='utf-8').write(s + ';\n' + add)
print('ok', len(EN))
