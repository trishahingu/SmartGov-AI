import re

def parse_document(ocr_text):
    data = {
        "document_type": "Unknown",
        "name": None,
        "aadhaar_number": None,
        "dob": None,
        "gender": None
    }

    text = ocr_text.replace("\n", " ")

    # Detect Aadhaar
    if "aadhaar" in text.lower() or "government of india" in text.lower():
        data["document_type"] = "Aadhaar Card"

    # Aadhaar Number
    aadhaar = re.search(r"\b\d{4}\s?\d{4}\s?\d{4}\b", text)

    if aadhaar:
        data["aadhaar_number"] = aadhaar.group()

    # DOB
    dob = re.search(r"\d{2}/\d{2}/\d{4}", text)

    if dob:
        data["dob"] = dob.group()

    # Gender
    if "male" in text.lower():
        data["gender"] = "Male"

    elif "female" in text.lower():
        data["gender"] = "Female"

    # Name
    lines = ocr_text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2:

            if not any(char.isdigit() for char in line):

                if len(line) < 40:

                    data["name"] = line

                    break

    return data