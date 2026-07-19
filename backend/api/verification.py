import os
from fastapi import APIRouter, UploadFile, File, HTTPException

from services.database_service import save_verification
from services.trust_service import calculate_trust_score
from services.face_service import detect_face
from services.ocr_service import extract_text
from services.liveness_service import check_liveness
from services.report_service import generate_report
from services.forgery_service import check_forgery
from services.document_parser import parse_document

router = APIRouter(
    prefix="/api",
    tags=["Verification"]
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/verify")
async def verify_document(
    document: UploadFile = File(...),
    selfie: UploadFile = File(...)
):
    try:

        # ---------------- Save Uploaded Files ----------------

        document_path = os.path.join(
            UPLOAD_FOLDER,
            document.filename
        )

        selfie_path = os.path.join(
            UPLOAD_FOLDER,
            selfie.filename
        )

        with open(document_path, "wb") as f:
            f.write(await document.read())

        with open(selfie_path, "wb") as f:
            f.write(await selfie.read())

        # ---------------- OCR ----------------

        ocr_text = extract_text(document_path)

        # ---------------- Parse Document ----------------

        document_data = parse_document(ocr_text)

        # ---------------- Face Detection ----------------

        face_result = detect_face(selfie_path)

        # ---------------- Liveness ----------------

        liveness = check_liveness(selfie_path)

        # ---------------- Forgery ----------------

        forgery = check_forgery(document_path)

        # ---------------- Trust Score ----------------

        trust = calculate_trust_score(
            face_result,
            ocr_text,
            forgery,
            liveness,
            document_data
        )

        # ---------------- Final Data ----------------

        verification_data = {

            "document": document_data,

            "ocr": {
                "text": ocr_text
            },

            "face": face_result,

            "liveness": liveness,

            "forgery": forgery,

            "trust": trust
        }

        # ---------------- Save Database ----------------

        save_verification(verification_data)

        # ---------------- Generate PDF ----------------

        report = generate_report(verification_data)

        # ---------------- API Response ----------------

        return {

            "success": True,

            "message": "Verification completed successfully.",

            "document": document_data,

            "ocr": verification_data["ocr"],

            "face": face_result,

            "liveness": liveness,

            "forgery": forgery,

            "trust": trust,

            "report": report

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )