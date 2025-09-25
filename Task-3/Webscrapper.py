import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)
if response.status_code != 200:
    print("Failed to fetch the webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text:  # avoid empty strings
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for idx, headline in enumerate(headlines, start=1):
        f.write(f"{idx}. {headline}\n")

print("✅ Headlines scraped and saved to headlines.txt")
