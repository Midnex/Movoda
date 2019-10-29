# scratch paper for upcoming features/changes

import config
from tabulate import tabulate
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda

itemslist = db.prices

data = []
i2f = input('item: ')
t2f = input('Buy or Sell: ')


for i in itemslist.find({'item':i2f}):
    if i['type'] == t2f.lower():
        table = i['timestamp'],i['location'],i['clan'],i['type'],i['item'],i['price'],i['store']
        data.append(table)

print(tabulate(data, headers=['timestamp','location','clan','type','item','price','store'], tablefmt='psql'))