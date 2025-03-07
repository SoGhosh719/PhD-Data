import csv
import time
import requests
import os

# Google Custom Search API Key & CSE ID
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "your_google_api_key_here")
CSE_ID = os.getenv("CSE_ID", "your_cse_id_here")

input_file = "/workspaces/PhD-Data/universities_list.csv"
output_file = "/workspaces/PhD-Data/universities_with_google_cse.csv"

# Function to get university homepage using Google CSE
def get_university_homepage(university_name):
    try:
        url = f"https://www.googleapis.com/customsearch/v1?q={university_name} official site&cx={CSE_ID}&key={GOOGLE_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["items"][0]["link"] if "items" in data else "Not Found"
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
