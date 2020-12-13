from flask import Flask, render_template, Response
from cam import cam

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

def start_detection(camera):
    while True:
        frame = camera.tracker()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/video_feed")
def video_feed():
    video = cam.camera()
    return Response(start_detection(video),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run()
