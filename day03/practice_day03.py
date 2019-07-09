from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
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


#
# 需求：打开注册A.html页面，完成以下操作
# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击
# 需求：打开注册A.html页面，完成以下操作
# 1).使用CSS定位方式中的层级选择器定位用户名输入框，并输入：admin
# 3.3 CSS延伸[了解]
# input[type^='p'] type属性以p字母开头的元素
# input[type$='d'] type属性以d字母结束的元素
# input[type*='w'] type属性包含w字母的元素
def text01():
    driver = get_chrom_driver()
    driver.find_element_by_css_selector('#userA').send_keys('admin')
    driver.find_element_by_css_selector('[name="passwordA"]').send_keys('123')
    driver.find_element_by_css_selector('.telA').send_keys('10086')
    sleep(1)
    driver.find_element_by_css_selector('#pa input').send_keys('ADMIN')
    driver.find_element_by_css_selector('input[name^="user"]').send_keys(123456)
    driver.find_element_by_css_selector('input[name$="A"]').send_keys(8888)
    driver.find_element_by_css_selector('input[class*="dzy"]').send_keys('123@qq.com')
    sleep(3)
    driver.find_element_by_css_selector('button').click()
    sleep(2)


# 需求：打开注册A页面，完成以下操作
# 1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
# 2).间隔3秒，修改电话号码为：18600000000
# 3).间隔3秒，点击‘注册’按钮
# 4).间隔3秒，关闭浏览器
# 5).元素定位方法不限
def text02():
    driver = get_chrom_driver()
    driver.find_element_by_css_selector('input[name^="user"]').send_keys("admin")
    tel_element = driver.find_element_by_css_selector('input[name$="lA"]')
    tel_element.send_keys(18611111111)
    driver.find_element_by_css_selector('input[class*="dzy"]').send_keys('123qq.com')
    sleep(3)
    tel_element.clear()
    tel_element.send_keys(18600000000)
    sleep(2)


# 需求：使用‘注册A.html’页面，完成以下操作：
# 1).获取用户名输入框的大小
# 2).获取页面上第一个超链接的文本内容
# 3).获取页面上第一个超链接的地址
# 4).判断页面中的span标签是否可见
# 5).判断页面中取消按钮是否可用
# 6).判断页面中'旅游'对应的复选框是否为选中的状态
def text03():
    driver = get_chrom_driver()
    print(driver.find_element_by_css_selector('#userA').size)
    aelement = driver.find_element_by_css_selector('a')
    print(aelement.text)
    print(aelement.get_attribute('href'))


# 需求：打开注册页面A，输入用户名admin，暂停3秒钟后，双击鼠标左键，选中admin
# 需求：打开注册A页面，完成以下操作
# 1). 输入用户名：admin1，暂停2秒，删除1
# 2). 全选用户名：admin，暂停2秒
# 3). 复制用户名：admin，暂停2秒
# 4). 粘贴到密码框
def text04():
    driver = get_chrom_driver()
    user = driver.find_element_by_css_selector('input[id^="user"]')
    user.send_keys('admin1')
    sleep(1)
    user.send_keys(Keys.BACK_SPACE)
    sleep(1)
    action = ActionChains(driver)
    action.double_click(user).perform()
    sleep(1)
    user.send_keys('ADMIN')
    sleep(1)
    action.double_click(user).perform()
    user.send_keys(Keys.CONTROL, 'c')
    sleep(1)
    driver.find_element_by_css_selector('#passwordA').send_keys(Keys.CONTROL, 'v')
    sleep(2)


# 打开‘drag.html’页面，把红色方框拖拽到蓝色方框上

# 需求：打开注册页面A，模拟鼠标悬停在‘注册’按钮上


if __name__ == '__main__':
    text04()
