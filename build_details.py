# -*- coding: utf-8 -*-
import os

ICONS = {
    'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="1.5"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="M3.5 16.5l5-5 4 4 3-3 5.5 5.5"/></svg>',
    'profile': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.5-4 4.5-6 7.5-6s6 2 7.5 6"/></svg>',
    'contact': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="M3.5 6.5l8.5 7 8.5-7"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}

# PROJECTS: the single source of truth for every work/proposal.
# `photos` is filled in below from assets/images/<cat>/<slug>/*.jpg
PROJECTS = [
    dict(cat='works', slug='yufuin-villa', title='YUFUIN VILLA', sub='由布院別荘', loc='大分県由布市',
         specs=[('敷地','大分県由布市'), ('構造','木造'), ('種別','新築'), ('用途','別荘'),
                ('設計','(株)環・設計工房 + 角建築研究室'), ('施工','(株)平野工務店'), ('竣工','2024.2'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['由布岳を望む敷地に、生活の場となるプライベート棟とゲストや近隣との交流を育むコミュニティ棟を分散配置した。',
                  '外壁は杉板の草木染め、由布岳への軸線に面する腰壁は自然石張りとし、時間をかけて由布院の風景に溶け込むことを意図した。']),
    dict(cat='works', slug='ohkusu-jukyo', title='大楠の住居', sub='マンションリノベーション', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('設計','角建築研究室'), ('施工','(株)イクスワークス'), ('竣工','2025.3'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['築52年のマンション一室を、和を基調とした一室空間へと再構成したリノベーション。',
                  '天井高を1780mmから2350mmのあいだで揺らし、立つ・座る・畳に座すといった姿勢ごとに変わる視線の高さを設計の軸に据えた。',
                  '障子越しに差し込む光が曲面天井に反射し、時間の移ろいを室内の表情として映し出す。']),
    dict(cat='works', slug='o-clinic', title='O CLINIC', sub='診療所併用住宅', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','鉄骨造'), ('種別','新築'), ('用途','診療所併用住宅'),
                ('設計','大石和彦建築アトリエ + 角建築研究室'), ('施工','半田建設(株)'), ('竣工','2023.4'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['診療所と住宅をひとつの敷地に併設した新築計画。大石和彦建築アトリエとの共同設計。']),
    dict(cat='works', slug='sakuragaoka-jukyo-1', title='桜ヶ丘の住居', sub='集合住宅リノベーション', loc='福岡県春日市',
         specs=[('敷地','福岡県春日市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('施工','(株)イクスワークス'), ('竣工','2021.12'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['福岡県春日市、桜ヶ丘の集合住宅一室をリノベーション。木質のしつらえで暮らしに寄り添う住空間へと更新した。']),
    dict(cat='works', slug='imaizumi-jukyo', title='今泉の住居', sub='フルリノベーション', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('施工','株式会社ジューテック'), ('竣工','2020.12'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['子どもの独立を機に、夫婦2人のための3LDKを2LDKへとフルリノベーション。',
                  '高さを操作した造作家具で視線を緩やかに制御し、壁で仕切らず互いの気配が伝わる住空間を目指した。']),
    dict(cat='works', slug='saga-yamato-jutaku', title='佐賀大和の住宅 Ⅰ', sub='新築住宅', loc='佐賀県佐賀市',
         specs=[('敷地','佐賀県佐賀市'), ('構造','木造2階建'), ('種別','新築'), ('用途','住宅'),
                ('施工','(株)鳥飼建設'), ('竣工','2020.08'), ('写真','Yusuke Nakamura / graphy')],
         concept=['佐賀市大和町に建つ木造2階建ての新築住宅。']),
    dict(cat='works', slug='rakuichi-apartment', title='楽市のアパートメント', sub='賃貸集合住宅', loc='福岡県飯塚市',
         specs=[('敷地','福岡県飯塚市'), ('構造','木造2階建'), ('種別','新築'), ('用途','共同住宅'),
                ('施工','(株)春田建設'), ('竣工','2019.07'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['10戸の賃貸住戸からなる木造メゾネットアパート。既製ディテールを積極的に採用してコストを抑えながら、細分化した住戸のあいだに路地・中庭・ポーチを生み出した。',
                  '日常的に使われる外部空間を目指し、集まって住むことの豊かさを形にした計画。']),
    dict(cat='works', slug='irodori-seikotsuin-jutaku', title='いろどり整骨院 / 住宅', sub='整骨院併用住宅リノベーション', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','軽量鉄骨造（型式適合認定）'), ('種別','改修'), ('用途','整骨院併用住宅'),
                ('設計','NOTEQUAL + 角建築研究室'), ('施工','(株)イクスワークス'), ('竣工','2020.06'), ('写真','Yousuke Harigane / 針金建築写真事務所')],
         concept=['整骨院と住宅を併設したリノベーション。NOTEQUALとの共同設計により、施術の場と暮らしの場をひとつの建物のなかに共存させた。']),
    dict(cat='works', slug='inherit', title='INHERIT', sub='美容室リノベーション', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','RC造3階建'), ('種別','改修'), ('用途','美容室'),
                ('施工','デコール田中'), ('竣工','2018.5'), ('写真','© DAISUKE SUMI')],
         concept=['築50年、ブライダル店舗を経て美容室へと用途を重ねてきたRC3階建てのリノベーション。',
                  '既存躯体に残る白壁とコンクリートの水平の境界線を建物のエッセンスとして継承し、新規の壁と造作家具でこのルールを拡張した。']),
    dict(cat='works', slug='anally-house', title='諏訪野町の住宅', sub='専用住宅', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('種別','新築'), ('用途','専用住宅'), ('構造設計','黒岩構造設計事務所'),
                ('施工','筑羽工務店'), ('竣工','2013'), ('写真','Kouji Okamoto / Techni Staff'), ('備考','大石和彦建築アトリエ在籍時に設計')],
         concept=['西鉄久留米駅から歩ける、2m幅の路地が何本も通る街区の端に建つ住宅。大石和彦建築アトリエ在籍時の設計。',
                  '路地が持つ身近な生活感を手がかりに、屋根のある外部的インナースペースを住まいに組み込んだ。']),
    dict(cat='works', slug='tenjin-hairmake-am', title='hair make am', sub='サイン計画・スクリーンデザイン', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('用途','美容室サイン・ロールスクリーン'), ('プロデュース','フォルツァ(株)'),
                ('施工','(有)ノーサイド'), ('写真','© DAISUKE SUMI')],
         concept=['福岡市中央区・西通りに面する美容室のサイン計画とロールスクリーンをデザイン。',
                  '通りに並ぶトチノキをモチーフに、夏は葉陰が店を隠し、冬は枝だけが残り輪郭が現れる、季節で表情を変える皮膜を考えた。']),
    dict(cat='works', slug='kurashi-no-nomi-ichi', title='クラシノノミノイチ vol.05', sub='イベント空間構成', loc='福岡県福岡市',
         specs=[('場所','福岡県福岡市（護国神社）'), ('主催','フォルツァ(株)'), ('開催','2017年5月'), ('用途','イベント')],
         concept=['護国神社で開催される蚤の市「クラシノノミノイチ」の一角で、企画・運営・空間構成を担当。',
                  '黄色いカラーコーンと構造用合板だけで組み立てられる簡易テーブルを考案し、建築家による作品を並べる会場をつくった。']),
    dict(cat='proposals', slug='aoishi-no-oka', title='青石の丘', sub='保育園・児童センターの提案', loc='愛媛県八幡浜市',
         specs=[('敷地','愛媛県八幡浜市'), ('構造','鉄骨造2階建'), ('用途','保育園・児童センター'), ('竣工','unbuild')],
         concept=['保育園と児童センターを併設する提案計画。']),
    dict(cat='proposals', slug='iizuka-apartment', title='飯塚のアパートメント', sub='木造長屋の提案', loc='福岡県飯塚市',
         specs=[('敷地','福岡県飯塚市'), ('構造','木造2階建'), ('用途','長屋'), ('竣工','unbuild')],
         concept=['木造2階建ての長屋形式による賃貸集合住宅の提案。']),
    dict(cat='proposals', slug='ohashi18-5', title='大島18.5', sub='交流拠点の提案', loc='愛媛県八幡浜市大島',
         specs=[('敷地','愛媛県八幡浜市大島'), ('構造','木造平屋'), ('用途','集会所'), ('竣工','unbuild')],
         concept=['大島の玄関口にふさわしい、島民と観光客をつなぐ「LDK」のような交流拠点の提案。',
                  '敷地幅いっぱいに延びるひとつのテーブルの上に島民と観光客それぞれの行為が並び、大島の新しいシンボルとなることを目指した。']),
    dict(cat='proposals', slug='oki-tsunagu-fukei', title='隠岐の暮らし つなぐ風景', sub='ターミナル周辺計画', loc='島根県隠岐の島',
         specs=[('敷地','島根県隠岐の島'), ('構造','鉄筋コンクリート造（一部木造）'), ('用途','ターミナル周辺計画'), ('竣工','unbuild')],
         concept=['隠岐の島のフェリーターミナル周辺を対象とした計画提案。']),
    dict(cat='proposals', slug='otsu-jutaku', title='大津の住宅', sub='木造平家住宅の提案', loc='滋賀県大津市',
         specs=[('敷地','滋賀県大津市'), ('構造','木造平家'), ('用途','住宅'), ('竣工','unbuild')],
         concept=['滋賀県大津市に計画した木造平家住宅の提案。']),
    dict(cat='proposals', slug='yane-no-gunkei', title='屋根の群景', sub='木造住宅の提案', loc='愛媛県西条市',
         specs=[('敷地','愛媛県西条市'), ('構造','木造2階'), ('用途','住宅'), ('竣工','unbuild')],
         concept=['愛媛県西条市に計画した木造2階建て住宅の提案。']),
]

for p in PROJECTS:
    photo_dir = os.path.join('assets', 'images', p['cat'], p['slug'])
    files = sorted(os.listdir(photo_dir))
    # store paths relative to a pages/<cat>/ page: ../../assets/images/<cat>/<slug>/NN.jpg
    p['photos'] = [f'../../assets/images/{p["cat"]}/{p["slug"]}/{f}' for f in files]
    p['outpath'] = os.path.join('pages', p['cat'], f'{p["slug"]}.html')


def header_html(active=None):
    def cls(name):
        return ' is-active' if active == name else ''
    return f"""
  <header class="site-header" id="siteHeader">
    <a href="../../index.html" class="wordmark">
      <span class="ja">角建築研究室</span>
      <span class="en">SUMI ARCHITECTURE LAB</span>
    </a>
    <nav class="icon-nav" aria-label="ページ移動">
      <a class="icon-btn{cls('home')}" href="../../index.html" aria-label="WORKS（トップ）" title="WORKS">{ICONS['home']}</a>
      <a class="icon-btn{cls('profile')}" href="../../profile.html" aria-label="PROFILE" title="PROFILE">{ICONS['profile']}</a>
      <a class="icon-btn{cls('contact')}" href="../../contact.html" aria-label="CONTACT" title="CONTACT">{ICONS['contact']}</a>
    </nav>
  </header>
"""


def gallery_html(photos):
    rest = photos[1:]
    if not rest:
        return ""
    rows_html = []
    i = 0
    while i < len(rest):
        chunk = rest[i:i + 2]
        cls = "gallery-row two" if len(chunk) == 2 else "gallery-row"
        frames = "".join(
            f'<div class="gallery-frame reveal"><img src="{src}" alt="" loading="lazy" /></div>'
            for src in chunk
        )
        rows_html.append(f'<div class="{cls}">{frames}</div>')
        i += 2
    return f'<section class="gallery">{"".join(rows_html)}</section>'


def spec_html(specs):
    rows = "".join(f'<div class="spec-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in specs)
    return f'<dl class="spec-table reveal" style="--d:1">{rows}</dl>'


def build_page(p, next_p):
    tag = "UNBUILT / 提案" if p['cat'] == 'proposals' else p['sub']
    concept_html = "".join(f"<p>{line}</p>" for line in p['concept'])
    next_tag = "NEXT PROPOSAL" if next_p['cat'] == 'proposals' else "NEXT WORK"
    next_href = f"../{next_p['cat']}/{next_p['slug']}.html" if next_p['cat'] != p['cat'] else f"{next_p['slug']}.html"

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{p['title']} | 角建築研究室 SUMI ARCHITECTURE LAB</title>
<meta name="description" content="{p['title']}（{p['loc']}）— 角建築研究室の作品紹介ページ。" />
<link rel="stylesheet" href="../../assets/css/base.css" />
<link rel="stylesheet" href="../../assets/css/theme-dark.css" />
<link rel="stylesheet" href="../../assets/css/detail.css" />
</head>
<body>
{header_html()}
  <main>
    <div class="hero">
      <img src="{p['photos'][0]}" alt="{p['title']}（{p['loc']}）" />
      <div class="hero-caption">
        <span class="hero-tag">{tag}</span>
        <h1 class="hero-title">{p['title']}</h1>
        <p class="hero-sub">{p['sub']} ／ {p['loc']}</p>
      </div>
    </div>

    <section class="detail-body wrap">
      <span class="eyebrow reveal">CONCEPT</span>
      <div class="concept reveal" style="--d:1">{concept_html}</div>
      {spec_html(p['specs'])}
    </section>

    {gallery_html(p['photos'])}

    <a class="next" href="{next_href}">
      <img src="{next_p['photos'][0]}" alt="" />
      <div class="next-inner">
        <span class="next-eyebrow">{next_tag}{ICONS['arrow']}</span>
        <p class="next-title">{next_p['title']}</p>
        <p class="next-sub">{next_p['sub']} ／ {next_p['loc']}</p>
      </div>
    </a>
  </main>

  <footer>
    <div class="footer-row">
      <span>&copy; 角建築研究室 SUMI ARCHITECTURE LAB</span>
      <span><a href="../../index.html">WORKS へ戻る</a></span>
    </div>
  </footer>

<script src="../../assets/js/main.js"></script>
</body>
</html>
"""


def main():
    os.makedirs('pages/works', exist_ok=True)
    os.makedirs('pages/proposals', exist_ok=True)
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        next_p = PROJECTS[(i + 1) % n]
        html = build_page(p, next_p)
        with open(p['outpath'], 'w', encoding='utf-8') as f:
            f.write(html)
        print(p['outpath'])


if __name__ == '__main__':
    main()
