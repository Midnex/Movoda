import lookup
import parse_spell
import parse_store
import location

def display():
    print('Choose a menu selection:')
    menuSelections = (
        '  1. Add: Finder Spell',
        '  2. Add: Store Parse',
        '  3. Add: Scan Auction',
        '  4. Search: Item',
        '  5. Search: Store (fuzzy)',
        '  6. Search: Location',
        '  7. Exit'
    )

    for item in menuSelections:
        print(item)

    menuItem = input('\n > ')

    if menuItem == '1':  # Finder Spell Parse
        parse_spell()
        display()
    elif menuItem == '2':  # Store Parse
        parse_store()
        display()
    elif menuItem == '3':  # Auction Parse
        # auction_scan_parse()
        display()
    elif menuItem == '4':  # Search by Item Name (strict)
        search = input('Item to find: ')
        searchQuery = search.split(',')
        lookup(searchQuery, 'item')
        display()
    elif menuItem == '5':  # search by Store
        search = input('Store to check: ')
        searchQuery = search.split(',')
        lookup(searchQuery, 'store')
        display()
    elif menuItem == '6':  # search by Location
        while True:
            search = input('Location to check: ')
            searchQuery = search.split(',')[0]
            if location(searchQuery) == True:
                lookup(searchQuery, 'location')
                break
        display()
    elif menuItem == '7':  # Exit
        print('Exiting...')
    else:
        print(f'\n {menuItem} is not a valid option.')
        display()


if __name__ == '__main__':
    print('run main.py')
