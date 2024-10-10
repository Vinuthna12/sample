import asyncio
import threading
import time
import aiohttp

async def fetch(session, url):
    
    #Fetch a URL asynchronously using aiohttp.
    try:
        async with session.get(url) as response:
        # Check if the request was successful
            if response.status == 200:
                return await response.text()
            else:
                return f"Error: {response.status}"
            #handles exception if url fails to respond
    except Exception as e:
        print("url fails to respond",e)

async def fetch_all(urls):
    
    #Fetching multiple URLs concurrently.   
    # Creating an aiohttp session
    
    async with aiohttp.ClientSession() as session:
        # Creating a list of tasks to fetch each URL
        tasks = [fetch(session, url) for url in urls]
        # Run all tasks concurrently and wait for them to complete
        results = await asyncio.gather(*tasks)
       
        return results


def run_async(urls):
    results = asyncio.run(fetch_all(urls))
    return results

def main():
    # List of URLs to fetch
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net'
    ]

    #time taken by all urls

    start_time = time.time()
    
    #calculating time using threading
    # Creating a thread to run the asynchronous code
    thread = threading.Thread(target=run_async, args=(urls,))
    thread.start()
    thread.join()  # Wait for the thread to finish
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken to fetch URLs using threading : {total_time:.2f} seconds")

    #calculating time using asyncio
    results = asyncio.run(fetch_all(urls))
    end_time = time.time()
    Total_Time = end_time-start_time
    print(f"Total time taken to fetch urls using asyncio is:{Total_Time:.2f} seconds")

    # Run the event loop and fetch all URLs
    results = asyncio.run(fetch_all(urls))
    
    # Print the results
    for url, content in zip(urls, results):
        print(f"URL: {url}\nContent Length: {len(content)}\n")
      # Print content of each page
        print(content)  
if __name__ == '__main__':
    main()
