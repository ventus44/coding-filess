import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = 'https://www.opap.gr/klhrwseis-apotelesmata-powerspin'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find a specific element using its tag name and (optionally) its attributes
element = soup.find('tag_name', attrs={'attribute_name': 'attribute_value'})

# Extract the data from the element
data = element.text
