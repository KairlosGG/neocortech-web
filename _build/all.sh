set -e
cd /home/claude/neocortech
python3 build/build_index.py
python3 build/build_pages.py
python3 build/wattprint_v2.py
mkdir -p out/assets/projects && rm -rf out/assets/projects && mkdir -p out/assets/projects && cp static/projects/*.webp out/assets/projects/
python3 build/selfhost.py
SITE=https://neocortech-kohl.vercel.app python3 build/add_meta.py
cp static/video/carlos_portrait.* out/assets/
cp static/img/cine-poster.webp out/assets/
mkdir -p out/assets/cv && cp static/cv/CV_Carlos_Gallego_Galan_ES.pdf static/cv/CV_Carlos_Gallego_Galan_EN.pdf out/assets/cv/
