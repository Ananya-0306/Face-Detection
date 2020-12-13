import cv2

face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class camera():
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
    
    def __del__(self):
        self.camera.release()

    def tracker(self):
        success,pic =self.camera.read()
        faces = face_model.detectMultiScale(pic)
        for face in faces:
                x,y,w,h=face
                pic = cv2.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)
        
        ret, jpeg = cv2.imencode('.jpg', pic)
        return jpeg.tobytes()
