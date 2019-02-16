# not working correctly yet.... Need to work on it a bit more. To be integrated into movvy_items.py
# www.movoda.net

import pyperclip as clip
from pprint import pprint
import re, csv

text = clip.paste()

with open('items.txt','a') as itemFile:
    itemWriter = csv.writer(itemFile)

    for item in text:
        if item != '1' or item != 'Buy' or item != '' or item != 'Currently buying the following items:':
            itemWriter.writerow(item)

itemFile.close()

# (^(.*\n)*Currently buying the following items:)|(.{0}1\n)|(Buy)|(Empty)
