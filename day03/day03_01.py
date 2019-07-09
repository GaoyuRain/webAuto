from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

zhuceURL = 'file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html'
dragUrl = r"H:\软件测试\课程\就业\day28_web自动化01\page\drag.html"


def quit(driver, time=3):
    sleep(time)
    driver.quit()


def get_chrom_driver(url=zhuceURL):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver


def text01():
    '''
    # from selenium.webdriver.common.by import By
    # 需求：打开注册A.html页面，完成以下操作
    # 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
    # 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
    # 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
    # 4).使用CSS定位方式中元素选择器定位注册按钮，并点击
    :return:
    '''
    driver = webdriver.Chrome()
    driver.get('file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html')
    driver.maximize_window()

    driver.find_element_by_css_selector('#userA').send_keys('ADMIN')
    driver.find_element_by_css_selector('[type="password"]').send_keys('123')
    driver.find_element_by_css_selector('.telA').send_keys('10086')
    driver.find_element_by_css_selector('#pa input').send_keys('admin')
    admin = driver.find_element_by_css_selector('#pa>input')
    admin.send_keys('abcde')
    admin.clear()
    admin.send_keys('admin')

    # driver.set_window_position(100, 100)
    #     # driver.set_window_size(600, 600)
    driver.set_window_rect(100, 100, 600, 600)

    sleep(2)
    # driver.find_element_by_css_selector('button').click()
    driver.find_element(By.TAG_NAME, 'button').click()

    sleep(3)
    driver.quit()


def text02():
    driver = get_chrom_driver('http://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('黑马')
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.back()
    sleep(2)
    driver.forward()
    sleep(2)
    driver.refresh()

    print(driver.current_url)
    print(driver.title)
    # print(driver.current_window_handle)

    quit(driver)


def text03():
    driver = get_chrom_driver()

    elementA = driver.find_elements_by_tag_name('a')[0]

    print(elementA.text)
    print(elementA.get_attribute('href'))

    spn_element = driver.find_element_by_name('sp1')
    print('is_displayed:', spn_element.is_displayed())
    cancel_element = driver.find_element_by_id('cancelA')
    print('is_enabled:', cancel_element.is_enabled())
    travel_elem = driver.find_element_by_id('lyA')
    print(travel_elem.is_selected())
    sleep(2)


def text04():
    driver = get_chrom_driver()

    action = ActionChains(driver)

    element = driver.find_element_by_id('userA')
    action.context_click(element)
    action.perform()
    sleep(2)


def text05():
    driver = get_chrom_driver()

    element = driver.find_element_by_id('userA')
    element.send_keys('admin')
    action = ActionChains(driver)
    action.double_click(element).perform()
    sleep(2)
    element.click()
    sleep(2)
    action.context_click(element).perform()
    sleep(2)
    element.click()
    sleep(2)


def text06():
    driver = get_chrom_driver(dragUrl)

    source = driver.find_element_by_id('div1')
    target = driver.find_element_by_id('div2')
    ActionChains(driver).drag_and_drop(source, target).perform()
    sleep(2)


def text07():
    driver = get_chrom_driver()

    zhuce = driver.find_element_by_tag_name('button')
    ActionChains(driver).move_to_element(zhuce).perform()
    sleep(2)


def text08():
    driver = get_chrom_driver()
    usera = driver.find_element_by_id('userA')
    pwd = driver.find_element_by_id('passwordA')

    usera.send_keys('admin1')
    sleep(1)
    usera.send_keys(Keys.BACK_SPACE)
    sleep(1)
    ActionChains(driver).double_click(usera).perform()
    sleep(1)
    usera.send_keys(Keys.CONTROL, 'c')
    sleep(1)
    pwd.send_keys(Keys.CONTROL, 'v')
    sleep(2)

if __name__ == '__main__':
    text08()
