# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static single-page marketing site for the **Museo Archipiélago de Humboldt** (Chungungo, La Higuera, Región de Coquimbo, Chile). Plain HTML/CSS/vanilla JS — no build step, no framework, no package manager, no tests. Content is in **Spanish** (`<html lang="es">`); keep all user-facing copy in Spanish. Deployed at `museoarchipielagodehumboldt.cl`.

## Running locally

Open `index.html` directly in a browser, or serve the folder so root-relative paths (e.g. `/favicon.ico`) resolve:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

There is nothing to build, lint, or test. To preview a change, open the page in a browser (a phone/narrow viewport matters — see Responsive below).

## Structure

- `index.html` — the entire page. All sections live here as `<section id="...">` blocks (hero, importancia, arte, galeria, impacto, actividades, visita) anchored to the nav links.
- `css/styles.css` — all styling, organized by `/* ===== SECTION ===== */` comment banners that mirror the HTML sections.
- `js/main.js` — all behavior (small).
- `images/` — all assets are `.webp` (recent history converted everything from `.jpg`; keep new images as `.webp`).

## Conventions that span files

- **Design tokens**: colors and max-width are CSS custom properties in `:root` at the top of `styles.css` (`--ocean`, `--seafoam #2cb8a0`, `--deep`, `--sand`, `--text`, `--muted`, `--maxw 1140px`). Use these vars rather than hardcoding hex values. Note: `js/main.js` hardcodes the active-nav color `#2cb8a0` — if `--seafoam` changes, update it there too.
- **Fonts**: loaded from Google Fonts in `<head>` — `Playfair Display` (serif, for headings) and `Source Sans 3` (body).
- **Lightbox gallery**: gallery items use inline `onclick="openLightbox(this)"` calling functions in `main.js`. `openLightbox` reads the item's `<img>` src/alt into `#lightbox-img`; Escape or click closes. Adding a gallery image = copy a `.gallery-item` block in the `#galeria` grid; no JS change needed.
- **Scroll-spy nav**: `main.js` uses an `IntersectionObserver` over `section[id]` to highlight the matching `.nav-links a` (matched by `href="#id"`). For this to work, a new nav link and its target section must share the same id.
- **Responsive**: breakpoints are `@media (max-width: 768px)` and `(max-width: 480px)` at the bottom of `styles.css`. The hero text sits over a photographic background, so legibility on small screens / iPhone / Firefox is a recurring concern — verify text contrast over images when touching hero or `.hero-eyebrow`.
