import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the QS World University Rankings page
qs_url = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2024'

# Send a GET request to the QS rankings page
qs_response = requests.get(qs_url)
qs_soup = BeautifulSoup(qs_response.text, 'html.parser')

# Extract university names and rankings from the QS page
qs_rankings = []
for row in qs_soup.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) > 1:
        rank = cols[0].text.strip()
        university = cols[1].text.strip()
        qs_rankings.append({'University': university, 'QS_Rank': rank})

# Convert QS rankings to DataFrame
qs_df = pd.DataFrame(qs_rankings)

# URL of the THE World University Rankings page
the_url = 'https://www.timeshighereducation.com/world-university-rankings/2024/world-ranking'

# Send a GET request to the THE rankings page
the_response = requests.get(the_url)
the_soup = BeautifulSoup(the_response.text, 'html.parser')

# Extract university names and rankings from the THE page
the_rankings = []
for row in the_soup.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) > 1:
        rank = cols[0].text.strip()
        university = cols[1].text.strip()
        the_rankings.append({'University': university, 'THE_Rank': rank})

# Convert THE rankings to DataFrame
the_df = pd.DataFrame(the_rankings)
# Load your existing list of universities
universities_df = pd.read_csv('universities_list.csv')

# Merge with QS rankings
merged_df = pd.merge(universities_df, qs_df, how='left', left_on='Name', right_on='University')

# Merge with THE rankings
merged_df = pd.merge(merged_df, the_df, how='left', left_on='Name', right_on='University')

# Drop redundant 'University' columns from merges
merged_df = merged_df.drop(columns=['University_x', 'University_y'])

# Save the updated DataFrame to a new CSV file
merged_df.to_csv('universities_with_rankings.csv', index=False)
