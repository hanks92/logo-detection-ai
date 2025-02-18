from flask import Flask, request, send_file
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)

# Charger le modèle YOLO entraîné
MODEL_PATH = "../runs/detect/train4/weights/best.pt"
model = YOLO(MODEL_PATH)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "API YOLO prête 🚀. Faites un POST sur /detect avec une image."

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return {"error": "Aucun fichier reçu"}, 400

    file = request.files["file"]
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    # Lancer la détection
    results = model(filename)
    for result in results:
        image_annotated = result.plot()

    # Sauvegarder l’image annotée
    output_path = os.path.join(RESULT_FOLDER, "output_" + file.filename)
    cv2.imwrite(output_path, image_annotated)

    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
