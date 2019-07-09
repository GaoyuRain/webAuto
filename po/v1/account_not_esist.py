from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://localhost/')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_id('username').send_keys('16645466859')
driver.find_element_by_id('password').send_keys('1234567890')
driver.find_element_by_id('verify_code').send_keys('8888')
driver.find_element_by_class_name('J-login-submit').click()
cont = driver.find_element_by_class_name('layui-layer-content').text
print(cont)

sleep(3)
driver.quit()
