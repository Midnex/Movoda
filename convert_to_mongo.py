import csv
import config
import pyperclip
import pymongo
import re
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda
# prices = db.prices
# locations = db.locations
# items = db.items
# clans = db.clans

# Import itemDB.csv
# with open('itemDB.csv', 'r') as f:
#     fcsv = csv.DictReader(f)
#     for line in fcsv:
#         prices_data = {
#             'timestamp': line['timestamp'],
#             'location': line['location'],
#             'clan': line['clan'],
#             'type': line['type'],
#             'item': line['item'],
#             'price': line['price'],
#             'store': line['store']}
#         result = prices.insert_one(prices_data)

# Import Locations - https://movoda.net/man/Locations
# locationlst = pyperclip.paste()
# for line in locationlst.split('\r\n'):
#     location = line.split(',')[0]
#     buildable = line.split(',')[1]
#     continent = line.split(',')[2]
#     location_data = {'name':location,'buildable':buildable,'continent':continent}
#     result = locations.insert_one(location_data)

# Import Items 
# itemlst = pyperclip.paste()
# for line in itemlst.split('\r\n'):
#     item_data = {'name': line.replace('?','')}
#     result = items.insert_one(item_data)

# Import Clans - https://movoda.net/api/csvranks.html?type=guildexp
# filterRegex = r'(\d*),(.*)(\(.*\)),(\d*),(\d*)'
# clanlst = pyperclip.paste()
# for line in clanlst.split('\r\n'):
#     match = re.match(filterRegex, line)
#     if match:
#         clan_data = {
#             'id': match.group(1).strip(),
#             'name': match.group(2).strip(),
#             'tag': match.group(3).strip(),
#         }
#         result = clans.insert_one(clan_data)

client.close()
