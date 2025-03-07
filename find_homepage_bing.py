import csv
import time
import requests
import os

# Set your Bing API Key (Replace with your actual key)
BING_API_KEY = os.getenv("BING_API_KEY", "your_bing_api_key_here")  

# Input and output file paths
input_file = "/workspaces/PhD-Data/universities_list.csv"
output_file = "/workspaces/PhD-Data/universities_with_homepages.csv"

# Function to get university homepage using Bing API
def get_university_homepage(university_name):
    try:
        url = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
        params = {"q": university_name + " official site", "count": 1}

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise error if request fails

        data = response.json()
        homepage = data["webPages"]["value"][0]["url"] if "webPages" in data else "Not Found"
        return homepage
    except Exception as e:
        print(f"Error fetching {university_name}: {e}")
        return "Error"

# Read university names from CSV and fetch homepage URLs
with open(input_file, "r", encoding="utf-8-sig") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.DictReader(infile)

    # Fix BOM issue in CSV headers
    reader.fieldnames = [name.strip() for name in reader.fieldnames]
    if "\ufeffName" in reader.fieldnames:
        reader.fieldnames[reader.fieldnames.index("\ufeffName")] = "Name"

    # Ensure "Name" column exists
    if "Name" not in reader.fieldnames:
        print(f"Error: 'Name' column not found. Available columns: {reader.fieldnames}")
        exit()

    writer = csv.writer(outfile)
    writer.writerow(["Name", "Homepage URL"])  # Write header

    for row in reader:
        university_name = row.get("Name", "").strip()
        if university_name:
            homepage_url = get_university_homepage(university_name)
            writer.writerow([university_name, homepage_url])
            print(f"Fetched: {university_name} -> {homepage_url}")
            time.sleep(1)  # Avoid hitting API rate limits

print(f"✅ Process completed! Results saved in {output_file}")
