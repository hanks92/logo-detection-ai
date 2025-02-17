from icrawler.builtin import GoogleImageCrawler
import os


logos = ["Google logo", "Microsoft logo", "Apple logo", "Intel logo", "Nvidia logo"]


dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)

for logo in logos:
    
    folder = os.path.join(dataset_dir, logo.replace(" ", "_"))
    os.makedirs(folder, exist_ok=True)
    
    print(f"Téléchargement de 50 images pour '{logo}' dans le dossier '{folder}'...")
    
   
    google_crawler = GoogleImageCrawler(storage={'root_dir': folder})
    
    
    google_crawler.crawl(keyword=logo, max_num=50)
    
    print(f"Terminé pour {logo}.\n")
