import os
from services.database_service import save_verification
from services.trust_service import calculate_trust_score
from services.face_service import detect_face
from services.ocr_service import extract_text
from services.liveness_service import check_liveness
from services.report_service import generate_report
from services.forgery_service import check_forgery
from services.document_parser import parse_document
from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/api",
    tags=["Verification"]
)

@router.post("/verify")
async def verify_document(
    document: UploadFile = File(...),
    selfie: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    document_path = f"uploads/{document.filename}"
    selfie_path = f"uploads/{selfie.filename}"

    with open(document_path, "wb") as f:
        f.write(await document.read())

    with open(selfie_path, "wb") as f:
        f.write(await selfie.read())

    # OCR

    ocr_text = extract_text(document_path)

    forgery = check_forgery(document_path)

    liveness = check_liveness(selfie_path)

    document_data = parse_document(ocr_text)

    face_result = detect_face(selfie_path)

    trust = calculate_trust_score(face_result, ocr_text, forgery,liveness)
    verification_data = {

    "document": document_data,

    "ocr": ocr_text,

    "face": face_result,

    "forgery": forgery,

    "liveness": liveness,

    "trust": trust

}

    save_verification(verification_data)

    return {

    "status": "success",

    "document": document.filename,

    "selfie": selfie.filename,

    "document_data": document_data,

    "ocr": {
        "text": ocr_text
    },

    "face": face_result,

    "forgery": forgery,

    "trust": trust

}