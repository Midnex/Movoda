import config
import csv
import pyperclip
from datetime import datetime
from tabulate import tabulate
from pymongo import MongoClient

client = MongoClient(config.credentials)
db = client.movoda
prices = db.prices
locations = db.locations

ver = '0.62'

def menuSystem():
    print('Choose a menu selection:')
    menuSelections = (
        'Add: Finder Spell',
        'Add: Store Parse',
        'Add: Scan Auction',
        'Search: Item',
        'Search: Store (Strict)',
        'Search: Location (Broke)',
        'Exit'
    )
    for num, item in enumerate(menuSelections, start=1):
        print(f"  {num}. {item}")
    menuItem = input('\n > ')

    if menuItem == '1':  # Finder Spell Parse
        clipboard_finder_parse()
        menuSystem()
    elif menuItem == '2':  # Store Parse
        clipboard_store_parse()
        menuSystem()
    elif menuItem == '3':  # Auction Parse
        # auction_scan_parse()
        menuSystem()
    elif menuItem == '4':  # Search by Item Name (strict)
        search = input('Item to find: ')
        searchQuery = search.split(',')
        lookUp(searchQuery, 'item')
        menuSystem()
    elif menuItem == '5':  # search by Store
        search = input('Store to check: ')
        searchQuery = search.split(',')
        lookUp(searchQuery, 'store')
        menuSystem()
    elif menuItem == '6':  # search by Location
        while True:
            search = input('Location to check: ')
            searchQuery = search.split(',')[0]
            if checkLocation_new(searchQuery) == True:
                lookUp(searchQuery, 'location')
                break
        menuSystem()
    elif menuItem == '7':  # Exit
        print('Exiting...')
    else:
        print(f'\n {menuItem} is not a valid option.')
        menuSystem()

def checkLocation_new(location):
    for i in locations.find({'name':location}):
        if i['name'] == location:
            return True
        else:
            print(f'{location} does not exist.')
            return False

def database_reader_new(searchQuery, queryItemType, term):
    data = []
    searchQuery = ''.join(searchQuery)
    if term == 'store':
        for i in prices.find({'store': searchQuery}):
            table = i['timestamp'], i['location'], i['clan'], i['type'], i['item'], int(i['price']), i['store']
            data.append(table)
    elif term == 'item':
        for i in prices.find({'item': searchQuery}):
            if i['type'] == queryItemType.lower():
                table = i['timestamp'], i['location'], i['clan'], i['type'], i['item'], int(i['price']), i['store']
                data.append(table)
            elif queryItemType == 'both':
                table = i['timestamp'], i['location'], i['clan'], i['type'], i['item'], int(i['price']), i['store']
                data.append(table)
    elif term == 'location':
        for i in prices.find({'location': searchQuery}):
            table = i['timestamp'], i['location'], i['clan'], i['type'], i['item'], int(i['price']), i['store']
            data.append(table)

    if len(data) == 0:
        print(f"No result found for {searchQuery}.\n")
    else:
        if queryItemType == 'sell':
            sorted_data = sorted(data, key=lambda x: x[5], reverse=True)
        elif queryItemType == 'buy':
            sorted_data = sorted(data, key=lambda x: x[5], reverse=False)
        else:
            sorted_data = data
        return sorted_data

def database_writer_new(line_to_write):
    '''writes to mongodb using data in line_to_write (list)'''

    timestamp, location, clan, queryItemType, item, price, store = line_to_write
    data = {'timestamp': timestamp,'location': location,'clan': clan,'type': queryItemType,'item': item,'price': price,'store': store}
    result = prices.insert_one(data)


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
            building_item_price = line.split(' for ')[1].split(' in ')[0].strip()[:-1]
            building_name = line.split(' in ')[1].strip()

            line_to_write = [stamp, building_location, building_clan,building_type, building_item, building_item_price, building_name]
            database_writer_new(line_to_write)
            count += 1
        except:
            pass
    if item == '':
        print(f'Added {count} items at {stamp}\n')
    else:
        print(f'Added {count} items at {stamp} while searching for {item}\n')
    pyperclip.copy('')


def clipboard_store_parse():
    '''Grabs the data in the clipboard that matches store data, and parses it to add to the database'''

    while True:
            location = input('Location Name: ')
            if checkLocation_new(location) == True:
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
                building_item = line.split(buy_sep)[0].replace('Building Administration', '').strip()
                building_price = line.split(buy_sep)[1].replace('V', '').replace(',', '').strip()
                building_type = 'buy'
            if sell_sep in line:
                building_item = line.split(sell_sep)[0].replace('Building Administration', '').strip()
                building_price = line.split(sell_sep)[1].replace('V', '').replace(',', '').strip()
                building_type = 'sell'
            if building_type != '':
                line_to_write = [stamp, location, clan, building_type, building_item, building_price, building_name]
                database_writer_new(line_to_write)
        count += 1
    print(f'Added {count} items at {stamp} from {location} - {clan} - {building_name}\n')


def auction_scan_parse():
    '''Once done will scan the auction house and new building type called auction'''
    return


def lookUp(searchQuery, term):
    '''Looks up items based on item, store or location'''
    if len(searchQuery) == 2:
        queryItem = searchQuery[0].strip()
        queryItemType = searchQuery[1].strip()
    else:
        queryItem = searchQuery
        queryItemType = 'both'
    sorted_data = database_reader_new(queryItem, queryItemType, term)
    if sorted_data != None:
        print(tabulate(sorted_data, headers=['timestamp', 'location', 'clan', 'type', 'item', 'price', 'store'], tablefmt='psql'),'\n')

if __name__ == '__main__':
    menuSystem()

client.close()
