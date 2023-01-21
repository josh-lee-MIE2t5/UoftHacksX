# I will be using this as a trial document for multiple things. 

# Just so I dont go insane
    # 1) try extract text
    # 2) try api
    # 3) do it manual like sahil 


# STEP 1: Try to see if you could extract text from the document. 

import datetime
import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.eventbrite.ca/'

headers = {
    'User-Agent': 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
}
 # search results
r = requests.get('https://www.eventbrite.ca/d/canada--toronto/events/', headers= headers) #sahil says this gives you the html

soup = BeautifulSoup(r.content, 'lxml') #r.content is the actual html_doc

eventLinks = [] # links for each event's page. 
tabContent = soup.find_all('div', class_="eds-event-card-content__primary-content")
for item in tabContent:
    for link in item.find_all('a', href=True):
        eventLinks.append(link['href'])

#print(eventLinks)
#testlink = 'https://www.eventbrite.com/e/witches-night-in-the-ultimate-fairytale-mystic-expo-50-tattoos-tickets-468593595057?aff=ebdssbcitybrowse'  #used in the place of event_link

eventTexts = [] # this is the list that will store the descriptions for our event. (Andrew's ML will later on filter the correct info from this.)

for event_link in eventLinks:
    r_event = requests.get(event_link, headers= headers)
    event_html_doc = r_event.content
    soup_event = BeautifulSoup(event_html_doc, 'html.parser')
    event_text = soup_event.get_text()
    eventTexts.append(event_text.strip())

