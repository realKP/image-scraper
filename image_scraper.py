import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_image_urls(keywords:str, max_links:int, wd:webdriver, sleep_time:int=1):
    """Helper function for image_scrape."""
    # Create google image URL and loads page
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    wd.get(search_url.format(q=keywords))

    # Initialize counters and set
    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_links:
        # Scrolls down page to load more images
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_time) 

        # Gets image thumbnail results
        thumbnail_results = wd.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
        number_results = len(thumbnail_results)

        for img in thumbnail_results[results_start:number_results]:
            # Tires to click thumbnail to get real image
            try:
                img.click()
                time.sleep(sleep_time)
            except Exception:
                continue

            # Extract image URLs
            actual_images = wd.find_elements(By.CSS_SELECTOR, 'img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)
            if len(image_urls) >= max_links:
                # Found number of images
                break
        else:
            time.sleep(30)
            load_more_button = wd.find_elements(By.CSS_SELECTOR, ".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # Moves result pointer further down page
        results_start = len(thumbnail_results)
    return image_urls


def image_scrape(keyword: str, num_of_links:int=1):
    """Returns set of image URLs."""
    # Enables chrome headless browsing
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    # Creates driver instance and calls helper function
    DRIVER_PATH = "C:/Users/kevin/Documents/Cloud Docs/OSU/CS 361/CS361-Project/Microservice/chromedriver"
    d = webdriver.Chrome(DRIVER_PATH, options=options)
    return get_image_urls(keyword, num_of_links, d)
