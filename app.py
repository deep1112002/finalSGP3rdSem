from flask import *
import cv2
import numpy as np
import base64
from keras.models import load_model
import math
import copy
import pyttsx3
import subprocess
app=Flask(__name__)

@app.route('/')
def starting():
    return render_template('index.html')
@app.route('/index.html')
def start1():
    return render_template('index.html')
@app.route('/instructions.html')
def go():
    return render_template('instructions.html')

@app.route('/american')#,methods=["POST"])  
def america():
    subprocess.run("python3 american_sign_language.py & python3 sound.py", shell=True)
    return render_template('thankyou.html')
@app.route('/indian')
def india():
    subprocess.run("python3 indian_sign_language.py & python3 sound.py", shell=True)
    return render_template('thankyou.html')
if __name__=='__main__':
    app.run(debug=True)