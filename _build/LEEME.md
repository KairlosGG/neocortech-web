# Cómo se genera la web

Las páginas publicadas (`index.html`, `newsletter.html`, `wattprint.html`) se generan con estos scripts a partir de los originales de `src/`. Vercel ignora esta carpeta (`.vercelignore`).

1. `index_body.v1.html` + `sections_new.html` → `restructure.py` → `index_body.html` (cuerpo del portfolio en español).
2. `index_en.js` + `en_maker.py` → `index_en_full.js` (textos en inglés).
3. `secciones.py` fija el orden de las secciones, su numeración y el menú (ES y EN); lo usan `restructure.py` y `en_maker.py`.
4. `fase1.css` (diseño y estructura), `fase2.css` (accesibilidad y UX) y `fase3.css` (contenido: botones del hero, CV, caso de LiVRe) se añaden al final de la cascada en `build_index.py`, tras `projects.css`. `build_index.py` también sustituye el menú por `fase2_menu.js` y añade `fase2.js` (anclas con foco y URL, sección al cargar con #, revelado al recibir foco).
5. `all.sh` lo ejecuta todo: `build_index.py`, `build_pages.py`, copia la herramienta y las imágenes, `selfhost.py` (fuentes y GSAP locales) y `add_meta.py` (SEO, `robots.txt`, `sitemap.xml`, `vercel.json`), copia el vídeo del retrato y su póster (`static/img/cine-poster.webp`) y los CV en PDF (`static/cv/` → `out/assets/cv/`, ES y EN; el enlace cambia con el idioma mediante la clave `cv_href`).

Las rutas de los scripts apuntan a `/home/claude/neocortech/`. Para reconstruir en otra sesión: copiar `_build/` a `/home/claude/neocortech/build`, `_build/src` a `/home/claude/neocortech/src`, `_build/static` a `/home/claude/neocortech/static`, y ejecutar `bash build/all.sh`; el resultado queda en `/home/claude/neocortech/out`.
