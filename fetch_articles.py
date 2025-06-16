import requests
from bs4 import BeautifulSoup
import os

# Define topics and URLs
TOPICS = {
    "lupus": "https://www.mayoclinic.org/diseases-conditions/lupus/symptoms-causes/syc-20365789",
    "diabetes": "https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444",
    "asthma": "https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653"
    # add more topics & URLs as needed
}

def fetch_mayo_article(topic, url, save_dir="data"):
    os.makedirs(save_dir, exist_ok=True)
    print(f"🔍 Fetching Mayo article for {topic}...")
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # Mayo Clinic article typically uses <div class="content"> tags
    content_div = soup.find("div", class_="content")
    paragraphs = content_div.find_all("p") if content_div else []
    text = "\n\n".join([p.get_text(strip=True) for p in paragraphs])

    if not text.strip():
        print(f"⚠️ No content found for {topic}")
        return

    file_path = os.path.join(save_dir, f"{topic}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Saved: {file_path}")

if __name__ == "__main__":
    for topic, url in TOPICS.items():
        try:
            fetch_mayo_article(topic, url)
        except Exception as e:
            print(f"❌ Failed to fetch {topic}: {e}")
