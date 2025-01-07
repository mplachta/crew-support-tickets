import os
import pandas as pd
import glob

"""
This script reads the most recent hubspot-knowledge CSV file and selects only the required columns.
It then saves the filtered data to a new CSV file used for the CrewAI Enterprise Knowledge Base.

In order to export knowledge from HubSpot:
1. Go to https://app.hubspot.com/knowledge/45732688/164382084353/articles/state/all
2. Select all articles (make sure your pagination includes all articles)
3. Click Actions > Export knowledge base articles
4. Download the CSV file sent to your email
5. Place it in the knowledge-prep directory
6. Run this script
"""

# Find the most recent hubspot-knowledge CSV file
latest_file = max(glob.glob('knowledge-prep/hubspot-knowledge*.csv'), key=os.path.getctime)

# Read the CSV file
df = pd.read_csv(latest_file)

# Select only the required columns
filtered_df = df[['Article title', 'Article subtitle', 'Article URL', 'Article body', 'Category', 'Keywords']]

# Save the filtered data to the new CSV file
filtered_df.to_csv('knowledge/enterprise_kb.csv', index=False)
