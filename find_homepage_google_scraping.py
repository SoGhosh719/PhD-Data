import csv
import time
import requests
from bs4 import BeautifulSoup

input_file = "/workspaces/PhD-Data/universities_list.csv"
output_file = "/workspaces/PhD-Data/universities_with_google_scraping.csv"

# Function to scrape Google search for homepage
def get_university_homepage(university_name):
    try:
        query = f"{university_name} official site"
        url = f"https://www.google.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find first search result
        for link in soup.select("a"):
            href = link.get("href")
            if "url?q=" in href and "google" not in href:
                return href.split("url?q=")[1].split("&")[0]
        return "Not Found"
    except Exception as e:
        print(f"Error fetching {university_name}: {e}")
        return "Error"

# Process universities list
with open(input_file, "r", encoding="utf-8-sig") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["Name", "Homepage URL"])

    for row in reader:
        university_name = row["Name"].strip()
        homepage_url = get_university_homepage(university_name)
        writer.writerow([university_name, homepage_url])
        print(f"Fetched: {university_name} -> {homepage_url}")
        time.sleep(1)

print(f"✅ Process completed! Results saved in {output_file}")
