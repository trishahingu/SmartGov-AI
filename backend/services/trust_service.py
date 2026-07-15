def calculate_trust(
    document,
    forgery,
    liveness
):

    score = 100

    reasons = []

    # Document Type

    if document["document_type"] == "Unknown":

        score -= 25

        reasons.append("Unknown document")

    # Document Number

    if document["document_number"] == "":

        score -= 15

        reasons.append("Document number not detected")

    # DOB

    if document["dob"] == "":

        score -= 10

        reasons.append("DOB not detected")

    # Forgery

    score = min(score, forgery["score"])

    if not liveness["face_detected"]:

        score -= 20

        reasons.append("Face not detected")
    if forgery["score"] < 75:

        reasons.append("Image quality is low")

    score = max(score, 0)

    if score >= 90:

        level = "HIGH"

    elif score >= 75:

        level = "MEDIUM"

    else:

        level = "LOW"

    return {

        "trust_score": score,

        "trust_level": level,

        "reasons": reasons

    }