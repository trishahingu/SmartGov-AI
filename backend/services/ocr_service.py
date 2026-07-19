import cv2
import easyocr
import numpy as np
import fitz
import os

reader = easyocr.Reader(['en'], gpu=False)


def preprocess_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.fastNlMeansDenoising(gray)

    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    gray = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    gray = cv2.filter2D(gray, -1, kernel)

    return gray


def extract_text(image_path):

    ext = os.path.splitext(image_path)[1].lower()

    try:

        if ext == ".pdf":

            doc = fitz.open(image_path)

            text = ""

            for page in doc:

                pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

                img = np.frombuffer(pix.samples, dtype=np.uint8)

                img = img.reshape(pix.height, pix.width, pix.n)

                if pix.n == 4:
                    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

                processed = preprocess_image(img)

                result = reader.readtext(processed, detail=0)

                text += "\n".join(result)

            doc.close()

            return text

        image = cv2.imread(image_path)

        if image is None:
            return ""

        processed = preprocess_image(image)

        result = reader.readtext(processed, detail=0)

        return "\n".join(result)

    except Exception as e:

        print("OCR Error:", e)

        return ""