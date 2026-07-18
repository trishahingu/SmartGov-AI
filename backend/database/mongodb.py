from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["smartgov_ai"]

verification_collection = db["verifications"]