
import os

cwd = os.getcwd()
model_path = os.path.join(cwd, 'model', 'keras_model.h5')
# model = load_model("/model/keras_model.h5")
file_path = str(model_path).replace('\\', '/')
print("++++++++++++++++++++++++++++++")
print(file_path)
# model = keras.models.load_model(model_path)