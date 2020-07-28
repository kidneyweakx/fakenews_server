"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect
import os
from utils import tesseract # utils 資料夾中 tesseract.py
app = Flask(__name__)

# Route 首頁
@app.route('/')
def home():
    return render_template('index.html') 

app.config["IMAGE_UPLOADS"] = os.path.dirname(__file__) 

# Route 上傳圖片頁面
@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            path = os.path.join(app.config["IMAGE_UPLOADS"], "image",image.filename)
            image.save(path)
            txt = tesseract.ocr(path)
            print(txt)
            return render_template('upload.html',value=str(txt))
    return render_template("upload.html",value="")
# for api
@app.route('/api/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            path = os.path.join(app.config["IMAGE_UPLOADS"], "image",image.filename)
            image.save(path)
            txt = tesseract.ocr(path)
            print(txt)
            return txt

# 執行該檔案時所開啟的網址
if __name__ == '__main__':
    # app.debug = True # hot reload with this Line(excute as Python File)
    # app.run(host = '0.0.0.0', port = 5000) 
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
