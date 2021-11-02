from flask import Flask, render_template, request, jsonify

import os
import json
import werkzeug
import cv2
import io
import base64
import time
from PIL import Image
import daltonize

path = "C:/Users/Jaadu/Downloads/colorapi/static/"
fn = []
app = Flask(__name__)


def get_response_image(image_path):
    with open(image_path,"rb") as file:
        content = base64.b64encode(file.read())
        image_base64 = {"base64" : content.decode()}
    return image_base64


def deleting_files():
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))


def model_run(disease):
    img=path+fn[0]
    daltonize.start(disease, img)
    encoded = get_response_image(path+"output.jpg")
    return encoded


@app.route("/api/colorblind",methods=['GET', 'POST'])
def api_call():
    
    
    incoming_files = list(request.files)
    print("Files recieved :",len(incoming_files))
    os.chdir(path)
    it = 1
    error=request.form.get('string')
    print(error)
    
    for file in incoming_files:
        image = request.files[file]
        filename = werkzeug.utils.secure_filename(image.filename)
        print(filename)
        #print()
        abc = filename.split(".")
        if abc[-1] != "json":  
            fn.append(str(it) + "." + abc[-1])
            image.save(fn[it-1])
        else:
            print("hi")
            error = str(image.read(),'UTF-8')
            if error == 'd':
                print(error)
        print("File saved ",it)
        it = it + 1
    cypher = model_run(error)
    #deleting_files()
    return jsonify(cypher)


@app.route("/", methods=['GET', 'POST'])
def home():
    return "HEllo World"


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
