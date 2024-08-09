from webcam import VideoCamera
from flask import Flask, jsonify, render_template, Response

app = Flask(__name__)

video_stream = VideoCamera()

@app.route("/")
def index():
	return render_template("index.html")

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b"--frame\r\n"
			   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")

@app.route("/video_feed")
def video_feed():
	return Response(gen(video_stream), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="3000")