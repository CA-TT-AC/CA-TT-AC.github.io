# Jing Xu - Academic homepage

A lightweight static academic homepage. Structure follows https://vicayang.cc/ with the original white, serif-and-blue visual direction. Only publicly released papers appear: 11 papers, each with its original paper figure. No Projects section.

## Preview

Run `python scripts/build.py`, then `python -m http.server 8765 --bind 127.0.0.1` and open http://127.0.0.1:8765. The generated index.html also works directly. No npm or Jekyll installation is needed.

## Maintain

- content/resume.json: public papers, full authors, statuses, figure filenames, resource links, education, experience, awards.
- scripts/build.py: HTML generator, biography, service entries.
- assets/homepage.css and assets/homepage.js: presentation and progressively enhanced filters.
- assets/media/: original research figures and portrait.
- The CV is maintained separately and is not linked or bundled with the homepage.

After editing, run `python scripts/build.py`. Do not place private manuscripts or unreleased figures in the website.

## Deployment status

The homepage is published from the master branch. Root index.html plus .nojekyll supports branch-based GitHub Pages hosting. Confirm the Pages source branch/folder when deployment is requested. Legacy Jekyll files remain for reference and are not used by the new homepage. Old /about/, /publications/, /cv/ and /portfolio/ bookmarks redirect to new sections.

## Verification

Playwright with local Chrome (Browser plugin unavailable): 1440, 768, 390 and 320 px; filters (11 total, 7 published, 4 arXiv), local links, images, no horizontal overflow, no console errors, and full content without JavaScript. Desktop/mobile screenshots visually reviewed. Source figures recorded in ASSET_SOURCES.md.
