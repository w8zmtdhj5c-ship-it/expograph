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

# Create output folder
os.makedirs("base", exist_ok=True)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    )
}

for url in urls:
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        if response.status_code == 200:

            # Get filename from URL
            filename = os.path.basename(url.rstrip("/"))

            if not filename.endswith(".html"):
                filename += ".html"

            filepath = os.path.join("base", filename)

            # Detect encoding from HTTP headers / HTML
            response.encoding = response.apparent_encoding

            # Decode content correctly
            html_text = response.text

            # Save explicitly as UTF-8
            with open(
                filepath,
                "w",
                encoding="utf-8",
                newline=""
            ) as file:
                file.write(html_text)

            print(f"Successfully saved -> {filepath}")
            print(f"Encoding used: {response.encoding}")

        else:
            print(
                f"Failed to download {url}. "
                f"Status: {response.status_code}"
            )

    except Exception as error:
        print(f"Error downloading {url}: {error}")