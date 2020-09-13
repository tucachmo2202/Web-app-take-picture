from flask import Flask, render_template, request, redirect, Response, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os 
import random
import base64
from __init__ import app
from base64 import decodebytes



@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if not request.form:
            return redirect(request.url)
        if not request.form['userID'] or not request.form['file']:
            return redirect(request.url)
        file_str = request.form['file']
        file_str = file_str.split('data:image/jpeg;base64,')[-1]
        rand = str(random.random()).split(".")[-1]
        filename = secure_filename(request.form['userID'] + "@" + rand + ".jpg")
        src = os.path.join(app.config["UPLOAD_IMAGE"], filename)
        if os.path.isfile(src):
            os.remove(src)
        else:
            with open (src, "wb") as outfile:
                outfile.write(base64.b64decode(file_str))
                print("save successfully!")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = '5000')
