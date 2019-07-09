import time

from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://www.baidu.com/")
time.sleep(3)
driver.quit()