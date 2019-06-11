import csv
from datetime import datetime
import pyperclip

def menuSystem():
    ''' A menu! '''
    print('Choose a menu number:')
    menuSelections = [
        '1. Add: Finder Spell',
        '2. Add: Store Parse',
        '3. Add: Scan Auction',
        '4. Search: Item',
        '5. Search: Store (fuzzy)',
        '6. Search: Location',
        '7. Exit'
    ]
    for item in menuSelections:
        print(item)
    menuItem = input()

    if menuItem == '1':  # Finder Spell Parse
        clipboard_finder_parse()
        menuSystem()
    elif menuItem == '2':  # Store Parse
        clipboard_store_parse()
        menuSystem()
    elif menuItem == '3':  # Auction Parse
        # auction_scan_parse()
        menuSystem()
    elif menuItem == '4':  # Search by Item Name (fuzzy)
        searchQuery = input('Item to find: ')
        lookUp(searchQuery, 'item')
        menuSystem()
    elif menuItem == '5':  # search by Store
        searchQuery = input('Store to check: ')
        lookUp(searchQuery, 'store')
        menuSystem()
    elif menuItem == '6':  # search by Location
        while True:
            searchQuery = input('Location to check: ')
            if checkLocation(searchQuery) == True:
                lookUp(searchQuery, 'location')
                break
        menuSystem()
    elif menuItem == '7':  # Exit
        print('Exiting...')
    else:
        print(f'\n {menuItem} is not a valid option.')
        menuSystem()

def checkLocation(location):
    loc_list = ['Ashia', 'Awaru', 'Barin Plains', 'Baron Plains', 'Bulbas',
                'Cardina', 'Cardina Valley', 'Cythe', 'Danycia', 'Droesar',
                'Echtin', 'Eptile', 'Essrom', 'Ferboi', 'Galawi', 'Garando Mines',
                'Giroc', 'Haldos Outpost', 'Hevalus Jungle', 'Hikori',
                'HMS Halieutika', 'Irotho', 'Jiroka', 'Kimdar',
                'Kolar Trading Post', 'Kudzum', 'Lake Essdar', 'Lake Trand',
                'Marossa', 'Martral', 'Moskim', 'Mount Pharos', 'Nalurn Woods',
                'Naton', 'Odude', 'Onnix', 'Pharos Peak', 'Ponat', 'Ponat Pier',
                'Port Barin', 'Port Baron', 'Port Schow', 'Radom Woods', 'Ravel',
                'Rissdra', 'Sepas', 'Therusia', 'Tropi', 'Unopos Mesa', 'Uzlea',
                'Yisildor Bay', 'Zhyack']
    if location in loc_list:
        return True
    else:
        print(f'"{location}" does not exist')
        return False

def database_reader():
    '''Loads data base into a variable to be used else where'''

    database = open('itemDB.csv', 'r', encoding='utf-8')
    return csv.DictReader(database)

def datebase_writer(line_to_write):
    '''writes to the data base using data in line_to_write'''

    with open('itemDB.csv', 'a', encoding='utf-8', newline='') as itemDB:
        itemDB_writer = csv.writer(itemDB, quoting=csv.QUOTE_ALL)
        itemDB_writer.writerow(line_to_write)

def checkBuildingType(line):
    '''Checks if the building type is a house, or if the item is being bought or sold'''

    if ' is buying ' in line:
        return 'buy'
    elif ' is selling ' in line:
        return 'sell'
    else:
        return 'house'

def getPrice(building_type, line):
    '''Gets the price of the item that is being bought or sold'''
    if building_type == 'buy':
        return line.split(' is buying ')[1].split(' for ')[0].strip()

    if building_type == 'sell':
        return line.split(' is selling ')[1].split(' for ')[0].strip()

def clipboard_finder_parse():
    '''Grabs the data in the clipboard that matches the finder spell data, and parses it to add to the database'''

    item = ''
    line_to_write = ''
    count = 0
    for line in pyperclip.paste().split('\n'):
        print(line)
        try:
            if len(line.split(' results for ')) == 2:
                item = line.split(' results for ')[1]
        except:
            pass
        stamp = datetime.now().strftime("%m/%d/%y %H:%M:%S")
        try:
            building_location = line.split('-')[0].strip()
            building_clan = line.split('-')[1].split(' is ')[0].strip()
            building_type = checkBuildingType(line)
            building_item = getPrice(building_type, line)
            building_item_price = line.split(' for ')[1].split(' in ')[
                0].strip()[:-1]
            building_name = line.split(' in ')[1].strip()

            line_to_write = [stamp, building_location, building_clan,
                             building_type, building_item, building_item_price, building_name]
            datebase_writer(line_to_write)
            count += 1
        except:
            pass
    if item == '':
        print(f'Added {count} items at {stamp}\n')
    else:
        print(f'Added {count} items at {stamp} while searching for {item}\n')
    pyperclip.copy('')

def clipboard_store_parse():
    '''Grabs the data in the clipboard that matches store data, and parses it to add to the data base'''

    while True:
            location = input('Location Name: ')
            if checkLocation(location) == True:
                break
    clan = input('Clan: ')
    line_to_write = ''
    building_name = ''
    count = 0
    stamp = datetime.now().strftime('%m/%d/%y %H:%M:%S')
    for line in pyperclip.paste().split('\n'):
        building_item = ''
        building_price = ''
        building_type = ''
        buy_sep = ' for '
        sell_sep = '\t'
        if count == 0:
            building_name = line.replace('(Change Name)', '').strip()
        if count > 1:
            if buy_sep in line:
                building_item = line.split(buy_sep)[0].replace(
                    'Building Administration', '').strip()
                building_price = line.split(buy_sep)[1].replace(
                    'V', '').replace(',', '').strip()
                building_type = 'buy'
            if sell_sep in line:
                building_item = line.split(sell_sep)[0].replace(
                    'Building Administration', '').strip()
                building_price = line.split(sell_sep)[1].replace(
                    'V', '').replace(',', '').strip()
                building_type = 'sell'
            if building_type != '':
                line_to_write = [stamp, location, clan, building_type,
                                 building_item, building_price, building_name]
                datebase_writer(line_to_write)
        count += 1
    print(f'Added {count} items at {stamp} from {location} - {clan} - {building_name}\n')

def auction_scan_parse():
    '''Once done will scan the auction house and new building type called auction'''
    return

def lookUp(searchQuery, term):
    '''Looks up items based on item, store or location'''

    searchQuery = searchQuery
    resultsFound = 0
    for line in database_reader():
        timestamp = line['timestamp']
        itemType = line['type']
        price = line['price']
        clan = line['clan']
        location = line['location']
        item = line['item']
        store = line['store']
        results = f'{timestamp} - {clan} is {itemType}ing {item} for {price}V in {location} at {store}.'
        if term == 'item':
            if searchQuery.lower() == item.lower():
                print(results)
                resultsFound += 1
        if term == 'store':
            if searchQuery.lower() in store.lower():
                print(results)
                resultsFound += 1
        if term == 'location':
            if searchQuery.lower() == location.lower():
                print(results)
                resultsFound += 1
    if resultsFound == 0:
        print(f'\n No result(s) found for "{searchQuery}" check spelling and try again.')
    else:
        print(f'\n {resultsFound} result(s) found for {searchQuery}.\n')

menuSystem()
