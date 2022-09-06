from copy import copy
from bs4 import BeautifulSoup
import requests #importing requests python package

# This function obtains the astronomy picture of the day and downloads the
# most recent picture of the day.
def obtain_image():
    
    #Sending http request to APOD website
    r = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

    #Defining vars
    image_info = {}

    #Checking if request was ok
    if r.ok:

        #Obtaining dictionary of our request.
        dict = r.json()

        #Obtaining other components of the image, key name explains all

        image_info['title'] = dict['title']
        image_info['explanation'] = dict['explanation']
        image_info['url'] = dict['url']

        # Obtaining the url of the image from the generated dictionary and
        # sending a GET request to obtain the image.
        new_r = requests.get(dict['url'])

        # Checking if image request was returned.
        if new_r.ok:
            with open('image.png' , 'wb') as f:
                f.write(new_r.content)
        
        else: #Printing a message to indicate Image request failed
            return new_r
    
    else: #Printing a message to indicate Initial APOD request was unsuccessful
        print('Initial HTTP request failed.')
        return r 
    
    return image_info
    
# Retrieves the top 3 latest news headlines (2 articles, 1 blog) at the moment, 
# by making use of the spacenews api. 
def get_news():
    
    # Retrieving the first 5 articles supplied by the library
    articles_r = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=5')

    #Checking if request was executed successfully
    if articles_r.ok:

        #Retrieving the latest blog published
        blogs_r = requests.get('https://api.spaceflightnewsapi.net/v3/blogs?_limit=1')

        # Checking if request for blog was executed successfully
        if blogs_r.ok:
            
            # Generating python lists from the requests supplied by requests library.
            articles_list = articles_r.json()
            blogs_list = blogs_r.json()

            # Creating a pen-ultimate news list which contains the title, url, and news site for each
            # article or blog returned.
            news_list = [[articles_list[0]['title'] , articles_list[0]['url'], articles_list[0]['newsSite']],
                         [articles_list[4]['title'] , articles_list[4]['url'], articles_list[4]['newsSite']],
                         [blogs_list[0]['title'] , blogs_list[0]['url'], blogs_list[0]['newsSite']]]

            return news_list
    else:
        return articles_r


# Retrieving the celestial event taking place tonight. Supplied by earthsky.org's
# tonight page. No use of APIs here, html of page obtained using requests and
# scraped using bs4
def get_celestial_events():

    # Getting html of page.
    source = requests.get('https://earthsky.org/tonight/')

    if source.ok:

        source = source.text
        # Creating a parser for html obtained.
        soup = BeautifulSoup(source, 'lxml')

        # Searching for tag which contains heading.
        h4 = soup.find('h4')

        # Creating and returning list which contains header and url.
        return [h4.text , 'https://earthsky.org/tonight/']
    else:
        return source
