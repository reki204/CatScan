from keras.applications.vgg16 import VGG16
from keras.layers import Dense, Dropout, Flatten, Input
from keras.models import Model
from keras import optimizers
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator

# ハイパーパラメータ
image_resize = 256
num_classes = 12 # データの種類の数
batch_size = 64 # 1回に計算するデータの数 32.
epochs = 50 # 学習回数

# ImageDataGeneratorのインスタンスを作成
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.5,
    horizontal_flip=True,
    validation_split=0.2 
)

# 訓練データのジェネレーター
train_generator = datagen.flow_from_directory(
    './dataset',  # データセットのパス
    subset='training',  # 訓練データ部分を選択
    target_size=(image_resize, image_resize),
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=False
)

# 検証データのジェネレーター
valid_generator = datagen.flow_from_directory(
    './dataset',
    subset='validation',
    target_size=(image_resize, image_resize),
    batch_size=batch_size,
    class_mode="categorical",
    shuffle=False
)

model_vgg16 = VGG16(
    weights='imagenet',
    include_top=False,
    input_tensor=Input(shape=(image_resize, image_resize, 3))
)

# 全結合層の構築
x = model_vgg16.output
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(num_classes, activation='softmax')(x)

# VGG16と構築した全結合層を結合
model = Model(inputs=model_vgg16.input, outputs=predictions)

for layer in model_vgg16.layers[:16]:
    layer.trainable = False

# 学習の設定
optimizer = Adam(learning_rate=0.0001)

model.compile(
    optimizer=optimizer,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 構築したモデルを確認
model.summary()

# 学習
history = model.fit(
    train_generator,
    batch_size=batch_size,
    epochs=epochs,
    validation_data=valid_generator,
    callbacks=[EarlyStopping(patience=3)]
)

# モデルを保存
model.save('cat_vgg16_model1.h5')
