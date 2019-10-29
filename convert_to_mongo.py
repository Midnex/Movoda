import csv
import pymongo
import config
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda
prices = db.prices

with open('itemDB.csv', 'r') as f:
    fcsv = csv.DictReader(f)
    for i, line in enumerate(fcsv):
        print(f"Processing Line: {i + 1}")
        prices_data = {
            'timestamp': line['timestamp'],
            'location': line['location'],
            'clan': line['clan'],
            'type': line['type'],
            'item': line['item'],
            'price': line['price'],
            'store': line['store']}
        result = prices.insert_one(prices_data)
client.close()