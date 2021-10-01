import unittest
import time

from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

    def test_googletest(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.wikipedia.org/')
        driver.find_element_by_id("searchInput").send_keys("piano")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
