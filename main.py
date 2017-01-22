from rapidconnect import RapidConnect
from os import path
import json
from pprint import pprint

app_dir = path.dirname(__file__)
image_dir = path.join(app_dir, 'images')

rapid = RapidConnect('WasteZero', '158eb1cd-10fa-409b-b652-d0f9cd3e9ab3')

with open('compost.txt', 'r+') as f:
    compost = f.read().split()
    compost = [x.lower() for x in compost]

with open('recyclables.txt', 'r+') as f:
    recycable = f.read().split()
    recycable = [x.lower() for x in recycable]

with open('landfill.txt', 'r+') as f:
    landfill = f.read().split()
    landfill = [x.lower() for x in landfill]

url = "https://static.esea.net/global/images/teams/149154.1480283401.jpg"
# Tags
result = rapid.call('MicrosoftComputerVision', 'tagImage', {
    'subscriptionKey': '7bf3cea7fe0646ff83fddf20147a1fa5',
    'image': url
})


data = json.loads(result)
pprint(data)
print
print landfill

for i in range(len(data['tags'])):
    if data['tags'][i]['name'] in compost:
        print(data['tags'][i]['name'])
        print("This item goes to the compost bin.")
        break
    elif data['tags'][i]['name'] in recycable:
        print(data['tags'][i]['name'])
        print("This item goes to the recycling bin.")
        break
    elif data['tags'][i]['name'] in landfill:
        print(data['tags'][i]['name'])
        print("This item goes to the landfill bin.")
        break
