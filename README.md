# CatScan（仮）

このリポジトリの詳細はGoogleドキュメントを見てください。

## 開発の手順

※mainブランチでは作業しないでください。必ずブランチを切って開発してください。

### ブランチの作り方

- `git branch`で現在のブランチを確認する
    - 必ずmainにいるか確認する。
- `git checkout -b 名前/機能名`
- 再びgit branchで作成されて緑になっているか確認する

### 仮想環境の有効化

- `cd desktop/catscan`
- `venv\Scripts\activate`
    - 仮想環境の有効化
- `code .`でVSCodeを起動
- `deactivate`
    - 仮想環境を無効にする
    - 開発が終わったら打つ

### VSCodeでのサーバーの立て方

- `ctrl + shift + @`でターミナル起動
- `flask run`でサーバーを起動
- `ctrl + c`でサーバーを終了する
- `pip install ○○`をした場合は、`pip freeze > requirements.txt`をする。

### GitHubへ反映する方法

コマンドプロンプト内で

- `git add .`
- `git commit -m “メッセージを入力する”`
    - メッセージは変更したことを一行で書く。
- `git push origin ブランチ名`

### PR（プルリクエスト）の作成

- git push後にGitHubのリポジトリで薄黄色のバーが表示
- 緑色のCompare & pull requestをクリック
- 緑色のCreate pull requestをクリックする

### 他人が開発したものを取り込む場合

- `git branch` → `git checkout main`
    - ブランチを確認して、mainにいるか確認。
- `git pull`
    - リモートの変更差分を取り込む。
- `git checkout ブランチ名` → `git merge main`
    - 自分のブランチに移動してmainの変更をマージする。
 

## こちらからも確認できます。
```
# 仮想環境の作成
py -3 -m venv venv

# 仮想環境の有効化（開発する度に打つ）
venv\Scripts\activate

# 仮想環境を無効にする（開発が終わる度に打つ）
deactivate

# 有効化した仮想環境内でFlaskをインストールする（初回のみ）
pip install Flask

# git cloneしたら依存関係のインストール（初回のみ）
pip install -r requirements.txt

# 現在の環境を書き出す（定期的に）
pip freeze > requirements.txt

# 開発サーバーの実行
flask run

# デバッグ
flask run --debugger --reload
```
