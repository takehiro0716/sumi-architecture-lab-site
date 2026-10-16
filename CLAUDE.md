# 角建築研究室（SUMI ARCHITECTURE LAB）WEBサイト リニューアル

## 1. 目的

福岡の一人設計事務所 **角建築研究室（SUMI ARCHITECTURE LAB / 角大輔）** の
公式サイト https://www.sumi-al.jp/ のリニューアル。

- **フェーズ1（完了）**：静的 HTML でデザイン・構成・コンテンツを確定させる（このフォルダの現状）
- **フェーズ2（これから）**：静的 HTML を **WordPress オリジナルテーマ化**し、**WordPress を導入**する。
  施主（事務所）側が管理画面から WORKS / PROPOSALS / BLOG を追加・更新できる状態をゴールとする。

架空の内容ではなく、実サイトから取得した**実データ**で構成している。

- 実プロジェクト名・スペック（敷地/構造/種別/用途/設計/施工/竣工/写真クレジット）
- 本人の実経歴・受賞歴、実ブログ記事
- 実連絡先：〒815-0033 福岡県福岡市南区大橋2-2-1 / TEL 092-231-0861 / info@sumi-al.com
- Instagram：https://www.instagram.com/sumi.architecture.lab/

## 2. フォルダ構成（現状）

```
MyProject260914/
├─ index.html            TOP（WORKS / PROPOSALS のみ。写真を全画面スライドで配置）  ← build_index.py が生成
├─ profile.html          プロフィール・経歴・受賞歴
├─ contact.html          連絡先（住所/TEL/メール。フォームは無し）
├─ blog.html             ブログ一覧（「もっと見る」ボタンで段階表示）           ← build_blog.py が生成
├─ pages/
│  ├─ works/*.html       竣工作品 12件                                          ← build_details.py が生成
│  ├─ proposals/*.html   計画案 6件                                             ← build_details.py が生成
│  └─ blog/*.html        ブログ記事 20件（slug = 日付 例 20201204）             ← build_blog.py が生成
├─ assets/
│  ├─ css/   base.css（共通）/ theme-dark.css / theme-light.css /
│  │         home.css / detail.css / profile.css / contact.css / blog.css
│  ├─ js/main.js   ヘッダーのスクロール変化・ナビ開閉・TOPへ戻る・スクロール表示・ブログ「もっと見る」
│  └─ images/{works,proposals,profile,blog}/   サイトで使う最適化済み写真
├─ source-photos/{works,proposals,profile,blog}/  高解像度の元写真（サイトからは参照しない）
├─ build_details.py      PROJECTS リスト（works/proposals 18件の正本）＋詳細ページ生成
├─ build_index.py        TOP 生成（build_details.PROJECTS を import）
├─ build_blog.py         POSTS リスト（ブログ 20件の正本）＋一覧/記事ページ生成
├─ handoff/              MacBook への引き継ぎ資料（セットアップ手順・現状・次の作業）
├─ hello.py              初期の動作確認用（不要）
└─ sumi-architecture.zip 配布用アーカイブ（2026-09-14 作成、.gitignore 対象）
```

テーマ：TOP・works・proposals・blog 記事は `theme-dark.css`、profile・contact・blog 一覧は `theme-light.css`。

## 3. 決まっていること

### コンテンツ・データ
- 写真・事実（構造種別・竣工年・協働事務所・撮影者クレジット）はすべて実サイト由来。**捏造しない。**
- プロジェクト追加時は、サムネの alt 文字から推測せず、実サイトの個別ページ
  （例 `/projects/大楠の住居/`）を必ず開いて事実を取る。
  （過去に空撮の集合住宅写真を取り違えるミスがあり、実ページ確認で修正済み）
- データの正本は Python 側：
  - `build_details.py` の `PROJECTS`：`cat`（works/proposals）, `slug`, `title`, `sub`, `loc`,
    `specs`（[(項目, 値)…]）, `concept`（段落リスト）, 写真
  - `build_blog.py` の `POSTS`：`slug`, `date`, `title`, `body`（段落リスト）, 写真
  - → WordPress 移行時は、この2つのリストを**投入データの元**として使う。

### デザイン・構成
- TOP は works / proposals のみ。写真を画面いっぱいに大胆配置。
- 詳細ページ：ヒーロー写真 → コンセプト文 → スペック表 → ギャラリー →
  全画面「next project」ティザー（works+proposals 18件を循環リンク）。スクロール過多にしない。
- profile / contact / blog は下層ページ。ナビはアイコンデザイン、レスポンシブ対応済み。
- CSS/JS は役割別の外部ファイル、画像は相対パス参照（base64 埋め込みはしない）。
- このデザインを WordPress テーマでも**そのまま再現する**（見た目は変えない）。

### 作業ルール（フェーズ1の間）
- 生成された HTML を直接手で編集しない。変更は build スクリプト側に入れて再生成する。
  （WordPress 化した後は、テーマ＋管理画面のデータが正本になり、build スクリプトは役目を終える）

## 4. 残りの作業

### A. 事前整理（Git / GitHub）
- [x] 未コミット変更をコミット（`c3afb1a`、2026-10-16）
- [x] GitHub へ push：https://github.com/takehiro0716/sumi-architecture-lab-site （ブランチ `main`）
      ※ gh CLI は未ログインのまま。push は git（Git Credential Manager）経由で成功
- [ ] `gh auth login`（任意。PR/Issue 操作に gh を使う場合のみ）
- [ ] 不要ファイル整理（`hello.py` など）

### B. WordPress 環境
- [ ] ローカル開発環境を決めて構築（例：Local / wp-env(Docker) / XAMPP など）
- [ ] 本番サーバー・ドメイン（既存 sumi-al.jp の移行方法）を確認
- [ ] 既存 sumi-al.jp の移行・置き換え方針を確認
      （写真が `image.jimcdn.com` 配信のため **Jimdo 製の可能性が高い**＝WordPress ではない。
      新規 WordPress で置き換え＋ドメイン切替＋旧 URL リダイレクトになる見込み）

### C. テーマ化（`wp-content/themes/sumi-al/` を想定）
- [ ] テーマ骨格：`style.css`（テーマヘッダ）, `functions.php`, `header.php`, `footer.php`, `index.php`
- [ ] `functions.php` で CSS/JS を `wp_enqueue_style/script` で読み込み、
      ページ種別ごとに theme-dark / theme-light を切り替え
- [ ] カスタム投稿タイプ：`works`（竣工）, `proposals`（計画案）。ブログは標準「投稿」を使う想定
- [ ] カスタムフィールド：sub / loc / スペック表（項目と値の繰り返し）/ ギャラリー
      （ACF を使うか、自前メタボックスにするか要決定）
- [ ] テンプレート対応
  - `front-page.php` … index.html（works / proposals の全画面スライド）
  - `single-works.php` / `single-proposals.php` … 詳細ページ＋next project 循環
  - `page-profile.php` / `page-contact.php` … 固定ページ
  - `home.php`（または `archive.php`）/ `single.php` … blog 一覧・記事
- [ ] 画像は WordPress メディアライブラリへ（アイキャッチ＝ヒーロー、ギャラリー＝カスタムフィールド）
- [ ] ナビをメニュー機能（`register_nav_menus`）へ。SVG アイコンはテーマ内に保持
- [ ] パーマリンク設計（例 `/works/<slug>/`、ブログ `/blog/<slug>/`）

### D. データ移行
- [ ] `PROJECTS` / `POSTS` から WordPress へ投入（WP-CLI スクリプト or WXR 生成 or 手入力を選択）
- [ ] 画像を `assets/images/`（または高解像度の `source-photos/`）から取り込み
- [ ] 全18件＋ブログ20件の表示を静的版と目視比較

### E. 公開前
- [ ] contact：フォームを設けるか決定（設けるなら Contact Form 7 等）
- [ ] SEO（タイトル/OGP/サイトマップ）、旧 URL からのリダイレクト
- [ ] セキュリティ・バックアップ系プラグイン、本番デプロイ手順

### 未決定事項（ユーザー確認が必要）
- ローカル環境のツール、本番サーバー／ドメイン移行方針
- カスタムフィールドの実装方式（ACF か自前か）
- contact フォームの有無
- 管理画面を誰がどこまで更新するか（運用範囲）

## 5. 経緯メモ

- 2026-07-08〜07-10：静的サイト制作（元チャットのログは自動削除済みで復元不可）。
  参照先を `nob-sakuma.com`（無関係）→ 実サイト `sumi-al.jp` に差し替え、写真収集・整理、
  全面再構築、下層ページ作成、CSS/JS 外部化、zip 作成まで実施。
- 2026-09-14：フォルダ名を `MyProject` → `MyProject260914` に変更（旧パス前提の設定・メモリは不一致に注意）。
  zip 配布アーカイブ作成。
- GitHub 連携は `gh auth login` 途中で中断。ローカルに2コミット（`bfe196b` Initial commit /
  `bd8892f` Sync detail pages）、remote 未設定。
- 2026-10-16：目的を「WordPress テーマ化と WordPress 導入」と明確化し、本ファイルを再構成。
  ローカルブランチを `master` → `main` に変更し、GitHub（takehiro0716/sumi-architecture-lab-site）へ push。
  以降は **MacBook で作業を継続**する予定。`handoff/` に引き継ぎ資料を作成
  （Mac では `py` ではなく `python3`、プロジェクトは `git clone` で取得）。
