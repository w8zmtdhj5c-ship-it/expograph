import requests
import os

urls = [
    "https://pub-industrie.com/nos-metiers/enseignes-lumineuses",
    "https://pub-industrie.com/nos-metiers/enseigne-publicitaire",
    "https://pub-industrie.com/nos-metiers/panneaux-publicitaires-lumineux",
    "https://pub-industrie.com/nos-metiers/panneaux-publicitaires-non-lumineux",
    "https://pub-industrie.com/nos-metiers/panneau-lumineux-drapeau",
    "https://pub-industrie.com/nos-metiers/panneau-de-publicite",
    "https://pub-industrie.com/nos-metiers/totem-publicitaire-lumineux",
    "https://pub-industrie.com/nos-metiers/signaletique",
    "https://pub-industrie.com/nos-metiers/habillage-voiture",
    "https://pub-industrie.com/nos-metiers/stickers-muraux",
    "https://pub-industrie.com/nos-metiers/habillage-de-magasin",
    "https://pub-industrie.com/nos-metiers/impression-serigraphie",
]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Extract the last part of the URL (e.g., 'impression-serigraphie')
            filename = os.path.basename(url.rstrip('/'))
            
            # If the link doesn't end with .html, add it automatically
            if not filename.endswith('.html'):
                filename = f"base/{filename}.html"
                
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Successfully saved as -> {filename}")
        else:
            print(f"Failed to download {url}. Status: {response.status_code}")
    except Exception as error:
        print(f"Error downloading {url}: {error}")