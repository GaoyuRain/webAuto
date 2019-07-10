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


def get_by_xpath():
    driver = get_chrom_driver()

    driver.find_element_by_xpath('/html/body/div/fieldset/form/p[1]/input').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="passwordA"]').send_keys('123')

    # /html/body/div/fieldset/form/p[4]/input /html/body/div/fieldset/form/p[4]/input

    time.sleep(4)
    driver.quit()


def get_by_fields():
    driver = get_chrom_driver()
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('admin')
    driver.find_element_by_xpath("//input[@class='login' and @name='user']").send_keys('admin')
    driver.find_element_by_xpath("//*[@id='p2']/input").send_keys('admin')
    quit(driver, 4)


if __name__ == '__main__':
    get_by_fields()
