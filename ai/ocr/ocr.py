import easyocr

# Load model only once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):

    results = reader.readtext(image_path)

    text = ""

    for detection in results:
        text += detection[1] + "\n"

    return text