import requests
from bs4 import BeautifulSoup

# URL of the Wimbledon Gentlemen's Singles draw
url = 'https://www.wimbledon.com/en_GB/draws/gentlemens-singles/full'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/115.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',  # optional but can help
}

# Send a GET request to fetch the page content
response = requests.get(url, headers=headers)
response.raise_for_status()  # Ensure the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

print(response.status_code)
print(response.url)
print(response.text)


# # Find the main draw table; it's typically the first table on the page
# draw_table = soup.find('table', {'class': 'draw-table'})

# # Initialize a list to store player names
# players = []

# # Iterate over each row in the table (excluding the header)
# for row in draw_table.find_all('tr')[1:]:
#     # Extract player names from the first and second columns
#     cols = row.find_all('td')
#     if len(cols) > 1:
#         player1 = cols[0].get_text(strip=True)
#         player2 = cols[1].get_text(strip=True)
#         players.extend([player1, player2])

# # Remove any empty strings from the list
# players = [player for player in players if player]

# # Print the list of players
# for player in players:
#     print(player)
