from flask import Flask


__author__ = "AS"
UPLOAD_IMAGE = 'static/image'
app = Flask(__name__)
app.secret_key = "secret key"
app.config["UPLOAD_IMAGE"] = UPLOAD_IMAGE
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
