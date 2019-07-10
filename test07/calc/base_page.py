from test07.calc.utils import DriverUtils


class CalcBasePage:
    '''对象库层基类'''

    def __init__(self):
        self.driver = DriverUtils.get_driver()

    def find_element(self, location):
        return self.driver.find_element(*location)
