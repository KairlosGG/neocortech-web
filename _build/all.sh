set -e
cd /home/claude/neocortech
python3 build/build_index.py
python3 build/build_pages.py
cp src/tool/wattprint/index.html out/tool/wattprint/index.html
mkdir -p out/assets/projects && cp static/projects/*.jpg out/assets/projects/
python3 build/selfhost.py
SITE=https://neocortech-kohl.vercel.app python3 build/add_meta.py
