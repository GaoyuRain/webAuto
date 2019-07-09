'"H:\软件测试\课程\就业\day28_web自动化01\page\注册A等待.html"'
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

zhuceURL = 'file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html'
zhuceWaitUrl = 'file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A等待.html'


def quit(driver, time=3):
    sleep(time)
    driver.quit()


def get_chrom_driver(url=zhuceWaitUrl):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver


def text01():
    driver = get_chrom_driver()
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('#passwordA').send_keys('admin')
    driver.find_element_by_css_selector('#userA').send_keys('admin')
    quit(driver)


def text02():
    driver = get_chrom_driver()
    # webdriverwait = WebDriverWait(driver, 5, 1.1)
    element = WebDriverWait(driver, 7, 1.1).until(lambda x: x.find_element_by_id('userA'))
    # print(str(if element))
    element.send_keys('admin')


def text03():
    driver = get_chrom_driver(zhuceURL)
    sel_ele = Select(driver.find_element_by_css_selector('#selectA'))
    sel_ele.select_by_index(3)
    sleep(2)
    sel_ele.select_by_value('gz')
    sleep(2)
    sel_ele.select_by_visible_text('A上海')
    sleep(2)


def text04():
    driver = get_chrom_driver(zhuceURL)
    driver.find_element_by_css_selector('#alerta').click()
    alerta = driver.switch_to.alert
    print(alerta.text)
    sleep(2)
    alerta.accept()

    sleep(2)
    driver.find_element_by_css_selector('#confirma').click()
    confirm = driver.switch_to.alert
    sleep(2)
    print(confirm.text)
    confirm.accept()

    sleep(2)
    driver.find_element_by_css_selector('#prompta').click()
    prompta = driver.switch_to.alert
    prompta.send_keys('123456')
    sleep(2)
    print(prompta.text)
    prompta.accept()
    quit(driver)


def text05():
    driver = get_chrom_driver()
    js_down = 'window.scrollTo(0,1000)'
    js_up = 'window.scrollTo(0,0)'
    sleep(2)
    driver.execute_script(js_down)
    sleep(2)
    driver.execute_script(js_up)
    sleep(2)


if __name__ == '__main__':
    text05()
