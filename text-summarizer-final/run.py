#!flask/bin/python

from flask import Flask, request, jsonify, render_template
import summary
import os


app = Flask(__name__)
#path="fb.txt"
@app.route('/api', methods=['POST'])
def out():
    file=request.files['file']
    summary.start(file.filename)
    return "HELLO"


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
