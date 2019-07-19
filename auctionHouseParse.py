from selenium import webdriver
import requests
from lxml import html
import time

webpage_to_get = 'https://movoda.net/forum.html'
chromedriver = 'chromedriver'
# page = requests.get(webpage_to_get)
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')

tree = html.fromstring(page.content)  # 0x3d18b40
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
# something = tree.xpath('//*[@id="group"]/span')
print(buyers, prices)

# browser = webdriver.Chrome(chromedriver)

# browser.get(webpage_to_get)

# elem = browser.find_element_by_class_name('ntitle')
# try:
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with the name <%s>.' % (elem.tag_name))

# click_thing = browser.find_elements_by_xpath('//*[@id="group"]/span[25]')

# time.sleep(5)
# browser.quit()

# click categry
#   Cards: //*[@id="group"]/span[25]
#   Equipment: //*[@id="group"]/span[27]
#   Food: //*[@id="group"]/span[29]
#   Other: //*[@id="group"]/span[31]
#   Price Check: //*[@id="group"]/span[33]
#   Raw Materials: //*[@id="group"]/span[35]

# Get Auction List: //*[@id="topic"]/table
'''
Start New Topic
Golden Hatchet Card	Dawnare	2019-05-27 00:39:41
Auction: 1 Lumber Card	Flying V Auctions	2019-05-26 08:09:22
Auction: 1 Iron Card	Flying V Auctions	2019-05-26 04:34:46
Lumber Card	Dawnare	2019-05-24 08:34:49
Tin Card	Dawnare	2019-05-22 22:14:51
Library Card	Dawnare	2019-05-20 15:41:43
Lumber Card	Dawnare	2019-05-19 19:51:27
Lion Card	Dawnare	2019-05-19 19:51:13
what a staff	wolfie	2019-05-18 18:38:51
Auction: 1 Iron Card	Flying V Auctions	2019-05-18 04:10:23
Auction: 2 Aluminum Card	Flying V Auctions	2019-05-09 21:17:46
Auction: 1 Chopping Card	Flying V Auctions	2019-05-05 10:12:21
Auction: 1 Magic Fish Card	Flying V Auctions	2019-05-03 13:11:50
Auction: 1 Hobgoblin Card	Flying V Auctions	2019-05-03 04:00:30
Auction: 1 Shark Card	Flying V Auctions	2019-04-30 13:42:02
Auction: 1 Lion Card	Flying V Auctions	2019-04-29 13:55:32
'''

# get list of tr with id "topicxxxxxxxxxx"

# import pyperclip

# lst = pyperclip.paste()

# count = 0
# won_row = False
# for line in lst.split('\n'):

#     # Search Inside thread for Auction being Held as the first line, if does not exist break loop and go to next thread.
#     '''Auction being held at Port Barin''' # Always row 1
#     if 'Auction being held at ' in line:
#         location = line.split(' at ')[1].strip()
#         print(location)

#     '''1 Golden Hatchet Card'''  # Always row 3 till Auction won by - 1 row
#     if won_row == False:
#         if count >= 3:
#             # get item quantity and name
#             '''1 Golden Hatchet Card''' # Always row 3 till Auction won by - 1 row
#             item_count = line.split(' ')[0]
#             item_name = line[len(item_count)+1:].strip()
#             print(item_count, '**' , item_name)

#         # Search for Auction Won By "Player" for "price"
#         '''Auction won by Reckless for 505V.'''  # Always row 5
#         if 'Auction won by ' in line:
#             won_row = True
#             item_buyer = line[15:].split(' for ')[0]
#             item_price = line.split(' for ')[1].replace('V','').replace('.','')
#             print(item_buyer, item_price)


#     # Get poster's name, or Auction House posted from
#     # item_poster
#     # Dawnare[LOG]	2019-05-27 00: 29: 14Golden Hatchet Card
#     # Happy Bidding
#     count += 1
