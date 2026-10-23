# Cómo se genera la web

Las páginas publicadas (`index.html`, `newsletter.html`, `wattprint.html`) se generan con estos scripts a partir de los originales de `src/`. Vercel ignora esta carpeta (`.vercelignore`).

1. `index_body.v1.html` + `sections_new.html` → `restructure.py` → `index_body.html` (cuerpo del portfolio en español).
2. `index_en.js` + `en_maker.py` → `index_en_full.js` (textos en inglés).
3. `all.sh` lo ejecuta todo: `build_index.py`, `build_pages.py`, copia la herramienta y las imágenes, `selfhost.py` (fuentes y GSAP locales) y `add_meta.py` (SEO, `robots.txt`, `sitemap.xml`, `vercel.json`).

Las rutas de los scripts apuntan a `/home/claude/neocortech/`. Para reconstruir en otra sesión: copiar `_build/` a `/home/claude/neocortech/build`, `_build/src` a `/home/claude/neocortech/src`, `_build/static` a `/home/claude/neocortech/static`, y ejecutar `bash build/all.sh`; el resultado queda en `/home/claude/neocortech/out`.
