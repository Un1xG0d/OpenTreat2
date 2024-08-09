import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, Response
from flask_basicauth import BasicAuth
from webcam import VideoCamera

load_dotenv()
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv("USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("PASSWORD")
basic_auth = BasicAuth(app)
video_stream = VideoCamera()

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b"--frame\r\n"
			   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")

@app.route("/")
@basic_auth.required
def index():
	return render_template("index.html")

@app.route("/video_feed")
def video_feed():
	return Response(gen(video_stream), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="3000")