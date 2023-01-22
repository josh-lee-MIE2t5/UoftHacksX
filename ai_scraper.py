print("Start")
import os
import openai
import cohere
import json
openai.organization = "org-zPrvVu8wSB03buxCiZpm7qoh"
openai.api_key = "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"
#openai.Model.list()

# This program is to extract text from a webpage. 

import datetime
import requests
from bs4 import BeautifulSoup

url = "" #josh to fill in with the website url
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
    full_event_text = description_heading + event_text2

    eventTexts.append(full_event_text)

#for testing:
# for description in eventTexts:
#     print(description)
# print(len(eventTexts))
#print(eventTexts[0])
##############Cohere######################
from cohere.classify import Example


examples=[
  Example("Abba dance night at bar", "night out with friends"),
  Example("Festival", "night out with friends"),
  Example("Art festival", "date"),
  Example("Movie", "date"),
  Example("Wine tasting", "date"),
  Example("Marathon","athletic"),
  Example("Bike ride", "athletic"),
  Example("Concert", "night out with friends"),
  Example("Comedy show", "night out with friends"),
  Example("Conference", "business"),
  Example("Seminar", "business"),
  Example("Trade show", "business"),
  Example("Beach day", "outdoor"),
  Example("Hiking trip", "outdoor"),
  Example("Museum visit", "culture"),
  Example("Theater performance", "culture"),
  Example("Opera", "culture"),
  Example("Wedding", "special occasion"),
  Example("Anniversary celebration", "special occasion"),
  Example("Retirement party", "special occasion"),
  Example("Birthday party", "special occasion"),
  Example("Pool party", "party"),
  Example("Barbecue", "party"),
  Example("Book club", "community"),
  Example("Volunteer work", "community"),
  Example("Yoga class", "fitness"),
  Example("Gym workout", "fitness"),
  Example("Cooking class", "education"),
  Example("Photography workshop", "education"),
  Example("University lecture", "education"),
  Example("Ski trip", "outdoor"),
  Example("Camping trip", "outdoor"),
  Example("Garden tour", "outdoor"),
  Example("Farmers market", "shopping"),
  Example("Flea market", "shopping"),
  Example("Black Friday sale", "shopping"),
  Example("Holiday bazaar", "shopping"),
  Example("Science fair", "science"),
  Example("Astronomy night", "science"),
  Example("Nature walk", "science"),
  Example("Bird watching", "science"),
  Example("Boat ride", "outdoor"),
  Example("Kayaking trip", "outdoor"),
  Example("Fishing trip", "outdoor"),
  Example("Zoo visit", "family"),
  Example("Aquarium visit", "family"),
  Example("Amusement park", "family"),
  Example("Rock concert", "night out with friends"),
  Example("Jazz concert", "night out with friends"),
  Example("Outdoor concert", "night out with friends"),
  Example("Indoor concert", "night out with friends"),
  Example("Stand-up comedy show", "night out with friends"),
  Example("Improv comedy show", "night out with friends"),
  Example("Business conference", "business"),
  Example("Tech conference", "business"),
  Example("Marketing seminar", "business"),
  Example("Sales seminar", "business"),
  Example("International trade show", "business"),
  Example("Local trade show", "business"),
  Example("Beach day", "outdoor"),
  Example("Mountain hiking trip", "outdoor"),
  Example("Urban hiking trip", "outdoor"),
  Example("Art museum visit", "culture"),
  Example("History museum visit", "culture"),
  Example("Theater performance", "culture"),
  Example("Musical theater performance", "culture"),
  Example("Opera", "culture"),
  Example("Wedding reception", "special occasion"),
  Example("Engagement party", "special occasion"),
  Example("Retirement party", "special occasion"),
  Example("Surprise birthday party", "party"),
  Example("Pool party", "party"),
  Example("Barbecue party", "party"),
  Example("Book club meeting", "community"),
  Example("Volunteer work", "community"),
  Example("Yoga class", "fitness"),
  Example("Gym workout", "fitness"),
  Example("Bridal shower", "wedding"),
  Example("Bachelor party", "wedding"),
  Example("Baby shower", "family"),
  Example("Christening", "religion"),
  Example("Bar/Bat Mitzvah", "religion"),
  Example("Funeral", "mourning"),
  Example("Memorial service", "mourning"),
  Example("Graduation ceremony", "education"),
  Example("Prom", "high school"),
  Example("Homecoming dance", "high school"),
  Example("Quinceañera", "culture"),
  Example("Kwanzaa celebration", "culture"),
  Example("Diwali celebration", "culture"),
  Example("New Year's Eve party", "holiday"),
  Example("Halloween party", "holiday"),
  Example("Thanksgiving dinner", "holiday"),
  Example("Christmas market", "holiday"),
  Example("Holiday light display", "holiday"),
  Example("Haunted house", "entertainment"),
  Example("Escape room", "entertainment"),
  Example("Laser tag", "entertainment"),
  Example("Go-kart racing", "entertainment"),
  Example("Indoor rock climbing", "entertainment"),
  Example("Food festival", "food"),
  Example("Food truck festival", "food"),
  Example("Wine festival", "food"),
  Example("Beer festival", "food"),
  Example("Farmers market", "food"),
  Example("Farm-to-table dinner", "food"),
  Example("Food and wine pairing", "food"),
  Example("Food tour", "food"),
  Example("Outdoor movie night", "entertainment"),
  Example("Outdoor concert", "entertainment"),
  Example("Outdoor theater performance", "entertainment"),
  Example("Outdoor comedy show", "entertainment"),
  Example("Outdoor art fair", "culture"),
  Example("Outdoor sculpture garden", "culture"),
  Example("Outdoor photography exhibit", "culture"),
  Example("Outdoor cultural festival", "culture"),
  Example("Outdoor fitness class", "fitness"),
  Example("Outdoor yoga class", "fitness"),
  Example("Outdoor bootcamp", "fitness"),
  Example("Outdoor cycling class", "fitness"),
  Example("Outdoor marathon", "athletic"),
  Example("Outdoor triathlon", "athletic"),
  Example("Outdoor rock climbing competition", "athletic"),
  Example("Outdoor adventure race", "athletic"),
  Example("Cosplay convention", "fandom"),
  Example("Comic con", "fandom"),
  Example("Anime convention", "fandom"),
  Example("Fanfiction convention", "fandom"),
  Example("Steampunk festival", "fandom"),
  Example("Airshow", "aviation"),
  Example("Balloon festival", "aviation"),
  Example("Paragliding competition", "aviation"),
  Example("Gliding competition", "aviation"),
  Example("Model airplane contest", "aviation"),
  Example("Amateur radio convention", "amateur Radio"),
  Example("Hamfest", "amateur Radio"),
  Example("Ham radio contest", "amateur Radio"),
  Example("Ham radio field day", "amateur Radio"),
  Example("Maker fair", "DIY"),
  Example("Hackerspace meetup", "DIY"),
  Example("FabLab open house", "DIY"),
  Example("Raspberry Jam", "DIY"),
  Example("Quilt show", "crafts"),
  Example("Knitting convention", "crafts"),
  Example("Sewing expo", "crafts"),
  Example("Cross stitch convention", "crafts"),
  Example("Bead and Jewelry show", "crafts"),
  Example("Market", "date"),
  Example("Romantic dinner at a fancy restaurant", "date"),
  Example("Picnic in the park", "date"),
  Example("Visit to a botanical garden", "date"),
  Example("Wine tasting at a vineyard", "date"),
  Example("Dinner and a show", "date"),
  Example("Visit to a planetarium", "date"),
  Example("Sunset cruise", "date"),
  Example("Visit to an art gallery", "date"),
  Example("Visit to a museum", "date"),
  Example("Visit to a zoo", "date"),
  Example("Visit to an aquarium", "date"),
  Example("Visit to a theme park", "date"),
  Example("Visit to a historic site", "date"),
  Example("Visit to a lighthouse", "date"),
  Example("Visit to a castle", "date"),
  Example("Visit to a fortress", "date"),
  Example("Visit to a palace", "date")

]


co = cohere.Client("kT1haqLPpDd2BIhyY2WMQf1hZrLbxOhTyXBQ9DoP")



####################################


for i in range(len(eventTexts)):
    response = co.classify(
        inputs=[eventTexts[i]],
        examples=examples,
    )
    predic = str(response.classifications[0])

    
    toParse = eventTexts[i]
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt='''can you extract information summarize the following input into a json format like this:
    "title": "event 2",
    "description": "death",
    "location": "my hall",
    "_type": "competition",
    "startDate": "2023-01-21",
    "endDate": "2023-01-25",
    "registrationReq": false,
    "frequency": "yearly"''' + toParse + '''but make
    the type equal to the prediction given here''' + predic,
    max_tokens=1000,
    temperature=0
    )
    
    requests.post(url, json = response.choices[0].text)
    print("response: ", response.choices[0].text)


