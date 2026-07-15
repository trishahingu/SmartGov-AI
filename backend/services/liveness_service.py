import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection

detector = mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)

def check_liveness(image_path):

    image = cv2.imread(image_path)

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = detector.process(rgb)

    if result.detections:

        return {

            "face_detected": True,

            "confidence": round(
                result.detections[0].score[0] * 100,
                2
            ),

            "status": "Face Detected"

        }

    return {

        "face_detected": False,

        "confidence": 0,

        "status": "No Face Found"

    }