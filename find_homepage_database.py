import pandas as pd

# Load university database
df = pd.read_csv("/workspaces/PhD-Data/universities_list_with_homepages.csv")

# Show sample output
print(df.head())

print("✅ Process completed! Using static university database.")
