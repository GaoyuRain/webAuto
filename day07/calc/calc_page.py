from selenium.webdriver.common.by import By

from day07.calc.base_page import CalcBasePage


class CalcPage(CalcBasePage):

    def __init__(self):
        super().__init__()

        self.add_btn = (By.ID, 'simpleAdd')
        self.sub_btn = (By.ID, 'simpleSubtr')
        self.multi_btn = (By.ID, 'simpleMulti')
        self.divi_btn = (By.ID, 'simpleDivi')
        self.equal_btn = (By.ID, 'simpleEqual')

    def find_digit_btn(self, num):
        return self.find_element((By.ID, 'simple' + num))

    def find_add_btn(self):
        return self.find_element(self.add_btn)

    def find_sub_btn(self):
        return self.find_element(self.sub_btn)

    def find_multi_btn(self):
        return self.find_element(self.multi_btn)

    def find_divi_btn(self):
        return self.find_element(self.divi_btn)

    def find_equal_btn(self):
        return self.find_element(self.equal_btn)


class CalcHandle:

    def __init__(self):
        self.calc_page = CalcPage()

    def click_digit_btn(self, num):
        '''数字按钮'''
        self.calc_page.find_digit_btn(num).click()

    def click_add_btn(self):
        ''' + 按钮'''
        self.calc_page.find_add_btn().click()

    def click_sub_btn(self):
        ''' - 按钮'''
        self.calc_page.find_sub_btn().click()

    def click_multi_btn(self):
        ''' * 按钮'''
        self.calc_page.find_multi_btn().click()

    def click_divi_btn(self):
        ''' % 按钮'''
        self.calc_page.find_divi_btn().click()

    def click_equal_btn(self):
        ''' = 按钮'''
        self.calc_page.find_equal_btn().click()


class CalcProxy:
    def __init__(self):
        self.calc_handle = CalcHandle()

    def add(self, num1, num2):
        self.click_num(num1)
        self.calc_handle.click_add_btn()
        self.click_num(num2)
        self.calc_handle.click_equal_btn()

    def sub(self, num1, num2):
        self.click_num(num1)
        self.calc_handle.click_sub_btn()
        self.click_num(num2)
        self.calc_handle.click_equal_btn()

    def multi(self, num1, num2):
        self.click_num(num1)
        self.calc_handle.click_multi_btn()
        self.click_num(num2)
        self.calc_handle.click_equal_btn()

    def divi(self, num1, num2):
        self.click_num(num1)
        self.calc_handle.click_divi_btn()
        self.click_num(num2)
        self.calc_handle.click_equal_btn()

    def click_num(self, num):
        num_list = [x for x in str(num)]
        # for n in num_list:
        for n in str(num):
            self.calc_handle.click_digit_btn(n)


if __name__ == '__main__':
    num = '123'
    num_list = [x for x in num]
    print(num_list)
