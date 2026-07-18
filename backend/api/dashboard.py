from fastapi import APIRouter
from database.mongodb import verification_collection

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/history")
def history():

    data = []

    for item in verification_collection.find():

        item["_id"] = str(item["_id"])

        data.append(item)

    return data