from selenium import webdriver
import time

chromedriver = 'chromedriver'
browser = webdriver.Chrome(chromedriver)

browser.get('https://movoda.net/forum.html')

elem = browser.find_element_by_class_name('ntitle')
try:
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with the name <%s>.' % (elem.tag_name))


time.sleep(5)
browser.quit()
