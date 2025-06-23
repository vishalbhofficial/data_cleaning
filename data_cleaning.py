import pandas as pd

df = pd.read_csv("netflix_titles.csv")
# It loads the dataset 

df = df.dropna(subset=["date_added", "rating", "duration"])
# Drop rows with missing critical fields

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
# Fill missing non-critical fields with "Unknown"

df = df.drop_duplicates()
# Remove duplicates

df["type"] = df["type"].str.strip().str.title()
df["country"] = df["country"].str.strip()
# It Standardize text fields 

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
# Convert date_added to datetime

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
# Clean column names

df.to_csv("netflix_titles_cleaned.csv", index=False)
# Save cleaned dataset

print("✅ Data Cleaned Successfully and file saved as 'netflix_titles_cleaned.csv'")
# print the statement after a code run