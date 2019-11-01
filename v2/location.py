import config
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda
locations = db.locations

def check(location):
    for id in locations.find({}):
        if location == id['name']:
            return True

def loc_list():
    loc_list = []
    for id in locations.find({}):
        loc_list.append(id['name'])
    return loc_list
