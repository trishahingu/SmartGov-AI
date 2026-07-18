def calculate_trust_score(face_result, ocr_text, forgery, liveness):
    score = 0
    reasons = []

    # Face Detection
    if face_result.get("face_detected"):
        score += 30
        reasons.append("Face detected successfully")
    else:
        reasons.append("No face detected")

    # Exactly one face
    if face_result.get("face_count") == 1:
        score += 20
        reasons.append("Single face found")
    elif face_result.get("face_count", 0) > 1:
        reasons.append("Multiple faces detected")

    # OCR
    if ocr_text and len(ocr_text.strip()) > 20:
        score += 30
        reasons.append("OCR extracted readable text")
    else:
        reasons.append("Poor OCR quality")

    # Forgery
    if forgery["status"] == "Authentic":
        score += 20
        reasons.append("Document appears authentic")

    elif forgery["status"] == "Needs Manual Review":
        score += 10
        reasons.append("Manual review recommended")

    else:
        reasons.append("Forgery suspected")

        # Liveness
    if liveness["status"] == "Live":
        score += 20
        reasons.append("Live face detected")
    elif liveness["status"] == "Review Required":
        score += 10
        reasons.append("Liveness requires review")
    else:
        reasons.append("Possible spoof attempt")    
    # Reserved for forgery detection
    score += 20

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
        "risk_level": risk,
        "status": status,
        "reasons": reasons,
        "liveness": liveness,
    }