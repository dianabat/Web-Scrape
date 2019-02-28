
def scrape():

    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    from splinter import Browser

    mars_scrape_dict = {}

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').find('a').text
    print(news_title)
    news_p = soup.find('div', class_='article_teaser_body').text
    print(news_p)

    mars_scrape_dict["news_title"] = news_title
    mars_scrape_dict["news_p"] = news_p

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img', class_='thumb')['src']
    featured_image_url = url + featured_image_url
    print(featured_image_url)

    mars_scrape_dict["featured_image_url"] = featured_image_url

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    print(mars_weather)

    mars_scrape_dict["mars_weather"] = mars_weather

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    html = browser.html
    htmldata = pd.read_html(html)
    html_df = pd.DataFrame(htmldata[0])
    marsfacts = html_df.to_html(header = False, index = False)
    print(marsfacts)

    mars_scrape_weather["marsfacts"] = marsfacts

    return mars_scrape_weather
