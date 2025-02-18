import os
from bing_image_downloader import downloader

# Dossier où stocker les images
output_dir = "collecte/logos"

# Liste des logos à télécharger
logos = ["Google logo", "Microsoft logo", "Apple logo", "Intel logo", "Nvidia logo"]

# Créer le dossier s'il n'existe pas
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Télécharger les images
for logo in logos:
    print(f"Téléchargement des images pour {logo}...")
    try:
        downloader.download(logo, limit=50, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)
        print(f"Téléchargement terminé pour {logo} !")
    except Exception as e:
        print(f"Erreur lors du téléchargement pour {logo}: {e}")

print("Téléchargement terminé !")
