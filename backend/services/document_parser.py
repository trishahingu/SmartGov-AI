import re


def clean_text(text):
    text = text.replace("|", " ")
    text = text.replace(":", " ")
    text = text.replace(",", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_aadhaar(text):

    match = re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", text)

    if match:
        return match.group()

    match = re.search(r"\b\d{12}\b", text)

    if match:
        num = match.group()
        return f"{num[:4]} {num[4:8]} {num[8:]}"

    return "Not Found"


def extract_dob(text):

    patterns = [

        r"\d{2}/\d{2}/\d{4}",

        r"\d{2}-\d{2}-\d{4}",

        r"\d{4}-\d{2}-\d{2}"

    ]

    for p in patterns:

        match = re.search(p, text)

        if match:
            return match.group()

    return "Not Found"


def extract_gender(text):

    lower = text.lower()

    if re.search(r"\bfemale\b", lower):
        return "Female"

    if re.search(r"\bmale\b", lower):
        return "Male"

    if re.search(r"\bother\b", lower):
        return "Other"

    return "Not Found"


def extract_name(ocr_text):

    lines = [line.strip() for line in ocr_text.split("\n")]

    ignore = [

        "government",

        "india",

        "aadhaar",

        "authority",

        "uidai",

        "unique",

        "dob",

        "birth",

        "male",

        "female",

        "address",

        "year",

        "vid",

        "help",

        "www",

        "resident",

        "enrolment",

        "download"

    ]

    candidates = []

    for line in lines:

        if len(line) < 3:
            continue

        lower = line.lower()

        if any(word in lower for word in ignore):
            continue

        if re.search(r"\d", line):
            continue

        if len(line.split()) > 4:
            continue

        if re.search(r"[A-Za-z]", line):

            candidates.append(line)

    if candidates:

        return max(candidates, key=len)

    return "Not Found"


def detect_document_type(text):

    lower = text.lower()

    # Aadhaar Card
    if (
        "aadhaar" in lower
        or "uidai" in lower
        or "unique identification authority of india" in lower
    ):
        return "Aadhaar Card"

    # PAN Card
    if (
        "income tax department" in lower
        or "permanent account number" in lower
        or "income tax" in lower
    ):
        return "PAN Card"

    # Driving License
    if (
        "driving licence" in lower
        or "driving license" in lower
        or "licence no" in lower
        or "license no" in lower
    ):
        return "Driving License"

    # Passport
    if (
        "passport" in lower
        or "republic of india" in lower
    ):
        return "Passport"

    # Voter ID
    if (
        "election commission of india" in lower
        or "elector photo identity card" in lower
        or "epic" in lower
    ):
        return "Voter ID"

    return "Unknown Document"


def parse_document(ocr_text):

    cleaned = clean_text(ocr_text)

    return {

        "document_type": detect_document_type(cleaned),

        "name": extract_name(ocr_text),

        "aadhaar_number": extract_aadhaar(cleaned),

        "dob": extract_dob(cleaned),

        "gender": extract_gender(cleaned)

    }
