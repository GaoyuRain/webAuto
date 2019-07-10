from selenium.webdriver.common.by import By

from test08.calc2.base_calc_page import CalcBasePage, CalcBaseHandle


class CalcPage(CalcBasePage):
    def __init__(self):
        super().__init__()
        self.digit_btn = (By.ID, 'simple{}')
        self.add_btn = (By.ID, 'simpleAdd')
        self.equal_btn = (By.ID, 'simpleEqual')
        self.result = (By.ID, 'resultIpt')

    def find_digit_btn(self, num):
        locaion = (self.digit_btn[0], self.digit_btn[1].format(num))
        return self.find_element(locaion)

    def find_add_btn(self):
        return self.find_element(self.add_btn)

    def find_equal_btn(self):
        return self.find_element(self.equal_btn)

    def find_result(self):
        return self.find_element(self.result)


class CalcHandle(CalcBaseHandle):
    def __init__(self):
        self.calc_page = CalcPage()

    def click_digit_btn(self, num):
        self.click_element(self.calc_page.find_digit_btn(num))

    def click_add_btn(self):
        self.click_element(self.calc_page.find_add_btn())

    def click_equal_btn(self):
        self.click_element(self.calc_page.find_equal_btn())

    def get_result(self):
        return self.calc_page.find_result().get_attribute('value')

    def input_digits(self, num):
        for n in num:
            self.click_digit_btn(n)


class CalcProxy:
    def __init__(self):
        self.calc_handle = CalcHandle()

    def add(self, num1, num2):
        self.calc_handle.input_digits(str(num1))
        self.calc_handle.click_add_btn()
        self.calc_handle.input_digits(str(num2))
        self.calc_handle.click_equal_btn()

    def get_result_func(self):
        return self.calc_handle.get_result()
