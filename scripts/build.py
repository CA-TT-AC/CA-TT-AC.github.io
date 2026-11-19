"""Build the homepage with Python's standard library: python scripts/build.py."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'content/resume.json').read_text(encoding='utf-8'))
e = escape
arrow = '<svg aria-hidden="true" viewBox="0 0 24 24" class="arrow"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'
def link(url, label, cls=''):
    return f'<a class="{cls}" href="{e(url,quote=True)}">{e(label)}{arrow}</a>'
def authors(names, corresponding):
    rendered=e(names).replace('Jing Xu','<strong>Jing Xu</strong>').replace('*','<sup>*</sup>')
    for name in corresponding:
        rendered=rendered.replace(e(name),e(name)+'<sup class="corresponding" aria-label="corresponding author">&#9993;</sup>')
    return rendered
papers=[]
for i,p in enumerate(data['publications']):
    pid=f'paper-{i+1}'
    resources=''.join(link(l['url'],l['label'],'resource') for l in p['links'])
    image=f'<a class="paper-image" href="{e(p["links"][0]["url"])}" aria-label="Read {e(p["title"])}"><img src="assets/media/{p["image"]}" alt="Research figure from {e(p["title"])}" loading="lazy" decoding="async"></a>'
    if p.get('image'): image=f'<div class="paper-figure">{image}</div>'
    else: image=''
    distinction=f'<strong class="paper-distinction">{e(p["distinction"])}</strong>' if p.get('distinction') else ''
    papers.append(f'<article class="paper {"paper-text-only" if not p.get("image") else ""}" id="{pid}" data-category="{p["category"]}">{image}<div class="paper-main"><h3><a href="{e(p["links"][0]["url"])}">{e(p["title"])}</a></h3><p class="authors">{authors(p["authors"],p.get("corresponding",[]))}</p><p class="venue">{e(p["venue"])} <span class="paper-year">{e(p["date"].split(".")[0])}</span>{distinction}</p><div class="resources">{resources}</div></div></article>')
def timeline(items):
    return '<ol class="timeline">'+''.join(f'<li><span class="date">{e(x["date"])}</span><h4>{e(x["title"])}</h4><p class="organization">{e(x["org"])}</p><p class="detail">{e(x["detail"])}</p></li>' for x in items)+'</ol>'
awards=''.join(f'<li><span class="date">{e(a["date"])}</span><div>{e(a["title"])}<strong>{e(a["result"])}</strong></div></li>' for a in data['awards'])
html='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jing Xu | Multimodal Learning &amp; Visualization</title>
<meta name="description" content="Jing Xu is a Ph.D. candidate in Data Science and Analytics at HKUST (Guangzhou), working on multimodal learning, visualization, and interactive visual tools.">
<meta name="theme-color" content="#faf8fd"><link rel="canonical" href="https://ca-tt-ac.github.io/">
<meta property="og:title" content="Jing Xu — Research &amp; Publications"><meta property="og:description" content="Multimodal learning and human-centered visual tools. Publications, education, and academic service."><meta property="og:type" content="website"><meta property="og:url" content="https://ca-tt-ac.github.io/"><meta property="og:image" content="https://ca-tt-ac.github.io/assets/media/jing-xu-scholar.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/homepage.css?v=20261119-purple-v2"><script src="assets/homepage.js" defer></script>
</head><body id="top"><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a href="#top" class="wordmark">Jing Xu<span lang="zh">徐敬</span></a><nav aria-label="Main navigation"><a href="#about">About</a><a href="#publications">Publications</a><a href="#background">Background</a><a href="#awards">Awards</a><a href="#service">Service</a></nav></div></header>
<main id="main" class="container"><section class="hero" id="about" aria-labelledby="name"><div class="intro"><h1 id="name">Jing Xu<span lang="zh">徐敬</span></h1><p class="research-line">Multimodal learning.<br>Human-centered visual tools.</p><div class="bio"><p>I am a Ph.D. candidate in <a href="https://dsa.hkust-gz.edu.cn/">Data Science and Analytics</a> at the Hong Kong University of Science and Technology (Guangzhou), advised by <a href="https://vicayang.cc/">Prof. Weikai Yang</a>. I received my bachelor’s degree in Artificial Intelligence from Nanjing University of Aeronautics and Astronautics (NUAA) in 2025, where I conducted research under the supervision of <a href="https://i2-multimedia-lab.github.io/publications.html">Prof. Pan Gao</a>.</p><p>I spent a wonderful few months at the University of Edinburgh as an exchange student in 2023, under the supervision of <a href="https://enigma-li.github.io/">Prof. Changjian Li</a>.</p><p>I develop AI algorithms and build interactive systems for understanding, creating, and editing visual content. My research interests span multimodal learning, computer vision, and human–AI interaction, with a focus on visual understanding and authoring.</p></div><div class="social-links"><a href="mailto:jing.xu@connect.hkust-gz.edu.cn">Email ↗</a><a href="https://scholar.google.com/citations?user=4_2m0_YAAAAJ&amp;hl=en">Google Scholar ↗</a><a href="https://github.com/CA-TT-AC">GitHub ↗</a></div></div><figure class="portrait"><img src="assets/media/jing-xu-scholar.jpg" width="256" height="256" alt="Jing Xu" fetchpriority="high"><figcaption>Ph.D. Candidate<br>HKUST (Guangzhou)</figcaption></figure></section>
<section id="publications" class="section" aria-labelledby="publications-title"><div class="section-heading publications-heading"><h2 id="publications-title">Publications</h2><div class="filters" role="group" aria-label="Filter publications" hidden><button type="button" data-filter="all" aria-pressed="true">All</button><button type="button" data-filter="published" aria-pressed="false">Published</button><button type="button" data-filter="preprint" aria-pressed="false">arXiv</button></div></div><p class="publication-note"><sup>*</sup> Equal contribution. <span class="corresponding-legend">&#9993; Corresponding author.</span> <span id="publication-count" role="status" aria-live="polite">11 papers</span></p><div class="paper-list">PAPERS</div></section>
<section id="background" class="section" aria-labelledby="background-title"><div class="section-heading"><h2 id="background-title">Background</h2></div><div class="background-grid"><div><h3>Education</h3>EDUCATION</div><div><h3>Experience</h3>EXPERIENCE</div></div></section>
<section id="awards" class="section" aria-labelledby="awards-title"><div class="section-heading"><h2 id="awards-title">Selected Awards</h2></div><ul class="award-list">AWARDS</ul></section>
<section id="service" class="section" aria-labelledby="service-title"><div class="section-heading"><h2 id="service-title">Academic Service</h2></div><div class="service-grid"><h3>Reviewer</h3><ul><li>IEEE Visualization and Visual Analytics Conference (IEEE VIS) <span>2026</span></li><li>ACM Multimedia <span>2026</span></li><li>IEEE Transactions on Emerging Topics in Computational Intelligence <span>2024</span></li><li>IEEE International Conference on Robotics and Automation <span>2024</span></li><li>CAAI International Conference on Artificial Intelligence <span>2023</span></li></ul></div></section>
</main><footer class="container"><a href="mailto:jing.xu@connect.hkust-gz.edu.cn">jing.xu@connect.hkust-gz.edu.cn</a><span>© 2026 Jing Xu</span><a href="#top">Back to top ↑</a></footer></body></html>'''
for marker,value in [('PAPERS',''.join(papers)),('EDUCATION',timeline(data['education'])),('EXPERIENCE',timeline(data['experience'])),('AWARDS',awards)]: html=html.replace(marker,value)
(ROOT/'index.html').write_text(html,encoding='utf-8')
(ROOT/'.nojekyll').touch()
# Preserve useful legacy bookmarks without serving obsolete profile content.
for path,target in [('about','about'),('publications','publications'),('cv','background'),('portfolio','publications')]:
    folder=ROOT/path;folder.mkdir(exist_ok=True)
    (folder/'index.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><title>Jing Xu</title><meta http-equiv="refresh" content="0;url=../#{target}"><a href="../#{target}">Continue to Jing Xu\'s homepage</a></html>',encoding='utf-8')
print('Built static homepage:',len(data['publications']),'papers')
