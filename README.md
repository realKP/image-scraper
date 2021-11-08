# image_scraper

Microservice for scraping image URLs from Google Images based on provided keywords. Microservice connects via Python sockets.

This project includes 3 files:
- image_scraper.py
- server.py
- client_example.py

**IMPORTANT NOTE:** This microservice works by using Google Chrome. If you do not have Google Chrome installed, please install before starting.

Required packages:
- pip install selenium

How to Start:
1. Download and unzip project in desired working directory.
2. Visit https://chromedriver.chromium.org/downloads and download the driver matching your major version of Chrome. [How to check your version of Chrome](https://www.google.com/chrome/update/)
3. Unzip the driver folder and move the executable file to the working directory.
4. Open a terminal for the server and run: python server.py
5. Open another terminal for the client and run: python client_example.py
