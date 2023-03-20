import ipywidgets as widgets
import io
from PIL import Image, ImageOps
from IPython.display import display,clear_output
from warnings import filterwarnings
import numpy as np
import pandas as pd
from keras.applications.inception_v3 import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
import flask
from flask import Flask, render_template, request
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.preprocessing import image

app = Flask(__name__)

model = load_model('C:/Users/ASUS/Downloads/Intel Global Impact/Cultural AI/Flask/batik/ARCHIVE ALL TRAIN/GTM epoch 200 h5 keras/keras_model.h5')

batikProp = [["Batik Bali", "Bali, Indonesia", "Bali is much inspired by the beauty of nature, culture, stories of gods, and religious ceremonies in Bali."],
["Batik Betawi", "Jakarta, Indonesia", "The initial motif followed the batik pattern of the northern coastal area of Java Island, which had a coastal theme. Betawi batik patterns are influenced by Chinese culture."],
["Batik Cendrawasih", "Papua, Indonesia", "Usually this motif combines images of birds of paradise with images of plants and flowers typical of Papua."],
["Batik Dayak", "Kalimantan, Indonesia", "The term Dayak means river. So that this batik describes a variety of activities that are often related to the river."],
["Batik Geblek Renteng", "Special Region of Yogyakarta, Indonesia", "Renteng diambil dari susunan desain yang dibuat secara geometris semirip motif geometris parang."],
["Batik Ikat Celup", "Yogyakarta & Bali, Indonesia", "is the process of making motifs and colors on plain white cloth with the technique of tying and covering part of the fabric with rubber / raffia and granulated sugar plastic then dyed in color / fabric dye"],
["Batik Insang", "Kalimantan, Indonesia", "This motif depicts the civilization of the Pontianak people who at that time lived along the outskirts of the Kapuas River."],
["Batik Kawung", "Yogyakarta, Indonesia", "Kawung Batik is a batik motif whose shape is in the form of a circle similar to a kawung fruit which is neatly arranged geometrically."],
["Batik Lasem", "Jawa Tengah, Indonesia", "Batik Lasem is the result of the acculturation process of the Chinese community with Indonesia."],
["Batik Megamendung", "Jawa Barat, Indonesia", "The blue color symbolizes the color of the sky which is wide, friendly and calm and symbolizes the rain bearer who is awaited as a bearer of fertility and a giver of life."],
["Batik Pala", "Maluku, indonesia", "Pala motif is taken from history where in ancient times the price of nutmeg seeds and mace nutmeg could be more expensive than gold."],
["Batik Parang", "Solo, Indonesia", "This parang batik has the meaning of advice to never give up, like ocean waves that never stop moving."],
["Batik Poleng", "Bali, Indonesia", "Poleng or chessboard pattern is a simple checkered pattern formed from alternating dark and light colors, usually black and white."],
["Batik Sekar Jagad", "Solo and Yogyakarta, Indonesia", "From the Javanese language (Kar = map; Jagad = world), so this motif also symbolizes diversity throughout the world."],
["Batik Tambal", "Yogyakarta, Indoneisa", "The patchwork motif has the meaning of patching, meaning patching or repairing things that are damaged."]]
cultGeneralDesc = [['Batik','Batik is a process to give motifs to the media with various dyeing processes.']]

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/input',methods=['POST'])
def input():
    # imageFile for image preview on html
    imagefile = request.files['imageFile']
    imagefile.save("C:/Users/ASUS/Downloads/Intel Global Impact/Cultural AI/Flask/static/image.jpg")

    # custom code
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open('C:/Users/ASUS/Downloads/Intel Global Impact/Cultural AI/Flask/static/image.jpg')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    classID = np.argmax(prediction)

    # Variables for output
    className = batikProp[classID][0]
    cultureName = className.split(' ')[0]
    origin = batikProp[classID][1]
    desc = batikProp[classID][2]

    # define function to find general description from culGeneralDesc array
    def cultGeneralDescFinder():
        for i in range(len(cultGeneralDesc)):
            if cultGeneralDesc[i][0] == cultureName:
                return cultGeneralDesc[i][1]
    
    return render_template('index.html',image = imagefile, cultureOutput=str(className), nameOutput=str(cultureName), cultureDesc= desc, cultureOrigin= origin, generalDescription=cultGeneralDescFinder())


if __name__ == '__main__':
    app.run(debug=True,port=3000)