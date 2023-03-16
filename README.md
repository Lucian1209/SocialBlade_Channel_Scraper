# SocialBlade Channel Scraper
This project is a simple scraper that extracts similar channels for a given YouTube channel ID from the website SocialBlade. The scraper uses Undetected Chromium to bypass Cloudflare bot protection.

## Installation
Clone this repository to your local machine.
Install Docker if you haven't already.
Build the Docker image using the provided Dockerfile: `docker build -t socialblade-scraper` .
## Usage
1. Make sure you have a PostgreSQL database set up and running on your local machine.
2. Create a table in the database to store the scraped data. The table should have the following columns:

   * `id` (integer)
  
   * `channel_id` (text)
  
   *  `name` (text)
  
   * `url` (text)
  
    * `description` (text)
  
    * `subscribers` (integer)
  
    * `views` (integer)
  
     * `uploads` (integer)
  
    * `country` (text)
  
3. Update the database connection parameters in `config.ini` to match your local setup.
4. Run the scraper using the following command:
   `docker run -v $(pwd)/logs:/app/logs socialblade-scraper python main.py`
  * This will mount a logs directory to the container and write the log files there.
5. The scraper will start running, fetching channel data for each channel ID in the database and storing the scraped data in the PostgreSQL table.
## Configuration
You can configure the following settings in the `config.ini` file:

  * `DATABASE_HOST`: The hostname or IP address of the PostgreSQL server.
  * `DATABASE_PORT`: The port on which the PostgreSQL server is listening.
  * `DATABASE_NAME`: The name of the PostgreSQL database to use.
  * `DATABASE_USER`: The username to use to connect to the PostgreSQL database.
  * `DATABASE_PASSWORD`: The password to use to connect to the PostgreSQL database.
  * `PROXY_HOST`: The hostname or IP address of the proxy server to use (optional).
  * `PROXY_PORT`: The port on which the proxy server is listening (optional).
  * `LOG_FILE`: The name of the log file to write to (optional).
## Credits
This project was created by Artem Babych.
