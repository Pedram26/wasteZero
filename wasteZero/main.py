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
