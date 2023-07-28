from flask import Flask, render_template, Response
from picamera import PiCamera
import time
import io

app = Flask(__name__)
camera = PiCamera()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        time.sleep(0.1)  # Add a small delay between frames
        frame = io.BytesIO()
        camera.capture(frame, format='jpeg', use_video_port=True)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame.getvalue() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.29.174', port=800, debug=True)
