from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
try:
    driver.get("http://cab-test4.skyway.capital")
except TimeoutException:
    print("can't load page")

time.sleep(5)
#driver.implicitly_wait(10) # seconds
driver.quit()


