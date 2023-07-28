from flask import Flask, render_template, Response
from picamera import PiCamera
import time

app = Flask(__name__)
camera = PiCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames():
    while True:
        # Capture video frames here and yield the frame as bytes
        # (You'll need to implement the camera capture logic here)
        time.sleep(0.1)  # Adjust the sleep time based on your camera's frame rate

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
