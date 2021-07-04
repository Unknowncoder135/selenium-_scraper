from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
url ='http://yellowpages.in/hyderabad/food-and-beverages/606286653'
driver.get(url)
# print(driver.title)
while(True):
    try:
        page = driver.find_element_by_name('Load More')
        page.click()
        time.sleep(10)
        # driver.implicitly_wait(7)
        print('page..')
    except NoSuchElementException:
        break
mal = driver.page_source
print(mal)

driver.quit()
