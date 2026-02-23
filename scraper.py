import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_data():
    url = "https://news.ycombinator.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This finds the very first headline on the page
        first_row = soup.find('span', class_='titleline')
        if first_row:
            headline = first_row.text
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # This creates (or opens) a file called log.csv to save the data
            with open('log.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([date, headline])
            
            print(f"Success! Saved: {headline}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_data()
