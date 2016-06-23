# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class BuildFormsTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', \
                                                desired_capabilities={ \
                                                    "browserName": "firefox", \
                                                    "platform": "WIN8_1", \
                                                    })

        self.driver.implicitly_wait(30)
        self.base_url = "http://perfdash-4602.phx01.dev.ebayc3.com:8080/Web_Project_1/seleniumTest.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_build_forms_test_case(self):
        driver = self.driver
        driver.get("http://perfdash-4602.phx01.dev.ebayc3.com:8080/Web_Project_1/seleniumTest.jsp")
        driver.find_element_by_link_text("Forms Demo").click()
        print("going to write in text boxes")
        driver.find_element_by_name("FirstName").clear()
        driver.find_element_by_name("FirstName").send_keys("Hermione")
        driver.find_element_by_name("LastName").clear()
        driver.find_element_by_name("LastName").send_keys("")
        driver.find_element_by_name("LastName").send_keys("Gran")
        driver.find_element_by_name("LastName").send_keys("ger")
        print("going to check boxes")
        if not driver.find_element_by_xpath("//input[@value='Bike']").is_selected():
            driver.find_element_by_xpath("//input[@value='Bike']").click()
        if driver.find_element_by_xpath("//input[@value='Bike']").is_selected():
            driver.find_element_by_xpath("//input[@value='Bike']").click()
        print("Going to click on I have a bike again")
        if driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        if not driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        if driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        if not driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        if driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        if not driver.find_element_by_xpath("//input[@value='Car']").is_selected():
            driver.find_element_by_xpath("//input[@value='Car']").click()
        print("going to select dropdown")
        Select(driver.find_element_by_xpath("//select[@name='selectBox1']")).select_by_visible_text("Audi")
        print("going to radio buttons")
        driver.find_element_by_xpath("(//input[@name='gender'])[2]").click()
        driver.find_element_by_xpath("//input[@name='gender'][1]").click()
        driver.find_element_by_xpath("(//input[@name='gender'])[2]").click()
        driver.find_element_by_xpath("//input[@value='Submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

