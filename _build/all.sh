set -e
cd /home/claude/neocortech
python3 build/build_index.py
python3 build/build_pages.py
mkdir -p out/tool/wattprint && python3 build/wattprint_v2.py
mkdir -p out/assets/projects && cp static/projects/*.jpg out/assets/projects/
python3 build/selfhost.py
SITE=https://neocortech-kohl.vercel.app python3 build/add_meta.py
