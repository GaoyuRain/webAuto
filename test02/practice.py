from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def quit(driver, sleep=3):
    time.sleep(sleep)
    driver.quit()


def get_chrom_driver():
    driver = webdriver.Chrome()
    driver.get('file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html')
    driver.maximize_window()
    return driver


def get_prac():
    driver = webdriver.Chrome()
    driver.get('file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html')
    driver.maximize_window()

    driver.find_element_by_xpath('//button').click()

    # driver.find_element_by_id('userA').send_keys('admin')
    driver.find_element_by_css_selector('#userA').send_keys('admin')
    driver.find_element_by_name('passwordA').send_keys('123')
    driver.find_element_by_class_name('telA').send_keys('10086', '110')
    driver.find_element_by_class_name('dzyxA').send_keys('120@qq.com')

    elements = driver.find_elements_by_tag_name('input')
    l = len(elements)
    elements[l - 4].send_keys('text1')
    elements[l - 3].send_keys('text2')
    elements[l - 2].send_keys('text3')
    elements[l - 1].send_keys('text4')

    # driver.find_element_by_link_text('打开百度').click()
    driver.find_element_by_partial_link_text('百度').click()

    time.sleep(4)
    driver.quit()


def text02():
    driver = get_chrom_driver()

    elements = driver.find_elements_by_xpath('//a')
    # elements[0].click()
    elements[1].click()


def text03():
    driver = get_chrom_driver()

    # driver.find_element_by_xpath('//*[@value="alert"]').click()
    # driver.find_element_by_xpath('//*[@type="button" and @value="confirm"]').click()
    driver.find_element_by_xpath('//*/input[@value="prompt"]').click()

    # driver.close()
    quit(driver)


def text04():
    driver = get_chrom_driver()

    driver.find_element_by_xpath('//*[@name="selecta"]').click()

    driver.find_element_by_xpath('//label/input[@id="pga"]').click()

    elements = driver.find_elements_by_name('hobby')
    for i in elements:
        i.click()

    driver.find_element_by_xpath('//div/input').click()

    quit(driver)


def textAll():
    driver = get_chrom_driver()

    element = driver.find_element_by_css_selector('#userA')
    element.send_keys('admin')
    time.sleep(1)
    element.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    element.send_keys(Keys.CONTROL, 'c')
    time.sleep(1)
    driver.find_element_by_name('passwordA').send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    driver.find_element_by_class_name('telA').send_keys('10086', '110')
    time.sleep(1)
    driver.find_element_by_class_name('dzyxA').send_keys('120@qq.com')
    time.sleep(1)

    driver.find_element_by_link_text('新浪').click()
    time.sleep(3.5)
    driver.back()
    time.sleep(1)

    driver.find_element_by_link_text('访问 新浪 网站').click()
    time.sleep(3.5)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@value="alert"]').click()
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.accept()
    time.sleep(1)

    driver.find_element_by_id('confirma').click()
    confirm = driver.switch_to.alert
    time.sleep(2)
    confirm.dismiss()
    time.sleep(1)

    driver.find_element_by_id('prompta').click()
    prom = driver.switch_to.alert
    prom.send_keys('text')
    time.sleep(2)
    prom.accept()
    time.sleep(1)

    # 单选框
    sl_element = driver.find_element_by_xpath('//*[@name="selecta"]')
    # sl_element.click()
    selet_element = Select(sl_element)
    selet_element.select_by_index(1)
    time.sleep(1)
    driver.find_element_by_xpath('//label/input[@id="pga"]').click()
    time.sleep(1)

    elements = driver.find_elements_by_name('hobby')
    for i in elements:
        time.sleep(0.5)
        if i.is_selected():
            continue
        i.click()

    time.sleep(1)
    file_element = driver.find_element_by_xpath('//div/input')
    file_element.send_keys("F:\TestTools\XMind\lgpl-3.0.html")
    # file_element.click()
    time.sleep(1.5)
    # driver.switch_to.window(driver.window_handles[0])
    # file_element.send_keys(Keys.ESCAPE)
    # time.sleep(1)

    elements = driver.find_elements_by_tag_name('input')
    l = len(elements)
    elements[l - 4].send_keys('text1')
    time.sleep(1)
    elements[l - 3].send_keys('text2')
    time.sleep(1)
    elements[l - 2].send_keys('text3')
    time.sleep(1)
    elements[l - 1].send_keys('text4')
    time.sleep(1)

    driver.find_element_by_partial_link_text('百度').click()
    time.sleep(3.5)
    driver.back()
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    # get_prac()
    # text02()
    # text03()
    # text04()
    textAll()
