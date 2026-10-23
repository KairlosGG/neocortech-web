# Neocortech · web

Web personal de Carlos Gallego Galán y de Neocortech, su proyecto de gobernanza de IA. Son tres páginas estáticas y una herramienta:

| Ruta | Qué es |
|---|---|
| `/` | Portfolio: perfil, proyectos de EONESIA, taller (productos propios), gobernanza, trayectoria e investigación |
| `/newsletter` | Newsletter de gobernanza de IA |
| `/wattprint` | Presentación de Wattprint |
| `/tool/wattprint/` | Wattprint: huella de carbono, energía y agua de la IA |

Las páginas están en español por defecto. El botón ES/EN las pasa a inglés y la elección se recuerda. También se puede enlazar directamente a la versión en inglés con `?lang=en`.

## Cómo está hecha

- HTML, CSS y JavaScript en un archivo por página, sin compilación.
- Animaciones con GSAP y ScrollTrigger y desplazamiento suave con Lenis.
- Una cortina de transición entre páginas. Si el navegador pide movimiento reducido, se desactiva.
- Despliegue en Vercel con rutas limpias (`vercel.json`).

## Vídeo del banner

El banner del perfil reproduce `assets/carlos_portrait.webm` o `assets/carlos_portrait.mp4` al hacer scroll. Si no existen, se muestra la imagen fija incrustada.

## Newsletter

El formulario envía el correo a un formulario de [Kit](https://kit.com) (plan gratuito). La URL de Kit se configura en `KIT_ACTION`, dentro del script de `newsletter.html`. Si se deja vacía, el botón abre un correo de alta.

## Autoría

Diseño, contenido y dirección: **Carlos Gallego Galán**. Construido con desarrollo asistido por IA.
