from services.face_service import detect_face

image_path = "uploads/Screenshot 2026-07-17 083719.png"   # Change to your uploaded image name

result = detect_face(image_path)

print(result)