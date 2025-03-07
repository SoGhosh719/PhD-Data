import csv
import time
import os
from serpapi import GoogleSearch

# Set your SerpAPI key
SERPAPI_KEY = "6c9f861c7e1acce3f3eb543c5cd680eed06cae3805a737ddbb2c75a952e12c1d"

# Function to get the homepage URL of a university
def get_university_homepage(university_name):
    search = GoogleSearch({
        "q": f"{university_name} official site",
        "location": "United States",
        "api_key": SERPAPI_KEY
    })
    results = search.get_dict()
    try:
        homepage_url = results["organic_results"][0]["link"]
        return homepage_url
    except (KeyError, IndexError):
        return "Not Found"

# Read the university names from a CSV file
input_file = "universities_list.csv"  # Ensure this CSV has a column named "University"
output_file = "universities_with_homepages.csv"

universities = []
with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        universities.append(row["University"])

# Fetch URLs and write to a new CSV file
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["University", "Homepage"])

    for university in universities:
        url = get_university_homepage(university)
        print(f"Fetched URL for {university}: {url}")
        writer.writerow([university, url])
        time.sleep(2)  # Sleep to avoid rate limits

print(f"Saved results in {output_file}")
