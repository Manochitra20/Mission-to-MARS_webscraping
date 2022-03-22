# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #Scraping the Mars webpage to collect new title and text
    news_url= "https://redplanetscience.com/"
    browser.visit(news_url)

    time.sleep(1)

    #scraping page into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #finding the first news item
    news = soup.find("div", class_='list_text')

    #finding the latest news title
    news_title = news.find_all("div", class_="content_title")[0].text

    #finding the latest news text
    news_para = news.find_all("div", class_ ="article_teaser_body")[0].text


    #Scraping the Mars webpage to collect featured image
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)

    #scraping into soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image_path = soup.find_all("img")[1]["src"]
    featured_img_url = image_url + image_path
    

    #Scraping the Mars webpage to collect facts about Mars
    table_url= "https://galaxyfacts-mars.com/"
    tables = pd.read_html(table_url)
    tables = tables[0]
    #setting first row as table header
    tables.columns = tables.iloc[0] 
    tables2 = tables[1:]
    #converting dataframe to html
    table_html=tables2.to_html()
    

    #Scraping the Mars webpage to collect hemisphere names and images
    hemisphere_url="https://marshemispheres.com/"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Finding the image and title based on div
    hemis=soup.find_all("div", class_="description")
    # Creating a list to hold the images and titles.
    hemis_url = []

    # Retrieving the image urls and names for each hemisphere.
    for hemi in hemis:
        
        #creating an empty dict
        hemispheres={}
        
        # Scraping title
        title = hemi.find('h3').text
        browser.click_link_by_partial_text(title)
        
        #parse html
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        
        #scraping images
        image_path = soup.find('img', class_="wide-image")["src"]
        image_url=hemisphere_url + image_path
        
        # Storing findings and appending to list

        hemispheres['Image_url'] = image_url
        hemispheres['Title'] =title
                    
        hemis_url.append(hemispheres)
        
        
        # Browse back to repeat
        browser.back()

    #Removing enhanced from the hemsiphere names
    #newhemi1 = hemi1.rsplit(' ', 1)[0]
    #hemi2='Schiaparelli Hemisphere Enhanced'
    #newhemi2 = hemi2.rsplit(' ', 1)[0]
    #hemi3='Syrtis Major Hemisphere Enhanced'
    #newhemi3 = hemi3.rsplit(' ', 1)[0]
    #hemi4='Valles Marineris Hemisphere Enhanced'
    #newhemi4 = hemi4.rsplit(' ', 1)[0]
    #title={newhemi1, newhemi2, newhemi3, newhemi4}

    #appending title to the list
    #hemis_url.append(title)

    #Storing all the scrapped data into dict
    mars_listing_data={
         "news_title": news_title,
         "news_para": news_para,
         "featured_image": featured_img_url,
         "mars_facts": table_html,
         "hemisphere_url": hemis_url
     }
    #Quit the browser
    browser.quit()

    #returning scrapping data
    return mars_listing_data

