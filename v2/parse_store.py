# new store parser, test file
# 2019.10.29

import config
import pyperclip
import re
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda
locations = db.locations

loc_list = []
for id in locations.find({}):
    loc_list.append(id['name'])

clipboard = pyperclip.paste()
regStr = r'(^[a-zA-Z].*) for (.*)(V)|(.*)\t(.*)(V)'

building_location = ''
guilds = []
data = []
building_name = ''
building_clan = ''
for count, line in enumerate(clipboard.split('\r\n')):
    if count == 0:
        building_name = line
    for location in loc_list:
        if location in line:
            building_location = location
        else:
            continue
    if ' Guild Compound' in line:
        guilds.append(line.replace(' Guild Compound',''))

print(f"Select a guild:")
for i, guild in enumerate(guilds, start=1):
    print(f'{i}. {guild}')
selection = int(input('\n > ')) - 1
building_clan = guilds[selection]

for line in clipboard.split('\r\n'):
    stamp = datetime.now().strftime("%m/%d/%y %H:%M:%S")
    match = re.match(regStr, line)
    if match:
        if '\t' in line:
            building_item = match.group(4)
            building_item_price = match.group(5)
            if ',' in match.group(5):
                building_item_price = building_item_price.replace(',','')
            data.append([stamp, building_location, building_clan, 'sell', building_item, building_item_price, building_name])
        elif ' for ' in line:
            building_item = match.group(1)
            building_item_price = match.group(2)
            if ',' in match.group(2):
                building_item_price = building_item_price.replace(',','')
            data.append([stamp, building_location, building_clan, 'buy',building_item, building_item_price, building_name])

print('Importing...')
for i in data:
    print(i)
print('Finished Importing\nExiting...')
client.close()
