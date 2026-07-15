import cv2
import numpy as np


def check_forgery(image_path):

    image = cv2.imread(image_path)

    if image is None:

        return {

            "score": 0,

            "status": "Unable to read image"

        }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur Detection

    blur = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    # Brightness

    brightness = np.mean(gray)

    # Resolution

    height, width = gray.shape

    resolution = width * height

    score = 100

    if blur < 100:

        score -= 25

    if brightness < 60:

        score -= 15

    if brightness > 220:

        score -= 15

    if resolution < 700000:

        score -= 20

    score = max(score, 0)

    return {

        "blur": round(blur, 2),

        "brightness": round(brightness, 2),

        "resolution": resolution,

        "score": score,

        "status": "Likely Original" if score >= 75 else "Needs Manual Review"

    }