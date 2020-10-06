import json
import os.path

def write_json(user,password):
    data = {}
    data['credentials'] = []
    data['credentials'].append({
        'login': user,
        'uri': f'mongodb://{user}:{password}@cluster0-shard-00-00-ltipa.gcp.mongodb.net:27017/movoda?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"\nlogin = {user}'})
    with open('data.json','w') as f:
        json.dump(data,f)

def read_json():
    if os.path.isfile('data.json'):
        with open('data.json','r') as f:
            data = json.load(f)
            for line in data['credentials']:
                return line['login']


if os.path.isfile('data.json'):
    print('check')
    print(read_json())
else:
    user = input()
    password = input()

    write_json(user, password)
