import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_dict = {}


# Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = (news_title.text)
    mars_dict['news_title'] = news_title

    html = browser.html
    soup = bs(html, 'html.parser')
    news_p = soup.find_all('div', class_='article_teaser_body')
    holding2 = []

    #print(len(news_p))

    for x in news_p:
        x = x.text
        #print(x[1])
        holding2.append(x)
    
    news_p = (holding2[0])

    #Append the dictionary

    mars_dict['news_p'] = news_p


# Get the image
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser_image.visit(url2)

    html = browser_image.html
    soup = bs(html, 'html.parser')
    featured_image = soup.find_all('a', class_='button fancybox')
    for y in featured_image:
        y = y.text
        #print(x[1])
        holding3.append(y)

    mars_dict["image"] = holding3


    # Get the weather
    url_weather = 'https://twitter.com/marswxreport?lang=en'
    browser_weather.visit(url_weather)
    html = browser_weather.html
    soup = bs(html, 'html.parser')
    mars_weather = soup.find('div', class_='js-tweet-text-container')

    mars_weather = (mars_weather.text)
    
    #Append the dictionary
    mars_dict['mars_weather'] =  mars_weather


# Get the mars facts
    #mars facts
    url_facts = 'http://space-facts.com/mars/'
    tables = pd.read_html(url_facts)
    tables_df = pd.DataFrame(tables[0])

   # tables_df
    html_table = tables_df.to_html()
    #html_table

    # Append the dictionary
    mars_dict["facts_table"] = html_table


    print(mars_dict)
    return mars_dict


