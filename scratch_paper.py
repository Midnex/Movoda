# scratch paper for upcoming features/changes

import config
from tabulate import tabulate
from pymongo import MongoClient

i2f = input('item: ')
t2f = input('Buy or Sell: ')

print('Loading Database')
client = MongoClient(config.credentials)
db = client.movoda

itemslist = db.prices


data = []

for i in itemslist.find({'item':i2f}):
    if i['type'] == t2f.lower():
        table = i['timestamp'],i['location'],i['clan'],i['type'],i['item'],int(i['price']),i['store']
        data.append(table)
if len(data) == 0:
    print(f"Nobody is {t2f}ing {i2f}.")
else:
    if t2f == 'sell':
        sorted_data = sorted(data, key=lambda x:x[5], reverse=True)
    else:
        sorted_data = sorted(data, key=lambda x:x[5], reverse=False)
    print(tabulate(sorted_data, headers=['timestamp','location','clan','type','item','price','store'], tablefmt='psql'))
client.close()