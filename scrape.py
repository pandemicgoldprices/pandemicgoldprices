
'''
a function which scrapes a webpage
'''
def scrape():

    ''' SAMPLE CODE
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    # HTML object


    url = 'https://mars.nasa.gov/news/?'
    browser.visit(url)
    html = browser.html
    time.sleep(5)
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    #get and print the latest news title and teaser paragraph
    latest_news_title = soup.find(class_='list_text').find('a').text
    #print(latest_news_title)
    latest_teaser = soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
    #print(latest_teaser)
    '''




