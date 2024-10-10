import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    """Fetch the webpage content for the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except Exception as e:
        print(f'Page cannot load due to: {e}')
        return None

def parse_quotes(soup):
    """Parse quotes from the BeautifulSoup object."""
    quotes_list = []
    names_list = []
    tags_list = []

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        # Extracting the quote text
        quote_text = quote.find('span', class_='text')
        quotes_list.append(quote_text.text if quote_text else 'Data not found')

        # Extracting the author name
        author_name = quote.find('small', class_='author')
        names_list.append(author_name.text if author_name else 'Data not found')

        # Extracting the tags
        tags = quote.find_all('a', class_='tag')
        tags_list.append(", ".join(tag.text for tag in tags) if tags else 'No tags')

    return quotes_list, names_list, tags_list

def extract_all_quotes(start_url):
    """Main function to extract all quotes from the given URL and handle pagination."""
    all_quotes = []
    all_authors = []
    all_tags = []

    url = start_url

    while url:
        page_content = fetch_page(url)
        if page_content is None:
            break
        
        soup = BeautifulSoup(page_content, 'html.parser')
        quotes, authors, tags = parse_quotes(soup)

        all_quotes.extend(quotes)
        all_authors.extend(authors)
        all_tags.extend(tags)

        # Finding the next page URL
        next_button = soup.find('li', class_='next')
        url = next_button.find('a')['href'] if next_button else None

        # Construct the full URL for the next request
        if url:
            url = f'http://quotes.toscrape.com{url}'

    # Creating a DataFrame with columns: quote text, author, tags
    df = pd.DataFrame({
        'quotes_text': all_quotes,
        'author_names': all_authors,
        'tags': all_tags
    })
    
    return df

# Example usage
df_quotes = extract_all_quotes('http://quotes.toscrape.com/')
df_quotes.to_csv('all_quotes.csv', index=False)

