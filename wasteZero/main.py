from rapidconnect import RapidConnect
from os import path
from pprint import pprint
import json


app_dir = path.dirname(__file__)
image_dir = path.join(app_dir, 'images')

# rapidAPI Initialize
rapid = RapidConnect('WasteZero', '158eb1cd-10fa-409b-b652-d0f9cd3e9ab3')

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

url = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTFPXRtq-D8ouFl3gZV88uT_0RzkI2xoL18jRhA-ng7H3zNVpky"


def sortImage(url):
    """
    Takes an image URL and returns its corresponding trash category.

    Args:
        url (str): an image url

    Returns:
        str: Image item's sorting category
    """
    result = rapid.call('MicrosoftComputerVision', 'tagImage', {
                        'subscriptionKey': '7bf3cea7fe0646ff83fddf20147a1fa5',
                        'image': url
                        })
    data = json.loads(result)
    pprint(data['tags'])
    for i in range(len(data['tags'])):
        if data['tags'][i]['name'] in compost:
            print(data['tags'][i]['name'])
            return ("This item goes to the compost bin.")
            break
        elif data['tags'][i]['name'] in recycable:
            print(data['tags'][i]['name'])
            return ("This item goes to the recycling bin.")
            break
        elif data['tags'][i]['name'] in landfill:
            print(data['tags'][i]['name'])
            return ("This item goes to the landfill bin.")
            break
        if i == len(data['tags']):
            print("Item not Found")


print(sortImage(url))
