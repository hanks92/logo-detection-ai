# Installer icrawler (si ce n'est pas déjà fait)
# pip install icrawler

from icrawler.builtin import GoogleImageCrawler
import os

# Liste des logos à collecter
logos = ["Google logo", "Microsoft logo", "Apple logo", "Intel logo", "Nvidia logo"]

# Créer le dossier principal pour le dataset
dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)

for logo in logos:
    # Créer un dossier pour le logo en remplaçant les espaces par des underscores
    folder = os.path.join(dataset_dir, logo.replace(" ", "_"))
    os.makedirs(folder, exist_ok=True)
    
    print(f"Téléchargement de 50 images pour '{logo}' dans le dossier '{folder}'...")
    
    # Créer un crawler Google pour ce logo
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder})
    
    # Lance la collecte : ajuste max_num si tu veux plus ou moins d'images
    google_crawler.crawl(keyword=logo, max_num=50)
    
    print(f"Terminé pour {logo}.\n")
