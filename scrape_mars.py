from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time

def scrape_info():

    # Setup Splinter
    executable_path={'executable_path': ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)

    # URL to scrape Mars news site
    mars_url= "https://redplanetscience.com/"

    # Connect to browser to collect html data
    browser.visit(mars_url)

    time.sleep(1)

    html=browser.html

    # Create BeautifulSoup object 
    soup=bs(html, 'html.parser')

    # Extract latest News Title and Paragraph Text
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text


    # Save into dictionary 
    post = {
        "title": news_title, 
        "info": news_p
    }

    browser.quit()

    return post