from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def scrape_info():

    # Setup Splinter
    executable_path={'executable_path': ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)

    # Scrape Mars news site
    mars_url= "https://redplanetscience.com/"
    browser.visit(mars_url)
    time.sleep(1)
    html=browser.html
    soup=bs(html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text

    browser.quit()

    executable_path={'executable_path': ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)

    # Scrape JPL Mars Space Imaged site
    jpl_url= "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    time.sleep(1)
    html=browser.html
    soup=bs(html, 'html.parser')

    featured_image_url = soup.find('img', class_="headerimage fade-in").get('src')
    full_featured_image_url = jpl_url + featured_image_url

    browser.quit()

    executable_path={'executable_path': ChromeDriverManager().install()}
    browser=Browser('chrome', **executable_path, headless=False)

    # Scrape Mars Fact Table
    facts_url= "https://galaxyfacts-mars.com"
    table=pd.read_html(facts_url)
    facts_df=table[1]
    facts_df.rename(columns={0:"Feature", 1: "Measurement"}, inplace=True)
    html_table=facts_df.to_html()
    html_table.replace('\n', '')
    facts_df.to_html('mars table', index=False, justify='center')

    browser.quit()

    # Save scraped data into dictionary 
    post = {
        "title": news_title, 
        "info": news_p, 
        "featured_image": full_featured_image_url, 
        "fact_table": html_table, 
    }

    return post