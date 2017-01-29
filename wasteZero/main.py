from rapidconnect import RapidConnect
from os import path
from pprint import pprint
import json


app_dir = path.dirname(__file__)
image_dir = path.join(app_dir, 'images')

API_KEY = ''
# rapidAPI Initialize
rapid = RapidConnect('WasteZero', API_KEY)

# Opening text files and spliting them into words
with open('compost.txt', 'r+') as f:
    compost = f.readlines()
    compost = [x.lower() for x in compost]
    compost = [x.strip() for x in compost]

with open('recyclables.txt', 'r+') as f:
    recycable = f.readlines()
    recycable = [x.lower() for x in recycable]
    recycable = [x.strip() for x in recycable]

with open('landfill.txt', 'r+') as f:
    landfill = f.readlines()
    landfill = [x.lower() for x in landfill]
    landfill = [x.strip() for x in landfill]

# Strawberry
url = """https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTFPXRtq-D8ouFl3gZV88uT_0RzkI2xoL18jRhA-
    ng7H3zNVpky"""

# Pen
url2 = 'http://www.killercrossexamination.com/wp-content/uploads/2016/12/Blue-Bic-biro-pen.jpg'

# Water Botlle
url3 = "http://www.berkeleyside.com/wp-content/uploads/2011/03/plastic-water-bottle-281x360.jpg"

# Broccoli
url4 = "http://www.newkidscenter.com/images/10415723/broccoli.jpg"

# Cigarrete
url5 = "http://cdn.newsapi.com.au/image/v1/671c348120ffe64315ae2a67b627c98e?width=1024"

# Spoon
url6 = "https://upload.wikimedia.org/wikipedia/commons/3/32/Dessert_Spoon.jpg"

# Orange
url7 = "https://d3nevzfk7ii3be.cloudfront.net/igi/rCjJcEgTAnWxY4Ck.large"


def sortImage(url):
    """
    Takes an image URL and returns its corresponding trash category.

    Args:
        url (str): an image url

    Returns:
        str: Image item's sorting category
    """
    tagImage = rapid.call('MicrosoftComputerVision', 'tagImage', {
                          'subscriptionKey':
                          API_KEY,
                          'image': url
                          })

    describeImage = rapid.call('MicrosoftComputerVision', 'describeImage', {
                               'subscriptionKey':
                               API_KEY,
                               'image': url,
                               'maxCandidates': ''
                               })

    tag = json.loads(tagImage)
    describe = json.loads(describeImage)

    pprint(tag['tags'])
    pprint(describe['description']['captions'][0]['text'])
    for i in range(len(tag['tags'])):
        if tag['tags'][i]['name'] in compost:
            print("ITEM: " + (tag['tags'][i]['name']).upper())
            print("DESCRIPTION: " + describe['description']['captions'][0]
                  ['text']
                  ).upper()
            return ("THIS ITEM GOES TO THE COMPOST BIN.")
            break
        elif tag['tags'][i]['name'] in recycable:
            print("ITEM: " + (tag['tags'][i]['name']).upper())
            print("DESCRIPTION: " + describe['description']['captions'][0]
                  ['text']
                  ).upper()
            return ("THIS ITEM GOES TO THE RECYCLING BIN.")
            break
        elif tag['tags'][i]['name'] in landfill:
            print("ITEM: " + (tag['tags'][i]['name']).upper())
            print("DESCRIPTION: " + describe['description']['captions'][0]
                  ['text']
                  ).upper()
            return ("THIS ITEM GOES TO THE LANDFILL BIN.")
            break
        if i == len(tag['tags']):
            print("THIS ITEM GOES TO THE LANDFILL BIN.")


print(sortImage("https://d3nevzfk7ii3be.cloudfront.net/igi/rCjJcEgTAnWxY4Ck.large"))
