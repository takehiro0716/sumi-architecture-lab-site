# -*- coding: utf-8 -*-
from build_details import PROJECTS, ICONS

works = [p for p in PROJECTS if p['cat'] == 'works']
proposals = [p for p in PROJECTS if p['cat'] == 'proposals']


def page_href(p):
    return f"pages/{p['cat']}/{p['slug']}.html"


def root_photo(p):
    # index.html lives at the project root, one level above assets/
    return p['photos'][0].replace('../../', '')


def work_slide(p, idx, total):
    return f"""
      <a class="slide reveal" href="{page_href(p)}">
        <img src="{root_photo(p)}" alt="{p['title']}（{p['loc']}）" />
        <div class="slide-caption">
          <p class="slide-title">{p['title']}</p>
          <p class="slide-meta">{p['loc']} ／ {p['sub']}</p>
        </div>
        <span class="slide-index">{idx:02d} / {total}</span>
      </a>
"""


def proposal_slide(p):
    return f"""
      <a class="slide proposal reveal" href="{page_href(p)}">
        <img src="{root_photo(p)}" alt="{p['title']}（{p['loc']}）" />
        <div class="slide-caption">
          <span class="proposal-tag">PROPOSAL</span>
          <p class="slide-title">{p['title']}</p>
          <p class="slide-meta">{p['loc']}</p>
        </div>
      </a>
"""


works_html = "".join(work_slide(p, i + 1, len(works)) for i, p in enumerate(works))
proposals_html = "".join(proposal_slide(p) for p in proposals)

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>角建築研究室 | SUMI ARCHITECTURE LAB</title>
<meta name="description" content="福岡・大橋を拠点とする一級建築士事務所、角建築研究室（代表：角大輔）の作品集。新築・リノベーションの設計実績と提案作品を紹介します。" />
<link rel="stylesheet" href="assets/css/base.css" />
<link rel="stylesheet" href="assets/css/theme-dark.css" />
<link rel="stylesheet" href="assets/css/home.css" />
</head>
<body>

  <header class="site-header" id="siteHeader">
    <a href="index.html" class="wordmark">
      <span class="ja">角建築研究室</span>
      <span class="en">SUMI ARCHITECTURE LAB</span>
    </a>
    <div class="header-right">
      <nav class="site-nav" id="siteNav">
        <a href="#works">WORKS</a>
        <a href="#proposals">PROPOSALS</a>
      </nav>
      <nav class="icon-nav" aria-label="ページ移動">
        <a class="icon-btn is-active" href="index.html" aria-label="WORKS（トップ）" title="WORKS">{ICONS['home']}</a>
        <a class="icon-btn" href="profile.html" aria-label="PROFILE" title="PROFILE">{ICONS['profile']}</a>
        <a class="icon-btn" href="contact.html" aria-label="CONTACT" title="CONTACT">{ICONS['contact']}</a>
      </nav>
    </div>
  </header>

  <main id="top">

    <div id="works">
{works_html}
    </div>

    <div id="proposals">

      <div class="section-intro reveal">
        <span class="eyebrow">PROPOSALS — 提案・コンペティション</span>
        <h2>設計競技・プロポーザルへの提案</h2>
      </div>
{proposals_html}
    </div>

  </main>

  <footer>
    <div class="footer-row">
      <span>&copy; 角建築研究室 SUMI ARCHITECTURE LAB</span>
      <span><a href="#top">TOP へ戻る</a></span>
    </div>
  </footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

import os
print('works:', len(works), 'proposals:', len(proposals))
print('index.html size:', os.path.getsize('index.html'), 'bytes')
