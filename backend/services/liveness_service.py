import cv2
from services.face_service import detect_face


def check_liveness(image_path):
    face = detect_face(image_path)

    if not face["face_detected"]:
        return {
            "status": "Failed",
            "confidence": 0,
            "reason": "No face detected"
        }

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightness = gray.mean()

    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

    score = 100
    reasons = []

    if brightness < 60:
        score -= 20
        reasons.append("Image too dark")

    if laplacian < 80:
        score -= 20
        reasons.append("Blur detected")

    if score >= 80:
        status = "Live"
    elif score >= 60:
        status = "Review Required"
    else:
        status = "Spoof Suspected"

    return {
        "status": status,
        "confidence": score,
        "brightness": round(float(brightness), 2),
        "sharpness": round(laplacian, 2),
        "reasons": reasons
    }