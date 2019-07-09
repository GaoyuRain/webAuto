from selenium import webdriver


class DriverUtils(object):
    '''
    获取浏览器对象
    '''
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    tpshop_url = 'http://localhost/'

    __driver = None

    @classmethod
    def get_driver(cls, type=CHROME, url=tpshop_url):
        '''
        :param type:
        :param url:
        :return:
        '''
        if cls.__driver is None:
            if cls.FIREFOX == type:
                cls.__driver = webdriver.Firefox()
            else:
                cls.__driver = webdriver.Chrome()
            cls.__driver.get(url)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None


def get_tips_msg(type=DriverUtils.CHROME):
    return DriverUtils.get_driver(type).find_element_by_class_name('layui-layer-content').text
