import matplotlib.pyplot as plt
import vgg16_model

history = vgg16_model.history

# 下の2つのグラフを横に並べる
print("-"*100)
plt.figure(1, figsize=(13,4))
plt.subplots_adjust(wspace=0.5)

# 学習曲線
plt.subplot(1, 2, 1)
plt.plot(history.history["loss"], label="train")
plt.plot(history.history["val_loss"], label="valid")
plt.title("train and valid loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend()
plt.grid()

# 精度表示
plt.subplot(1, 2, 2)
plt.plot(history.history["accuracy"], label="train")
plt.plot(history.history["val_accuracy"], label="valid")
plt.title("train and valid accuracy")
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend()
plt.grid()

plt.show()
