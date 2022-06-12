# Mission to Mars-Web Scraping

![mission_to_mars](Images/mission_to_mars.png)

In this project, I have built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Step 1 - Scraping

* Initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Jupyter Notebook file  `mission_to_mars.ipynb` was created and used to complete all of the scraping and analysis tasks. 

### NASA Mars News

* The latest News Title and Paragraph Text was scraped and collected from the [Mars News Site](https://redplanetscience.com/). 

### JPL Mars Space Images - Featured Image

* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Splinter was used to navigate the Featured Space Image site [here](https://spaceimages-mars.com) and find the image url for the current Featured Mars Image.

### Mars Facts

* Pandas was used to scrape the the table containing facts about the planet including Diameter, Mass, etc, from the Mars Facts webpage [here](https://galaxyfacts-mars.com).

* The data was then converted to a HTML table string.

### Mars Hemispheres

* High resolution images for each of Mar's hemispheres was obtained by visiting the astrogeology site [here](https://marshemispheres.com/).

## Step 2 - MongoDB and Flask Application

Using MongoDB with Flask template, a new HTML page was created that displays all of the information that was scraped from the URLs above.

## Repo structure

- "templates" folder: index.html codes
- "Screenshots" folder: images of the scrapped data displayed in the html page
- mission_to_mars.ipynb: python codes for webscraping
- scrap_mars.py: codes to wrap data from scraping works and put into functions
- app.py: Flask route created to display scraping data onto index.html file

