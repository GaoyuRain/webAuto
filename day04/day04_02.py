import os
from time import sleep

from selenium import webdriver

zhuceUrl = 'file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册实例.html'


def quit(driver, time=3):
    '''
    退出
    :param driver:
    :param time:
    :return:
    '''
    sleep(time)
    driver.quit()


def init_chrom_driver(url=zhuceUrl):
    '''
    初始化浏览器驱动
    :param url:
    :return:
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver


def text01():
    driver = init_chrom_driver()
    driver.find_element_by_css_selector('#user').send_keys('admin')
    driver.find_element_by_css_selector('#password').send_keys('admin')

    # driver.switch_to.frame('myframe1')
    driver.switch_to.frame(0)
    driver.find_element_by_css_selector('#userA').send_keys('admin1')
    driver.find_element_by_css_selector('#passwordA').send_keys('admin1')

    driver.switch_to.default_content()
    # driver.switch_to.frame('myframe2')
    driver.switch_to.frame(1)
    driver.find_element_by_css_selector('#userB').send_keys('admin2')
    driver.find_element_by_css_selector('#passwordB').send_keys('admin2')
    sleep(3)


def text02():
    driver = init_chrom_driver()

    driver.find_element_by_css_selector('#ZCA').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_css_selector('#userA').send_keys('admin')
    driver.find_element_by_css_selector('#passwordA').send_keys('123456')
    sleep(1)
    driver.find_element_by_partial_link_text('新浪 网站').click()
    sleep(2)
    driver.find_element_by_css_selector('#telA').send_keys('110')
    print(driver.current_window_handle)
    print(driver.window_handles)
    sleep(3)


def text03():
    driver = init_chrom_driver()
    driver.find_element_by_css_selector('#user').send_keys('admin')
    driver.find_element_by_css_selector('#password').send_keys('123')
    os.mkdir('images')
    driver.get_screenshot_as_file('./images/text.jpg')
    sleep(2)


def text04():
    # FJOFlETm9UTFVZMTNrTUl0WG16ZnRJdmFFcmREY0RSMkZCWGF5YmowbGRlclZiQVFBQUFBJCQAAAAAAAAAAAEAAAC~rFxpR1nYvHJhaW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF3tjVtd7Y1bbk
    driver = init_chrom_driver('http://www.baidu.com')
    baidu_dict = {'name': 'BDUSS',
                  'value': 'FJOFlETm9UTFVZMTNrTUl0WG16ZnRJdmFFcmREY0RSMkZCWGF5YmowbGRlclZiQVFBQUFBJCQAAAAAAAAAAAEAAAC'
                           '~rFxpR1nYvHJhaW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                           'F3tjVtd7Y1bbk'}
    driver.add_cookie(baidu_dict)
    sleep(3)
    driver.find_element_by_partial_link_text('登录').click()
    sleep(3)
    driver.refresh()
    sleep(4)
    cookies = driver.get_cookies()
    for i in cookies:
        print(i)


if __name__ == '__main__':
    text04()
