# new store parser, test file
# 2019.10.25

import pyperclip, re
from datetime import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.movoda

locations = db.locations

loc_list = []
for id in locations.find():
    loc_list.append(id['location'])
        
# loc_list = ['Ashia', 'Awaru', 'Barin Plains', 'Baron Plains', 'Bulbas',
#             'Cardina', 'Cardina Valley', 'Cythe', 'Danycia', 'Droesar',
#             'Echtin', 'Eptile', 'Essrom', 'Ferboi', 'Galawi', 'Garando Mines',
#             'Giroc', 'Haldos Outpost', 'Hevalus Jungle', 'Hikori',
#             'HMS Halieutika', 'Irotho', 'Jiroka', 'Kimdar',
#             'Kolar Trading Post', 'Kudzum', 'Lake Essdar', 'Lake Trand',
#             'Marossa', 'Martral', 'Moskim', 'Mount Pharos', 'Nalurn Woods',
#             'Naton', 'Odude', 'Onnix', 'Pharos Peak', 'Ponat', 'Ponat Pier',
#             'Port Barin', 'Port Baron', 'Port Schow', 'Radom Woods', 'Ravel',
#             'Rissdra', 'Sepas', 'Therusia', 'Tropi', 'Unopos Mesa', 'Uzlea',
#             'Yisildor Bay', 'Zhyack']


clipboard = pyperclip.paste()
# buyReg = '(^[a-zA-Z].*) for (.*)(V)'
# sellReg = '(.*)\t(.*)(V)'
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

print(f"Guild Compunds at {building_location}:\n{', '.join(guilds)}")
for i in data:
    print(i)
