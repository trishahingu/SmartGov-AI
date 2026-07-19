import os
import cv2

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "face_detection_yunet_2023mar.onnx"
)


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

        h, w = image.shape[:2]

        detector = cv2.FaceDetectorYN.create(
            MODEL_PATH,
            "",
            (w, h),
            score_threshold=0.8,
            nms_threshold=0.3,
            top_k=5000
        )

        detector.setInputSize((w, h))

        _, faces = detector.detect(image)

        if faces is None or len(faces) == 0:

            return {
                "success": True,
                "face_detected": False,
                "face_count": 0,
                "confidence": 0,
                "message": "No face detected"
            }

        confidences = []

        for face in faces:
            confidences.append(float(face[-1]) * 100)

        best_confidence = round(max(confidences), 2)

        return {
            "success": True,
            "face_detected": True,
            "face_count": len(faces),
            "confidence": best_confidence,
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