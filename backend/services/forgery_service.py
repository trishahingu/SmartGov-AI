import cv2
import numpy as np


def check_forgery(image_path):

    try:

        image = cv2.imread(image_path)

        if image is None:
            return {
                "status": "Invalid Document",
                "confidence": 0,
                "reason": "Unable to read image"
            }

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # ---------- Blur Detection ----------
        blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

        # ---------- Brightness ----------
        brightness = np.mean(gray)

        # ---------- Edge Detection ----------
        edges = cv2.Canny(gray, 100, 200)

        edge_density = np.sum(edges > 0) / edges.size

        confidence = 100

        reasons = []

        if blur_score < 80:
            confidence -= 25
            reasons.append("Image is blurry")

        if brightness < 40:
            confidence -= 15
            reasons.append("Image is too dark")

        elif brightness > 220:
            confidence -= 15
            reasons.append("Image is overexposed")

        if edge_density < 0.02:
            confidence -= 20
            reasons.append("Low document detail detected")

        confidence = max(0, min(100, int(confidence)))

        if confidence >= 85:
            status = "Authentic"

        elif confidence >= 60:
            status = "Needs Manual Review"

        else:
            status = "Forgery Suspected"

        return {

            "status": status,

            "confidence": confidence,

            "blur_score": round(blur_score, 2),

            "brightness": round(float(brightness), 2),

            "edge_density": round(float(edge_density), 4),

            "reasons": reasons

        }

    except Exception as e:

        return {

            "status": "Error",

            "confidence": 0,

            "reason": str(e)

        }