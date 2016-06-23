__author__ = 'Donald'

from selenium import webdriver
import unittest

class UnitTestExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() # note that this creates a class instance variable
        self.driver.implicitly_wait(30)
        self.base_url = "http://somewebsite.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def testWebSite1(self): # a first test case there can be others
        driver = self.driver  # class instance variable used here
        driver.get("http://somewebsite.com")

        # put your test code here


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()