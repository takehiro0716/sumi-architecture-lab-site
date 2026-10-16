# 01. MacBook のセットアップ

ターミナル（アプリケーション → ユーティリティ → ターミナル）で実行します。
すでに入っているものは飛ばしてください。

## 1. 必要なツールを入れる

```bash
# Homebrew（Mac 用のパッケージ管理）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# git / GitHub CLI / Python
brew install git gh python

# Claude Code
curl -fsSL https://claude.ai/install.sh | bash
```

WordPress のローカル環境として **Local** を使う場合（おすすめ）は、
https://localwp.com/ から Mac 版をダウンロードしてインストールします。
（どの環境にするかは未決定。03_next-steps.md 参照）

## 2. GitHub にログインしてリポジトリを取得

```bash
gh auth login        # GitHub.com → HTTPS → ブラウザでログイン を選ぶ
gh auth setup-git    # git push でも同じログインを使う設定

mkdir -p ~/Projects && cd ~/Projects
git clone https://github.com/takehiro0716/sumi-architecture-lab-site.git
cd sumi-architecture-lab-site
```

> Windows では gh のログインが途中で止まりました。Mac では
> 「表示されたコードをコピー → ブラウザで https://github.com/login/device に貼る」
> まで終えるとログインが完了します。

コミットの作者名を設定します（Windows では作者名が `MyProject` になっていました）。

```bash
git config --global user.name  "あなたの名前"
git config --global user.email "takehirohujita@gmail.com"
```

## 3. 動作確認

```bash
# 静的サイトを表示
open index.html

# 生成スクリプトが動くか（写真処理に Pillow を使う場合がある）
python3 -m pip install --user Pillow
python3 build_details.py && python3 build_index.py && python3 build_blog.py
git status   # 何も変わっていなければ OK
```

> Windows では `py` コマンドで実行していました。Mac では `python3` を使います。
> 再生成後に `git status` で差分が大量に出る場合は改行コード（Windows は CRLF）の違いです。
> 中身が同じなら気にしなくて大丈夫ですが、気になる場合は Claude に
> 「改行コードを LF に揃えて .gitattributes を追加して」と頼んでください。

## 4. Claude Code を起動

```bash
cd ~/Projects/sumi-architecture-lab-site
claude
```

起動したら `/login` でログインし、03_next-steps.md の「最初に送る文」を送ってください。
