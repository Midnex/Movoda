#! python3
# movvy_greenHouse.py calculates when a crop will come in, along with information about that cropself.

import json
#TODO: Database for crop times
#TODO: Check current time and get summer/winter growth times and calculate when it will be in.
with open('ghTable.json') as data_file:
    data = json.load(data_file)
    print(data['Item']['Winter']['Summer'])
