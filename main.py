import argparse
from scraper.scraper import Scraper
from database.database import Database

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--proxy', default=None, help='Proxy URL')
    args = parser.parse_args()

    # Connect to the database
    db = Database(host='localhost', port=5432, user='User', password='123456', dbname='mydatabase')
    # Get the channel IDs from the database
    channel_ids = db.get_channel_ids()
    # Create a scraper object with the specified proxy (if any)
    scraper = Scraper(proxy=args.proxy)
    # Loop through the channel IDs and scrape the similar channels
    for channel_id in channel_ids:
        scraper.scrape_similar_channels(channel_id)
    # Close the scraper and database connections
    scraper.close()
    db.close()