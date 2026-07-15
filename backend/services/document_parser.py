import re


def parse_document(text):

    data = {

        "document_type": "Unknown",

        "name": "",

        "dob": "",

        "gender": "",

        "document_number": ""

    }

    # Aadhaar Detection
    aadhaar = re.search(r"\d{4}\s\d{4}\s\d{4}", text)

    if aadhaar:

        data["document_type"] = "Aadhaar"

        data["document_number"] = aadhaar.group()

    # PAN Detection
    pan = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)

    if pan:

        data["document_type"] = "PAN"

        data["document_number"] = pan.group()

    # DOB
    dob = re.search(r"\d{2}/\d{2}/\d{4}", text)

    if dob:

        data["dob"] = dob.group()

    # Gender

    if "MALE" in text.upper():

        data["gender"] = "Male"

    elif "FEMALE" in text.upper():

        data["gender"] = "Female"

    return data