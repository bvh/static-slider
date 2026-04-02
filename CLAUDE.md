# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static Slider is a static site generator for photography galleries. It takes source images and a JSON manifest, then produces a set of HTML pages with a thumbnail grid and a CSS scroll-snap image slider. The slider is driven by `:target` CSS selectors and minimal vanilla JavaScript — no frameworks or build tools.

## Commands

Generate the gallery into `public/`:
```
uv run generate.py
```

Preview locally:
```
open public/index.html
```

Deploy to remote server (requires `.env` — copy `.env.example` and fill in `REMOTE_HOST`/`REMOTE_PATH`):
```
./publish.sh
```

Python 3.14+, managed via `uv`. Only external dependency is Jinja2.

## Architecture

- **`generate.py`** — Main build script. Reads `config.json` and `images/gallery.json`, merges them into a template context, renders Jinja2 templates, copies source images and static assets, and writes everything to `public/`. Cleans `public/` on each run.
- **`config.json`** — Site-wide settings (stylesheet/script paths), keyed under `site`.
- **`images/gallery.json`** — Gallery manifest: ordered list of images with metadata (title, description, EXIF data, artist, dates). Each image's `id` doubles as its subdirectory name in the output. Data is nested as `site.gallery.images[]`. Note: the entire `images/` directory is gitignored (including `gallery.json` itself); only `gallery.json` matters for templates.
- **`templates/index.html`** — Gallery index template. Renders a thumbnail grid and a full-screen slider. Uses Jinja2 `{{ }}` / `{% %}` syntax. Context variables: `site`, `gallery`, `images`.
- **`templates/image.html`** — Individual image detail page template. Displays the photo with EXIF metadata. Context variables: `site`, `img`.
- **`css/styles.css`** — All styling. Supports light/dark mode via `prefers-color-scheme`. Uses `dvw`/`dvh` units with `vw`/`vh` fallbacks.
- **`js/slider.js`** — Slider behavior: keyboard navigation (arrow keys, Escape, Tab trapping), scroll-snap synchronization, hash-based routing, prev/next buttons, and accessibility (ARIA attributes, focus management).

## Output Structure

The generator should produce `public/index.html` and a subdirectory per image (e.g., `public/BVH_9845-5x4/index.html`) so that the slider's info button links (`{id}/`) resolve correctly. Static assets (`css/`, `js/`) and image files should also be copied into `public/`.

## Template Context

`generate.py` merges `config.json` (site-level settings like stylesheet/script paths) with `gallery.json` (site title, gallery metadata, images array). After merging, it pops `gallery` and `images` out of `site` so templates receive three top-level variables:
- `site` — merged site settings (`title`, `stylesheet`, `script`)
- `gallery` — gallery metadata (`title`)
- `images` — the ordered image list (each has `id`, `filename`, `title`, `description`, EXIF fields, etc.)

## Key Design Decisions

- The slider opens/closes purely via CSS `:target` — `body:has(.slider :target)` shows the overlay. JavaScript only handles scrolling, keyboard nav, and focus.
- Images are referenced by `id` (e.g., `BVH_9845-5x4`) which serves as both the URL hash fragment and the output subdirectory name.
- Image source files live in `images/` (gitignored) alongside `gallery.json`. The generator copies each image into its `public/{id}/` subdirectory.
- Both `images/` and `public/` are gitignored. The repo tracks only templates, static assets, config, and the generator script.
