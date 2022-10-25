"""Main screen sharing app"""

import cv2
import requests
import pyautogui
import numpy as np

from flask import Flask, Response

app = Flask(__name__)

def get_frame():
    while True:
        image = pyautogui.screenshot(region=(0, 0, 1920, 1080))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        encoded = cv2.imencode('.jpg', image)[1]
    
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpg\r\n\r\n' + encoded.tobytes() + b'\r\n'
        )

@app.route('/')
def vid():
    return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='localhost', debug=True, threaded=True)
