from ultralytics import YOLO
import cv2

# Charger le modèle
model = YOLO("runs/detect/train4/weights/best.pt")

# Image à tester
image_path = "dataset/test/images/000044_jpg.rf.496f6574f04d8491045ce2db1823cd3b.jpg"  # Remplace par une image réelle

# Faire la prédiction
results = model(image_path)

# Enregistrer l’image annotée
for result in results:
    image_annotated = result.plot()  # Génère une image avec les annotations
    output_path = "output_detected.jpg"
    cv2.imwrite(output_path, image_annotated)  # Sauvegarde l’image détectée
    print(f"✅ Image détectée enregistrée sous : {output_path}")