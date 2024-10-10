import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making a request to the webpage
try:
    response = requests.get('http://quotes.toscrape.com/')
    response.raise_for_status()  # Raise an error for bad responses
except Exception as e:
    print(f'Page cannot load due to: {e}')
    exit()  # Exit if the page cannot be loaded

# Parsing the response text using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting all the quotes present in div tag with class 'quote'
quotes = soup.find_all('div', class_='quote')

# Creating lists to store respective data
quotes_list = []
names_list = []
tags_list = []

# To print the first 10 quotes from the homepage of quotes.toscrape
for quote in quotes[:10]:
    # Extracting the quote text
    quote_text = quote.find('span', class_='text')
    if quote_text:
        quotes_list.append(quote_text.text)
    else:
        quotes_list.append('Data not found')

    # Extracting the author name
    author_name = quote.find('small', class_='author')
    if author_name:
        names_list.append(author_name.text)
    else:
        names_list.append('Data not found')

    # Extracting the tags
    tags = quote.find_all('a', class_='tag')
    if tags:
        tags_list.append(", ".join(tag.text for tag in tags))  # Joining tags as a single string
    else:
        tags_list.append('No tags')

# Creating a DataFrame with columns: quote text, author, tags
df = pd.DataFrame({
    'quotes_text': quotes_list,
    'author_names': names_list,
    'tags': tags_list
})

# Saving the DataFrame to a CSV file
df.to_csv('quot.csv', index=False)
