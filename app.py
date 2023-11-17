from flask import Flask, render_template, request, url_for
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_edge():
    # Đọc hình ảnh gốc
    img = cv2.imread('static/chim1.png')

    # Áp dụng các thuật toán Canny, Sobel và Laplacian
    canny1 = cv2.Canny(img, 100, 200)
    cv2.imwrite('static/a.png', canny1)

    canny2 = cv2.Canny(img, 300, 400)
    cv2.imwrite('static/b.png', canny2)

    sobel1x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    cv2.imwrite('static/c.png', sobel1x)

    sobel1y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    cv2.imwrite('static/d.png', sobel1y)

    sobel2x = cv2.Sobel(img, cv2.CV_64F, 1, 2, ksize=3)
    cv2.imwrite('static/e.png', sobel2x)

    sobel2y = cv2.Sobel(img, cv2.CV_64F, 2, 1, ksize=3)
    cv2.imwrite('static/f.png', sobel2y)

    laplacian1 = cv2.Laplacian(img, cv2.CV_64F)
    cv2.imwrite('static/g.png', laplacian1)

    laplacian2 = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
    cv2.imwrite('static/h.png', laplacian2)

    # Truyền các kết quả vào template để hiển thị
    return render_template('result.html', canny1=canny1, canny2=canny2, sobel1x=sobel1x, sobel1y=sobel1y, sobel2x=sobel2x, sobel2y=sobel2y, laplacian1=laplacian1, laplacian2=laplacian2)

if __name__ == '__main__':
    app.run(debug=True)