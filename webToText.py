# This program is to extract text from a webpage. 

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
tabContent = soup.find_all('div', class_="eds-event-card-content__primary-content") #locate the "tab" of events
for item in tabContent:
    for link in item.find_all('a', href=True): #where you get the link
        eventLinks.append(link['href'])

eventTexts = [] # this is the list that will store the descriptions for our event. (Andrew's ML will later on filter the correct info from this.)

for event_link in eventLinks:
    r_event = requests.get(event_link, headers= headers)
    event_html_doc = r_event.content
    soup_event = BeautifulSoup(event_html_doc, 'html.parser')
    event_text1 = soup_event.get_text().strip() #this has the weird whitespace in the middle for eventbrite

    description_heading = (str(soup_event.title).replace("<title>","").replace("</title>",""))
    event_text2 = event_text1.replace(description_heading, "").strip() #only the description left. (i presume that if there is no whitespace issue then this wont change much)
    full_event_text = description_heading, event_text2

    eventTexts.append(full_event_text)

#for testing:
# for description in eventTexts:
#     print(description)
# print(len(eventTexts))