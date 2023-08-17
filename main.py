from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy
app = Flask(__name__)

# ここでデータベースのURLを指定
#　db_uri = "mysql+pymysql://root:@charest=utf8"
#　app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#　db = SQLAlchemy(app) 

# ここでclassを定義
# class 

@app.route('/')
def index():
    message = "Hello CatScan!!"
    return render_template('index.html', massage = message)
