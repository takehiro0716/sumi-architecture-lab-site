# -*- coding: utf-8 -*-
import os

ICON_BLOG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3.5h8l4 4v13a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1v-16a1 1 0 0 1 1-1z"/><path d="M14 3.5v4h4"/><path d="M8 12.5h8M8 16h8M8 9h3"/></svg>'
ICON_HOME = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10.5 12 4l8 6.5"/><rect x="5.5" y="10.5" width="13" height="9" rx="1"/><path d="M10 19.5v-5h4v5"/></svg>'
ICON_PROFILE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.5"/><path d="M4.5 20c1.5-4 4.5-6 7.5-6s6 2 7.5 6"/></svg>'
ICON_CONTACT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="M3.5 6.5l8.5 7 8.5-7"/></svg>'
ICON_INSTAGRAM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="0.8" fill="currentColor" stroke="none"/></svg>'
INSTAGRAM_URL = 'https://www.instagram.com/sumi.architecture.lab/'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
NAV_TOGGLE = '''<button type="button" class="nav-toggle" aria-expanded="false" aria-label="メニューを開く">
      <svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>'''
ARROW_LEFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'

# POSTS: single source of truth for every blog article, sourced from sumi-al.jp/blog/.
# `photo` is filled in below from assets/images/blog/<slug>.(jpg|png)
POSTS = [
    dict(slug='20201204', date='2020.12.04', title='今泉のリノベーション内覧会',
         body=['お施主様のご厚意により福岡市中央区で進めておりましたプロジェクトの内覧会を行いました。',
               'お子様が独立されたご夫婦が心地よい距離感で暮らせる環境を目指し、約80㎡のマンション1室をフルリノベーションしました。',
               '感染予防対策を考慮して1組ずつの案内のうえに換気時間を設けたことから、十分な時間の確保はなかなか難しかったのですが、たくさんの方々にご来場いただき様々なご意見も頂くことができました。',
               '改めてありがとうございました。']),
    dict(slug='20210114', date='2021.01.14', title='キッチンショールーム廻り',
         body=['師である大石和彦さんとの共同設計で進めているプロジェクトの打ち合わせで施主、施主のお母様とともにキッチンショールーム廻りを行いました。',
               '平面図を元にキッチンの奥行きや長さ、バックセットとの間隔などの確認を細かく行います。',
               '天板の面材についても確認を行い、高圧メラミン、コーリアン、クオーツ、セラミックなどの様々な素材の中から選択することになりますが、それぞれ素材の持つ特性や、シンクとの相性などをメリットデメリット含めて複合的に考えながら選択をする必要があります。',
               '造作家具としてキッチンを設計・デザインすることも多いのですが、ハッ！と思う、気付くようなディテールやキッチンの組み合わせをみていると何かフツフツとキッチンを設計したくなってくる欲求が湧いてきます、、、',
               'それを何気無い会話で伝えたところ「それは君、やっぱり住宅が好きなんだよ！」と大石さんからの言葉があり、確かに！と。']),
    dict(slug='20210116', date='2021.01.16', title='今泉の住居をプロジェクトに追加いたしました。',
         body=['お子様が独立されたご夫婦が心地よい距離感で生活できる環境を目指し、約80㎡のマンションの一室のフルリノベーションを行いました。',
               '既存3LDKを2LDK+WICとし、LDKの既存壁を取り除くことによって東西に視線の抜けを与えました。']),
    dict(slug='20210201', date='2021.02.01', title='第33回福岡県美しいまちづくり建築賞に応募した2つのプロジェクトがそれぞれ賞を受賞しました。',
         body=['福岡県美しいまちづくり建築賞受賞作品。',
               '設計と施主と施工がチームとして尽力して生まれた、とても思い入れのあるプロジェクトであり、どちらの建築も「これから」へとつながるテーマを含んでいたと思います。',
               '共同住宅として、路地上の外部空間に入居者の個性が滲み出すことで、共同住宅の在り方を作り上げられる風景。',
               '整骨院として、視線を柔らかくつなげるようなワンルームの空間で、セミナーやイベントなどが展開される風景。',
               'コロナの影響により、なかなか身動きがとりづらい状況ではありますが、今後、様々な展開がされていく双方の空間に訪れることで、その時感じた感覚とは異なる新たな刺激がありそうで楽しみです。',
               '今回いただいた賞に甘んじることなく、前進していきたいと思います！']),
    dict(slug='20210624', date='2021.06.24', title='２つの賞状',
         body=['福岡県美しいまちづくり賞の受賞を受け、賞状を受け取りました。',
               '本来であればアクロス福岡での授賞式にて表彰される予定でしたが、コロナ渦の状況によって授賞式は残念ながら中止となってしまいました。',
               'そんな中、てっきり紙の賞状のみの送付を想定していたのですが、届いたのは大きな段ボールが。',
               '2つの賞状が立派な額縁に入れられ、とても丁寧に梱包されていました。',
               '最後の最後まで丁寧な対応をして頂き、感謝しかありません。',
               '賞への応募は、設計中に自分の考えていたことの再確認と整理に繋がります。',
               'また、応募する賞によって審査員の方も変わるため、様々な貴重な意見を聞く事ができます。',
               '今後ともチャンスを作り、挑戦していくための良い経験となりました。']),
    dict(slug='20210718', date='2021.07.18', title='佐賀大和での地鎮祭',
         body=['前日の天気予報では曇りのち雨（雷）となっており心配でしたが天気も良く無事地鎮祭を行うことができました。',
               '敷地には建物形状がわかるように地縄が張られ、施主、施工チームと共に開口からの見え方や、位置関係について確認を行いながら内容を詰めていきます。',
               '安全に工事が進むことを祈り、年内竣工を目指して着工準備中です。']),
    dict(slug='20210720', date='2021.07.20', title='楽市のアパートメント その後の路地空間',
         body=['楽市のアパートメントが竣工して2年経ちました。',
               'タイミングよく訪れる機会があり、ぐるぐると路地を歩いていると夏休みに入った子供たちの姿も見え隠れし軒のかかった玄関ポーチに要素が点在している風景を見ることができます。',
               'オーナーさんが手を入れてくれている花壇には花が植えられ、自転車や植物、かわいらしいブタの蚊取り線香入れも置かれていたり、夏を感じます。',
               '賃貸ということもあり、なかなかコミュニティの形成が難しいと思う反面、今後、熟成していけばもっと魅力的な空間の質となる可能性が含まれていると改めて思いました。',
               'コロナが収束し、中庭空間で季節の行事が行われたりすればとても楽しそうです。',
               '完成して終わりではなく、変化していく過程を入居者と共有し楽しめるようなコミュニティを成熟させるための出来事のデザインについて、考えてみようと思いました。']),
    dict(slug='20210910', date='2021.09.10', title='佐賀大和の住宅上棟！',
         body=['佐賀大和の住宅が上棟しました。',
               '家相の要望を取り入れ、基本となるスクエアな平面から計画を行い、鬼門、裏鬼門を外しながら平面形状を削りとるように建物形状を決定しています。',
               '屋根はよく見られる切妻屋根の棟を建物の対角線状に渡しているため、平面形状とともにカットすることで東西南北の外観は全て異なる特徴的な見え方になっています。',
               '一つのシンプルなルールでどれだけ変化を与えることができるか形態のスタディを繰り返し施工業者の協力によって無事、上棟することができました。',
               '施主の要望を最大限叶えるために、丁寧に監理を進めていく予定です。']),
    dict(slug='20210913', date='2021.09.13', title='桜ヶ丘のリノベーション',
         body=['今年の年明けから計画が始まった春日市桜ヶ丘のリノベーションがいよいよ着工となりました。',
               'もともとは各部屋に段差が生じている2LDKの住まいを段差を解消し、1LDK+ゲストスペースとして再構築しました。',
               '日々の生活をイメージしながら動線を整えることによって回遊性をもつ空間になっています。',
               '施工は「いろどり整骨院/住宅」を施工いただいたイクスワークスさんです。',
               '風がよく通り抜け、柔らかな住空間となるように年内の竣工を目指して設計監理を行なっていきます。']),
    dict(slug='20211020', date='2021.10.20', title='2021グッドデザイン賞 受賞',
         body=['楽市のアパートメントが色々と評価して頂いているのをきっかけに今年度のグッドデザイン賞に応募をしました。',
               'グッドデザイン賞は、文具のような小さいものから、車、家具や建築やコミュニティなど大小様々なジャンルが一堂に集まるデザインのお祭りです。',
               'そんなお祭りの一次審査を無事通過し、コロナ禍ではありましたが、愛知にて最終審査が行われました。',
               '愛知での最終審査のためにパネルや約90cm角の模型を作ったりして「伝わるように」を心がけて臨みましたが、無事、2021年度グッドデザイン賞を受賞することができました。',
               '審査員の評価として「細分化されたボリューム群による共同住宅が、周辺環境との調和や、路地といった豊かな外部共用空間を生み出しているが」と記されています。',
               '本来であれば対面での審査となるので、直接お会いしてもっと話を聞けることができたのでしょうが、やはり少し残念でした。',
               '僕の大学の恩師は、家具デザインにおいてグッドデザイン賞を数多く受賞しています。',
               'ジャンルは少し異なりますが、恩師と同じようにグッドデザイン賞を取ることができ、先は長いのですがほんの少しだけ、近づけたのでしょうか。']),
    dict(slug='20211205', date='2021.12.05', title='桜ヶ丘のリノベーション 内覧会のご案内',
         body=['桜ヶ丘で進めておりました住戸リノベーションがあと少しで竣工致します。',
               'お施主様のご厚意により内覧会を開催する運びとなりましたので是非ご高覧いただきたくご案内申し上げます。',
               '日時：12月11日(土)、12日(日)　10:00から17:00',
               '場所：福岡県春日市桜ヶ丘　※参加ご希望の方に詳細情報をお送り致しますので「CONTACT」からメールにて希望日時をお知らせ下さい。']),
    dict(slug='20220331', date='2022.03.31', title='architecturephotoに掲載頂きました',
         body=['「楽市のアパートメント」をarchitecturephotoに掲載して頂きました。',
               'ダイアグラムなども一部載せていますので、ぜひご覧ください。']),
    dict(slug='20220421', date='2022.04.21', title='旦過市場について',
         body=['川に迫り出す建築。',
               '北九州の台所として栄える「旦過市場」で4月20日に大きな火災が起こった。',
               'この場所は私にとって特別に思い入れのある場所であり、大学院の修了設計のテーマとなっている。',
               '初めて訪れた時から、この市場の持つ空気感に魅了された。',
               '当時、大規模な再開発の話が上がり、その案を見て愕然とした記憶がある。',
               '河川に迫り出した魅力的な建築も全て撤去された上でスーパーマーケットのような「整えられすぎる市場」に加えて「高層の居住空間」が計画されていた。',
               'いわゆるザ・再開発プランであり、闇市から始まった100年の文脈を完全にリセットするかのような計画ではないかと考えてしまう。',
               '旦過市場の魅力の一つである雑然さは、発生して100年以上の時間の経過によってもたらされている。',
               '現在の市場の姿は、限られた敷地いっぱいに建物が建てられ、それでも面積が必要なため鉛直方向に増改築が繰り返されて今に至る。',
               'パッチワークのような素材の変化、トタン屋根の重なりによって混沌さが現れている。',
               '大学院当時、増改築が繰り返されてきたこの市場は当然だが既存図もなく、まずは既存図の作成を始める必要があった。',
               '昼夜問わず3ヶ月間旦過市場に入り浸り、営業時間に邪魔をするわけにはいけないので、店舗のファサードは夜に市場まで行き徹夜で実測を行なったことは今ではいい思い出となっている。',
               '誰よりもこの市場のことに詳しくなりたい気持ちで挑み、営業者の方々にご協力いただいて、ほぼ全ての店舗の商品棚のレイアウトを含めた実測を行わせてもらった。',
               '1階は市場としてとても賑わっているが、2階は使われていた痕跡が残る住居のまま、もしくは店舗の倉庫として活用されている裏の顔を持つ。',
               '賑わいの裏に隠された生活の記憶も私にとってはこの場所の魅力の一つとなっている。',
               'その市場で、今回大きな火災が起こったことを知り、ニュースで音声入りの動画を見た時はとてもいたたまれない気持ちになった。',
               '幸いなことに怪我をされた人はいないようで安堵したが、40店舗、面積にして1600㎡が焼失してしまった。',
               '北九州にとどまらず、たくさんの人々に愛される集合体としての旦過市場が、日常の活気ある市場の姿をいち早く取り戻せることを願ってやまない。']),
    dict(slug='20220617', date='2022.06.17', title='新規プロジェクトの追加のお知らせ',
         body=['ご夫婦の日々の生活の中に機能的な回遊動線を取り入れることによって風が通り抜ける気持ちのよい落ち着いた空間を目指しました。']),
    dict(slug='20221007', date='2022.10.07', title='筆の里創造の丘公苑「体験交流施設」新築工事プロポーザル',
         body=['広島県熊野町で行われた筆の里創造の丘公苑「体験交流施設」新築工事プロポーザルにおいて設計者として選定されました。',
               'これから環境デザイン機構と共同で設計を進めていきます。',
               'ランドスケープを重視し、筆の里工房、公園エリア、旧街道などを繋げる結節点として建築を位置付け、施設利用者の活動の場を点在させています。',
               '外部へと活動が滲み出し、内部も路地空間を使いフレキシブルに利用可能となる空間とし、町民の方々の活動に自由度を含ませた施設を目指します。']),
    dict(slug='20230413', date='2023.04.13', title='久留米O CLINIC 完了検査',
         body=['久留米O CLINICの完了検査でした。',
               '共同設計として大石さんから声をかけて頂き、2020年から計画が始まって約2年と10ヶ月。',
               '現場の方々のお力添えもあり、外構の植栽を残すのみとなりました。',
               '検査の待ち時間に常駐のガードマンの方と完成に至るまでのお話しするタイミングがあり、患者さんや先生、スタッフの方々からいつも気持ちよく挨拶をしてもらっていたとのこと。',
               'ガードマンの方の気さくで明るい性格もあるのでしょう、信頼関係が垣間見れます。',
               '工事が終わってしまうのが寂しいのと同時に完成を見れたのがとても感慨深い。と、うれしい言葉を頂きました。',
               '次の現場は久留米を離れて鳥栖の方になるそう。',
               '施主には施主の、設計には設計の、現場には現場のそれぞれストーリーがありますが、季節を跨いで道路境界線と敷地境界線のあいだを守ってくれた物語、とても美しいと思いました。',
               '工事期間中、通行人の安全を守ってくれてありがとうございました。',
               'お疲れ様でした。']),
    dict(slug='20230718', date='2023.07.18', title='由布院別荘 地鎮祭',
         body=['設計工房と共同設計している由布院別荘の地鎮祭が執り行われました。',
               '昔より由布院は美しい街並みと自然、文化をもつ場所であり、磯崎新氏の設計された由布院駅などがあります。',
               '現在では隈研吾氏のCOMICO ART MUSEUM YUFUINや、坂茂氏のYUFUiNFOなど、由布院の伝統を尊重しつつも現代建築の新旧融合を点在して見ることができます。',
               '海外の観光客も増え、湯の坪街道は平日でも人であふれていますが、賑わいのある通りから一つ入ると田園が広がり、木々が生い茂る自然豊かで閑静な風景が展開されます。',
               'その落ち着いた場所に、今回別荘を計画することとなりました。',
               '地鎮祭の当日は、日田の高速道路が通行止めになっているため朝6:30に事務所を出発し、8:30に湯の坪街道の人通りが疎らな由布院に到着。',
               '雨の心配をしていましたが天候にもなんとか恵まれ、敷地を通り抜ける風によって敷地周辺の木々の木漏れ日が揺れるとても気持ちの良い日となりました。',
               'テントを通して美しい由布岳を臨み、施主・設計者・施工者が日々安全に工事にとりかかれるよう願います。',
               '外壁には大分県産の木材を使用し、落ち着いた雰囲気を持つ周辺環境と馴染ませながら由布岳に向かって開くことをテーマとしています。']),
    dict(slug='20230804', date='2023.08.04', title='由布院別荘 配筋検査',
         body=['配筋検査のため由布院へ。',
               '配筋検査では基礎配筋の配置や間隔が守られているか、鉄筋の継手の長さは適切か、排水立上げ位置などをチェックし、建物の構造が設計図通りに進められているか確認を行います。',
               'このプロジェクトは、変形敷地であることと規模が大きいことに加えて住宅が3つの棟に別れています。',
               'そのため、奥の棟から順を追って施工を行う必要があるのですが、基礎を打ち終わった段階、基礎の配筋を行っている段階、基礎配筋をするための地業を行なっている段階を今日の検査では同時に見ることができました。',
               '8月19日に敷地奥の住戸が上棟予定となっており、ようやく建築の骨格が現れるためとても楽しみです。']),
    dict(slug='20230822', date='2023.08.22', title='新規プロジェクトの追加のお知らせ',
         body=['O CLINICをプロジェクトに追加いたしました。',
               '旧クリニック横の駐車場に新規クリニックを建築し、建築完了後、既存クリニックを解体し駐車場へと変更しました。',
               'クリニックの運営をストップすることがないローリング計画としました。',
               '旧クリニックでの先生とスタッフの方々の使い勝手にも配慮しつつ、きめ細やかな機能性を目指しました。']),
    dict(slug='20240625', date='2024.06.25', title='新規プロジェクトの追加のお知らせ',
         body=['敷地に広がる豊かな自然環境を空間に取り込みながら、日常生活の豊かな一コマを家族やゲストとともに過ごす居場所を計画しました。',
               'この建築が時間をかけて地域の景観に対して馴染むと同時に、近隣環境と人をつなげる新しい場となることを期待しています。']),
]

for p in POSTS:
    for ext in ('jpg', 'png'):
        path = os.path.join('assets', 'images', 'blog', f"{p['slug']}.{ext}")
        if os.path.exists(path):
            p['photo'] = f"../../assets/images/blog/{p['slug']}.{ext}"
            break
    p['outpath'] = os.path.join('pages', 'blog', f"{p['slug']}.html")

# newest first, matching the real site's listing order
POSTS.sort(key=lambda p: p['slug'], reverse=True)


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
      <a class="icon-btn{cls('home')}" href="../../index.html" aria-label="WORKS（トップ）" title="WORKS">{ICON_HOME}</a>
      <a class="icon-btn{cls('blog')}" href="../../blog.html" aria-label="BLOG" title="BLOG">{ICON_BLOG}</a>
      <a class="icon-btn{cls('profile')}" href="../../profile.html" aria-label="PROFILE" title="PROFILE">{ICON_PROFILE}</a>
      <a class="icon-btn{cls('contact')}" href="../../contact.html" aria-label="CONTACT" title="CONTACT">{ICON_CONTACT}</a>
      <a class="icon-btn" href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" aria-label="Instagram（別タブで開く）" title="Instagram">{ICON_INSTAGRAM}</a>
    </nav>
  </header>
"""


def build_article(p, next_p):
    body_html = "".join(f"<p>{line}</p>" for line in p['body'])
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{p['title']} | BLOG | 角建築研究室 SUMI ARCHITECTURE LAB</title>
<meta name="description" content="{p['title']}（{p['date']}）— 角建築研究室のブログ記事。" />
<link rel="stylesheet" href="../../assets/css/base.css" />
<link rel="stylesheet" href="../../assets/css/theme-dark.css" />
<link rel="stylesheet" href="../../assets/css/blog.css" />
</head>
<body>
{header_html('blog')}
  <main>
    <div class="article-hero">
      <img src="{p['photo']}" alt="{p['title']}" />
      <div class="article-caption">
        <span class="article-date">{p['date']}</span>
        <h1 class="article-title">{p['title']}</h1>
      </div>
    </div>

    <section class="article-body wrap">
      <div class="reveal" style="--d:1">{body_html}</div>
      <nav class="article-nav">
        <a href="../../blog.html">{ARROW_LEFT}BLOG 一覧へ戻る</a>
        <a href="../../index.html">WORKS を見る{ARROW}</a>
      </nav>
    </section>

    <a class="article-next" href="{next_p['slug']}.html">
      <img src="{next_p['photo']}" alt="" />
      <div class="article-next-inner">
        <span class="article-next-eyebrow">NEXT POST{ARROW}</span>
        <p class="article-next-title">{next_p['title']}</p>
      </div>
    </a>
  </main>

  <footer>
    <div class="footer-row">
      <span>&copy; 角建築研究室 SUMI ARCHITECTURE LAB</span>
      <span><a href="../../blog.html">BLOG へ戻る</a></span>
    </div>
  </footer>

<script src="../../assets/js/main.js"></script>
</body>
</html>
"""


PAGE_SIZE = 10


def build_index_listing():
    def card(p, idx):
        hidden = " is-hidden" if idx >= PAGE_SIZE else ""
        return f"""
      <a class="blog-card reveal{hidden}" href="pages/blog/{p['slug']}.html">
        <div class="blog-card-frame"><img src="{p['photo'].replace('../../', '')}" alt="{p['title']}" loading="lazy" /></div>
        <span class="blog-card-date">{p['date']}</span>
        <p class="blog-card-title">{p['title']}</p>
      </a>"""

    cards = "".join(card(p, i) for i, p in enumerate(POSTS))
    more_button = (
        f"""
    <div class="blog-more-wrap">
      <button type="button" id="blogMoreBtn" class="blog-more-btn" data-page-size="{PAGE_SIZE}">
        <span class="blog-more-label">もっと見る</span>
        <svg class="blog-more-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>
      </button>
    </div>"""
        if len(POSTS) > PAGE_SIZE else ""
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>BLOG | 角建築研究室 SUMI ARCHITECTURE LAB</title>
<meta name="description" content="角建築研究室の設計・施工の記録や近況を綴るブログです。" />
<link rel="stylesheet" href="assets/css/base.css" />
<link rel="stylesheet" href="assets/css/theme-light.css" />
<link rel="stylesheet" href="assets/css/blog.css" />
</head>
<body>

  <header class="site-header" id="siteHeader">
    <a href="index.html" class="wordmark">
      <span class="ja">角建築研究室</span>
      <span class="en">SUMI ARCHITECTURE LAB</span>
    </a>
    {NAV_TOGGLE}
    <nav class="icon-nav" aria-label="ページ移動">
      <a class="icon-btn" href="index.html" aria-label="WORKS（トップ）" title="WORKS">{ICON_HOME}</a>
      <a class="icon-btn is-active" href="blog.html" aria-label="BLOG" title="BLOG">{ICON_BLOG}</a>
      <a class="icon-btn" href="profile.html" aria-label="PROFILE" title="PROFILE">{ICON_PROFILE}</a>
      <a class="icon-btn" href="contact.html" aria-label="CONTACT" title="CONTACT">{ICON_CONTACT}</a>
      <a class="icon-btn" href="{INSTAGRAM_URL}" target="_blank" rel="noopener noreferrer" aria-label="Instagram（別タブで開く）" title="Instagram">{ICON_INSTAGRAM}</a>
    </nav>
  </header>

  <main>
    <section class="blog-hero wrap">
      <h1 class="reveal" style="--d:1">BLOG</h1>
      <p class="reveal" style="--d:2">設計・施工にまつわる記録や近況をお伝えします。</p>
    </section>

    <div class="blog-grid wrap">{cards}
    </div>{more_button}
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


def main():
    os.makedirs('pages/blog', exist_ok=True)
    n = len(POSTS)
    for i, p in enumerate(POSTS):
        next_p = POSTS[(i + 1) % n]
        with open(p['outpath'], 'w', encoding='utf-8') as f:
            f.write(build_article(p, next_p))
        print(p['outpath'])

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(build_index_listing())
    print('blog.html')


if __name__ == '__main__':
    main()
