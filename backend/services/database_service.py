from database.mongodb import verification_collection
from datetime import datetime


def save_verification(data):

    data["created_at"] = datetime.now()

    verification_collection.insert_one(data)

    return True