import datetime
import os
import re
from flask import Flask, render_template, send_from_directory
import random


root_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(root_dir, "templates")
js_dir = os.path.join(template_folder, 'js')

app = Flask(__name__, template_folder=template_folder)



@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory(js_dir, path)

if __name__ == '__main__':
    app.run()
