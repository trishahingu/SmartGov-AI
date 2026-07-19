from datetime import datetime

def save_verification(data):
    data["created_at"] = datetime.now()
    print("Database disabled. Verification not saved.")
    return True