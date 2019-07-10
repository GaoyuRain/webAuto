from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def quit(driver, time=3):
    sleep(time)
    driver.quit()


def init_chrom_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver


def text():
    driver = init_chrom_driver('http://www.baidu.com')
    baidu_dict = {'name': 'BDUSS',
                  'value': 'FJOFlETm9UTFVZMTNrTUl0WG16ZnRJdmFFcmREY0RSMkZCWGF5YmowbGRlclZiQVFBQUFBJCQAAAAAAAAAAAEAAAC'
                           '~rFxpR1nYvHJhaW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                           'F3tjVtd7Y1bbk'}
    driver.implicitly_wait(5)

    # setting = driver.find_element_by_css_selector("#s_usersetting_top")
    driver.find_element_by_link_text('登录').click()
    sleep(2)
    driver.add_cookie(baidu_dict)
    driver.refresh()

    element = driver.find_element_by_link_text('设置')
    print('设置:', element)
    ActionChains(driver).move_to_element(element).perform()
    sleep(1.5)
    driver.find_element_by_css_selector('.setpref').click()
    sleep(1.5)
    select = WebDriverWait(driver, 8, 2).until(lambda x: driver.find_element_by_css_selector('#nr'))
    select.click()
    print('select:', select)
    sleep(2)
    Select(select).select_by_visible_text('每页显示50条')
    sleep(1.5)
    driver.find_element_by_css_selector('.prefpanelgo').click()
    sleep(1.5)
    driver.switch_to.alert.accept()
    sleep(2)

    driver.find_element_by_css_selector('#kw').send_keys('黑马测试')
    sleep(1)
    driver.find_element_by_css_selector('#su').click()
    sleep(3)
    driver.get_screenshot_as_file('images/test.png')

    print(driver.get_window_size())
    scroll_start = "window.scrollTo(0, 0)"
    scroll_down1 = "window.scrollTo(0, 800)"
    scroll_down2 = "window.scrollTo(0, 1600)"
    scroll_down3 = "window.scrollTo(0, 2400)"
    driver.execute_script(scroll_down1)
    sleep(0.5)
    driver.execute_script(scroll_down2)
    sleep(0.5)
    driver.execute_script(scroll_down3)
    sleep(1.5)
    driver.execute_script(scroll_start)
    sleep(1)
    driver.find_element_by_partial_link_text('黑马程序员').click()
    sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    driver.back()
    quit(driver, 5)


def text01():
    driver = init_chrom_driver('http://time.geekbang.org/')
    driver.implicitly_wait(6)
    jike_dict = {'name': 'GCESS',
                 'value': 'BAYEZiSnBQkBAQsCBAAMAQEEBAAvDQACBNl9D10KBAAAAAAIAQMFBAAAAAAHBEMSYqABBAZwEgADBNl9D10-'}
    cookies = driver.get_cookies()
    for c in cookies:
        print(c)
    print('*'*50)
    driver.find_element_by_link_text('登录').click()
    sleep(2)
    driver.add_cookie(jike_dict)
    sleep(2)
    driver.refresh()
    sleep(1)
    cookies1 = driver.get_cookies()
    for c in cookies1:
        print(c)
    sleep(20)


if __name__ == '__main__':
    text01()
