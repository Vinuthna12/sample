import aiohttp
import asyncio
import pylance
from Flask.async import fetch_allasync import fetch_all

async def fetch(session,url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            return f"Error: {response.status}"
    async def fetch_all(urls):
        async with aiohttp.ClientSession() as session:
        # Create a list of tasks to fetch each URL
            tasks = [fetch(session, url) for url in urls]
        # Run all tasks concurrently and wait for them to complete
            results = await asyncio.gather(*tasks)
            return results
def main():
    # List of URLs to fetch
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net'
    ]
    
    # Run the event loop and fetch all URLs
    results = asyncio.run(fetch_all(urls))
    
    # Print the results
    for url, content in zip(urls, results):
        print(f"URL: {url}\nContent Length: {len(content)}\n")
        # Uncomment the following line if you want to see the content
        # print(content[:200])  # Print first 200 characters of each page content

if __name__ == '__main__':
    main()

