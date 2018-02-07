from flask import Flask, current_app, request, jsonify
import io
import model
import base64
import logging


# from urllib.request import urlopen
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.applications.vgg16 import preprocess_input
app = Flask(__name__)

@app.route('/', methods=['GET'])
def predict1():
    return "hello world"

@app.route('/', methods=['POST'])
def predict():
    data = {}

   
    # url = request.args.get('my_var', None)
    

    # #load image from url
    # file = urlopen(url)
    
    # # load an image from file
    # image = load_img(file, target_size=(224, 224))


    # # convert the image pixels to a numpy array
    # image = img_to_array(image)
    # # reshape data for the model
    # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # # prepare the image for the VGG model
    # image = preprocess_input(image)
        


    try:
        data = request.get_json()['data']
    except Exception:
        return jsonify(status_code='400', msg='Bad Request'), 400

    data = base64.b64decode(data)

    image = io.BytesIO(data)



    predictions = model.predict(image)
    current_app.logger.info('Predictions: %s', predictions)
    return jsonify(predictions=predictions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)