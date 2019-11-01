import pyperclip
import re
from datetime import datetime
import location

clipboard = pyperclip.paste()
regStr = r'(^[a-zA-Z].*) for (.*)(V)|(.*)\t(.*)(V)'

building_location = ''
guilds = []
data = []
building_name = ''
building_clan = ''
for count, line in enumerate(clipboard.split('\r\n')):
    if count == 0:
        if 'Finder results for ' in line:
            #   TODO: Add Finder Spell Parser
            pass
        else:
            building_name = line
            for location in location.loc_list:
                if location in line:
                    building_location = location
                else:
                    continue
            if ' Guild Compound' in line:
                guilds.append(line.replace(' Guild Compound',''))

for count, line in enumerate(clipboard.split('\r\n')):
    if count == 0:
        #   TODO: FINDER PARSE
        if 'Finder results for ' not in line:
            print('store')
        #   TODO: STORE PARSE
        else:
            print(line)


    #   TODO: WRITE TO DATABASE