from services.liveness_service import check_liveness
from services.report_service import generate_report
from services.trust_service import calculate_trust
from services.forgery_service import check_forgery
from services.document_parser import parse_document
from services.ocr_service import extract_text
from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/verify")
async def verify_document(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )
        

    text = extract_text(file_path)
    document = parse_document(text)
    forgery = check_forgery(file_path)
    liveness = check_liveness(file_path)
    trust = calculate_trust(
    document,
    forgery,
    liveness
)
    report = generate_report(
    document,
    forgery,
    trust
)
    return{

    "status":"success",

    "document":document,

    "forgery":forgery,

    "liveness":liveness,

    "trust":trust,

    "report":report

}