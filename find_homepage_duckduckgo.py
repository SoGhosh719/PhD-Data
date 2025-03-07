import csv
import time
import requests

input_file = "/workspaces/PhD-Data/universities_list.csv"
output_file = "/workspaces/PhD-Data/universities_with_duckduckgo.csv"

# Function to get homepage using DuckDuckGo API
def get_university_homepage(university_name):
    try:
        url = f"https://api.duckduckgo.com/?q={university_name} official site&format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["RelatedTopics"][0]["FirstURL"] if "RelatedTopics" in data and data["RelatedTopics"] else "Not Found"
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
