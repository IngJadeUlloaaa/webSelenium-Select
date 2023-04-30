import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')
    def test_using_select(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        time.sleep(3)
        select = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/select')
        container = select.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)
        for undername in container:
            print("I found: %s" % undername.get_attribute('value'))
            undername.click()
            time.sleep(1)
        get_toyota = Select(driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/div[3]/div[1]/select'))
        get_toyota.select_by_value('11')
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()