# -*- coding: utf-8 -*-
"""University_Database_RAW

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DVUEq2ZwqRu2UUFxmP8-zDZpR63Fowfv
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
University_Database_RAW = pd.read_csv(io.BytesIO(uploaded['University_Database_RAW.csv']))
print(University_Database_RAW)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set a user-agent header to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# URL for Clark University Graduate Programs
url = "https://www.clarku.edu/graduate-education/graduate-programs/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all Areas of Study (Departments)
    areas_of_study = soup.find_all("div", class_="accordion-item")

    data = []

    for area in areas_of_study:
        # Extract Department Name
        department = area.find("h3").text.strip() if area.find("h3") else "Unknown Department"

        # Find all course lists inside the department
        course_lists = area.find_all("ul")  # Courses are inside <ul> lists

        for course_list in course_lists:
            courses = course_list.find_all("li")  # Find all <li> items inside <ul>

            for course in courses:
                course_name_tag = course.find("a")  # Course names are inside <a> tags
                if course_name_tag:
                    course_name = course_name_tag.text.strip()
                    course_url = course_name_tag["href"] if "href" in course_name_tag.attrs else "No URL"

                    data.append([department, course_name, course_url])

    # Convert to DataFrame
    courses_df = pd.DataFrame(data, columns=["Department", "Course Name", "Course URL"])

    # Save to CSV instead of using ace_tools
    courses_df.to_csv("clark_university_courses.csv", index=False)

    print("Data successfully saved to clark_university_courses.csv")
    print(courses_df.head())  # Show first 5 rows in console

else:
    print("Failed to fetch webpage:", response.status_code)

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

url = "https://www.clarku.edu/graduate-education/graduate-programs/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Print a sample of the HTML for debugging
    print(soup.prettify())  # Shows the page structure

else:
    print("Failed to fetch webpage:", response.status_code)

!pip install selenium webdriver-manager

!apt-get update
!apt-get install -y google-chrome-stable

!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!chmod +x chromedriver
!mv chromedriver /usr/bin/

!google-chrome --version

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import shutil

# Locate the Chrome binary
chrome_path = shutil.which("google-chrome")

# Configure Chrome for Colab
chrome_options = Options()
chrome_options.binary_location = chrome_path  # Set the correct Chrome binary path
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up ChromeDriver
service = Service("/usr/bin/chromedriver")  # Explicitly set the ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test if it works
driver.get("https://www.google.com")
print("Selenium is working!")
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening a browser

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL for Clark University Graduate Programs
url = "https://www.clarku.edu/graduate-education/graduate-programs/"
driver.get(url)

# Get the page source after JavaScript loads
page_source = driver.page_source
driver.quit()  # Close the browser

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find all Areas of Study (Departments)
areas_of_study = soup.find_all("div", class_="accordion-item")

data = []

for area in areas_of_study:
    department = area.find("h3").text.strip() if area.find("h3") else "Unknown Department"

    # Find courses within the department
    course_lists = area.find_all("ul")

    for course_list in course_lists:
        courses = course_list.find_all("li")

        for course in courses:
            course_name_tag = course.find("a")
            if course_name_tag:
                course_name = course_name_tag.text.strip()
                course_url = course_name_tag["href"] if "href" in course_name_tag.attrs else "No URL"
                data.append([department, course_name, course_url])

# Convert to DataFrame
courses_df = pd.DataFrame(data, columns=["Department", "Course Name", "Course URL"])

# Save to CSV
courses_df.to_csv("clark_university_courses.csv", index=False)

print("Data successfully saved to clark_university_courses.csv")
print(courses_df.head())  # Show first 5 rows