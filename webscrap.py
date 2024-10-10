import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making a request to the webpage
try:
    response = requests.get('http://quotes.toscrape.com/')

# Parsing the response text using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
except Exception as e:
    print(f'page can not load due to {e}')

# Extracting all the quotes present in div tag with class 'quote'
quotes = soup.find_all('div', class_='quote')

# Creating lists to store respective data
quotes_list = []
names_list = []
tags_list = []
print(len(quotes))
# To print the first 10 quotes from the homepage of quotes.toscrape
for quote in quotes[:10]:
    quote_text = quote.find('span', class_='text').text if quote.find('span', class_='text').text else f'data not found'
    print(quote_text)    
for quote in quotes:
    # Extracting the quote text and handling missing data
    quote_text = quote.find('span', class_='text').text if quote.find('span', class_='text').text else f'data not found'
    #appending quotes to list
    quotes_list.append(quote_text)
    #printing quotes
    print(quote_text)

    # Extracting the author name and handling missing data
    author_name = quote.find('small', class_='author').text if quote.find('small', class_='author').text else f'data not found'
    #appending author names to list
    names_list.append(author_name)
    #printing author names
    print(author_name)

    # Extracting the tags
    tags = [tag.text for tag in quote.find_all('a', class_='tag')] 
    # Joining tags as a single string and appending to list
    tags_list.append(", ".join(tags)) 
    #printing the tags 
    print(tags)

# Creating a DataFrame with columns: quote text, author, tags
df = pd.DataFrame({
    'quotes_text': quotes_list,
    'author_names': names_list,
    'tags': tags_list
})

#Saving the DataFrame to a CSV file
#df.to_csv('quotes.csv', index=False)
