"""
27、需求：对《注册实例.html》进行信息注册 账号：admin,密码：123456，
电话：18600000000，电子邮件：123@qq.com 要求：
1. 对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
2. 定位方式不限 3. 暂停3秒钟关闭浏览器
"""
from time import sleep

from selenium import webdriver


def test_27():
    driver = webdriver.Chrome()
    driver.get('file:///C:/Users/Rain/Desktop/test/注册实例.html')
    driver.maximize_window()

    driver.find_element_by_css_selector('#user').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_class_name('tel').send_keys('18600000000')
    driver.find_element_by_css_selector('#email').send_keys('123@qq.com')

    driver.switch_to.frame('idframe1')

    driver.find_element_by_css_selector('#userA').send_keys('admin')
    driver.find_element_by_id('passwordA').send_keys('123456')
    driver.find_element_by_class_name('telA').send_keys('18600000000')
    driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com')

    driver.switch_to.default_content()
    driver.switch_to.frame('myframe2')

    driver.find_element_by_css_selector('#userB').send_keys('admin')
    driver.find_element_by_id('passwordB').send_keys('123456')
    driver.find_element_by_class_name('telB').send_keys('18600000000')
    driver.find_element_by_css_selector('#emailB').send_keys('123@qq.com')

    sleep(3)
    driver.quit()


if __name__ == '__main__':
    test_27()
