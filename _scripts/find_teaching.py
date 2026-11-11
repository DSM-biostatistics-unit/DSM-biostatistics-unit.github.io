import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://degree.units.it"

DOCENTI = [
    "GANDIN ILARIA",
    "BARBATI GIULIA",
    "TORELLI LUCIO",
]

# Per ora partiamo dalle pagine del catalogo 2025/2026
URLS = [
    "https://degree.units.it/it/0320107300700001/area-studenti/insegnamenti/2025/",
]

for url in URLS:
    print(f"\nControllo: {url}")

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = urljoin(BASE, link["href"])
        text = link.get_text(" ", strip=True)

        if "/insegnamenti/2025/" in href:
            print(text, "->", href)

