import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://www.topuniversities.com/programs/north-america/phd/accounting-and-finance?region=[4011]&country=[US]&study_level=[5]&subjects=[455,4046,1601,3313,4049,477,581,3316,508,3830,1601]&pagerlimit=[25]"

# Headers to avoid getting blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a request to the website
response = requests.get(url, headers=headers)

# Check if the page was successfully retrieved
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the sections containing university details
    universities = []
    
    for uni in soup.find_all("div", class_="teaser__title"):
        name = uni.get_text(strip=True)
        link = uni.find("a")["href"] if uni.find("a") else "N/A"
        
        # Extract location (if available)
        location_tag = uni.find_next("div", class_="teaser__location")
        location = location_tag.get_text(strip=True) if location_tag else "Unknown"

        universities.append([name, location, link])

    # Convert to DataFrame
    df = pd.DataFrame(universities, columns=["University Name", "Location", "URL"])

    # Save to CSV
    csv_filename = "phd_accounting_finance_universities.csv"
    df.to_csv(csv_filename, index=False, encoding="utf-8")

    print(f"Data successfully saved to {csv_filename}")
else:
    print("Failed to retrieve the webpage. Check the URL or try again later.")
