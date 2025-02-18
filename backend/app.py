import os
from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_cors import CORS  # Importation de flask-cors
from ultralytics import YOLO
import cv2

# Initialisation de l'application Flask et activation de CORS
app = Flask(__name__)
CORS(app)  # Permet toutes les origines

# Charger le modèle YOLO
MODEL_PATH = "../runs/detect/train4/weights/best.pt"
model = YOLO(MODEL_PATH)

# Dossiers pour stocker les fichiers téléchargés et les résultats
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
RESULT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "API YOLO prête 🚀. Faites un POST sur /detect avec une image."

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400

    file = request.files["file"]
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    # Lancer la détection
    results = model(filename)

    # Liste pour stocker les objets détectés
    detected_objects = []
    for result in results:
        for obj in result.boxes:
            # Extraire le label et le score de manière sécurisée
            label = result.names[int(obj.cls.item())]  # Convertir obj.cls en entier
            score = obj.conf.item()  # Score de confiance de la détection
            detected_objects.append({"label": label, "score": score})

    # Sauvegarder l'image annotée
    output_filename = "output_" + file.filename
    output_path = os.path.join(RESULT_FOLDER, output_filename)

    print(f"Image enregistrée sous : {output_path}")  # Log pour vérifier le chemin

    image_annotated = results[0].plot()  # Annoter l'image
    cv2.imwrite(output_path, image_annotated)

    # Vérification si l'image a été enregistrée correctement
    if not os.path.exists(output_path):
        return jsonify({"error": "Erreur lors de l'enregistrement de l'image annotée"}), 500

    # Retourner l'URL de l'image annotée et les objets détectés
    return jsonify({
        "image_url": f"/results/{output_filename}",  # Serve the image under the /results path
        "detected_objects": detected_objects
    })

@app.route('/results/<filename>')
def serve_image(filename):
    # Serve the image from the 'results' directory
    try:
        return send_from_directory(RESULT_FOLDER, filename)
    except FileNotFoundError:
        return jsonify({"error": "Image non trouvée"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
