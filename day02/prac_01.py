from selenium import webdriver
import time


def quit(driver, sleep=3):
    time.sleep(sleep)
    driver.quit()


def get_chrom_driver():
    driver = webdriver.Chrome()
    driver.get('file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html')
    driver.maximize_window()
    return driver


def text01_id():
    driver = webdriver.Chrome()
    driver.get('file:///H:/软件测试/课程/就业/day28_web自动化01/page/注册A.html')

    username = driver.find_element_by_id('userA')
    pwd = driver.find_element_by_id('passwordA')
    username.send_keys('admin')
    pwd.send_keys('123456')

    time.sleep(3)
    driver.quit()


def text02_name():
    driver = get_chrom_driver()

    username = driver.find_element_by_name('userA')
    pwd = driver.find_element_by_name('passwordA')

    username.send_keys('admin')
    pwd.send_keys('q23')

    time.sleep(5)
    driver.quit()


def text03_classname():
    driver = webdriver.Chrome()
    driver.get(r"H:\软件测试\课程\就业\day28_web自动化01\page\注册A.html")
    driver.maximize_window()

    tel = driver.find_element_by_class_name('telA')
    email = driver.find_element_by_class_name('emailA')

    tel.send_keys('18611111111')
    email.send_keys('123@qq.com')

    time.sleep(3)
    driver.quit()


def text04_tag_name():
    driver = get_chrom_driver()

    user = driver.find_element_by_tag_name('input')
    user.send_keys('admin')

    quit(driver)


def text05_link_text():
    driver = get_chrom_driver()

    # driver.find_element_by_link_text('访问 新浪 网站').click()
    driver.find_element_by_partial_link_text('新浪').click()

    quit(driver, 5)


def text06_find_elements_by():
    driver = get_chrom_driver()

    elements = driver.find_elements_by_tag_name('input')
    for i in elements:
        print(i)
    elements[0].send_keys('admin')
    elements[1].send_keys('123')

    quit(driver, 3)


if __name__ == '__main__':
    # text01_id()
    # text02_name()
    # text03_classname()
    # text04_tag_name()
    # text05_link_text()
    text06_find_elements_by()