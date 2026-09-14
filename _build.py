#!/usr/bin/env python3
"""
Generates the static site into the repo root.
Run:  python3 _build.py
Edit the PAGES dict below (or the body files) and re-run to regenerate.
Every path is relative, so the site works at a domain root, in a /repo/
subfolder on GitHub Pages, or opened straight off your hard drive.
"""
import os, re, pathlib

ROOT = pathlib.Path(__file__).parent
SITE_NAME   = "Keith James II"
SITE_TAG    = "Author of Kinesthoria"
YEAR        = 2026

NAV = [
    ("",            "Home"),
    ("kinesthoria", "Kinesthoria"),
    ("world",       "The World"),
    ("webtoon",     "Webtoon"),
    ("about",       "About"),
    ("news",        "News"),
    ("contact",     "Contact"),
]

SPOKES = '''<svg class="hero__spokes" viewBox="0 0 400 400" aria-hidden="true" focusable="false">
  <g fill="none" stroke="#c8963e" stroke-width="1.1">
    <circle cx="200" cy="200" r="196"/><circle cx="200" cy="200" r="178"/>
    <circle cx="200" cy="200" r="52"/><circle cx="200" cy="200" r="30"/>
    <circle cx="200" cy="200" r="9" fill="#c8963e"/>
    {spokes}
  </g>
</svg>'''
import math
_sp = "".join(
    '<line x1="200" y1="200" x2="{:.1f}" y2="{:.1f}"/>'.format(
        200 + 178 * math.cos(math.radians(a)),
        200 + 178 * math.sin(math.radians(a)))
    for a in range(0, 360, 15)
)
SPOKES = SPOKES.format(spokes=_sp)

FAVICON = ("data:image/svg+xml,"
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
  "%3Crect width='32' height='32' fill='%2314161c'/%3E"
  "%3Cg fill='none' stroke='%23c8963e' stroke-width='1.6'%3E"
  "%3Ccircle cx='16' cy='16' r='11'/%3E%3Ccircle cx='16' cy='16' r='3'/%3E"
  "%3Cpath d='M16 5v22M5 16h22M8.2 8.2l15.6 15.6M23.8 8.2L8.2 23.8'/%3E"
  "%3C/g%3E%3C/svg%3E")

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{favicon}">
<link rel="stylesheet" href="{p}assets/css/main.css">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{p}assets/fonts/alfa-slab-one-latin-400-normal.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="{p}assets/fonts/inter-latin-400-normal.woff2">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}">{site_name}</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">&#9776;</button>
    <nav class="nav" id="nav">{nav}</nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div style="max-width:340px">
        <p style="font-family:var(--serif);font-weight:700;font-size:1.2rem;color:var(--bone);margin-bottom:.4em">{site_name}</p>
        <p>{site_tag}, a post-apocalyptic novel of the One Land.<br><em style="color:var(--brass)">Movement is Life, Motion is Power.</em></p>
      </div>
      <div>
        <p class="eyebrow" style="margin-bottom:.7rem">Explore</p>
        <ul class="footer-nav">{fnav}</ul>
      </div>
      <div>
        <p class="eyebrow" style="margin-bottom:.7rem">Elsewhere</p>
        <ul class="footer-nav">
          <li><a href="{amazon}">Kinesthoria on Amazon</a></li>
          <li><a href="{p}contact/">Rights &amp; press</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">&copy; {year} {site_name}. All rights reserved.</p>
  </div>
</footer>

<script>
(function () {{
  var b = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  if (!b || !n) return;
  b.addEventListener('click', function () {{
    var open = n.classList.toggle('is-open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
}})();
</script>
</body>
</html>
"""

AMAZON = "https://www.amazon.com/dp/B0HHY83GPY"

def render(slug, title, desc, body, ogtype="website"):
    depth = 0 if slug == "" else slug.count("/") + 1
    p = "../" * depth if depth else "./"
    nav = "".join(
        '<a href="{}{}"{}>{}</a>'.format(
            p, (s + "/" if s else ""),
            ' aria-current="page"' if s == slug else "", label)
        for s, label in NAV)
    fnav = "".join(
        '<li><a href="{}{}">{}</a></li>'.format(p, (s + "/" if s else ""), label)
        for s, label in NAV if s)
    html = SHELL.format(
        title=title, desc=desc, ogtype=ogtype, favicon=FAVICON, p=p,
        site_name=SITE_NAME, site_tag=SITE_TAG, nav=nav, fnav=fnav,
        body=body.replace("{p}", p).replace("{spokes}", SPOKES).replace("{amazon}", AMAZON),
        year=YEAR, amazon=AMAZON)
    out = ROOT / (slug + "/index.html" if slug else "index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out

if __name__ == "__main__":
    import pages
    made = [render(*args) for args in pages.PAGES]
    for m in made:
        print("wrote", m.relative_to(ROOT))
