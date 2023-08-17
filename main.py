from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy
from flaskext.markdown import Markdown

# パイソンで”$ sudo pip3 install Flask-Markdown”を入力してマークダウンを有効にする
app = Flask(__name__)
Markdown(app)

# ここでデータベースのURLを指定
#　db_uri = "mysql+pymysql://root:@charest=utf8"
#　app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#　db = SQLAlchemy(app) 

# ここでclassを定義
# class 

# トップページのルート
@app.route('/')
def index():
    message = "Hello CatScan!!"
    return render_template('index.html', massage = message )

# 判別結果のルート
@app.route("/result")
def result():
    message = "This Cat!!"
    return render_template("result.html", massage = message )

#　自分のプロフィールのルート
@app.route("/profile")
def profile():
    message = "Your Profile!!"
    return render_template("profile.html", message = message )

#　猫図鑑のルート
@app.route("/book")
def book():
    message = "Cats Book!!"
    return render_template("book.html", message = message )

#　サインインとログイン画面のルートについては後々作成
