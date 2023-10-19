from flask import Flask, request, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# モデルの読み込み
model_path = "cat_vgg16_model1.h5"
model = load_model(model_path)

# トップページのルート
@app.route('/')
def index():
    message = "Hello CatScan!!"
    return render_template('index.html', massage = message )

# 種類判別
@app.route('/predict', methods=['post'])
def predict():
    file = request.files['file']
    print(file)
    return render_template('index.html', predicted_class='三毛猫')
    # if file:
    #     # 画像ファイルをリサイズ
    #     img = image.load_img(file, target_size=(256, 256))
    #     x = image.img_to_array(img)
    #     x = np.expand_dims(x, axis=0)

        # preds = model.predict(x)
        # preds_class = np.argmax(preds, axis=-1)
        # preds_class = np.argmax(preds[0])

        # return jsonify({'predicted_class': preds_class})
        # return render_template('index.html', predicted_class=preds_class)

#　自分のプロフィールのルート
@app.route("/profile")
def profile():
    message = "Your Profile!!"
    return render_template("profile.html", message = message )

