import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):
    result = reader.readtext(image_path)

    text = "\n".join([item[1] for item in result])

    return text


def detect_document_type(text):

    text = text.upper()

    if "AADHAAR" in text or "GOVERNMENT OF INDIA" in text:
        return "Aadhaar Card"

    elif "INCOME TAX DEPARTMENT" in text or "PERMANENT ACCOUNT NUMBER" in text:
        return "PAN Card"

    elif "PASSPORT" in text:
        return "Passport"

    elif "DRIVING LICENCE" in text or "DRIVING LICENSE" in text:
        return "Driving License"

    return "Unknown Document"


def extract_fields(text):

    data = {
        "Name": "Not Found",
        "DOB": "Not Found",
        "Document Number": "Not Found"
    }

    # Date
    dob = re.search(r"\d{2}/\d{2}/\d{4}", text)

    if dob:
        data["DOB"] = dob.group()

    # Aadhaar
    aadhaar = re.search(r"\d{4}\s\d{4}\s\d{4}", text)

    if aadhaar:
        data["Document Number"] = aadhaar.group()

    # PAN
    pan = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)

    if pan:
        data["Document Number"] = pan.group()

    lines = text.split("\n")

    for line in lines:

        if len(line.split()) >= 2 and line.isupper():

            data["Name"] = line.title()

            break

    return data