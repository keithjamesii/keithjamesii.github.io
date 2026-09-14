# keithjamesii.github.io

Author site for Keith James II. Home of *Kinesthoria: The Weight of Wheels*,
a novel of the One Land.

> Movement is Life, Motion is Power.

## How this works

Plain static HTML and CSS. No build tools, no dependencies, no npm. GitHub Pages
serves the files exactly as they sit in this repo.

```
index.html            home
kinesthoria/          the book
world/                worldbuilding
webtoon/              adaptation + art
about/                author bio
news/                 updates
contact/              contact + press
assets/css/main.css   all styling
assets/fonts/         self-hosted woff2 (Alfa Slab One, Bitter, Inter, IBM Plex Mono)
assets/img/           cover.jpg, author.jpg, webtoon art
404.html              not-found page
```

## Editing

Two ways, pick whichever you prefer.

**Direct.** Open any `index.html` on GitHub, click the pencil, change the text,
commit. The site updates in about a minute. Look for `EDIT-ME` comments — they
mark every spot holding placeholder copy.

**Regenerate.** All copy lives in `pages.py`; the page shell (header, nav,
footer, meta tags) lives in `_build.py`. Edit `pages.py`, run `python3 _build.py`,
and every page is rewritten with consistent navigation. Requires Python 3, nothing else.

## Adding images

Drop files into `assets/img/`, then replace the placeholder `<div>` with an
`<img>`. Each placeholder has the exact replacement line in a comment above it.

Cover art: 1000px wide or more, JPG. Author photo: 800px wide, JPG.


## Where the design came from

Palette and type are sampled from the printed cover: background `#110c06`,
headline orange `#d07a3a`, body cream `#e8dcc6`, sage rule `#a9bf92`.
Display face is Alfa Slab One, headings Bitter, body Inter.

Fonts are self-hosted in `assets/fonts/` rather than loaded from Google — one
fewer third-party request, and the page renders correctly on networks that
block font CDNs.

`assets/img/cover.jpg` is the front panel extracted from the paperback wrap PDF
at 400 dpi. Re-extract from the print file if the cover is ever revised.
