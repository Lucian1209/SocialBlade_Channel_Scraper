from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome, ChromeOptions
from database.database import Database

class Scraper:
    def __init__(self, proxy=None):
        self.proxy = proxy
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        if self.proxy:
            chrome_options.add_argument(f'--proxy-server={self.proxy}')
        self.driver = Chrome(options=chrome_options)

    def scrape_similar_channels(self, channel_id):
        url = f'https://socialblade.com/youtube/channel/{channel_id}/similarrank/sbscore'
        self.driver.get(url)
        # Add scraping logic here to get the similar channels
        # You can use Selenium to find the elements and extract the information

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    # Connect to the database
    db = Database(host='localhost', port=5432, user='postgres', password='password', dbname='mydatabase')
    # Get the channel IDs from the database
    channel_ids = db.get_channel_ids()
    # Create a scraper object
    scraper = Scraper()
    # Loop through the channel IDs and scrape the similar channels
    for channel_id in channel_ids:
        scraper.scrape_similar_channels(channel_id)
    # Close the scraper and database connections
    scraper.close()
    db.close()