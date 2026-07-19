import os
import cv2

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "face_detection_yunet_2023mar.onnx"
)


def check_liveness(image_path):

    try:

        image = cv2.imread(image_path)

        if image is None:
            return {
                "status": "Spoof",
                "live": False,
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
                "status": "Spoof",
                "live": False,
                "confidence": 0,
                "message": "No face detected"
            }

        face = max(faces, key=lambda x: x[-1])

        confidence = round(float(face[-1]) * 100, 2)

        x, y, fw, fh = map(int, face[:4])

        face_roi = image[y:y + fh, x:x + fw]

        gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

        brightness = gray.mean()

        if confidence >= 90 and sharpness > 100 and brightness > 40:

            status = "Live"
            live = True

        elif confidence >= 75:

            status = "Review Required"
            live = False

        else:

            status = "Spoof"
            live = False

        return {
            "status": status,
            "live": live,
            "confidence": confidence,
            "sharpness": round(sharpness, 2),
            "brightness": round(brightness, 2),
            "message": "Liveness check completed"
        }

    except Exception as e:

        return {
            "status": "Error",
            "live": False,
            "confidence": 0,
            "message": str(e)
        }