"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect
import os
import tesseract
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

app.config["IMAGE_UPLOADS"] = os.path.dirname(__file__) 

@app.route("/upload", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            path = os.path.join(app.config["IMAGE_UPLOADS"], "image",image.filename)
            image.save(path)
            txt = tesseract.ocr(path)
            print(txt)
            return redirect(request.url)
    return render_template("upload.html")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
