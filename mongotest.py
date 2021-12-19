# from pymongo import MongoClient
import pymongo

connStr = "mongodb+srv://Duckabush:KleYdOgv1z1z5LPl@cluster0.ltipa.gcp.mongodb.net/movoda?retryWrites=true&w=majority"

client = pymongo.MongoClient(connStr)
db = client.movoda
prices = db.prices
locations = db.locations
users = db.users


search = prices.find({"price": {"$regex": ".*,.*"}})


for i in search:
    print(i)
