import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_insider_trades(ticker):
    url = f"https://www.insiderscreener.com/en/company/{ticker}"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='table table-sm text-dark')

    if table is None:
        print("No table found for ticker:", ticker)
        return

    headers = [header.text.strip().replace('\n', ' ') for header in table.find_all('th')]

    data = []
    for row in table.find_all('tr')[1:]: 
        cols = [col.text.strip().replace('\n', ' ') for col in row.find_all('td')]
        data.append(cols)

    df = pd.DataFrame(data, columns=headers)

    filename = f'insider_trades_{ticker}.json'
    df.to_json(filename, orient='records', lines=True, indent=4)

    print(f"Data has been scraped and saved to '{filename}'")

ticker = input("Enter the ticker symbol: ")
scrape_insider_trades(ticker)
