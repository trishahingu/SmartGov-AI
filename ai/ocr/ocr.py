import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):

    result = reader.readtext(image_path)

    text = ""

    for item in result:
        text += item[1] + "\n"

    return text


def detect_document_type(text):

    text = text.upper()

    if "AADHAAR" in text:
        return "Aadhaar Card"

    if "GOVERNMENT OF INDIA" in text:
        return "Aadhaar Card"

    if "INCOME TAX" in text:
        return "PAN Card"

    if "PASSPORT" in text:
        return "Passport"

    if "DRIVING" in text:
        return "Driving Licence"

    return "Unknown"


def extract_fields(text):

    data = {
        "Name": "Not Found",
        "DOB": "Not Found",
        "Document Number": "Not Found"
    }

    dob = re.search(r"\d{2}/\d{2}/\d{4}", text)

    if dob:
        data["DOB"] = dob.group()

    aadhaar = re.search(r"\d{4}\s\d{4}\s\d{4}", text)

    if aadhaar:
        data["Document Number"] = aadhaar.group()

    pan = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)

    if pan:
        data["Document Number"] = pan.group()

    for line in text.split("\n"):

        if len(line.split()) >= 2:

            if line.replace(" ", "").isalpha():

                data["Name"] = line

                break

    return data