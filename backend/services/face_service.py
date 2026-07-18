import cv2
import os

CASCADE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)


def detect_face(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return {
            "success": False,
            "message": "Image not found."
        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    return {
        "success": True,
        "face_detected": len(faces) > 0,
        "face_count": len(faces)
    }