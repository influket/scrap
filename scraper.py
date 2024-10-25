import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import os

def scrape_nse():
    # r4jajkChqpsuuQlA
    mongo_uri = os.getenv('MONGODB_URI')  # Use an environment variable for security
    client = MongoClient(mongo_uri)
    db = client['nse_database']
    collection = db['nse_data']

    url = 'https://www.nseindia.com/market-data/live-equity-market'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []  # Add your data extraction logic here

        # Example: Insert data into MongoDB
        if data:
            collection.insert_many(data)
            print("Data saved to MongoDB!")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == '__main__':
    scrape_nse()
