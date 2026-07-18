import cv2
import numpy as np


def check_forgery(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return {
            "status": "Invalid Image",
            "confidence": 0
        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur Detection
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Brightness
    brightness = np.mean(gray)

    # Resolution
    height, width = gray.shape

    score = 100
    reasons = []

    # Blur
    if blur_score < 80:
        score -= 25
        reasons.append("Image is blurry")

    # Brightness
    if brightness < 60:
        score -= 15
        reasons.append("Image too dark")

    if brightness > 220:
        score -= 15
        reasons.append("Image overexposed")

    # Resolution
    if width < 500 or height < 500:
        score -= 20
        reasons.append("Low resolution")

    # Status
    if score >= 90:
        status = "Authentic"

    elif score >= 70:
        status = "Needs Manual Review"

    else:
        status = "Possible Forgery"

    return {
        "status": status,
        "confidence": score,
        "blur_score": round(blur_score, 2),
        "brightness": round(float(brightness), 2),
        "resolution": f"{width}x{height}",
        "reasons": reasons
    }