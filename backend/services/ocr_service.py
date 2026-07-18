import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (3,3), 0)

    cv2.imwrite("uploads/temp.png", gray)

    result = reader.readtext("uploads/temp.png")

    text = ""

    for item in result:
        text += item[1] + "\n"

    return text