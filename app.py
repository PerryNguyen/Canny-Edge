from flask import Flask, render_template, url_for, request
import cv2
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_edges():
    image = request.files['image']
    
    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

    lap = np. uint8(np.absolute (lap))

    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)

    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    edges = cv2.Canny(img, 100, 200)

    sobelX = np.uint8(np.absolute(sobelX))

    sobelY = np.uint8(np.absolute(sobelY))

    sobelCombined = cv2.bitwise_or(sobelX, sobelY)

    cv2.imwrite('static/chim2.png', lap)

    # cv2.imwrite('static/chim2.png', edges)

    # cv2.imwrite('static/chim2.png', sobelX)

    # cv2.imwrite('static/chim2.png', sobelY)

    # cv2.imwrite('static/chim2.png', sobelCombined)


    return render_template('result.html')


if __name__ == '_main_':
    app.run(debug=True)