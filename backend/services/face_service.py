import os
import cv2

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "face_detection_yunet_2023mar.onnx"
)

detector = None


def get_detector(width, height):
    global detector

    if detector is None:
        print("Loading YuNet face detector...")

        detector = cv2.FaceDetectorYN.create(
            MODEL_PATH,
            "",
            (width, height),
            score_threshold=0.8,
            nms_threshold=0.3,
            top_k=5000
        )

        print("YuNet loaded.")

    detector.setInputSize((width, height))
    return detector


def detect_face(image_path):

    try:
        image = cv2.imread(image_path)

        if image is None:
            return {
                "success": False,
                "face_detected": False,
                "face_count": 0,
                "confidence": 0,
                "message": "Unable to read image"
            }

        height, width = image.shape[:2]

        detector = get_detector(width, height)

        _, faces = detector.detect(image)

        if faces is None or len(faces) == 0:
            return {
                "success": True,
                "face_detected": False,
                "face_count": 0,
                "confidence": 0,
                "message": "No face detected"
            }

        confidences = [
            round(float(face[-1]) * 100, 2)
            for face in faces
        ]

        return {
            "success": True,
            "face_detected": True,
            "face_count": len(faces),
            "confidence": max(confidences),
            "message": "Face detected successfully"
        }

    except Exception as e:
        return {
            "success": False,
            "face_detected": False,
            "face_count": 0,
            "confidence": 0,
            "message": str(e)
        }