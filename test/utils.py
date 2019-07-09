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
    def get_driver(cls, type=CHROME):
        '''
        :param type:
        :return:
        '''
        if cls.__driver is None:
            if cls.FIREFOX == type:
                cls.__driver = webdriver.Firefox()
            else:
                cls.__driver = webdriver.Chrome()
            cls.__driver.get(cls.tpshop_url)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(30)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None


def get_user_name(type=DriverUtils.CHROME):
    return DriverUtils.get_driver(type).find_element_by_class_name('mu-m-phone').text
