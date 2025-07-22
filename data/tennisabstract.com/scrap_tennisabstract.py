import pandas as pd

# URL for Carlos Alcaraz match stats
# url = "https://www.tennisabstract.com/cgi-bin/player.cgi?p=CarlosAlcaraz"
url = "https://tennisabstract.com/reports/atpRankings.html"

# Use read_html to extract tables
tables = pd.read_html(url)

# Print number of tables found
print(f"Found {len(tables)} tables")
# print(tables)

# Preview
df = tables[1]
print(df.head())

df1 = df.iloc[:128]
print(df1)

