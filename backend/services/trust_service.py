def calculate_trust_score(face_result, ocr_text, forgery, liveness, document=None):

    score = 0
    reasons = []

    if document is None:
        document = {}

    # ---------------- Face Detection ----------------

    if face_result.get("face_detected", False):
        score += 20
        reasons.append("Face detected successfully")
    else:
        reasons.append("Face not detected")

    # ---------------- Single Face ----------------

    if face_result.get("face_count", 0) == 1:
        score += 10
        reasons.append("Single face detected")
    elif face_result.get("face_count", 0) > 1:
        reasons.append("Multiple faces detected")

    # ---------------- OCR ----------------

    if ocr_text and len(ocr_text.strip()) > 20:
        score += 15
        reasons.append("OCR extracted readable text")
    else:
        reasons.append("Poor OCR quality")

    # ---------------- Document Fields ----------------

    if document.get("name") != "Not Found":
        score += 10
        reasons.append("Citizen name extracted")
    else:
        reasons.append("Citizen name missing")

    if document.get("aadhaar_number") != "Not Found":
        score += 10
        reasons.append("Aadhaar number extracted")
    else:
        reasons.append("Aadhaar number missing")

    if document.get("dob") != "Not Found":
        score += 5
        reasons.append("DOB extracted")
    else:
        reasons.append("DOB missing")

    if document.get("gender") != "Not Found":
        score += 5
        reasons.append("Gender extracted")
    else:
        reasons.append("Gender missing")

    # ---------------- Forgery ----------------

    status = forgery.get("status", "")

    if status == "Authentic":
        score += 15
        reasons.append("Document appears authentic")

    elif status == "Needs Manual Review":
        score += 8
        reasons.append("Forgery needs review")

    else:
        reasons.append("Forgery suspected")

    # ---------------- Liveness ----------------

    if liveness.get("live", False):
        score += 10
        reasons.append("Live face detected")

    elif liveness.get("confidence", 0) >= 70:
        score += 5
        reasons.append("Liveness requires review")

    else:
        reasons.append("Spoof suspected")

    score = max(0, min(100, score))

    if score >= 90:
        risk = "Low"
        status = "Verified"

    elif score >= 70:
        risk = "Medium"
        status = "Needs Review"

    else:
        risk = "High"
        status = "Rejected"

    return {

        "trust_score": score,

        "status": status,

        "risk_level": risk,

        "reasons": reasons,

        "face": face_result,

        "forgery": forgery,

        "liveness": liveness
    }