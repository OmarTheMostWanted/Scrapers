import pandas as pd
import requests
from bs4 import BeautifulSoup

def search_product(product):

    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    
    # Replace this with the actual search URL
    url = f"https://www.amazon.nl/s?k={product}"
    
    # Send a GET request
    response = requests.get(url , headers=HEADERS)
    
    # Parse the response text with BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Check if the product was found (this will depend on the structure of the webpage)
    result_list = soup.find('span', text="s-search-results")

    print(result_list)

    return 1;

def main():
    # Read the CSV file
    df = pd.read_csv('./vi_io_guide-partial.csv')
    
    # loop over all row of the first column except the first row

    # Iterate over the products
    for product in df.iloc[:, 0]:
        # Search for the product
        found = search_product(product)
        
        # if found:
        #     print(f"Product '{product}' found: {found}")

if __name__ == "__main__":
    main()
