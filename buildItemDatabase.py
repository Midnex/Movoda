import requests

r = requests.get("http://www.movoda.net/man/BronzePickaxe")

print(r.text)
