# 引き継ぎ資料（Windows → MacBook）

作成：2026-10-16 ／ 作成元：Windows PC（`MyProject260914` フォルダ）

角建築研究室サイトを **WordPress テーマ化・WordPress 導入** するプロジェクトを、
MacBook で続けるための資料です。

## 読む順番

| # | ファイル | 内容 |
|---|---|---|
| 0 | [MEMO.md](MEMO.md) | **人が読む用のメモ**。全体像・ToDo・決めることを箇条書きで |
| 1 | [01_mac-setup.md](01_mac-setup.md) | Mac に入れるもの、リポジトリの取得、動作確認 |
| 2 | [02_status.md](02_status.md) | 2026-10-16 時点の状態（終わったこと / 決まっていること / 未決定） |
| 3 | [03_next-steps.md](03_next-steps.md) | 次にやること（あなたの作業 / Claude の作業）と、最初に Claude に送る文 |
| — | [../CLAUDE.md](../CLAUDE.md) | プロジェクトの正本資料。Claude Code が毎回自動で読み込む |

## 3行まとめ

- コードと写真はすべて GitHub にあります：https://github.com/takehiro0716/sumi-architecture-lab-site （`main`）
- Mac では `git clone` して、Claude Code をそのフォルダで起動すれば、CLAUDE.md から作業を再開できます。
- 次の山場は「WordPress のローカル環境づくり」と「テーマ化の方針決め（03_next-steps.md の4項目）」です。

## GitHub に入っていないもの（Mac に必要なら別途コピー）

| もの | 場所（Windows） | 必要性 |
|---|---|---|
| `sumi-architecture.zip` | プロジェクト直下（19MB） | 不要。リポジトリと同じ内容の配布用アーカイブ |
| `.claude/settings.local.json` | プロジェクト直下 | 不要。Windows 用のコマンド許可設定 |
| Claude Code の会話履歴・メモリ | `C:\Users\藤田　雄大\.claude\` | 引き継がれません。必要な内容はすべて CLAUDE.md とこのフォルダに書いてあります |
