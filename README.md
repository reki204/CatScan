# CatScan（仮）

このリポジトリの詳細はGoogleドキュメントを見てください。

## Git

#### ブランチ名
 - ブランチを確認して、mainにいるか確認。
   - $ git branch
   - `$ git checkout -b  ブランチ名`※ ←ブランチを作成して移動する。
   - ##### 命名規則
     - `〇〇/機能名`
     - ○○は、開発者の名前
#### 他人が開発したものを取り込む場合
 - ブランチを確認して、mainにいるか確認。`git branch` → `git checkout main`
 - リモートの変更差分を取り込む。`git pull`
 - 自分のブランチに移動してmainの変更をマージする。`git checkout ○○` → `git merge main`


## 開発の手順

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
```
