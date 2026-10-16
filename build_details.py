# -*- coding: utf-8 -*-
import os

ICONS = {
    'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5 12 4l8 6.5"/><rect x="5.5" y="10.5" width="13" height="9" rx="1"/><path d="M10 19.5v-5h4v5"/></svg>',
    'blog': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3.5h8l4 4v13a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1v-16a1 1 0 0 1 1-1z"/><path d="M14 3.5v4h4"/><path d="M8 12.5h8M8 16h8M8 9h3"/></svg>',
    'profile': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.5-4 4.5-6 7.5-6s6 2 7.5 6"/></svg>',
    'contact': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="M3.5 6.5l8.5 7 8.5-7"/></svg>',
    'instagram': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="0.8" fill="currentColor" stroke="none"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}

INSTAGRAM_URL = 'https://www.instagram.com/sumi.architecture.lab/'

NAV_TOGGLE = '''<button type="button" class="nav-toggle" aria-expanded="false" aria-label="メニューを開く">
      <svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>'''

# PROJECTS: the single source of truth for every work/proposal.
# `photos` is filled in below from assets/images/<cat>/<slug>/*.jpg
PROJECTS = [
    dict(cat='works', slug='yufuin-villa', title='YUFUIN VILLA', sub='由布院別荘', loc='大分県由布市',
         specs=[('敷地','大分県由布市'), ('構造','木造'), ('種別','新築'), ('用途','別荘'),
                ('設計','(株)環・設計工房 + 角建築研究室'), ('外構','ランドスケープムラ(株)'), ('照明','B&Lighting'),
                ('設備','(株)総合設備計画'), ('施工','(株)平野工務店'), ('竣工','2024.2'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['九州の避暑地として賑わう由布院の地域特性は、シンボルとしての由布岳／外部からの観光客やマーケットの参入／地元(ムラ)ネットワークの強さなどがあげられる。',
                  'YUFUIN VILLAは、賑わいのある湯の坪街道から大分川を渡った静けさのある場所に位置する。',
                  '居住空間を機能性が異なる4つの棟に分散し、施主家族の主な生活空間となるプライベート棟(A、B)と、ゆとりを持たせた空間で家族・ゲストとの交流を育む場となるコミュニティ棟(A)、ゲストの宿泊の場・近隣住民との交流の場となるコミュニティ棟(B)とした。',
                  '近隣建物と馴染ませるため屋根形状は高さを抑えた切妻屋根にすることに加え、外壁は杉板張りの草木染とし、由布岳への軸線に面する腰壁を自然石張とした。']),
    dict(cat='works', slug='ohkusu-jukyo', title='大楠の住居', sub='マンションリノベーション', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('設計','角建築研究室'), ('施工','(株)イクスワークス'), ('竣工','2025.3'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['築52年を迎えるマンション一室のリノベーションである。',
                  '２DKの住戸を施主の要望であった和を基調とする一室空間に変換し、生活機能を玄関付近にコンパクトに集約しながら、住まい全体を回遊できる動線を確保した。',
                  '多くの友人が訪れることもあり、壁で空間を細かく区切らず、生活における出来事を水平方向に展開できる自由度の高い一室空間を目指した。',
                  '畳による床座を基本とする暮らしで長い時間を過ごす住まい手にとって、天井高は空間心理に大きく作用することが想定される。',
                  'そこで、立位・座位・椅子座といった姿勢によって変化する天井までの距離及び生活場面における視線の高さの推移を計画のテーマに設定し、空間スケールの調整を丁寧に行った。',
                  '天井高さは最高2350mmから最低1780mmのあいだを揺れ動き、平均天井高2100mmを確保しながら、柔らかな曲線で抑揚を与え一体的に生活を包み込む形状とした。',
                  'シナ合板を曲面で仕上げ、光沢のある塗装を施し、間接照明の反射光のみで照度を得る柔らかな光環境をつくり出している。',
                  '一室空間のなかで天井高の変化が場の境界を暗示し、自然な切り替えを生む。',
                  'その境界によって、住空間を明確に分断していくのではなく、生活領域を緩やかに重ねながら、生活が水平方向に連続して展開される。',
                  '窓の正面には大きな病院が建つため、外の風景を直接取り込むのではなく、障子によって光の移ろいだけを室内に受け入れることとした。',
                  '障子越しに差し込む外光が曲面天井に反射し、時間の流れを光の表情として室内に映し出す。',
                  '外部と内部、時間と光が静かに重なり合うような心地よい住まいを目指した。']),
    dict(cat='works', slug='o-clinic', title='O CLINIC', sub='診療所併用住宅', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','鉄骨造'), ('種別','新築'), ('用途','診療所併用住宅'),
                ('設計','大石和彦建築アトリエ + 角建築研究室'), ('構造設計','黒岩構造設計事務所'), ('設備','蟻設備設計事務所'),
                ('施工','半田建設(株)'), ('竣工','2023.4'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['診療所と住宅をひとつの敷地に併設した新築計画。大石和彦建築アトリエとの共同設計。']),
    dict(cat='works', slug='sakuragaoka-jukyo-1', title='桜ヶ丘の住居', sub='集合住宅リノベーション', loc='福岡県春日市',
         specs=[('敷地','福岡県春日市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('施工','(株)イクスワークス'), ('竣工','2021.12'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['福岡県春日市、桜ヶ丘の集合住宅一室をリノベーション。木質のしつらえで暮らしに寄り添う住空間へと更新した。']),
    dict(cat='works', slug='imaizumi-jukyo', title='今泉の住居', sub='フルリノベーション', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('構造','鉄筋コンクリート造'), ('種別','改修'), ('用途','住宅'),
                ('施工','株式会社ジューテック'), ('竣工','2020.12'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['子供が独立し、夫婦2人となった3LDKの住居を2LDKへフルリノベーションを行った。',
                  'LDKはキッチンバックセットとリビング収納を兼ねた造作家具を中心とし、高さの調整を行うことで緩やかに視線の制御と接続を促すオープンな空間となっている。',
                  'ゲストスペース兼書斎は、建具を全開放することでLDKと一体的な利用が可能となり、数枚残した建具によって視線の制御を行うことも可能である。',
                  '夫婦のための居場所を点在させ、視線の制御を行いながら適度な距離感を与えた。',
                  '境界としての強く作用する壁を設けず、それぞれの気配が伝わるような接続性のある住空間を目指した。']),
    dict(cat='works', slug='saga-yamato-jutaku', title='佐賀大和の住宅 Ⅰ', sub='新築住宅', loc='佐賀県佐賀市',
         specs=[('敷地','佐賀県佐賀市'), ('構造','木造2階建'), ('種別','新築'), ('用途','住宅'),
                ('施工','(株)鳥飼建設'), ('竣工','2020.08'), ('写真','Yusuke Nakamura / graphy')],
         concept=['佐賀市大和町に建つ木造2階建ての新築住宅。']),
    dict(cat='works', slug='rakuichi-apartment', title='楽市のアパートメント', sub='賃貸集合住宅', loc='福岡県飯塚市',
         specs=[('敷地','福岡県飯塚市'), ('構造','木造2階建'), ('種別','新築'), ('用途','共同住宅'),
                ('施工','(株)春田建設'), ('竣工','2019.07'), ('写真','Kouji Okamoto / Techni Staff')],
         concept=['楽市のアパートメントは、福岡県飯塚市の幹線道路から一本入った敷地に建つ木造2階建てのメゾネット型賃貸アパートである。',
                  '10世帯の賃貸住戸をローコストの条件のもとで設計することを求められた。',
                  '不特定な入居者の入れ替わりを考慮し、造作でディテールを積み上げていくのではなく、既製品（標準ディテール）を多用しコストを抑えた。',
                  '地方都市における一般的な木造アパートと同等の建設コストにしながらも、いかに豊かな空間性を与えることができるかをテーマとした。',
                  '地方都市に点在する共同住宅・長屋は、建築を大きな1つのボリュームにまとめ、敷地の余った部分を住人の共用空間として確保する計画が多い。',
                  'また、建物先行の計画によって追いやられた共用空間は、完成後に閑散としている現状があり、常に利用されている空間とは言い難い。',
                  '本計画では、日々使われる外部空間を目指し、集まって住むための住環境の見直しを図った。',
                  '細分化した住戸ボリュームを変形敷地に沿うように配置し、建物のあいだに生じる外部空間を路地、中庭、ポーチ(上部バルコニー)として扱う。',
                  '路地は角度が与えられた住戸に挟まれることで、視線の方向性がぼかされながら幅の伸縮を繰り返す。',
                  '歩みを進めることで現れるスペースに路地が接続され、変化していく奥行は歩く豊かさを与える。',
                  'コンパクトにまとめられた各住戸は、2つの白のユニットと、その間に挟まれた黒の膜によって構成される。',
                  '白のユニットは、住戸の構造耐力を保持し、プライベート性の高い水廻りや寝室などを配置している。',
                  '黒の膜は、1階の居室に安定した光を落とすハイサイドライトを設けた吹抜を含み、密集した住戸群のなかでの住環境を補完する。',
                  '採算性が重視された一般的な木造賃貸アパートとの比較を行い、社会的なニーズを満たしながら形態・住環境改善の可能性を示した。',
                  '路地空間は、各住戸へアプローチするための通路であると同時に、密集した住戸群の住環境を改善する役割を果たしている。',
                  '点在する軒下空間は、入居者の生活の気配を感じることができる中間領域として機能し、路地空間に視覚的変化を与える。',
                  '専有部と共用部の領域が緩やかに重なり合い、入居者の個性の表出により展開される風景は、集まって住むことの豊かさになると考えている。',
                  '入居者によって彩られる外部空間がコミュニティ形成のきっかけとなることを期待している。']),
    dict(cat='works', slug='irodori-seikotsuin-jutaku', title='いろどり整骨院 / 住宅', sub='整骨院併用住宅リノベーション', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','軽量鉄骨造（型式適合認定）'), ('種別','改修'), ('用途','整骨院併用住宅'),
                ('設計','NOTEQUAL + 角建築研究室'), ('植栽','relier'), ('サイン・WEB','5ive Inc.'),
                ('施工','(株)イクスワークス'), ('竣工','2020.06'), ('写真','Yousuke Harigane / 針金建築写真事務所')],
         concept=['整骨院と住宅を併設したリノベーション。NOTEQUALとの共同設計により、施術の場と暮らしの場をひとつの建物のなかに共存させた。']),
    dict(cat='works', slug='inherit', title='INHERIT', sub='美容室リノベーション', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('構造','RC造3階建'), ('種別','改修'), ('用途','美容室'),
                ('施工','デコール田中'), ('竣工','2018.5'), ('写真','© DAISUKE SUMI')],
         concept=['福岡市久留米市内にあるRC3階建の美容室リノベーションを行った。',
                  '建築当時はブライダル店舗、そして美容室へと姿を変え、今回の美容室の姿へと50年の歳月を経て実現した。',
                  '過去の表皮を剥ぎ取ると既存躯体に高さ約1mのラインでコンクリートの腰壁が廻り、建築当初の仕上げであった白壁とコンクリート色による水平方向の境界線が広がっていた。',
                  'この境界線を建物が持つエッセンスとして捉え、今回の美容室の構成に継承し、新規壁と造作家具でこのルールを周到し拡張を行った。',
                  '黒と白の境界による風景に人が介入することにより、まるで水に浸かっているような状況が生まれる。',
                  '新しく染められた髪色が白壁に浮かび上がり、これから先の時間を歩む空間を彩らせる。']),
    dict(cat='works', slug='anally-house', title='諏訪野町の住宅', sub='専用住宅', loc='福岡県久留米市',
         specs=[('敷地','福岡県久留米市'), ('種別','新築'), ('用途','専用住宅'), ('構造設計','黒岩構造設計事務所'),
                ('施工','筑羽工務店'), ('竣工','2013'), ('写真','Kouji Okamoto / Techni Staff'), ('備考','大石和彦建築アトリエ在籍時に設計')],
         concept=['久留米市の中心部西鉄久留米駅から歩いて行けるこの場所は、2m幅の路地が東西方向に何本も通っている地域の端部に位置し、地区協定により敷地北側の2mを路地として提供しなければならないことが義務付られている。',
                  '路地に面する住宅からは各々の生活がにじみ出し、路地空間に独特な生活感を与えていた。',
                  'このような路地スペースの持つ身近感を暗喩として住宅の中に屋根のある外部的インナースペースを含んだ住まい方を提案した。',
                  '建物は1層の箱と2層の箱を路地空間(外部的インナースペース)を挟み、平行に並べ、路地空間側に開くことで様々な関係性が偶発的に起こることを期待している。',
                  'その為、1階階高を抑え2階スペースをできるだけ1階に近づけ身近感が出るような距離感と開口部の配置に注意を払い計画を行った。']),
    dict(cat='works', slug='tenjin-hairmake-am', title='hair make am', sub='サイン計画・スクリーンデザイン', loc='福岡県福岡市',
         specs=[('敷地','福岡県福岡市'), ('用途','美容室サイン・ロールスクリーン'), ('プロデュース','フォルツァ(株)'),
                ('施工','(有)ノーサイド'), ('写真','© DAISUKE SUMI')],
         concept=['福岡市中央区の西通りに面する美容室のサイン計画とロールスクリーンのデザインを行った。',
                  '西通りに並ぶトチノキは5月になるとピンク色のかわいらしい花が咲く落葉樹である。',
                  'スクリーンにはトチノキの葉をモチーフとしてデザインを行なった。',
                  '夏は生い茂った樹木に隠れ影を演出し、冬は葉が全て落ちることで枝だけが残り春の輪郭が現れる。',
                  '生きる樹木と正面に立つ建物を繋ぐための皮膜としてスクリーンのデザインを取り入れた。']),
    dict(cat='works', slug='kurashi-no-nomi-ichi', title='クラシノノミノイチ vol.05', sub='イベント空間構成', loc='福岡県福岡市',
         specs=[('場所','福岡県福岡市（護国神社）'), ('主催','フォルツァ(株)'), ('開催','2017年5月'), ('用途','イベント')],
         concept=['福岡市護国神社で行われている蚤の市の一つのブースの中で企画、運営、空間構成を担当した。',
                  '2012年から始まったクラシノノミノイチ黄色のカラーコーンを使用し、構造用合板に65φの穴を開け簡易に設営できるテーブルを設ける。',
                  'テント内で帯状に曲げられたテーブルの上に建築家による作品を並べ彩るイベントの計画を行なった。']),
    dict(cat='proposals', slug='aoishi-no-oka', title='青石の丘', sub='保育園・児童センターの提案', loc='愛媛県八幡浜市',
         specs=[('敷地','愛媛県八幡浜市'), ('構造','鉄骨造2階建'), ('用途','保育園・児童センター'), ('竣工','unbuild')],
         concept=['保育園と児童センターを併設する提案計画。']),
    dict(cat='proposals', slug='iizuka-apartment', title='飯塚のアパートメント', sub='木造長屋の提案', loc='福岡県飯塚市',
         specs=[('敷地','福岡県飯塚市'), ('構造','木造2階建'), ('用途','長屋'), ('竣工','unbuild')],
         concept=['木造2階建ての長屋形式による賃貸集合住宅の提案。']),
    dict(cat='proposals', slug='ohashi18-5', title='大島18.5', sub='交流拠点の提案', loc='愛媛県八幡浜市大島',
         specs=[('敷地','愛媛県八幡浜市大島'), ('構造','木造平屋'), ('用途','集会所'), ('竣工','unbuild')],
         concept=['愛媛県八幡浜市大島の玄関口としてふさわしい、島民と観光客をつなぐ「LDK」ような新しい交流拠点の在り方を考えた。',
                  '敷地幅いっぱいに延びるテーブルの上には、島民や観光客によって起こる様々な行為が並べられ、島民と観光客が一緒になりテーブルの上につくりあげる風景が大島の新しいシンボルとなることを目指した。']),
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
    {NAV_TOGGLE}
    <nav class="icon-nav" aria-label="ページ移動">
      <a class="icon-btn{cls('home')}" href="../../index.html" aria-label="WORKS（トップ）" title="WORKS">{ICONS['home']}</a>
      <a class="icon-btn{cls('blog')}" href="../../blog.html" aria-label="BLOG" title="BLOG">{ICONS['blog']}</a>
      <a class="icon-btn{cls('profile')}" href="../../profile.html" aria-label="PROFILE" title="PROFILE">{ICONS['profile']}</a>
      <a class="icon-btn{cls('contact')}" href="../../contact.html" aria-label="CONTACT" title="CONTACT">{ICONS['contact']}</a>
      <a class="icon-btn" href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" aria-label="Instagram（別タブで開く）" title="Instagram">{ICONS['instagram']}</a>
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
