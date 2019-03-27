import csv, datetime, pyperclip

# TODO: make a read database function to elimate extra code.
#       Search by location
#       Update to only show newest data for any given store, instead of all.
#       Fuzzy and Strict Search, with quotes "" to do strict, allow store, guild, player, item or location results, specify buy or sell, maybe sort buy/sell.

def add_to_file(add_to_file):
    stamp = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    if add_to_file == 'clipboard':
        toImport = pyperclip.paste()
        newList = toImport.split('\n')
        fullLine = []

        with open('itemDB.csv', 'a', encoding='utf-8', newline='') as itemDB:
            itemDB_writer = csv.writer(itemDB, quoting=csv.QUOTE_ALL)
            for line in newList:
                if len(line.split('\t')) == 2:
                    stamp = line.split('\t')[1].replace('\t','')
                if ' in house ' in line: # for now just removes house scans.
                    location = line[0:line.find('-')-1]
                    clan = ''
                    type = 'house'
                    item = ''
                    price = ''
                    store = line[line.find(' in house ')+10:]
                else:
                    location = line[0:line.find('-')-1]
                    clan = line[line.find('-')+2:line.find(' is ')]
                    if ' is buying ' in line:
                        type = 'buy'
                        item = line[line.find(' is buying ')+11:line.find(' for ')]
                    else:
                        type = 'sell'
                        item = line[line.find(' is selling ')+12:line.find(' for ')]
                    price = line[line.find(' for ')+5:line.find(' in ')].replace('V','').replace(',','')
                    store = line[line.find(' in ')+4:line.find('\t')]
                    itemDB_writer.writerow([stamp,location,clan,type,item,price,store])
        itemDB.close()
        print('Added finder spell list to Database')
    elif add_to_file == 'store':
        newList = pyperclip.paste().split('\n')
        location = input('Location: ')
        clan = input('Guild: ')
        store = ''
        item = ''
        price = ''
        type = ''
        for i in newList:
        	if i == newList[0]:
        		store = newList[0]
        	elif ' for ' in i:
        		type = 'buy'
        		item = i[0:i.find(' for ')]
        		price = i[i.find(' for ')+5:].replace('V','')
        		print(stamp,location,clan,type,item,price,store)
        	elif 'Buy' in i: ## needs to be fixed still
        		type = 'sell'
        		item = i[0:10]
        		print(stamp,location,clan,type,item,price,store)
        print('Added store list to Database')
    elif add_to_file == 'auction':
        print('this does not exist yet')

    pyperclip.copy('')

def lookUp(item):
    if item == 'item':
        # should probably sort, only print latest files, space the formatting into columns.
        with open('itemDB.csv', 'r', encoding='utf-8') as itemDB:
            itemName = input('Enter Item: ')
            databaseReader = csv.DictReader(itemDB)
            resultsFound = 0
            for row in databaseReader:
                "timestamp","location","clan","type","item","price","store"
                if itemName.lower() in row['item'].lower():
                    print(row['timestamp'].strip(),'-',row["type"],'-',row['price'] + 'V',row["clan"],'in',row["location"],row["item"],'at',row["store"] + '.')
                    resultsFound += 1
            if resultsFound == 0:
                print('\n No results found for',itemName,'check spelling and try again')
            elif resultsFound == 1:
                print('\n',resultsFound, 'result found for',itemName + '.\n')
            else:
                print('\n',resultsFound, 'results found for',itemName + '.\n')
        itemDB.close()
        menuSystem()
    if item == 'store':
        print('Coming Soon!\n')
        menuSystem()
    if item == 'location':
        print('Coming Soon!\n')
        menuSystem()


def menuSystem():
    menuItem = input('Choose a menu item:\n1 Add: Finder Spell Parse\n2 Add: Store Parse\n3 Add: Auction Parse\n4 Search: Item\n5 Search: Store\n6 Search: Location\n7 Exit\n')
    if menuItem == '1': # Finder Spell Parse
        add_to_file('clipboard')
        menuSystem()
    elif menuItem == '2': # Store Parse
        add_to_file('store')
        menuSystem()
    elif menuItem == '3': # Auction Parse
        add_to_file('auction')
        menuSystem()
    elif menuItem == '4': # Search by Item Name (fuzzy)
        lookUp('item')
    elif menuItem == '5': # search by Store
        lookUp('store')
    elif menuItem == '6': # search by Location
        lookUp('location')
    elif menuItem == '7': # Exit
        print('Exiting...')
    else:
        print('\n"' + menuItem + '" is not a valid option.')
        menuSystem()

menuSystem()
