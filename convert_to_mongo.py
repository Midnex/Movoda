# import csv
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017')

# db = client.movoda

# prices = db.prices

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