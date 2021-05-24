# WEB SCRAPING CHALLENGE

For this assignment I built a web application that scrapes various websites for data related to the Mission to Mars and displays such information in a single HTML page. 

Web-Scraping was completed initially in Jupyter Notebook using Beautiful Soup, Pandas, and Requests/Splinter. The following was included: 

- NASA Mars News including the latest news title and description from https://redplanetscience.com/
- A featured image from https://spaceimages-mars.com/
- A table including mars information from https://galaxyfacts-mars.com/


Once the data was scraped from the above sites, I used MongoDB with Flask templating to create a new HTML page to display all of the information. My Jupyter Notebook was converted into a Python Script using a scrape function to execute the above scraping code and return a dictionary. A route (/scrape) was then created to import this script when the scrape function is called. This value was then stored in Mongo as a Python dictionary. The root route is able to query the Mongo database and pass the mars data into an HTML page to better display the data. 


